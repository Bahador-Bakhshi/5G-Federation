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
model_env = None

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


def generate_active_demands(domains_alives, domain_index, action, requests):
    this_domain_alives = domains_alives[domain_index]

    for class_index in range(len(this_domain_alives)):
        if this_domain_alives[class_index] > 0:
            service = Environment.known_traffic_params[class_index][0]
            load = Environment.known_traffic_params[class_index][1]
            for _ in range(this_domain_alives[class_index]):
                life = np.random.exponential(1.0 / load.mu)
                req = Environment.Request(service.cpu, 0, life, service.revenue, class_index)
                req.known_action = action
                req.deployed = domain_index

                requests.append(req)


def set_model_init_state(state, new_req_num):
    global model_env 
    model_env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota)

    domains_alives = state.domains_alives.copy()
    requests = list()

    generate_active_demands(domains_alives, 0, Environment.Actions.accept, requests)
    generate_active_demands(domains_alives, 1, Environment.Actions.federate, requests)

    new_req_set = Environment.generate_req_set(new_req_num)
    requests += new_req_set
    model_env.set_requests(requests)


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
        debug("sate =", state)
        print_Q(Q_table)
    
    action = get_action(state, epsilon)

    next_state, reward, done = env.step(state, action)
    if verbose:
        debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
    if done:
        return reward, None

    td_update(Q_table, state, action, next_state, reward, gamma, alpha)

    set_model_init_state(next_state, 100)
    model_state = model_env.reset()
    while model_state != None:
        req = model_state.req

        if hasattr(req, 'known_action') and req.known_action != None:
            model_action = req.known_action
            q_update = False
        else:
            model_action = get_action(model_state, epsilon)
            q_update = True
        
        model_next_state, model_reward, model_done = model_env.step(model_state, model_action)
        if q_update:
            td_update(Q_table, model_state, model_action, model_next_state, model_reward, gamma, alpha)

        model_state = model_next_state
    
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


