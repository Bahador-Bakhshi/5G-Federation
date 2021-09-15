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
rho = 0
counter = 0
alpha = 0
beta = 0
epsilon = 0

def print_Q(Q):
    debug("-------- Q_table ----------")
    for s, s_a in Q.items():
        debug("{}: {}".format(s, s_a))
    debug("*********************")

def init_val(env, state):
    if state in Q_table:
        return

    va = Environment.get_valid_actions(state)
    Q_table[state] = [-1 * np.inf] * len(env.action_space)

    for action in va:
        Q_table[state][action] = 0
    

def createEpsilonGreedyPolicy(Q, env): 
    def policyFunction(state, epsilon): 
        if not (state in Q_table):
            init_val(env, state)

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


observation_window = 0

def generate_active_demands(real_env, domains_alives, domain_index, action, requests):
    this_domain_alives = domains_alives[domain_index]

    for class_index in range(len(this_domain_alives)):
        if this_domain_alives[class_index] > 0:

            '''
            if np.random.uniform(0,1) < 0.1:
                print(real_env.learned_traffic_params)
            '''

            service = Environment.known_traffic_params[class_index][0]
            if class_index in real_env.learned_traffic_params and real_env.learned_traffic_params[class_index]["ht_seen"] > observation_window:
                avg_ht = real_env.learned_traffic_params[class_index]["ht"]
            else:
                avg_ht = np.random.uniform(0,10)

            for _ in range(this_domain_alives[class_index]):
                life = np.random.exponential(avg_ht)
                req = Environment.Request(service.cpu, 0, life, service.revenue, class_index)
                req.known_action = action
                req.deployed = domain_index

                requests.append(req)

def set_model_init_state(real_env, state, new_req_num):
    global model_env 
    model_env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota)

    domains_alives = state.domains_alives.copy()
    requests = list()

    generate_active_demands(real_env, domains_alives, 0, Environment.Actions.accept, requests)
    generate_active_demands(real_env, domains_alives, 1, Environment.Actions.federate, requests)
    
    class_index = state.arrivals_departures.index(1)
    service = Environment.known_traffic_params[class_index][0]
    if class_index in real_env.learned_traffic_params:
        params = real_env.learned_traffic_params[class_index]
        life = np.random.exponential(params["ht"])
    else:
        life = np.random.uniform(0, 1)

    arrived_request = Environment.Request(service.cpu, 0, life, service.revenue, class_index)

    tmp_list = list()
    tmp_list.append(arrived_request)
    requests += tmp_list

    new_req_set = Environment.generate_req_set_with_learned_param(new_req_num, real_env.learned_traffic_params, observation_window)
    requests += new_req_set
    model_env.set_requests(requests)


def init(env):
    global Q_table
    #Q_table = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))
    Q_table = dict()
    
    global policy
    policy = createEpsilonGreedyPolicy(Q_table, env)

    global rho
    rho = 0

    global counter, alpha, beta, epsilon
    counter = 0
    alpha = 0.1
    beta = 0.1
    epsilon = 0.3


def td_update(state, action, next_state, reward, alpha):
    best_next_action = np.argmax(Q_table[next_state])
    
    td_target = reward - rho + Q_table[next_state][best_next_action]
    if verbose:
        debug("td_target = ", td_target)
                
    td_delta = td_target - Q_table[state][action]
    if verbose:
        debug("td_delta = ", td_delta)

    Q_table[state][action] += alpha * td_delta
 

def td_update_rho(state, next_state, reward, beta):
    max_state_inedx = np.argmax(Q_table[state])
    max_next_state_index = np.argmax(Q_table[next_state])

    td_target = reward - Q_table[state][max_state_inedx] + Q_table[next_state][max_next_state_index]
    
    global rho
    td_delta = td_target - rho

    rho += beta * td_delta

    #print("rho = ", rho)


def get_action(state, epsilon):
    action_probabilities = policy(state, epsilon)
    if verbose:
        debug("action_probabilities = ", action_probabilities)

    action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
    action = Environment.Actions(action_index)
    if verbose:
        debug("selected action =", action)
   
    if action_index == np.argmax(Q_table[state]):
        update_rho = True
    else:
        update_rho = False

    return action, update_rho


