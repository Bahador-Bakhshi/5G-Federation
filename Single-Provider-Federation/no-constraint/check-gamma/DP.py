#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import random
import collections
import datetime
from operator import add
#import QL
import heapq
import itertools 
import Environment
import parser
from Environment import debug, error, warning
from tester import test_policy, test_greedy_random_policy

accuracy = 0.000000
NM = -1000000

def arrival_events(next_state_alives, arrival_index):
    arrivals = [0] * len(next_state_alives)
    arrivals[arrival_index] = 1
    ns = (tuple(next_state_alives), tuple(arrivals))
    total_rates = get_total_rates(next_state_alives)
    p = Environment.traffic_loads[arrival_index].lam / total_rates
    return {ns: p}


def departure_events(next_state_alives, dep_index):
    departures = [0] * len(next_state_alives)
    departures[dep_index] = -1
    ns = (tuple(next_state_alives), tuple(departures))
    total_rates = get_total_rates(next_state_alives)
    p = (next_state_alives[dep_index] * Environment.traffic_loads[dep_index].mu) / total_rates
    return {ns: p}


def get_total_rates(state_alives):
    
    total_rates = 0
    for j in range(len(state_alives)):
        total_rates += Environment.traffic_loads[j].lam
        total_rates += state_alives[j] * Environment.traffic_loads[j].mu
    
    return total_rates


def pr(state, action):
    prob = {}
    alives = state[0]
    events = state[1]

    #debug("State = ", state, ", action = ", action)

    active = 0
    for i in range(len(events)):
        active += abs(events[i])

    if active != 1:
        error("Error in events:", events)
        sys.exit()

    if action == Environment.Actions.no_action:
        if not(-1 in events):
            error("Error in actions no_action")
            sys.exit()

        #debug("No action")
        reward = 0
        new_state_alives = alives
        new_state_alives = list(map(add, new_state_alives, events))

    elif action == Environment.Actions.reject:
        if not(1 in events):
            error("Error in actions reject")
            sys.exit()

        #debug("Reject")
        reward = 0
        new_state_alives = alives
        
    elif action == Environment.Actions.accept:
        if not(1 in events):
            error("Error in actions accept")
            sys.exit()

        req_index = np.argmax(events)
        capacity = Environment.compute_capacity(alives)
            
        #debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)

        if capacity < Environment.traffic_loads[req_index].service.cpu:
            #debug("Try to accept but no resource")
            #cannot be accepted, it is like reject but -inf for reward
            reward = -1 * np.inf
            new_state_alives = alives

        else:
            #debug("Accepting")
            reward = Environment.traffic_loads[req_index].service.revenue
            new_state_alives = alives
            new_state_alives = list(map(add, new_state_alives, events))

    elif action == Environment.Actions.federate:
        if not(1 in events):
            error("Error in actions Federate")
            sys.exit()

        req_index = np.argmax(events)
        capacity = Environment.compute_capacity(alives)
            
        #debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)
        #debug("In this version, Federation is always possible")
        provider_domain = Environment.providers[0] # in this version, there is only one provider
        reward = Environment.traffic_loads[req_index].service.revenue - provider_domain.federation_costs[Environment.traffic_loads[req_index].service]

        new_state_alives = alives

    else:
        error("Error: Unknown action")
        sys.exit()


    for j in range(Environment.total_classes):
        prob.update(arrival_events(new_state_alives, j))
            
    for j in range(Environment.total_classes):
        if new_state_alives[j] > 0:
            prob.update(departure_events(new_state_alives, j))
 

    tp = 0
    for i in prob.keys():
        tp += prob[i]
    if abs(tp - 1.0) > 0.0001:
        error("Error in p: ", prob)
        sys.exit()

    #debug("State = ", state, ", action = ", action)
    #debug("\t Prob: ", prob)
    #debug("\t Reward: ", reward)

    return prob, reward


def add_rand_events(alives, all_states):
    rand_events = (0,) * len(alives)
    for i in range(len(alives)):
        tmp_events = list(rand_events)
        tmp_events[i] = 1
        tmp_events = tuple(tmp_events)
        all_states.append((alives, tmp_events))

    for i in range(len(alives)):
        if alives[i] > 0:
            tmp_events = list(rand_events)
            tmp_events[i] = -1
            tmp_events = tuple(tmp_events)
            all_states.append((alives, tmp_events))


