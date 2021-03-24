from __future__ import absolute_import, division, print_function

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
from tf_agents.utils import common

import environment
import kpath


def object_to_array_state(observation):
    res = np.zeros(kpath.FixKpathSinglePair.obs_fields_num, dtype=np.dtype('int32'))
    index = 0
    for i in range(len(observation.kpaths_bw)):
        res[index] = observation.kpaths_bw[i]
        index += 1

    res[index] = observation.request.src
    index += 1

    res[index] = observation.request.dst
    index += 1

    res[index] = observation.request.sfc.sfc_id
    index += 1

    print("state --> array: state = ", observation, ", array = ", res)
    return res

'''
def array_to_object_state(array):

    src = array[kpath.FixKpathSinglePair.k]
    dst = array[kpath.FixKpathSinglePair.k + 1]
    sfc_id = array[kpath.FixKpathSinglePair.k + 2]

    dummy_sfc = requests.SFC_e2e_bw(sfc_id, [], 0)

    req = requests.Request(src, dst, dummy_sfc, 0, 0)
    
    print("array --> state: array = ", array, ", state = ", res)
    return res
'''


class TF_Agent_Env_Wrapper(tf_agents.environments.py_environment.PyEnvironment):
    def __init__(self, topology, src_dst_list, sfcs_list, discount=0.99, sim_num = 0, requests = None):
        #print("SmallMazeEnv: __init__")
        super().__init__()

        self.the_first_action = 1

        self.requests = requests
       
        kpath.FixKpathSinglePair.find_all_pair_kpaths(topology, src_dst_list)
        self.env = environment.Environment(topology, kpath.FixKpathSinglePair.observer, src_dst_list, sim_num, sfcs_list)

        
        self._action_spec = tf_agents.specs.BoundedArraySpec(
                             shape = (), 
                             dtype = np.int32, 
                             name = "action", 
                             minimum = 0, 
                             maximum = kpath.FixKpathSinglePair.k - 1 )
       
        self.obs_len = kpath.FixKpathSinglePair.obs_fields_num

        self._observation_spec = tf_agents.specs.BoundedArraySpec(
                                        shape = (self.obs_len, ), 
                                        dtype = np.int32, 
                                        name = "observation", 
                                        minimum = 0, 
                                        maximum = topology.max_bw
                    )
        
        self.discount = discount

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
      
        self.the_first_action = 0 

        s = self.env.reset()

        self._state = s

        obs = object_to_array_state(s)
        print("\t obs = ", obs)
        
        return tf_agents.trajectories.time_step.restart(obs)


    def _step(self, action):

        if self.the_first_action == 1:
            return self.reset()

        
        print("TF_Env_Wrapper: action = ", action)
       
        next_state, reward, done = self.env.step(self._state, action)
        print("\t s' = ", next_state, ", r = ", reward, ", done = ", done)
       
        self._state = next_state

        if done == 1:
            self.the_first_action = 1
            tmp_state = Environment.State(len(Environment.traffic_loads))
            obs = object_to_array_state(tmp_state)
            return tf_agents.trajectories.time_step.termination(obs, reward)

        else:
            self._state = next_state
            obs = object_to_array_state(next_state)
            print("\t obs = ", obs)
            
            return tf_agents.trajectories.time_step.transition(obs, reward, self.discount)