def get_greedy_action(env, state):
    if not (state in Q_table):
        init_val(env, state)

    action_index = np.argmax(Q_table[state])
    return Environment.Actions(action_index)


def apply_model(real_env, state, epsilon, alpha, beta, sample_num, sample_len):
    if verbose:
        print("..................... MBQL Start .......................")
    
    for _ in range(sample_num):
        set_model_init_state(real_env, state, sample_len)
        model_state = model_env.reset()
    
        while model_state != None:
            req = model_state.req

            if hasattr(req, 'known_action') and req.known_action != None:
                model_action = req.known_action
                q_update = False
                update_rho = False
            else:
                model_action, update_rho = get_action(model_state, epsilon)
                q_update = True
        
            model_next_state, model_reward, model_done = model_env.step(model_state, model_action)

            if model_next_state != None:
                if not (model_next_state in Q_table):
                    init_val(real_env, model_next_state) 
            
                    if q_update:
                        td_update(model_state, model_action, model_next_state, model_reward, alpha)
            
                    if update_rho:
                        td_update_rho(model_state, model_next_state, model_reward, beta)
 
            model_state = model_next_state
    
    if verbose:
        print("..................... MBQL End .......................")
    
def estimate_action_value(state, action, real_env, sample_len, alpha, beta):
    if verbose:
        print("..................... Estimation Start .......................")
        print("state  = ", state)
        print("action = ", action)

    current_q_copy = Q_table[state].copy()
    Q_table[state][action] = np.inf

    update_trace = list()

    set_model_init_state(real_env, state, sample_len)
    
    model_state = model_env.reset()
    
    while model_state != None:
        req = model_state.req
        
        if hasattr(req, 'known_action') and req.known_action != None:
            model_action = req.known_action
            q_update = False
        else:
            model_action = get_greedy_action(model_env, model_state)
            q_update = True
       
        if model_action == Environment.Actions.no_action:
            print("Q = ", Q_table[model_state])
            print("s = ", model_state)
            print("a = ", model_action)
            sys.exit(-1)

        model_next_state, model_reward, model_done = model_env.step(model_state, model_action)
            
        if q_update:
            update_trace.append((model_state, model_next_state, model_reward, model_action, model_done))
 
        model_state = model_next_state

    #print("update_trace = ", update_trace)
    Q_table[state] = current_q_copy.copy()

    for i in range(len(update_trace) - 1, -1, -1):
        transition = update_trace[i]
        if transition[1] == None:
            continue #the last one
        
        td_update(transition[0], transition[3], transition[1], transition[2], alpha)
        if i > 0:
            td_update_rho(transition[0], transition[1], transition[2], beta)

    if verbose:
        print("..................... Estimation End .......................")
 

def init_new_state(state, real_env, alpha, beta):
    va = Environment.get_valid_actions(state)
    #Q_table[state] = [-1 * np.inf] * len(real_env.action_space)

    for action in va:
        #Q_table[state][action] = 0
        estimate_action_value(state, action, real_env, 10, alpha, beta)


def MBrLearning(env, state):
    if verbose:
        debug("sate =", state)
        print_Q(Q_table)
    
    global counter, epsilon, alpha, beta

    counter += 1
    if (counter + 1) % 100 == 0:
        alpha = max(0.05, alpha * 0.85)
        beta = max(0.05, beta * 0.85)
        epsilon = max(0.1, epsilon * 0.85)

        print("alpha = ", alpha, "beta = ", beta, "epsilon = ", epsilon)

    action, update_rho = get_action(state, epsilon)

    next_state, reward, done = env.step(state, action)
    if verbose:
        debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
    if done:
        return reward, None

    if not (next_state in Q_table):
        #init_new_state(next_state, env, alpha, beta)
        init_val(env, next_state)

    td_update(state, action, next_state, reward, alpha)

    if update_rho:
        td_update_rho(state, next_state, reward, beta)
 
    apply_model(env, next_state, 1.0, alpha, beta, 10, 10)
    init_new_state(next_state, env, alpha, beta)
    
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


