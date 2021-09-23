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
#from DP import policy_iteration, print_policy

def print_Q(Q):
    debug("---------------------")
    for s, s_a in Q.items():
        debug("{}: {}".format(s, s_a))
    debug("*********************")


def get_q_values_stat(Q):
    min_q = np.inf
    max_q = 0
    avg_q = 0.0
    num   = 0

    for i, (k, v) in enumerate(Q.items()):
        min_q = min(min_q, max(v))
        max_q = max(max_q, max(v))
        avg_q += max(v)
        num += 1

    return min_q, avg_q / num, max_q 


def createEpsilonGreedyPolicy(Q, env): 
    def policyFunction(state, epsilon, seen_states): 
        va = Environment.get_valid_actions(state)
        num_actions = len(va)

        if not (state in seen_states):
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
            if not (a in va):
                Action_probabilities[a] = 0
                Q[state][a] = -1 * np.inf
        
        if verbose:
            debug("Action_probabilities after: ", Action_probabilities)
        
        return Action_probabilities 

    return policyFunction 


