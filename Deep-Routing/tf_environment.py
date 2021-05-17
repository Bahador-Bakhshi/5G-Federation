from __future__ import absolute_import, division, print_function

import sys
import base64
import imageio
import IPython
import numpy as np
import PIL.Image
import pyvirtualdisplay

import tensorflow as tf
import tf_agents

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.networks import sequential
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.specs import tensor_spec
from tf_agents.specs import array_spec
from tf_agents.utils import common

import environment
import kpath
import requests
import network
import graph

from graph import debug

def object_to_array_state(observation):
    res = np.zeros(kpath.FixKpathAllPairs.obs_fields_num, dtype=np.dtype('int32'))
    index = 0
    
    for (src, dst) in kpath.FixKpathAllPairs.all_pairs_kpaths.keys():
        if debug > 3:
            print("object_to_array_state: (src, dst) = ", src, dst)
            print("object_to_array_state: observation = ", observation)
            print("object_to_array_state: kpaths_bw[(src,dst)] = ", observation.kpaths_bw[(src,dst)])
        
        src_dst_bws = (observation.kpaths_bw[(src,dst)]).copy()
        for i in range(len(src_dst_bws)):
            res[index] = src_dst_bws[i]
            index += 1

    res[index] = observation.request.src
    index += 1

    res[index] = observation.request.dst
    index += 1

    res[index] = observation.request.sfc.sfc_id
    index += 1

    if debug > 2:
        print("state --> array: state = ", observation, ", array = ", res)
    
    return res


