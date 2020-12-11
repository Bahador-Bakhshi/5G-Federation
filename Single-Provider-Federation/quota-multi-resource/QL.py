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


def qLearning(env, num_episodes, dynamic, alpha,  epsilon, gamma):

    Q = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))
    
    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, env)
    seen_states = set()

    discount_factor = 0.0
    decay = 0.0005

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
                print_Q(Q)

            seen_states.add(state)
            
            if verbose:
                debug("seen_states = ", seen_states)

            action_probabilities = policy(state, epsilon)
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

            if Environment.is_active_state(state):
                discount_factor = gamma
            else:
                discount_factor = 1.0

            best_next_action = np.argmax(Q[next_state])
                
            if verbose:
                debug("best_next_action = ", best_next_action)

            #if state == next_state:
            #        pass #FIXME!!!!!!!!!!!!!!!!!

            td_target = reward + discount_factor * Q[next_state][best_next_action]

            if verbose:
                debug("td_target = ", td_target)
                
            td_delta = td_target - Q[state][action]
                    
            if verbose:
                debug("td_delta = ", td_delta)

            Q[state][action] += alpha * td_delta
            
            state = next_state
    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    if verbose:
        print(final_policy)
    
    return final_policy


if __name__ == "__main__":

    sim_time = 100

    parser.parse_config("config.json")

    pi_policy = policy_iteration(0.995)
    print("********* DP Policy ***********")
    print_policy(pi_policy)

    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time)
    ql_policy = qLearning(env, 20, 1)

    print("********* QL Policy ***********")
    print_policy(ql_policy)


