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
from Environment import debug, error, warning, verbose, State
#from tester import test_policy, test_greedy_random_policy

def arrival_events(all_domains_alives, arrival_index, base_prob):
    arrivals = [0] * len(Environment.traffic_loads)
    arrivals[arrival_index] = 1
    ns = State(len(Environment.traffic_loads))
    ns.domains_alives = all_domains_alives.copy()
    ns.arrivals_departures = tuple(arrivals)

    total_rates = get_total_rates(all_domains_alives)
    p = Environment.traffic_loads[arrival_index].lam / total_rates
    p *= base_prob
    return {ns: p}


def departure_events(all_domains_alives, dep_index, base_prob):
    total_dep_rate = 0.0
    for d in range(len(all_domains_alives)):
        total_dep_rate += all_domains_alives[d][dep_index]
    
    if total_dep_rate == 0:
        return None

    departures = [0] * len(Environment.traffic_loads)
    departures[dep_index] = -1
    ns = State(len(Environment.traffic_loads))
    ns.domains_alives = all_domains_alives.copy()
    ns.arrivals_departures = tuple(departures)

    total_rates = get_total_rates(all_domains_alives)
    p = (total_dep_rate * Environment.traffic_loads[dep_index].mu) / total_rates
    p *= base_prob
    return {ns: p}


def get_total_rates(all_domains_alives):
    
    total_rates = 0

    for j in range(len(Environment.traffic_loads)):
        total_rates += Environment.traffic_loads[j].lam

    for d in range(len(all_domains_alives)):
        for j in range(len(all_domains_alives[d])):
            total_rates += all_domains_alives[d][j] * Environment.traffic_loads[j].mu
    
    return total_rates

def get_next_state_pr(state, action, next_state):
    if action == Environment.Actions.reject or action == Environment.Actions.accept or action == Environment.Actions.federate:
        bias_pr = 1.0
    else:
        depart_tc_in_state = state.arrivals_departures.index(-1)
        depart_domain = -1
        total_depart = 0.0

        for d in range(len(state.domains_alives)):
            total_depart += state.domains_alives[d][depart_tc_in_state]
            if (state.domains_alives[d][depart_tc_in_state] - 1) == next_state.domains_alives[d][depart_tc_in_state]:
                depart_domain = d
        
        bias_pr = state.domains_alives[depart_domain][depart_tc_in_state] / total_depart
            

    total_rates = get_total_rates(next_state.domains_alives)
    
    for i in range(len(next_state.arrivals_departures)):
        if next_state.arrivals_departures[i] == 1:
            return bias_pr * Environment.traffic_loads[i].lam / (total_rates * 1.0)
        
        if next_state.arrivals_departures[i] == -1:
            dep_rate = 0
            for d in range(len(next_state.domains_alives)):
                dep_rate += next_state.domains_alives[d][i]
            dep_rate *= Environment.traffic_loads[i].mu 
            return bias_pr * dep_rate / (total_rates * 1.0)


def print_trans_prob(p):
    print("---------- transition probabilities -----------")
    for s in p:
        print(s,": ", p[s]) 