def rec_sate_generate(total_capacity, classes, current, alives, all_states):
    #debug("---------------------------------------------")
    #debug("total_capacity = ", total_capacity)
    #debug("current = ", current)
    #debug("alives   = ", alives)
    #debug("all_states = ", all_states)
    
    if current == len(classes) - 1:
        i = 0
        while (classes[current].cpu * i <= total_capacity):
            tmp_alives = alives + (i,)
            add_rand_events(tmp_alives, all_states)
            i += 1

        return

    i = 0
    while classes[current].cpu * i <= total_capacity:
        tmp_alives = alives + (i,)
        rec_sate_generate(total_capacity - classes[current].cpu * i, classes, current + 1, tmp_alives, all_states)
        i += 1


def generate_all_states(c, loads):
    all_states = []
    alives = ()
    tcs = []

    for load in loads:
        tcs.append(load.service)

    rec_sate_generate(c, tcs, 0, alives, all_states)
    return all_states


def print_V(V, all_s):
    ##debug("**************************")
    print("**************************")
    for s in all_s:
        if V[s] != 0:
            ##debug("V[{}] = {}".format(s,V[s]))
            print("V[{}] = {}".format(s,V[s]))
    ##debug("==========================")
    print("==========================")


def print_policy(policy):
    ##debug("**************************")
    print("**************************")
    op = collections.OrderedDict(sorted(policy.items()))
    for s in op:
        ##debug(s, ": ", Environment.Actions(policy[s]))
        print(s, ": ", Environment.Actions(policy[s]))
    ##debug("----------------------------")
    print("----------------------------")


def init_random_policy(policy, all_states):
    for s in all_states:
        va = Environment.get_valid_actions(s)
        if len(va) == 1:
            policy.update({s: Environment.Actions.no_action})
        else:
            action = np.random.randint(0, len(va)) 
            policy.update({s: va[action]})

    #debug("Init random policy")
    #print_policy(policy)

policy_iteration_accuracy = 0.0001
def policy_evaluation(V, policy, all_states, gamma):
    while True:
        diff = 0
        for s in all_states:
            old_v = V[s]
            old_action = policy[s]
        
            #debug("\n state = ", s, ", old_action = ", old_action, "old_v = ", old_v)
            va = Environment.get_valid_actions(s)
        
            if not(old_action in va):
                error("current actions is not valid action")
                sys.exit(-1)
            
            new_v = 0
            p, r = pr(s, old_action)
            #debug("\t p = ", p)
            #debug("\t r = ", r)
            for ns in p.keys():
                if Environment.is_active_state(s):
                    new_v += (p[ns] * (r + gamma * V[ns]))
                else:
                    new_v += (p[ns] * (r + V[ns]))

            V[s] = new_v
            #debug("\t new_v = ", new_v)

            diff = max(diff, abs(old_v - V[s]))

        #debug("diff = ", diff)
        if diff < policy_iteration_accuracy:
            return


def policy_improvment(V, policy, all_states, gamma):
    policy_stable = True
    for s in all_states:
        #debug("\n state = ", s)
        old_action = policy[s]
        improve = np.zeros(Environment.total_actions)
        va = Environment.get_valid_actions(s)
        
        for a in va:
            p, r = pr(s, a)
            for ns in p.keys():
                #debug("a  = ", a)
                #debug("ns = ", ns)
                #debug("p[ns] = ", p[ns])
                #debug("r = ", r)
                #debug("V[ns] = ", V[ns])
             
                improve[a] += (p[ns] * (r + gamma * V[ns]))
            #debug("\t improve[",a,"] = ", improve[a])
        
        new_val = -1 * np.inf
        best_action = None
        for a in va:
            if improve[a] > new_val:
                new_val = improve[a]
                best_action = a
        
        policy.update({s: best_action})
        #debug("\t best_action = ", best_action, "old_action = ", old_action)
        if (best_action != old_action) and (abs(improve[best_action] - improve[old_action]) > policy_iteration_accuracy):
            policy_stable = False

    return policy_stable


def state_tuple_to_num(tuple_states):
    index = 0
    num_states = []
    tuple_to_num = {}
    num_to_tuple = {}

    for s in tuple_states:
        num_states.append(index)
        tuple_to_num.update({s: index})
        num_to_tuple.update({index: s})
        index += 1

    return num_states, tuple_to_num, num_to_tuple


def compute_Pr_R(states, actions, tuple_to_num, num_to_tuple, Actions):

    Pr = [None] * len(states)
    for s in states:
        Pr[s] = [None] * len(actions)
        for a in actions:
            Pr[s][a] = [None] * len(states)
            for ns in states:
                Pr[s][a][ns] = 0
    
    R = [None] * len(states)
    for s in states:
        R[s] = [None] * len(actions)
        for a in actions:
            R[s][a] = NM

    for s in states:
        state_tuple = num_to_tuple[s]
        va_tuple = Environment.get_valid_actions(state_tuple)
        va = action_enum_to_num(va_tuple)
        for a in va:
            action_code = Actions(a)

            p, r = pr(state_tuple, action_code)

            R[s][a] = r

            for ns_tuple in p.keys():
                ns = tuple_to_num[ns_tuple]
                Pr[s][a][ns] = p[ns_tuple] 
    
    return Pr, R



