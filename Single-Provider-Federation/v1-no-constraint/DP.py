#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import random
import collections
import datetime
import QL
import heapq
import itertools 
import Environment
import parser
from Environment import debug, error, warning
from tester import test_policy


def arrival_after_reject(cs, arrival_index, total_rates):
    alives = cs[0]
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[arrival_index].lam / total_rates
    return {ns: p}


def departure_after_reject(cs, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[dep_index].mu / total_rates
    return {ns: p}


def arrival_after_no_action(cs, arrival_index, total_rates):
    return arrival_after_reject(cs, arrival_index, total_rates)


def departure_after_no_action(cs, dep_index, total_rates):
    return departure_after_reject(cs, dep_index, total_rates)


def arrival_after_federaion(cs, arrival_index, total_rates):
    #FIXME: update the inter-domain link usage
    return arrival_after_reject(cs, arrival_index, total_rates)


def departure_after_federation(cs, dep_index, total_rates):
    #FIXME: Update the inter-domain link usage
    return departure_after_reject(cs, dep_index, total_rates)


def arrival_after_accept(cs, accept_index, arrival_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[arrival_index].lam / total_rates
    return {ns: p}


def departure_after_accept(cs, accept_index, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[dep_index].mu / total_rates
    return {ns: p}


def get_total_rates(total_classes, state):
    alives = state[0]
    requests = state[1]
 
    total_rates = 0
    for j in range(total_classes):
        total_rates += Environment.traffic_loads[j].lam
        if alives[j] > 0:
            total_rates += Environment.traffic_loads[j].mu
    
    return total_rates


def pr(state, action):
    prob = {}
    alives = state[0]
    requests = state[1]
    capacity = Environment.compute_capacity(alives)

    total_rates = get_total_rates(Environment.total_classes, state)
    
    debug("State = ", state, ", action = ", action)

    active = 0
    for i in range(len(requests)):
        if requests[i] > 0:
            active += 1
    if active > 1:
        error("Error in requests: ", requests)
        sys.exit()

    if action == Environment.Actions.no_action:
        if active != 0:
            error("Error in actions")
            sys.exit()

        debug("No action")
        reward = 0
        
        for j in range(Environment.total_classes):
            prob.update(arrival_after_no_action(state, j, total_rates))
            
        for j in range(Environment.total_classes):
            if alives[j] > 0:
                prob.update(departure_after_no_action(state, j, total_rates))
 
    elif action == Environment.Actions.reject:
        debug("Reject")
        reward = 0
        
        for j in range(Environment.total_classes):
            prob.update(arrival_after_reject(state, j, total_rates))
            
        for j in range(Environment.total_classes):
            if alives[j] > 0:
                prob.update(departure_after_reject(state, j, total_rates))
            
    elif action == Environment.Actions.accept:
        active = 0
        for i in range(len(requests)):
            if requests[i] > 0:
                active += 1

        if active == 0:
            error("Accept for no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.domain.services[req_index].cpu)

            if capacity < Environment.domain.services[req_index].cpu:
                debug("Try to accept but no resource")
                #cannot be accepted, it is like reject but -inf for reward

                reward = -1 * np.inf

                for j in range(Environment.total_classes):
                    prob.update(arrival_after_reject(state, j, total_rates))
            
                for j in range(Environment.total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_reject(state, j, total_rates))
            else:
                debug("Accepting")
                reward = Environment.domain.services[req_index].revenue

                for j in range(Environment.total_classes):
                    prob.update(arrival_after_accept(state, req_index, j, total_rates))

                for j in range(Environment.total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_accept(state, req_index, j, total_rates))

    elif action == Environment.Actions.federate:
        active = 0
        for i in range(len(requests)):
            if requests[i] > 0:
                active += 1

        if active == 0:
            error("Federate no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.domain.services[req_index].cpu)

            debug("In this version, Federation is always possible")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            reward = Environment.domain.services[req_index].revenue - provider_domain.federation_costs[Environment.domain.services[req_index]]

            for j in range(Environment.total_classes):
                prob.update(arrival_after_federaion(state, j, total_rates))

            for j in range(Environment.total_classes):
                if alives[j] > 0:
                    prob.update(departure_after_federation(state, j, total_rates))

    else:
        error("Error: Unknown action")
        sys.exit()

    tp = 0
    for i in prob.keys():
        tp += prob[i]
    if abs(tp - 1.0) > 0.0001:
        error("Error in p: ", prob)
        sys.exit()

    debug("State = ", state, ", action = ", action)
    debug("\t Prob: ", prob)
    debug("\t Reward: ", reward)

    return prob, reward


def add_arrival_events(alives, all_states):
    requests = (0,) * len(alives)
    all_states.append((alives, requests))
    for i in range(len(alives)):
        tmp_requests = list(requests)
        tmp_requests[i] = 1
        tmp_requests = tuple(tmp_requests)
        all_states.append((alives, tmp_requests))


def rec_sate_generate(total_capacity, classes, current, alives, all_states):
    debug("---------------------------------------------")
    debug("total_capacity = ", total_capacity)
    debug("current = ", current)
    debug("alives   = ", alives)
    debug("all_states = ", all_states)

    if classes[current].cpu > total_capacity:
        zero_suffix = (0,) * (len(classes) - current)
        alives = alives + zero_suffix
        add_arrival_events(alives, all_states)
        return

    if current == len(classes) - 1:
        i = 0
        while (classes[current].cpu * i <= total_capacity):
            tmp_alives = alives + (i,)
            add_arrival_events(tmp_alives, all_states)
            i += 1

        return

    i = 0
    while classes[current].cpu * i <= total_capacity:
        tmp_alives = alives + (i,)
        rec_sate_generate(total_capacity - classes[current].cpu * i, classes, current + 1, tmp_alives, all_states)
        i += 1

def generate_all_states(c, tcs):
    all_states = []
    alives = ()
    rec_sate_generate(c, tcs, 0, alives, all_states)
    return all_states

    for i in range (int(c / tcs[0].cpu) + 1):
        for j in range(int(c / tcs[1].cpu) + 1):
            if i * tcs[0].cpu + j * tcs[1].cpu <= c:
                capacity = c - (i * tcs[0].cpu + j * tcs[1].cpu)
                alives = (i , j)
                
                requests = (0, 0)
                s = (alives, requests)
                res.append(s)
                
                requests = (0, 1)
                s = (alives, requests)
                res.append(s)
                
                requests = (1, 0)
                s = (alives, requests)
                res.append(s)
                

    debug("All States:", res)

    return res


def print_V(V, all_s):
    debug("**************************")
    for s in all_s:
        if V[s] != 0:
            debug("V[{}] = {}".format(s,V[s]))
    debug("==========================")


def print_policy(policy):
    op = collections.OrderedDict(sorted(policy.items()))
    for s in op:
        #debug(s, ": ", Environment.Actions(policy[s]))
        debug(s, ": ", op[s])

def init_random_policy(policy, all_states):
    for s in all_states:
        va = Environment.get_valid_actions(s)
        if len(va) == 1:
            policy.update({s: Environment.Actions.no_action})
        else:
            action = np.random.randint(0, len(va)) 
            policy.update({s: va[action]})

    debug("Init random policy")
    print_policy(policy)


def policy_evaluation(V, policy, all_states, gamma):
    while True:
        diff = 0
        for s in all_states:
            old_v = V[s]
            old_action = policy[s]
        
            debug("state = ", s, ", old_action = ", old_action, "old_v = ", old_v)
            va = Environment.get_valid_actions(s)
        
            if not(old_action in va):
                error("current actions is not valid action")
            
            new_v = 0
            p, r = pr(s, old_action)
            for ns in p.keys():
                new_v += (p[ns] * (r + gamma * V[ns]))
            V[s] = new_v
            debug("\t new_v = ", new_v)

            diff = max(diff, abs(old_v - V[s]))

        debug("diff = ", diff)
        if diff < 0.1:
            return


def policy_improvment(V, policy, all_states, gamma):
    policy_stable = True
    for s in all_states:
        old_action = policy[s]
        improve = np.zeros(Environment.total_actions)
        va = Environment.get_valid_actions(s)
        for a in va:
            p, r = pr(s, a)
            for ns in p.keys():
                improve[a] += (p[ns] * (r + gamma * V[ns]))
        
        new_val = -1 * np.inf
        best_action = None
        for a in va:
            if improve[a] > new_val:
                new_val = improve[a]
                best_action = a
        
        policy.update({s: best_action})
        debug("state = ", s, "best_action = ", best_action, "old_action = ", old_action)
        if best_action != old_action:
            policy_stable = False

    return policy_stable


def policy_iteration(gamma = 1.0):
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.domain.services)
    init_random_policy(policy, all_possible_state)
    gamma = 0.97
    while True:
        print_V(V, all_possible_state)
        policy_evaluation(V, policy, all_possible_state, gamma)
        if policy_improvment(V, policy, all_possible_state, gamma) == True:
            break

    return policy

def value_iteration(gamma = 1.0):
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.domain.services)
    loop = True
    while loop:
        random.shuffle(all_possible_state)
        gamma = 0.95 #* gamma
        debug("Gamma = ", gamma)
        max_diff = 0

        for s in all_possible_state:
            print_V(V, all_possible_state)
            improve = np.zeros(Environment.total_actions)
            va = Environment.get_valid_actions(s)

            for a in va:
                p, r = pr(s, a)
                for ns in p.keys():
                    debug("a  = ", a)
                    debug("ns = ", ns)
                    debug("p[ns] = ", p[ns])
                    debug("r = ", r)
                    debug("V[ns] = ", V[ns])
                    improve[a] += (p[ns] * (r + gamma * V[ns]))
                debug("improve[a] = ", improve[a])
            
            new_val = -1 * np.inf
            best_action = None
            for a in va:
                if improve[a] > new_val:
                    new_val = improve[a]
                    best_action = a

            debug("new_val = ", new_val)
            debug("best_action = ", best_action)

            policy.update({s: best_action})
            debug("--------------------------------------")

            diff = abs(V[s] - new_val)
            if diff > max_diff:
                max_diff = diff

            V[s] = new_val
            debug("Updated V[s] = ", V[s])

        if max_diff < 0.01:
            loop = False

    return policy


if __name__ == "__main__":

    sim_time = 70

    parser.parse_config("config.json")

    init_size = 20
    step = 20
    scale = 0

    i = 0

    while i <= scale:
        #Environment.domain.total_cpu = init_size + i * step
        i += 1
       
        print("Total Capacity = ", Environment.domain.total_cpu)
        all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.domain.services)
        print(*all_possible_state, sep = "\n") 
        
        '''
        t1 = datetime.datetime.now()
        print(t1)
        pi_policy = policy_iteration()
        t2 = datetime.datetime.now()
        print(t2)
        vi_policy = value_iteration() 
        t3 = datetime.datetime.now()
        print(t3)
        
        pi_profit = vi_profit = 0

        iterations = 20
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            pi_profit += test_policy(demands, pi_policy) / float(len(demands))
            vi_profit += test_policy(demands, vi_policy) / float(len(demands))


        print("Capacity = ", Environment.domain.total_cpu)
        print("PI Profit = ", pi_profit / iterations, "time = ", t2 - t1)
        print("VI Profit = ", vi_profit / iterations, "time = ", t3 - t2) 
        '''