def pr(state, action):
    prob = {}

    domains_alives_list = []
    domains_alives_rate = []

    current_domains_alives = state.domains_alives.copy()
    events = state.arrivals_departures

    if verbose:
        debug("State = ", state, ", action = ", action)

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
        dep_index = np.argmin(events)
        total_alives = 0.0
        for d in range(len(current_domains_alives)):
            total_alives += current_domains_alives[d][dep_index]

        for d in range(len(current_domains_alives)):
            if current_domains_alives[d][dep_index] > 0:
                new_domains_alives = current_domains_alives.copy()
                state_alives = new_domains_alives[d]
                state_alives = tuple(map(add, state_alives, events))
                new_domains_alives[d] = state_alives

                domains_alives_list.append(new_domains_alives)
                domains_alives_rate.append(current_domains_alives[d][dep_index] / total_alives)
                
    elif action == Environment.Actions.reject:
        if not(1 in events):
            error("Error in actions reject")
            sys.exit()

        #debug("Reject")
        reward = 0

        domains_alives_list.append(current_domains_alives)
        domains_alives_rate.append(1.0)
                
    elif action == Environment.Actions.accept:
        if not(1 in events):
            error("Error in actions accept")
            sys.exit()

        req_index = np.argmax(events)
        domain_index = State.local_domain
            
        if not Environment.can_be_deployed(1, req_index, domain_index, 1, current_domains_alives):
            error("Invalid accept action")
            sys.exit(-1)

        else:
            if verbose:
                debug("Accepting")
            
            reward = Environment.traffic_loads[req_index].service.revenue
            new_domains_alives = current_domains_alives.copy()
            domain_state_alives = new_domains_alives[State.local_domain]
            domain_state_alives = tuple(map(add, domain_state_alives, events))
            new_domains_alives[State.local_domain] = domain_state_alives

            domains_alives_list.append(new_domains_alives)
            domains_alives_rate.append(1.0)


    elif action == Environment.Actions.federate:
        if not(1 in events):
            error("Error in actions Federate")
            sys.exit()

        req_index = np.argmax(events)

        #In this version, there is only one provider
        domain_index = 1
        provider_domain = Environment.providers[domain_index]

        if Environment.can_be_deployed(1, req_index, domain_index, provider_domain.reject_threshold, current_domains_alives):
            if verbose:
                debug("Try to federate")
            
            federation_cost_scale = 0

            if Environment.can_be_deployed(1, req_index, domain_index, 1, current_domains_alives):
                federation_cost_scale = 1
            else:
                federation_cost_scale = provider_domain.overcharge
            
            reward = Environment.traffic_loads[req_index].service.revenue - provider_domain.federation_costs[Environment.traffic_loads[req_index].service] * federation_cost_scale

            new_domains_alives = current_domains_alives.copy()
            domain_state_alives = new_domains_alives[domain_index]
            domain_state_alives = tuple(map(add, domain_state_alives, events))
            new_domains_alives[domain_index] = domain_state_alives

            domains_alives_list.append(new_domains_alives)
            domains_alives_rate.append(1.0)
        else:
            error("Invalid federation, there is not any resource for federation")
            sys.exit(-1)

    else:
        error("Error: Unknown action")
        sys.exit()


    for i in range(len(domains_alives_list)):
        all_domains_alives = domains_alives_list[i]
        base_prob = domains_alives_rate[i]

        for j in range(Environment.total_classes):
            prob.update(arrival_events(all_domains_alives, j, base_prob))
            
        for j in range(Environment.total_classes):
            res = departure_events(all_domains_alives, j, base_prob)
            if res != None:
                prob.update(res)

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


def add_arrive_depart_events(all_domains_alives, domain_index, all_states):
    if verbose:
        debug("---------- add_arrive_depart_events ----------")
        debug("\t all_domains_alives = ", all_domains_alives)
        debug("\t domain_index = ", domain_index)

    tc_num = len(all_domains_alives[0])
    for i in range(tc_num):
        state = State(tc_num)
        for j in range(len(all_domains_alives)):
            state.domains_alives[j] = tuple(all_domains_alives[j])

        arrive_depart_events = [0] * tc_num
        arrive_depart_events[i] = 1
        state.arrivals_departures = tuple(arrive_depart_events)

        all_states.append(state)

    for i in range(tc_num):
        for d in range(Environment.providers_num + 1):
            if all_domains_alives[d][i] > 0:
                state = State(tc_num)
                for j in range(len(all_domains_alives)):
                    state.domains_alives[j] = tuple(all_domains_alives[j])

                arrive_events = [0] * tc_num
                state.arrivals = tuple(arrive_events)

                arrive_depart_events = [0] * tc_num
                arrive_depart_events[i] = -1
                state.arrivals_departures = tuple(arrive_depart_events)
                
                if not(state in all_states):
                    all_states.append(state)


def is_sufficient_resource(instance_num, service, domain_capacities):
    for index in range(len(service.resources)):
        if (service.resources[index] * instance_num) > domain_capacities[index]:
            return False

    return True


