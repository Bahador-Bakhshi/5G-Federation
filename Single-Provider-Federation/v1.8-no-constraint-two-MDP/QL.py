#!/usr/bin/python3

import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys 
from collections import defaultdict 
import OldEnvironment
import parser

matplotlib.style.use('ggplot') 


def print_Q(Q):
    for s, s_a in Q.items():
        if OldEnvironment.Environment.verbose:
            OldEnvironment.Environment.debug("{}: {}".format(s, s_a))
    if OldEnvironment.Environment.verbose:
        OldEnvironment.Environment.debug("*********************")


def print_policy(Q):
    for s, s_a in Q.items():
        if OldEnvironment.Environment.verbose:
            OldEnvironment.Environment.debug("{}: {}".format(s, np.argmax(s_a)))


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
        va = OldEnvironment.get_valid_actions(state)
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
        
        if OldEnvironment.Environment.verbose:
            OldEnvironment.Environment.debug("Action_probabilities before: ", Action_probabilities)
        for a in env.action_space:
            v_flag = False
            for sa in va:
                if a == sa:
                    v_flag = True

            if v_flag == False:
                Action_probabilities[a] = 0
                Q[state][a] = -1 * np.inf
        if OldEnvironment.Environment.verbose:
            OldEnvironment.Environment.debug("Action_probabilities after: ", Action_probabilities)
        
        return Action_probabilities 

    return policyFunction 


def qLearning(env, num_episodes, dynamic, discount_factor = 1.0, alpha = 1.0, epsilon = 1.0):
    """
    Q-Learning algorithm: Off-policy TD control.
    Finds the optimal greedy policy while improving
    following an epsilon-greedy policy"""

    # Action value function
    # A nested dictionary that maps
    # state -> (action -> action-value).
   
    Q = defaultdict(lambda: np.append([-1 * np.inf], np.random.uniform(0, 1, len(env.action_space) - 1)))

    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, env)
    seen_states = set()

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            alpha = alpha * 0.99
            epsilon = epsilon * 0.99
            discount_factor =  0.99
        else:
            alpha = discount_factor = 0.95
            epsilon = 0.1

        if OldEnvironment.Environment.verbose:
            OldEnvironment.Environment.debug("alpha = ", alpha, "epsilon = ", epsilon, "discount_factor = ", discount_factor)
            OldEnvironment.Environment.debug("=======================================================")
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            if OldEnvironment.Environment.verbose:
                OldEnvironment.Environment.debug("\nt =", t, "sate =", state)
            
            seen_states.add(state)

            # get probabilities of all actions from current state
            action_probabilities = policy(state, epsilon)

            # choose action according to
            # the probability distribution
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = OldEnvironment.Environment.Actions(action_index)
            if OldEnvironment.Environment.verbose:
                OldEnvironment.Environment.debug("action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if OldEnvironment.Environment.verbose:
                OldEnvironment.Environment.debug("next_state =", next_state, "reward =", reward, ", done =", done)

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
        final_policy[i] = OldEnvironment.Environment.Actions(np.argmax(Q[i]))

    #print(final_policy)
    return final_policy


if __name__ == "__main__":

    sim_time = 109

    parser.parse_config("config.json")

    env = OldEnvironment.Env(OldEnvironment.Environment.domain.total_cpu, sim_time)
    ql_policy = qLearning(env, 10, 1)
    OldEnvironment.Environment.debug("********* QL Policy ***********")
    #print_policy(ql_policy)
    print(ql_policy)