def policy_iteration(gamma):
    #V = defaultdict(lambda: np.random.uniform(100, 500))
    V = defaultdict(lambda: 0)
    policy = {}
    
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)
    #debug("---------------  all_possible_state  --------------------------")
    #debug(all_possible_state)
    
    init_random_policy(policy, all_possible_state)
    
    while True:
        #debug("********** At Beginning ************")
        #print_V(V, all_possible_state)
        #print_policy(policy)
        
        policy_evaluation(V, policy, all_possible_state, gamma)
        
        #debug("********** After Evaluation ************")
        #print_V(V, all_possible_state)
        #print_policy(policy)
        
        stable = policy_improvment(V, policy, all_possible_state, gamma)
        
        #debug("********** After improve ************")
        #print_V(V, all_possible_state)
        #print_policy(policy)

        if stable == True:
            break


    debug("********** DP Final ************")
    print_V(V, all_possible_state)
    print_policy(policy)

    return policy

def value_iteration(gamma):
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)
    loop = True
    while loop:
        random.shuffle(all_possible_state)
        #debug("Gamma = ", gamma)
        max_diff = 0

        for s in all_possible_state:
            print_V(V, all_possible_state)
            improve = np.zeros(Environment.total_actions)
            va = Environment.get_valid_actions(s)

            for a in va:
                p, r = pr(s, a)
                for ns in p.keys():
                    #debug("a  = ", a)
                    #debug("ns = ", ns)
                    #debug("p[ns] = ", p[ns])
                    #debug("r = ", r)
                    #debug("V[ns] = ", V[ns])
                    improve[a] += (p[ns] * (r + gamma * V[ns]))
                #debug("improve[a] = ", improve[a])
            
            new_val = -1 * np.inf
            best_action = None
            for a in va:
                if improve[a] > new_val:
                    new_val = improve[a]
                    best_action = a

            #debug("new_val = ", new_val)
            #debug("best_action = ", best_action)

            policy.update({s: best_action})
            #debug("--------------------------------------")

            diff = abs(V[s] - new_val)
            if diff > max_diff:
                max_diff = diff

            V[s] = new_val
            #debug("Updated V[s] = ", V[s])

        if max_diff < 0.01:
            loop = False

    return policy


def gen_greedy_policy():
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)

    for state in all_possible_state:
        current_alives = state[0]
        current_requests = state[1]
        current_capacity = Environment.compute_capacity(current_alives)
        
        count = 0
        req_index = 0
        for i in range(len(current_requests)):
            if current_requests[i] != 0:
                count += 1
                req_index = i
            
        if count > 1:
            error("Error in requests = ", current_requests)
            sys.exit()

        if count == 0: 
            policy.update({state: Environment.Actions.no_action})
        else:
            req = Environment.traffic_loads[req_index].service
            if current_capacity >= req.cpu:
                policy.update({state: Environment.Actions.accept})
            else:
                policy.update({state: Environment.Actions.federate})
        
    return policy


if __name__ == "__main__":

    gamma = 0.995
    parser.parse_config("config.json")
   
    init_size = 10
    step = 50
    scale = 1

    i = 0
    sim_time = 100
    while i <= scale:
        Environment.domain.total_cpu = init_size + i * step
        i += 1
       
        pi_policy = policy_iteration(gamma)
        print("------------- PI Policy -----------------")
        print_policy(pi_policy)
        
        env = Environment.Env(Environment.domain.total_cpu, sim_time)
        ql_policy = QL.qLearning(env, 100, 1)
        print("------------- QL Policy -----------------")
        print_policy(ql_policy)


        pi_profit = ql_profit = gr_profit = 0
        iterations = 20
        for j in range(iterations):
        
            demands = Environment.generate_req_set(5 * sim_time)
            Environment.print_reqs(demands)

            p, a, f = test_policy(demands, pi_policy)
            pi_profit += p / float(len(demands))

            p, a, f = test_policy(demands, ql_policy)
            ql_profit += p / float(len(demands))

            p, a, f =  test_greedy_random_policy(demands, 1.0)
            gr_profit += p / float(len(demands))

        print("Profit CPU = ", Environment.domain.total_cpu)
        print("PI Profit  = ", pi_profit / iterations)
        print("QL Profit  = ", ql_profit / iterations)
        print("Gr Profit  = ", gr_profit / iterations) 
        print("", flush=True)
