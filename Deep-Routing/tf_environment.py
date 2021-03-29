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
    def __init__(self, topology, src_dst_list, sfcs_list, discount=0.99, req_num = 0, requests = None):
        super().__init__()

        self.the_first_action = 1

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
                             maximum = len(self.src_dst_list) * kpath.FixKpathAllPairs.k - 1) 
       
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
                                            shape = ((kpath.FixKpathAllPairs.k * len(src_dst_list)), ), 
                                            dtype = np.bool_,
                                            name  = "valid_actions")
                                }
        
        self.discount = discount


    def get_valid_actions_masks(self, obs):
        req = obs.request
        res = [False] * len(self.src_dst_list) * kpath.FixKpathAllPairs.k

        '''
        index = 0

        for (src,dst) in self.src_dst_list:
            mask = 0
            if (src, dst) == (req.src, req.dst):
                for i in range(kpath.FixKpathAllPairs.k):
                    res[index * kpath.FixKpathAllPairs.k + i] = True
            
            index += 1
        '''

        for i in range(req.src_dst_index * kpath.FixKpathAllPairs.k, (req.src_dst_index + 1) * kpath.FixKpathAllPairs.k):
            res[i] = True

        if debug > 1:
            print("get_valid_actions_masks: req = ", req ,", res = ", res)
        
        return np.array(res)


    def check_action_validity(self, action, obs):
        req = obs.request
        res = [False] * len(self.src_dst_list) * kpath.FixKpathAllPairs.k
        index = 0

        res = (action < (req.src_dst_index * kpath.FixKpathAllPairs.k)) or (action >= ((req.src_dst_index + 1) * kpath.FixKpathAllPairs.k))
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
      
        self.the_first_action = 0 

        s = self.env.reset()

        self._state = s

        obs = self.get_observation_actions(s)
        print("_reset: obs = ", obs)
        
        return tf_agents.trajectories.time_step.restart(obs)


    def _step(self, action):

        if self.the_first_action == 1:
            return self.reset()


        observation = self._state
        kpaths = kpath.FixKpathAllPairs.all_pairs_kpaths[(observation.request.src, observation.request.dst)]
        
        if debug > 0:
            print("TF_Env_Wrapper:")
            print("\t action = ", action)
            print("\t request = ", observation.request)
            print("\t kpaths = ", kpaths)

        if not self.check_action_validity(action, observation):
            print("Invalid action = ", action, ", observation = ", observation)
            sys.exit(-1)
        else:
            req = observation.request
            path_index = action - req.src_dst_index * kpath.FixKpathAllPairs.k
            observation.request.path = kpaths[path_index]
            real_action = environment.Actions.accept
        
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


