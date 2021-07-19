#!/usr/bin/python3

import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys 
from collections import defaultdict 
import Environment
from Environment import debug, error, verbose
import parser
from DP import policy_iteration, print_policy


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


def rLearning(env, num_episodes, dynamic, alpha = 0.2,  epsilon = 0.8, beta = 0.6):
    
    Q = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))

    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, env)
    seen_states = set()

    rho = 1.0

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            alpha = alpha * 0.99
            epsilon = epsilon * 0.99
            beta = beta * 0.99

        if verbose:
            debug("alpha = ", alpha, "epsilon = ", epsilon)
        
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            seen_states.add(state)
            
            # get probabilities of all actions from current state
            action_probabilities = policy(state, epsilon)
            
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)
            
            if verbose:
                debug("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
            # done is True if episode terminated
            if done:
                break


            if Q[state][action] != -1 * np.inf:
                # TD Update
                best_next_action = np.argmax(Q[next_state])
                
                if verbose:
                    debug("best_next_action = ", best_next_action)
                    debug("reward = ", reward, ", rho = ", rho, " Q = ", Q[next_state][best_next_action])
                
                td_target = reward - rho + Q[next_state][best_next_action]

                if verbose:
                    debug("td_target = ", td_target)
                
                td_delta = td_target - Q[state][action]
                
                if verbose:
                    debug("td_delta = ", td_delta)

                Q[state][action] += alpha * td_delta

                current_best_action = np.argmax(Q[state])

                if Q[state][action] == Q[state][current_best_action]:
                    rho += beta * (reward - rho + Q[next_state][best_next_action] - Q[state][current_best_action])
                
                if verbose:
                    debug("rho = ", rho)
            
            else:
                if reward != -1 * np.inf:
                    error("Error in invalid actions!!!")
                    sys.exit()

            state = next_state
    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    return final_policy


if __name__ == "__main__":

    sim_time = 100

    parser.parse_config("config.json")

    pi_policy = policy_iteration(0.995)
    print("------------- PI Policy -----------------")
    print_policy(pi_policy)
 

    env = Environment.Env(Environment.domain.total_cpu, sim_time)
    rl_policy = rLearning(env, 10, 1)
    print("********* RL Policy ***********")
    print_policy(rl_policy)


