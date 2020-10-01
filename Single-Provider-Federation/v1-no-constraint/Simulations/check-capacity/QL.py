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

matplotlib.style.use('ggplot') 


def print_Q(Q):
    for s, s_a in Q.items():
        debug("{}: {}".format(s, s_a))
    debug("*********************")


def print_policy(Q):
    for s, s_a in Q.items():
        debug("{}: {}".format(s, np.argmax(s_a)))


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
        print_Q(Q)
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
        
        debug("Action_probabilities before: ", Action_probabilities)
        for a in env.action_space:
            v_flag = False
            for sa in va:
                if a == sa:
                    v_flag = True

            if v_flag == False:
                Action_probabilities[a] = 0
                Q[state][a] = -1 * np.inf
        debug("Action_probabilities after: ", Action_probabilities)
        
        return Action_probabilities 

    return policyFunction 


def qLearning(env, num_episodes, discount_factor = 0.7,	alpha = 0.9, epsilon = 0.9):
    """
    Q-Learning algorithm: Off-policy TD control.
    Finds the optimal greedy policy while improving
    following an epsilon-greedy policy"""

    # Action value function
    # A nested dictionary that maps
    # state -> (action -> action-value).
    
    # FIXME TODO
    #Q = defaultdict(lambda: np.zeros(env.action_space.n))
    Q = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))

    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, env)
    seen_states = set()

    max_val = 0.9
    min_val = 0.1
    # For every episode
    for ith_episode in range(num_episodes):
        #alpha = alpha / (ith_episode + 1.0)
        #epsilon = epsilon / (ith_episode + 1.0)
        alpha = max_val - ((max_val - min_val) / (num_episodes - 1)) * ith_episode

        debug("alpha = ", alpha, "epsilon = ", epsilon)
        debug("=======================================================")
        old_Q = copy_Q(Q)
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            debug("\nt =", t, "sate =", state)
            seen_states.add(state)

            # get probabilities of all actions from current state
            action_probabilities = policy(state, epsilon)

            # choose action according to
            # the probability distribution
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)
            debug("action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            debug("next_state =", next_state, "reward =", reward, ", done =", done)

            if Q[state][action] != -1 * np.inf:
                # TD Update
                best_next_action = np.argmax(Q[next_state])
                if next_state in seen_states:
                    td_target = reward + discount_factor * Q[next_state][best_next_action]
                else:
                    td_target = reward
                td_delta = td_target - Q[state][action]
                Q[state][action] += alpha * td_delta
            else:
                if reward != -1 * np.inf:
                    error("Error in invalid actions!!!")
                    sys.exit()

            state = next_state


            # done is True if episode terminated
            if done:
                #print_Q(Q)
                #print("Total Changes =", Q_change(Q, old_Q))
                break

    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    #print(final_policy)
    return final_policy


if __name__ == "__main__":

    sim_time = 100

    parser.parse_config("config.json")

    env = Environment.Env(Environment.domain.total_cpu, sim_time)
    ql_policy = qLearning(env, 100)
    debug("********* QL Policy ***********")
    print_policy(ql_policy)

