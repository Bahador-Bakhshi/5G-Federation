#!/usr/bin/python3

import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys 
from collections import defaultdict 
import Environment
from Environment import debug
from Environment import error
import parser
from DP import policy_iteration, print_policy


def print_Q(Q):
    #debug("---------------------")
    for s, s_a in Q.items():
        #debug("{}: {}".format(s, s_a))
        pass
    #debug("*********************")

def Q_change(Q, old_Q):
    total = 0
    for s, s_a in Q.items():
        try:
            old_s_a = old_Q[s]
            for i in range(len(old_s_a)):
                if s_a[i] != -1 * np.inf and old_s_a[i] != -1 * np.inf:
                    total += abs(s_a[i] - old_s_a[i])
        except:
            #print(s)
            pass
    return total


def copy_Q(Q):
    copy = defaultdict(lambda: np.zeros(len(env.action_space)))
    for s, s_a in Q.items():
        copy_s_a = [0] * len(s_a)
        for i in range(len(s_a)):
            copy_s_a[i] = s_a[i]
        copy[s] = copy_s_a

    return copy


def createEpsilonGreedyPolicy(Q, env): 
    """ 
    Creates an epsilon-greedy policy based 
    on a given Q-function and epsilon. 
	
    Returns a function that takes the state 
    as an input and returns the probabilities 
    for each action in the form of a numpy array 
    of length of the action space(set of possible actions). 
    """
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
        
        #debug("Action_probabilities before: ", Action_probabilities)
        for a in env.action_space:
            v_flag = False
            for sa in va:
                if a == sa:
                    v_flag = True

            if v_flag == False:
                Action_probabilities[a] = 0
                Q[state][a] = -1 * np.inf
        #debug("Action_probabilities after: ", Action_probabilities)
        
        return Action_probabilities 

    return policyFunction 


def rLearning(env, num_episodes, dynamic, alpha = 0.2,  epsilon = 0.8, beta = 0.6):
    """
    Q-Learning algorithm: Off-policy TD control.
    Finds the optimal greedy policy while improving
    following an epsilon-greedy policy"""

    # Action value function
    # A nested dictionary that maps
    # state -> (action -> action-value).
    
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
            #alpha =  0.99
            epsilon = epsilon * 0.99
            #epsilon = 0.99
        else:
            #alpha = epsilon =  0.8
            pass

        #debug("alpha = ", alpha, "epsilon = ", epsilon)
        
        #old_Q = copy_Q(Q)
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            #debug("\nt =", t, "sate =", state)
            #print_Q(Q)
            seen_states.add(state)
            #debug("seen_states = ", seen_states)

            # get probabilities of all actions from current state
            action_probabilities = policy(state, epsilon)
            #debug("action_probabilities = ", action_probabilities)

            # choose action according to
            # the probability distribution
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)
            #debug("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            #debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
            # done is True if episode terminated
            if done:
                #print_Q(Q)
                #print("Total Changes =", Q_change(Q, old_Q))
                break


            if Q[state][action] != -1 * np.inf:
                # TD Update
                best_next_action = np.argmax(Q[next_state])
                #debug("best_next_action = ", best_next_action)

                #debug("reward = ", reward, ", rho = ", rho, " Q = ", Q[next_state][best_next_action])
                td_target = reward - rho + Q[next_state][best_next_action]

                #debug("td_target = ", td_target)
                
                td_delta = td_target - Q[state][action]
                #debug("td_delta = ", td_delta)

                Q[state][action] += alpha * td_delta

                current_best_action = np.argmax(Q[state])

                if Q[state][action] == Q[state][current_best_action]:
                    rho += beta * (reward - rho + Q[next_state][best_next_action] - Q[state][current_best_action])
                
                #debug("rho = ", rho)
            else:
                if reward != -1 * np.inf:
                    error("Error in invalid actions!!!")
                    sys.exit()

            state = next_state
    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    #print(final_policy)
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