def per_domain_state_generate(domain_capacities,  domain_index, classes, current, all_domains_alives, all_states):
    if verbose:
        debug("------------------ per_domain_state_generate -----------------")
        debug("Domain capacity = ", domain_capacities)
        debug("current = ", current)
        debug("alives   = ", all_domains_alives)
        debug("all_states = ", all_states)
   
    if current == len(classes) - 1:
        i = 0
        while is_sufficient_resource(i, classes[current], domain_capacities):
            tmp_all_domains_alives = all_domains_alives.copy()
            alives_list = list(tmp_all_domains_alives[domain_index])
            alives_list[current] = i
            tmp_all_domains_alives[domain_index] = tuple(alives_list)
            add_arrive_depart_events(tmp_all_domains_alives, domain_index, all_states)
            i += 1

        return

    i = 0
    while is_sufficient_resource(i, classes[current], domain_capacities):
        tmp_all_domains_alives = all_domains_alives.copy()
        alives_list = list(tmp_all_domains_alives[domain_index])
        alives_list[current] = i
        tmp_all_domains_alives[domain_index] = tuple(alives_list)
        tmp_domain_capacities = domain_capacities.copy()
        Environment.deploy_service(i, classes[current], tmp_domain_capacities)
        per_domain_state_generate(tmp_domain_capacities, domain_index, classes, current + 1, tmp_all_domains_alives, all_states)
        i += 1


def all_possible_alives(classes, capacities, index, alives, result):
    if index == len(classes) - 1:
        i = 0
        while is_sufficient_resource(i, classes[index], capacities):
            tmp_alives = alives + (i,)
            result.append(tmp_alives)
            i += 1
        return

    i = 0
    while is_sufficient_resource(i, classes[index], capacities):
        temp_alives = alives + (i,)
        tmp_capacities = capacities.copy()
        Environment.deploy_service(i, classes[index], tmp_capacities)
        all_possible_alives(classes, tmp_capacities, index + 1, temp_alives, result)
        i += 1


def rec_state_generate(all_domains_capacities, all_domains_alives, current_domain, classes, all_states):
    if verbose:
        debug("----------- rec_state_generate ---------- ")
        debug("\t all_domains_capacities: ", all_domains_capacities)
        debug("\t all_domains_alives: ", all_domains_alives)
        debug("\t current_domain: ", current_domain)
        debug("\t all_states: ", all_states)

    if current_domain == Environment.providers_num:
        per_domain_state_generate(all_domains_capacities[current_domain], current_domain, classes, 0, all_domains_alives, all_states)
        return

    tmp_alives = ()
    domain_possible_alives = []
    all_possible_alives(classes, all_domains_capacities[current_domain], 0, tmp_alives, domain_possible_alives)

    if verbose:
        debug("\t all_possible_alives: ", domain_possible_alives)

    for alive in domain_possible_alives:
        all_domains_alives[current_domain] = alive
        rec_state_generate(all_domains_capacities, all_domains_alives, current_domain + 1, classes, all_states)


def generate_all_states():
    Environment.seen_state_valid_actions = {}
    all_states = []
    
    all_domains_capacities = [None] * (Environment.providers_num + 1)
    all_domains_capacities[0] = Environment.domain.capacities.copy()
    for i in range (Environment.providers_num + 1):
        if i == 0:
            pass
        else:
            all_domains_capacities[i] = Environment.providers[i].quotas.copy()
            all_domains_capacities[i] = [x * Environment.providers[i].reject_threshold for x in all_domains_capacities[i]]

    all_domains_alives = [()] * (Environment.providers_num + 1)
    for i in range(Environment.providers_num + 1):
        all_domains_alives[i] = (0,) * len(Environment.traffic_loads)
    
    tcs = []
    for load in Environment.traffic_loads:
        tcs.append(load.service)

    rec_state_generate(all_domains_capacities, all_domains_alives, 0, tcs, all_states)
    return all_states


def print_states(all_states):
    print("-------- All States ---------")
    for state in all_states:
        print(state)


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
    print("**************************")
    #op = collections.OrderedDict(sorted(policy.items()))
    for s in policy:
        print(s, ": ", Environment.Actions(policy[s]))
    print("----------------------------")


