from __future__ import absolute_import, division, print_function

import base64
import imageio
import IPython
import matplotlib
import matplotlib.pyplot as plt
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
import Environment


def object_to_array_state(state):
    res = np.zeros(Environment.State.state_fields_num, dtype=np.dtype('int32'))
    index = 0
    for i in range(len(state.domains_alives)):
        for j in range(len(state.domains_alives[i])):
            res[index] = state.domains_alives[i][j]
            index += 1

    for i in range(len(state.arrivals_departures)):
        res[index] = state.arrivals_departures[i]
        index += 1

    #print("state --> array: state = ", state, ", array = ", res)
    return res


def array_to_object_state(state):
    res = Environment.State(Environment.total_classes)
    index = 0
    
    for i in range(len(res.domains_alives)):
        tmp_list = [0] * Environment.total_classes
        for j in range(len(res.domains_alives[i])):
            tmp_list[j] = state[index]
            index += 1
            
        res.domains_alives[i] = tuple(tmp_list)

    tmp_list = [0] * Environment.total_classes
    for i in range(len(res.arrivals_departures)):
        tmp_list[i] = state[index]
        index += 1

    res.arrivals_departures = tuple(tmp_list)
    
    #print("array --> state: array = ", state, ", state = ", res)
    return res



class TF_Agent_Env_Wrapper(tf_agents.environments.py_environment.PyEnvironment):
    def __init__(self, discount=0.99, sim_num = 0, requests = None):
        #print("SmallMazeEnv: __init__")
        super().__init__()

        self.the_first_action = 1

        self.action_enum_bias = 1

        self.requests = requests
        
        self.env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_num)
        
        self._action_spec = tf_agents.specs.BoundedArraySpec(
                             shape = (), 
                             dtype = np.int32, 
                             name = "action", 
                             minimum = 1 - self.action_enum_bias, 
                             maximum = len(Environment.Actions) - 1 - self.action_enum_bias
                    )
        
        s = Environment.State(len(Environment.traffic_loads))
        s = object_to_array_state(s)
        self.obs_len = len(s)

        max_capacity = max(Environment.domain.total_cpu, Environment.providers[1].quota)
        min_req = min([serv.cpu for serv in Environment.domain.services])
        obs_max = int(max_capacity / min_req) + 1

        self._observation_spec = tf_agents.specs.BoundedArraySpec(
                                        shape = (self.obs_len, ), 
                                        dtype = np.int32, 
                                        name = "observation", 
                                        minimum = 0, 
                                        maximum = obs_max
                    )
        
        self.discount = discount

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
      
        self.the_first_action = 0 

        s = self.env.reset(self.requests)

        self._state = s

        obs = object_to_array_state(s)
        if Environment.verbose:
            print("\t obs = ", obs)
        
        return tf_agents.trajectories.time_step.restart(obs)


    def _step(self, action):

        if self.the_first_action == 1:
            return self.reset()

        action += self.action_enum_bias
        
        if Environment.verbose:
            print("TF_Env_Wrapper: action = ", action)
       
        next_state, reward, done = self.env.step(self._state, action)
        if Environment.verbose:
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
            if Environment.verbose:
                print("\t obs = ", obs)
            return tf_agents.trajectories.time_step.transition(obs, reward, self.discount)