class TF_Agent_Env_Wrapper(tf_agents.environments.py_environment.PyEnvironment):
    
    def __init__(self, topology, src_dst_list, sfcs_list, discount=0.60, req_num = 0, requests = None):
        super().__init__()

        self.the_first_action = 1

        self.topology = topology
        self.requests = requests
        self.src_dst_list = src_dst_list
       
        kpath.FixKpathAllPairs.find_all_pair_kpaths(topology, src_dst_list)
        self.env = environment.Environment(topology, kpath.FixKpathAllPairs.observer, src_dst_list, req_num, sfcs_list)
       
        if self.requests != None:
            self.env.set_test_requests(self.requests)

        self._action_spec = tf_agents.specs.BoundedArraySpec(
                             shape = (), 
                             dtype = np.int32, 
                             name = "action", 
                             minimum = 0, 
                             maximum = len(self.src_dst_list) * len(sfcs_list) * (kpath.FixKpathAllPairs.k  + 1) - 1) #kpaths + reject action
       
        self.obs_len = kpath.FixKpathAllPairs.obs_fields_num

        self._observation_spec = {
                                'observations': tf_agents.specs.BoundedArraySpec(
                                        shape = (self.obs_len, ), 
                                        dtype = np.int32, 
                                        name = "observation", 
                                        minimum = 0, 
                                        maximum = network.topo_max_bw
                                    ), 
                                'valid_actions': array_spec.ArraySpec(
                                            shape = (((kpath.FixKpathAllPairs.k + 1) * len(sfcs_list) * len(src_dst_list)), ), 
                                            dtype = np.bool_,
                                            name  = "valid_actions"
                                    )
                                }
        
        self.min_gamma = 0.2
        self.max_gamma = 0.9
        self.gamma_steps = 1500
        self.discount = self.min_gamma


    def get_valid_actions_masks(self, obs):
        sfcs_num = requests.traffic_config["max_sfc_num"]
        req = obs.request
        res = [False] * (self._action_spec.maximum + 1)

        if req.src == 0 and req.dst == 0: #This is the dummy request in the termination step
            return np.array(res)
        
        kpaths = kpath.FixKpathAllPairs.all_pairs_kpaths[(req.src, req.dst)]

        start_index = (req.src_dst_index * (sfcs_num * (kpath.FixKpathAllPairs.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.FixKpathAllPairs.k + 1))
        end_index = start_index + (kpath.FixKpathAllPairs.k + 1) - 1
        
        for i in range(start_index, end_index):
            path_index = i - start_index

            if path_index < len(kpaths):
                if debug > 2:
                    print("get_valid_actions_masks: path = ", kpaths[path_index], ", bw = ", graph.get_path_bw(self.topology, kpaths[path_index]))
                if (path_index < len(kpaths)) and (graph.get_path_bw(self.topology, kpaths[path_index]) >= req.sfc.bw):
                    res[i] = True

        res[end_index] = True #the last one is reject

        if debug > 3:
            print("get_valid_actions_masks: req = ", req ,", res = ", res)
        
        return np.array(res)


    def check_action_validity(self, action, obs):
        sfcs_num = requests.traffic_config["max_sfc_num"]
        req = obs.request
        
        start_index = (req.src_dst_index * (sfcs_num * (kpath.FixKpathAllPairs.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.FixKpathAllPairs.k + 1))
        end_index = start_index + (kpath.FixKpathAllPairs.k + 1) - 1
        
        mask = self.get_valid_actions_masks(obs)
        res = (action < start_index) or (action > end_index) or (not mask[action])

        return (not res)


    def get_observation_actions(self, obs):
        res = {'observation' : None, 'valid_actions' : None}
        res['observation'] = object_to_array_state(obs)
        res['valid_actions'] = self.get_valid_actions_masks(obs)
        
        if debug > 1:
            print("get_observation_actions: shape(valid_actions) = ", np.shape(res['valid_actions']))
       
        return res

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
     
        self.discount += (self.max_gamma - self.min_gamma) / self.gamma_steps
        self.discount = min(self.max_gamma, self.discount)

        self.the_first_action = 0 

        s = self.env.reset()

        self._state = s

        obs = self.get_observation_actions(s)
        print("_reset: gamma = ",self.discount,", obs = ", obs)
        
        return tf_agents.trajectories.time_step.restart(obs)


    def _step(self, action):

        if self.the_first_action == 1:
            return self.reset()


        observation = self._state
        kpaths = kpath.FixKpathAllPairs.all_pairs_kpaths[(observation.request.src, observation.request.dst)]
        
        if debug > -1000:
            print("TF_Env_Wrapper:")
            print("\t action = ", action)
            print("\t request = ", observation.request)
            print("\t kpaths = ", kpaths)

        if not self.check_action_validity(action, observation):
            print("Invalid action = ", action, ", observation = ", observation)
            sys.exit(-1)
        else:
            req = observation.request
            sfcs_num = requests.traffic_config["max_sfc_num"]
            start_index = (req.src_dst_index * (sfcs_num * (kpath.FixKpathAllPairs.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.FixKpathAllPairs.k + 1))
            path_index = action - start_index
            if path_index < kpath.FixKpathAllPairs.k:
                observation.request.path = kpaths[path_index]
                real_action = environment.Actions.accept
            else:
                observation.request.path = None
                real_action = environment.Actions.reject
        
        next_state, reward, done = self.env.step(real_action)
        
        if debug > 2:
            print("\t s' = ", next_state, ", r = ", reward, ", done = ", done)
       
        self._state = next_state

        if done == 1:
            self.the_first_action = 1

            dummy_sfc = requests.SFC_e2e_bw(0, [], 0)
            dummy_req = requests.Request(0, 0, 0, dummy_sfc, 0, 0)
            dummy_bws = {(src,dst):[] for (src,dst) in kpath.FixKpathAllPairs.all_pairs_kpaths}
            dummy_obs = kpath.FixKpathAllPairs.Observation(dummy_bws, dummy_req)

            obs = self.get_observation_actions(dummy_obs)
            return tf_agents.trajectories.time_step.termination(obs, reward)

        else:
            self._state = next_state
            obs = self.get_observation_actions(next_state)
            if debug > 2:
                print("\t obs = ", obs)
            
            return tf_agents.trajectories.time_step.transition(obs, reward, self.discount)