def init_random_policy(policy, all_states):
    for s in all_states:
        va = Environment.get_valid_actions(s)
        action = np.random.randint(0, len(va)) 
        policy.update({s: va[action]})

    if verbose:
        debug("------- Init random policy ----------")
        print_policy(policy)
    

policy_iteration_accuracy = 0.0001
def policy_evaluation(V, policy, all_states, gamma):
    while True:
        diff = 0
        for s in all_states:
            old_v = V[s]
            old_action = policy[s]
        
            if verbose:
                debug("\n state = ", s, ", old_action = ", old_action, "old_v = ", old_v)
            
            va = Environment.get_valid_actions(s)
        
            if not(old_action in va):
                error("current actions is not valid action")
                sys.exit(-1)
            
            new_v = 0
            p, r = pr(s, old_action)
            
            if verbose:
                print_trans_prob(p)
                debug("\t r = ", r)
            
            for ns in p.keys():
                if Environment.is_active_state(s):
                    new_v += (p[ns] * (r + gamma * V[ns]))
                else:
                    new_v += (p[ns] * (r + V[ns]))

            V[s] = new_v
            
            if verbose:
                debug("\t new_v = ", new_v)

            diff = max(diff, abs(old_v - V[s]))
        
        if verbose:
            debug("diff = ", diff)
        
        if diff < policy_iteration_accuracy:
            return


def policy_improvment(V, policy, all_states, gamma):
    policy_stable = True
    for s in all_states:
        if verbose:
            debug("\n policy_improvment: state = ", s)
        
        old_action = policy[s]
        improve = np.zeros(Environment.total_actions)
        va = Environment.get_valid_actions(s)
        
        for a in va:
            p, r = pr(s, a)
            for ns in p.keys():
                if verbose:
                    debug("\t a  = ", a)
                    debug("\t ns = ", ns)
                    debug("\t p[ns] = ", p[ns])
                    debug("\t r = ", r)
                    debug("\t V[ns] = ", V[ns])
             
                improve[a] += (p[ns] * (r + gamma * V[ns]))
            
            if verbose:
                debug("\t improve[",a,"] = ", improve[a])
        
        new_val = -1 * np.inf
        best_action = None
        for a in va:
            if improve[a] > new_val:
                new_val = improve[a]
                best_action = a
        
        policy.update({s: best_action})
        
        if verbose:
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


def policy_iteration(gamma):
    V = defaultdict(lambda: 0)
    policy = {}
    
    all_possible_state = generate_all_states()
    if verbose:
        debug("---------------  all_possible_state  --------------------------")
        print_states(all_possible_state)

    init_random_policy(policy, all_possible_state)
    
    while True:
        if verbose:
            debug("********** At Beginning ************")
            print_V(V, all_possible_state)
            print_policy(policy)
        
        policy_evaluation(V, policy, all_possible_state, gamma)
       
        if verbose:
            debug("********** After Evaluation ************")
            print_V(V, all_possible_state)
            print_policy(policy)
        
        stable = policy_improvment(V, policy, all_possible_state, gamma)
       
        if verbose:
            debug("********** After improve ************")
            print_V(V, all_possible_state)
            print_policy(policy)

        if stable == True:
            break
    
    if verbose:
        debug("********** DP Final ************")
        print_V(V, all_possible_state)
        print_policy(policy)
    
    return policy


if __name__ == "__main__":

    gamma = 0.995
    parser.parse_config("config.json")
   
    demand_num = 20
    iterations = 10
    scale = 0

    i = 0
    while i <= scale:
        i += 1
       
        pi_policy = policy_iteration(gamma)
        print("------------- PI Policy -----------------")
        print_policy(pi_policy)
        
        pi_profit = ql_profit = gr_profit = 0
        for j in range(iterations):
        
            demands = Environment.generate_req_set(demand_num)

            p, a, f = test_policy(demands, pi_policy)
            pi_profit += p / float(len(demands))

            p, a, f =  test_greedy_random_policy(demands, 1.0)
            gr_profit += p / float(len(demands))

        print("PI Profit  = ", pi_profit / iterations)
        print("Gr Profit  = ", gr_profit / iterations) 
        print("", flush=True)
