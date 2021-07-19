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

import environment_pps
import kpath
import requests
import network
import graph

from graph import debug

def object_to_array_state(observation):
    res = np.zeros(kpath.PerKpathStat.obs_fields_num, dtype=np.dtype('float32'))
    index = 0

    src_one_hot = tf.one_hot(observation.request.src, observation.topology.number_of_nodes() + 1)
    src_one_hot_numpy = src_one_hot.numpy()
    for i in range(len(src_one_hot_numpy)):
        res[index] = src_one_hot_numpy[i]
        index += 1

    dst_one_hot = tf.one_hot(observation.request.dst, observation.topology.number_of_nodes() + 1)
    dst_one_hot_numpy = dst_one_hot.numpy()
    for i in range(len(dst_one_hot_numpy)):
        res[index] = dst_one_hot_numpy[i]
        index += 1

    sfc_num_index = observation.request.sfc.sfc_id
    sfc_index_one_hot = tf.one_hot(sfc_num_index, int(requests.traffic_config["max_sfc_num"]))
    sfc_index_one_hot_numpy = sfc_index_one_hot.numpy()
    for i in range(len(sfc_index_one_hot_numpy)):
        res[index] = sfc_index_one_hot_numpy[i]
        index += 1

    for (src, dst) in observation.pairs_paths_active_sfcs.keys():
        for paths in observation.pairs_paths_active_sfcs[(src,dst)]:
            for actives in paths:
                res[index] = actives
                index += 1

    if debug > 2:
        print("state --> array: state = ", observation, ", array = ", res)
    
    return np.array([res])


class TF_Agent_Env_Wrapper(tf_agents.environments.py_environment.PyEnvironment):
    
    def __init__(self, topology, src_dst_list, sfcs_list, discount=0.95, req_num = 0, requests = None, punish = True, report_invalid_actions = False):
        super().__init__()

        self.the_first_action = 1

        self.discount = discount
        self.topology = topology
        self.requests = requests
        self.src_dst_list = src_dst_list
        self.invalid_action_punishment = punish
        self.report_invalid_actions = report_invalid_actions
       
        kpath.PerKpathStat.find_all_pair_kpaths(topology, src_dst_list)
        this_PerKpathStat = kpath.PerKpathStat()
        self.env = environment_pps.Environment(topology, this_PerKpathStat.observer, src_dst_list, req_num, sfcs_list, kpath.PerKpathStat.k)
        if debug > 3:
            print("tf: env = ", self.env, "report_invalid_actions = ", report_invalid_actions)
        
        this_PerKpathStat.environment = self.env
       
        if self.requests != None:
            self.env.set_test_requests(self.requests)

        self._action_spec = tf_agents.specs.BoundedArraySpec(
                             shape = (), 
                             dtype = np.int32, 
                             name = "action", 
                             minimum = 0, 
                             maximum = len(self.src_dst_list) * len(sfcs_list) * (kpath.PerKpathStat.k + 1) - 1) #kpaths + reject action
       
        self.obs_len = kpath.PerKpathStat.obs_fields_num

        self._observation_spec = tf_agents.specs.BoundedArraySpec(
                                        shape = (1, self.obs_len), 
                                        dtype = np.float32, 
                                        name = "observation", 
                                        minimum = 0, 
                                        maximum = network.topo_max_bw
                                    )
       

    def get_valid_actions_masks(self, obs):
        sfcs_num = requests.traffic_config["max_sfc_num"]
        req = obs.request
        res = [False] * (self._action_spec.maximum + 1)

        if req.src == 0 and req.dst == 0: #This is the dummy request in the termination step
            return np.array(res)
        
        kpaths = kpath.PerKpathStat.all_pairs_kpaths[(req.src, req.dst)]

        start_index = (req.src_dst_index * (sfcs_num * (kpath.PerKpathStat.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.PerKpathStat.k + 1))
        end_index = start_index + (kpath.PerKpathStat.k + 1) - 1
        
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
        
        start_index = (req.src_dst_index * (sfcs_num * (kpath.PerKpathStat.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.PerKpathStat.k + 1))
        end_index = start_index + (kpath.PerKpathStat.k + 1) - 1
        
        mask = self.get_valid_actions_masks(obs)
        res = (action < start_index) or (action > end_index) or (not mask[action])

        return (not res)

    def get_observation_actions(self, obs):
        '''
        res = {'observation' : None, 'valid_actions' : None}
        res['observation'] = object_to_array_state(obs)
        res['valid_actions'] = self.get_valid_actions_masks(obs)
        
        if debug > 1:
            print("get_observation_actions: shape(valid_actions) = ", np.shape(res['valid_actions']))
       
        return res
        '''
        return object_to_array_state(obs)


    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
    
        '''
        self.discount += (self.max_gamma - self.min_gamma) / self.gamma_steps
        self.discount = min(self.max_gamma, self.discount)
        '''

        self.the_first_action = 0 

        s, tmp_discount = self.env.reset()

        self._state = s

        obs = self.get_observation_actions(s)
        if debug > 2:
            print("_reset: self = ",self,", env = ",self.env,", obs = ",obs)
        
        return tf_agents.trajectories.time_step.restart(obs)


    def _step(self, action):

        if self.the_first_action == 1:
            return self.reset()

        observation = self._state
        kpaths = kpath.PerKpathStat.all_pairs_kpaths[(observation.request.src, observation.request.dst)]
        
        if debug > -1000:
            print("TF_Env_Wrapper:")
            print("\t action = ", action)
            print("\t request = ", observation.request)
            print("\t kpaths = ", kpaths)

        if not self.check_action_validity(action, observation):
            
            if debug > 1:
                print("Invalid action = ", action, ", observation = ", observation)
            
            if self.report_invalid_actions:
                print("Invalid action = ", action , "(src,dst) = ", observation.request.src, observation.request.dst)
            
            next_state, reward, done, tmp_discount = self.env.step(environment_pps.Actions.reject)
            if self.invalid_action_punishment:
                #reward = -1000
                reward = 0
            else:
                reward = 0
        else:
            req = observation.request
            sfcs_num = requests.traffic_config["max_sfc_num"]
            start_index = (req.src_dst_index * (sfcs_num * (kpath.PerKpathStat.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.PerKpathStat.k + 1))
            path_index = action - start_index
            if path_index < kpath.PerKpathStat.k:
                observation.request.path = kpaths[path_index]
                observation.request.path_id = path_index
                real_action = environment_pps.Actions.accept
            else:
                observation.request.path = None
                real_action = environment_pps.Actions.reject
        
             #self.last_discount = self.discount
            next_state, reward, done, tmp_discount = self.env.step(real_action)
            #self.discount = tmp_discount 
        
        if debug > 2:
            print("\t s' = ", next_state, ", r = ", reward, ", done = ", done, ", disc = ", self.discount)
       
        self._state = next_state

        if done == 1:
            self.the_first_action = 1

            dummy_sfc = requests.SFC_e2e_bw(0, [], 0)
            dummy_req = requests.Request(0, 0, 0, dummy_sfc, 0, 0)
            dummy_obs = kpath.PerKpathStat.Observation(dummy_req, self.topology, self.src_dst_list, self.env.global_pairs_paths_actives)

            obs = self.get_observation_actions(dummy_obs)
            return tf_agents.trajectories.time_step.termination(obs, reward)

        else:
            self._state = next_state
            obs = self.get_observation_actions(next_state)
            if debug > 2:
                print("\t obs = ", obs)
            
            return tf_agents.trajectories.time_step.transition(obs, reward, self.discount)


