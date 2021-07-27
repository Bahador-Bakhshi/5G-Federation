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

import Environment
from debugger import verbose

class TF_Agent_Env_Wrapper(tf_agents.environments.py_environment.PyEnvironment):
    
    def __init__(self, req_num = 0, requests = None):
        super().__init__()

        self.discount = 0.99995

        self.env = Environment.Env(eplen = req_num, demands = requests)

        self._action_spec = tf_agents.specs.BoundedArraySpec(
                             shape = (), 
                             dtype = np.int32, 
                             name = "action", 
                             minimum = 0, 
                             maximum = len(Environment.all_actions)
                        )
       
        self._observation_spec = {
                                'observations': tf_agents.specs.BoundedArraySpec(
                                        shape = (
                                            len(Environment.all_domains) * len(Environment.all_simple_ns) + 
                                            len(Environment.all_domains) * len(Environment.all_domains[0].quotas) +
                                            len(Environment.all_composite_ns) +
                                            len(Environment.all_traffic_loads) + 
                                            len(Environment.all_traffic_loads)
                                            , ), 
                                        dtype = np.int32, 
                                        name = "observation", 
                                        minimum = 0, 
                                        maximum = 200
                                    ), 
                                'valid_actions': array_spec.ArraySpec(
                                            shape = (len(Environment.all_actions) + 1, ), 
                                            dtype = np.bool_,
                                            name  = "valid_actions"
                                    )
                                }

    def object_to_array_state(self, obs):
        obs_fields_num = self._observation_spec["observations"].shape[0]
        res = np.zeros(obs_fields_num, dtype=np.dtype('int32'))
        index = 0
    
        for i in range(len(Environment.all_domains)):
            for sns in range(len(Environment.all_simple_ns)):
                res[index] = obs.domains_deployed_simples[i][sns]
                index += 1

        for i in range(len(Environment.all_domains)):
            for free_res in range(len(Environment.all_domains[i].quotas)):
                res[index] = obs.domains_resources[i][free_res]
                index += 1

        for i in range(len(Environment.all_composite_ns)):
            res[index] = obs.alive_composites[i]
            index += 1
        
        for i in range(len(Environment.all_traffic_loads)):
            res[index] = obs.alive_traffic_classes[i]
            index += 1

        for i in range(len(Environment.all_traffic_loads)):
            res[index] = obs.arrivals_departures[i]
            index += 1
        if verbose:
            print("state --> array: state = ", obs, ", array = ", res)
        
        return res

    def get_valid_actions_masks(self, obs):
        res = [False for i in range(self._action_spec.maximum + 1)]
        valid_actions = Environment.find_valid_actions(obs)
        for a in valid_actions:
            res[a] = True
        return np.array(res)
    
    def check_action_validity(self, action, obs):
        '''
        sfcs_num = requests.traffic_config["max_sfc_num"]
        req = obs.request
        
        start_index = (req.src_dst_index * (sfcs_num * (kpath.FixKpathAllPairs.k + 1))) + (requests.sfc_id_to_index(req.sfc.sfc_id) * (kpath.FixKpathAllPairs.k + 1))
        end_index = start_index + (kpath.FixKpathAllPairs.k + 1) - 1
        
        mask = self.get_valid_actions_masks(obs)
        res = (action < start_index) or (action > end_index) or (not mask[action])

        return (not res)
        '''

    def get_observation_actions(self, obs):
        res = {'observation' : None, 'valid_actions' : None}
        res['observation'] = self.object_to_array_state(obs)
        res['valid_actions'] = self.get_valid_actions_masks(obs)
        
        if verbose:
            print("get_observation_actions: shape(valid_actions) = ", np.shape(res['valid_actions']))
       
        return res

    def action_spec(self):
        if verbose:
            print("tf_env_wrapper: action_spec")
        return self._action_spec

    def observation_spec(self):
        if verbose:
            print("tf_env_wrapper: observation_spec")
        return self._observation_spec

    def _reset(self):
        if verbose:
            print("tf_env_wrapper: _reset")
    
        self.the_first_action = 0 

        s = self.env.reset()

        self._state = s

        obs = self.get_observation_actions(s)
        if verbose:
            print("_reset: self = ",self,", env = ",self.env,", obs = ",obs)
        
        return tf_agents.trajectories.time_step.restart(obs)

    def _step(self, action):
        if verbose:
            print("tf_env_wrapper: _step")

        if self.the_first_action == 1:
            return self.reset()

        observation = self._state
        
        if verbose:
            print("TF_Env_Wrapper:_step:")
            print("\t action = ", action)
            print("\t observation = ", observation)

        if False:
            '''
            not self.check_action_validity(action, observation):
            print("Invalid action = ", action, ", observation = ", observation)
            sys.exit(-1)
            '''
        else:
            real_action = action
        
        next_state, reward, done = self.env.step(observation, real_action)
        #self.discount = tmp_discount 
        
        if verbose:
            print("\t s' = ", next_state, ", r = ", reward, ", done = ", done, ", disc = ", self.discount)
       
        self._state = next_state

        if done == 1:
            self.the_first_action = 1

            dummy_obs = Environment.State(
                    [[0 for i in range(len(Environment.all_simple_ns))] for j in range(len(Environment.all_domains))],
                    [[0 for i in range(len(Environment.all_domains[0].quotas))] for j in range(len(Environment.all_domains))], 
                    [0 for i in range(len(Environment.all_composite_ns))],
                    [0 for i in range(len(Environment.all_traffic_loads))],
                    [0 for i in range(len(Environment.all_traffic_loads))]
                )
            obs = self.get_observation_actions(dummy_obs)
            return tf_agents.trajectories.time_step.termination(obs, reward)

        else:
            self._state = next_state
            obs = self.get_observation_actions(next_state)
            if verbose:
                print("\t obs = ", obs)
            
            return tf_agents.trajectories.time_step.transition(obs, reward, self.discount)

