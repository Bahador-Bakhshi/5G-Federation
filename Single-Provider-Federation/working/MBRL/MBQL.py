#!/usr/bin/python3

import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys 
from collections import defaultdict 
import Environment
from Environment import verbose, debug, error
import parser
from DP import policy_iteration, print_policy


Q_table = None
policy  = None

def print_Q(Q):
    debug("---------------------")
    for s, s_a in Q.items():
        debug("{}: {}".format(s, s_a))
    debug("*********************")


def createEpsilonGreedyPolicy(Q, env): 
    def policyFunction(state, epsilon): 
        va = Environment.get_valid_actions(state)
        num_actions = len(va)

        for a in env.action_space:
            v_flag = False
            for sa in va:
                if a == sa:
                    v_flag = True

            if v_flag == False:
                Q[state][a] = -1 * np.inf

        Action_probabilities = np.ones(len(env.action_space), dtype = float) * epsilon / num_actions 
				
        best_action = np.argmax(Q[state]) 
        Action_probabilities[best_action] += (1.0 - epsilon) 
       
        if verbose:
            debug("Action_probabilities before: ", Action_probabilities)
        
        for a in env.action_space:
            v_flag = False
            for sa in va:
                if a == sa:
                    v_flag = True

            if v_flag == False:
                Action_probabilities[a] = 0
                Q[state][a] = -1 * np.inf
        
        if verbose:
            debug("Action_probabilities after: ", Action_probabilities)
        
        return Action_probabilities 

    return policyFunction 


def init(env):
    global Q_table
    Q_table = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))
    
    global policy
    policy = createEpsilonGreedyPolicy(Q_table, env)


def td_update(Q, state, action, next_state, reward, discount_factor, alpha):
    best_next_action = np.argmax(Q[next_state])
    
    td_target = reward + discount_factor * Q[next_state][best_next_action]
    if verbose:
        debug("td_target = ", td_target)
                
    td_delta = td_target - Q[state][action]
    if verbose:
        debug("td_delta = ", td_delta)

    Q[state][action] += alpha * td_delta
 

def get_action(state, epsilon):
    action_probabilities = policy(state, epsilon)
    if verbose:
        debug("action_probabilities = ", action_probabilities)

    action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
    action = Environment.Actions(action_index)
    if verbose:
        debug("selected action =", action)
    
    return action


def MBqLearning(env, state, alpha = 0.1,  epsilon = 0.3, gamma = 0.5):
    if verbose:
        debug("\nt =", t, "sate =", state)
        print_Q(Q_table)
    
    action = get_action(state, epsilon)

    next_state, reward, done = env.step(state, action)
    if verbose:
        debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
    if done:
        return reward, None

    td_update(Q_table, state, action, next_state, reward, gamma, alpha)
           
    return reward, next_state


if __name__ == "__main__":

    sim_time = 10000

    parser.parse_config("config.json")

    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time)

    init(env)
    
    state = env.reset()
    while state != None:
        reward, state = MBqLearning(env, state)
        print("s' = ", state)
        print("r  = ", reward)


