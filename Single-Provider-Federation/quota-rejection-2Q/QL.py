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


def print_Q(Q):
    print("---------------------")
    for s, s_a in Q.items():
        print("{}: {}".format(s, s_a))
    print("*********************")


def e_greedy_exploration(Q1, Q2, env, state, epsilon): 
    va = Environment.get_valid_actions(state)
    num_actions = len(va)

    for a in env.action_space:
        v_flag = False
        for sa in va:
            if a == sa:
                v_flag = True

        if v_flag == False:
            Q1[state][a] = -1 * np.inf
            Q2[state][a] = -1 * np.inf

    Action_probabilities = np.ones(len(env.action_space), dtype = float) * epsilon / num_actions 
				
    Q_state= [sum(x) for x in zip(Q1[state], Q2[state])]
    best_action = np.argmax(Q_state) 
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
            Q1[state][a] = -1 * np.inf
            Q2[state][a] = -1 * np.inf
        
    if verbose:
        debug("Action_probabilities after: ", Action_probabilities)
        
    return Action_probabilities 


def qLearning(env, num_episodes, dynamic, alpha = 0.1,  epsilon = 0.8, gamma = 0.5):

    Q1 = defaultdict(lambda: np.random.uniform(0, 0, len(env.action_space)))
    Q2 = defaultdict(lambda: np.random.uniform(0, 0, len(env.action_space)))
    
    discount_factor = 0.0

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            alpha = alpha * 0.99
            epsilon = epsilon * 0.99
        
        if verbose:
            debug("alpha = ", alpha, "epsilon = ", epsilon, "gamma = ", gamma)
        
        state = env.reset()

        for t in itertools.count():
            if verbose:
                debug("\nt =", t, "sate =", state)
                debug("Q1:")
                print_Q(Q1)
                debug("Q2:")
                print_Q(Q2)
            
            
            action_probabilities = e_greedy_exploration(Q1, Q2, env, state, epsilon)
            #action_probabilities = e_greedy_exploration(Q1, Q1, env, state, epsilon)
            
            if verbose:
                debug("action_probabilities = ", action_probabilities)

            # choose action according to the probability distribution
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)

            if verbose:
                debug("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
            if done:
                break

            Q_target = None
            Q_estimator = None
            discount_factor = gamma
            
            rand = np.random.uniform(0, 1)
            if rand < 0.5:
                Q_target = Q1
                Q_estimator = Q2
                #Q_estimator = Q1
            else:
                Q_target = Q2
                #Q_target = Q1
                Q_estimator = Q1

            best_next_action = np.argmax(Q_target[next_state])
                
            if verbose:
                debug("best_next_action = ", best_next_action)

            td_target = reward + discount_factor * Q_estimator[next_state][best_next_action]

            if verbose:
                debug("td_target = ", td_target)
                
            td_delta = td_target - Q_target[state][action]
                    
            if verbose:
                debug("td_delta = ", td_delta)

            Q_target[state][action] += alpha * td_delta
            
            state = next_state
   

    final_policy = {}
    keys1 = set(Q1.keys())
    keys2 = set(Q2.keys())
    #keys2 = set(Q1.keys())
    keys = keys1.union(keys2)
    Q = {}
    for k in keys:
        Q[k] = [sum(x) for x in zip(Q1[k], Q2[k])]
        #Q[k] = [sum(x) for x in zip(Q1[k], Q1[k])]

    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    if verbose:
        print("Q1")
        print_Q(Q1)
        print("Q2")
        print_Q(Q2)
        print("Q")
        print_Q(Q)
    
    return final_policy


if __name__ == "__main__":

    sim_time = 1

    parser.parse_config("config.json")

    pi_policy = policy_iteration(0.995)
    print("********* DP Policy ***********")
    print_policy(pi_policy)

    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time)

    ql_policy = qLearning(env, 20, 1)
    print("********* QL Policy ***********")
    print_policy(ql_policy)


