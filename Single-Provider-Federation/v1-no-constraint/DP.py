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
from tester import test_policy, test_greedy_random_policy

accuracy = 0.000000
NM = -1000000

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


def next_state_after_reject(cs):
    alives = cs[0]
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = 1.0
    return {ns: p}


def arrival_after_no_action(cs, arrival_index, total_rates):
    alives = cs[0]
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[arrival_index].lam / total_rates
    return {ns: p}


def departure_after_no_action(cs, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = Environment.traffic_loads[dep_index].mu / total_rates
    return {ns: p}


def arrival_after_federaion(cs, arrival_index, total_rates):
    return arrival_after_reject(cs, arrival_index, total_rates)


def departure_after_federation(cs, dep_index, total_rates):
    return departure_after_reject(cs, dep_index, total_rates)


def next_state_after_federate(cs):
    return next_state_after_reject(cs)


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

def next_state_after_accept(cs, accept_index):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = 1.0
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
        prob.update(next_state_after_reject(state))
        
    elif action == Environment.Actions.accept:
        if active == 0:
            error("Accept for no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            capacity = Environment.compute_capacity(alives)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)

            if capacity < Environment.traffic_loads[req_index].service.cpu:
                debug("Try to accept but no resource")
                
                #cannot be accepted, it is like reject but -inf for reward
                reward = -1 * np.inf
                prob.update(next_state_after_reject(state))

            else:
                debug("Accepting")
                reward = Environment.traffic_loads[req_index].service.revenue
                prob.update(next_state_after_accept(state, req_index))

    elif action == Environment.Actions.federate:
        if active == 0:
            error("Federate no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            capacity = Environment.compute_capacity(alives)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)

            debug("In this version, Federation is always possible")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            reward = Environment.traffic_loads[req_index].service.revenue - provider_domain.federation_costs[Environment.traffic_loads[req_index].service]

            prob.update(next_state_after_federate(state))

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


def pr_old(state, action):
    prob = {}
    alives = state[0]
    requests = state[1]

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
        if active == 0:
            error("Accept for no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            capacity = Environment.compute_capacity(alives)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)

            if capacity < Environment.traffic_loads[req_index].service.cpu:
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
                reward = Environment.traffic_loads[req_index].service.revenue

                for j in range(Environment.total_classes):
                    prob.update(arrival_after_accept(state, req_index, j, total_rates))

                for j in range(Environment.total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_accept(state, req_index, j, total_rates))

    elif action == Environment.Actions.federate:
        if active == 0:
            error("Federate no demand!!!")
            error("Invalid action")
            sys.exit()
        else:
            req_index = np.argmax(requests)
            capacity = Environment.compute_capacity(alives)
            
            debug("alives = ", requests)
            debug("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", Environment.traffic_loads[req_index].service.cpu)

            debug("In this version, Federation is always possible")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            reward = Environment.traffic_loads[req_index].service.revenue - provider_domain.federation_costs[Environment.traffic_loads[req_index].service]

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


def generate_all_states(c, loads):
    all_states = []
    alives = ()
    tcs = []

    for load in loads:
        tcs.append(load.service)

    rec_sate_generate(c, tcs, 0, alives, all_states)
    return all_states


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
        print(s, ": ", op[s])
    #debug("----------------------------")
    print("----------------------------")


def init_random_policy(policy, all_states):
    for s in all_states:
        va = Environment.get_valid_actions(s)
        if len(va) == 1:
            policy.update({s: Environment.Actions.no_action})
        else:
            action = np.random.randint(0, len(va)) 
            policy.update({s: va[action]})

    debug("Init random policy")
    #print_policy(policy)

policy_iteration_accuracy = 0.0001
def policy_evaluation(V, policy, all_states, gamma, Pr, R):
    while True:
        diff = 0
        for s in all_states:
            old_v = V[s]
            old_action = policy[s]
        
            debug("\n state = ", s, ", old_action = ", old_action, "old_v = ", old_v)
            va = Environment.get_valid_actions(s)
        
            if not(old_action in va):
                error("current actions is not valid action")
                sys.exit(-1)
            
            new_v = 0
            #p, r = pr(s, old_action)
            p = Pr[s][old_action]
            r = R[s][old_action]
            print("\t p = ", p)
            print("\t r = ", r)
            for ns in p.keys():
                new_v += (p[ns] * (r + gamma * V[ns]))
            V[s] = new_v
            debug("\t new_v = ", new_v)

            diff = max(diff, abs(old_v - V[s]))

        debug("diff = ", diff)
        if diff < policy_iteration_accuracy:
            return


def policy_improvment(V, policy, all_states, gamma, Pr, R):
    policy_stable = True
    for s in all_states:
        debug("\n state = ", s)
        old_action = policy[s]
        improve = np.zeros(Environment.total_actions)
        va = Environment.get_valid_actions(s)
        for a in va:
            #p, r = pr(s, a)
            p = Pr[s][a]
            r = R[s][a]
            for ns in p.keys():
                debug("a  = ", a)
                debug("ns = ", ns)
                debug("p[ns] = ", p[ns])
                debug("r = ", r)
                debug("V[ns] = ", V[ns])
             
                improve[a] += (p[ns] * (r + gamma * V[ns]))
            debug("\t improve[",a,"] = ", improve[a])
        
        new_val = -1 * np.inf
        best_action = None
        for a in va:
            if improve[a] > new_val:
                new_val = improve[a]
                best_action = a
        
        policy.update({s: best_action})
        debug("\t best_action = ", best_action, "old_action = ", old_action)
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
    num_states, tuple_to_num, num_to_tuple = state_tuple_to_num(all_possible_state)
    num_actions = action_enum_to_num(Environment.Actions)
    
    Pr, R = compute_Pr_R(num_states, num_actions, tuple_to_num, num_to_tuple, Environment.Actions)
    
    print("Before Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    
    Pr, R, reduce_num_to_num = correct_mdp(Pr, R, num_actions, num_to_tuple, tuple_to_num, Environment.Actions)
 
    print("After Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    
    reduced_all_possible_state = []
    for s in range(len(Pr)):
        num_s = reduce_num_to_num[s]
        debug("num_s = ", num_s)
        tuple_s = num_to_tuple[num_s]
        debug("tuple_s = ", tuple_s)
        reduced_all_possible_state.append(tuple_s)

    print("----------- reduced_all_possible_state ---------")
    print(reduced_all_possible_state)

    new_Pr = {}
    new_R  = {}
    for s in range(len(Pr)):
        tuple_s = num_to_tuple[reduce_num_to_num[s]]
        new_Pr.update({tuple_s: {}})
        new_R.update({tuple_s: {}})
        for a in range(len(Pr[s])):
            new_R[tuple_s].update({Environment.Actions(a): R[s][a]})
            new_Pr[tuple_s].update({Environment.Actions(a): {}})
            for ns in range(len(Pr[s][a])):
                tuple_ns = num_to_tuple[reduce_num_to_num[ns]]
                new_Pr[tuple_s][Environment.Actions(a)].update({tuple_ns: Pr[s][a][ns]})

    print("------- new_Pr ------------")
    print(new_Pr)
    print("------- new_R  ------------")
    print(new_R)

    init_random_policy(policy, reduced_all_possible_state)
    
    while True:
        debug("********** At Beginning ************")
        print_V(V, all_possible_state)
        print_policy(policy)
        
        policy_evaluation(V, policy, reduced_all_possible_state, gamma, new_Pr, new_R)
        
        debug("********** After Evaluation ************")
        print_V(V, all_possible_state)
        print_policy(policy)
        
        stable = policy_improvment(V, policy, reduced_all_possible_state, gamma, new_Pr, new_R)
        
        debug("********** After improve ************")
        print_V(V, all_possible_state)
        print_policy(policy)

        if stable == True:
            break

    return policy

def value_iteration(gamma):
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)
    loop = True
    while loop:
        random.shuffle(all_possible_state)
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

def is_active_request(state):
    alives   = state[0]
    requests = state[1]

    for i in range(len(requests)):
        if requests[i] != 0:
            return True
    
    else:
        return False


def action_enum_to_num(Actions):
    num_actions = [e.value for e in Actions]
    return num_actions


def get_next_actives(state, Pr, R, num_to_tuple, tuple_to_num, Actions):
    debug("get_next_actives: state = ", state)
    no_action_next_states = {}
    state_tuple = num_to_tuple[state]
    va_tuple = Environment.get_valid_actions(state_tuple)
    if Actions.accept in va_tuple or Actions.federate in va_tuple or Actions.reject in va_tuple:
        print("Error in get_next_actives")
        sys.exit()

    actions = action_enum_to_num(va_tuple)

    for action in actions:
        for ns in range(len(Pr[state][action])):
            pr = Pr[state][action][ns]

            if pr > 0:
                next_state_tuple = num_to_tuple[ns]
                if is_active_request(next_state_tuple):
                    total_pr = 0
                    if ns in no_action_next_states:
                        total_pr = no_action_next_states[ns]

                    total_pr += pr
                    no_action_next_states.update({ns: total_pr})
                else:
                    next_actives_list = get_next_actives(ns, Pr, R, num_to_tuple, tuple_to_num, Actions)
                    for s in next_actives_list.keys():
                        p = next_actives_list[s] * pr
                        if s in no_action_next_states:
                            p += no_action_next_states[s]
                        next_actives_list.update({s: p})

                    no_action_next_states.update(next_actives_list)

    return no_action_next_states


def start_finding_next_active_states(state, Pr, R, num_to_tuple, tuple_to_num, Actions):
    debug("Start: state = ", num_to_tuple[state])

    state_tuple = num_to_tuple[state]
    va_tuple = Environment.get_valid_actions(state_tuple)
    va = action_enum_to_num(va_tuple)
    all_next_active_states = [None] * len(Actions)

    for action in va:
        for ns in range(len(Pr[state][action])):
            pr = Pr[state][action][ns]
            if pr > 0:
                next_state_tuple = num_to_tuple[ns]
                if is_active_request(next_state_tuple):
                    print("Error in Pr")
                    sys.exit()

                next_list = get_next_actives(ns, Pr, R, num_to_tuple, tuple_to_num, Actions)
                for s in next_list:
                    p = next_list[s] * pr
                    next_list.update({s: p})

                all_next_active_states[action] = next_list

    
    debug("\t all_next_active_states: ", all_next_active_states)
    return all_next_active_states


def correct_mdp(extra_state_Pr, extra_state_R, actions, num_to_tuple, tuple_to_num, Actions):
    Pr_dict = {}
    num_to_reduce_num = {}
    reduce_num_to_num = {}

    #scan active states
    for s in range(len(extra_state_Pr)):
        state_tuple = num_to_tuple[s]
        if is_active_request(state_tuple):
            debug("Active Request State: ", state_tuple)
            next_states = start_finding_next_active_states(s, extra_state_Pr, extra_state_R, num_to_tuple, tuple_to_num, Actions)
            Pr_dict.update({s: next_states})

    print("-------------- Pr_dict ----------------")
    print(Pr_dict)

    new_index = 0
    for active_state in Pr_dict.keys():
        num_to_reduce_num.update({active_state: new_index})
        reduce_num_to_num.update({new_index: active_state})
        new_index += 1

    print("num_to_reduce_num: ", num_to_reduce_num)
    print("reduce_num_to_num: ", reduce_num_to_num)

    Pr = [None] * len(reduce_num_to_num)
    for old_s in Pr_dict.keys():
        s = num_to_reduce_num[old_s]
        Pr[s] = [None] * len(actions)
        for a in actions:
            Pr[s][a] = [None] * len(reduce_num_to_num)
            for old_ns in Pr_dict.keys():
                ns = num_to_reduce_num[old_ns]
                Pr[s][a][ns] = 0

    R = [None] * len(Pr_dict.keys())
    for old_s in Pr_dict.keys():
        s = num_to_reduce_num[old_s]
        R[s] = [None] * len(actions)
        for a in actions:
            R[s][a] = NM

    reduced_states = Pr_dict.keys()
    for s in reduced_states:
        new_s = num_to_reduce_num[s]
        for a in actions:
            probs = Pr_dict[s][a]
            if probs != None:
                for ns in probs.keys():
                    new_ns = num_to_reduce_num[ns]
                    Pr[new_s][a][new_ns] = probs[ns]
            
            R[new_s][a] = extra_state_R[s][a]

    for s in range(len(Pr)):
        for a in range(len(Pr[s])):
            pr_sum = 0
            for ns in range(len(Pr[s][a])):
                pr_sum += Pr[s][a][ns]

            if (pr_sum > 0 and abs(pr_sum - 1.0) > 0.000001):
                print("Error in Pr, 1 != sum_ns pr[s][a] = ", pr_sum)
                sys.exit()


    return Pr, R, reduce_num_to_num


if __name__ == "__main__":


    parser.parse_config("config.json")
    
    init_size = 0.05
    step = 0.1
    scale = 0

    i = 0
    sim_time = 100
    while i <= scale:
        gamma = i * step + init_size
        i += 1
       
        #pi_policy = policy_iteration(gamma)
        pi_policy = policy_iteration()
        #pi_policy = gen_greedy_policy()
        print_policy(pi_policy)
        
        pi_profit = greedy_profit = 0
        iterations = 20
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            pi_profit += test_policy(demands, pi_policy) / float(len(demands))
            greedy_profit += test_greedy_random_policy(demands, 1.0) / float(len(demands))


        print("gamma = ", gamma)
        print("PI Profit     = ", pi_profit / iterations)
        print("Greedy Profit = ", greedy_profit / iterations) 
