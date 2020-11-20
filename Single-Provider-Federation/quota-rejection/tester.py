#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
#import QL
import heapq
import itertools 
import random
import Environment
import parser
import DP
from Environment import State, debug, error, warning, verbose

def test_greedy_random_policy(demands, greediness):
    if verbose:
        debug("-------- test_greedy_random_policy -------")
    
    profit = 0
    accepted_num = 0
    federate_num = 0
    alive = []
    local_capacity = Environment.domain.total_cpu
    provider_capacity = Environment.providers[1].quota

    for i in range(len(demands)):
        req = demands[i]

        if local_capacity < 0 or local_capacity > Environment.domain.total_cpu or provider_capacity < 0 or provider_capacity > Environment.providers[1].quota:
            error("local_capacity = ", local_capacity)
            error("provider_capacity = ", provider_capacity)
            error("Bug in capacity")
            sys.exit()

        t = req.st
       
        j = 0
        while j < len(alive):
            tmp_req = alive[j]
            if tmp_req.dt <= t:
                #debug("remove: ", tmp_req)
                
                if tmp_req.deployed == 0: #local domain
                    local_capacity += tmp_req.w
                elif tmp_req.deployed == 1: #the provider # 1
                    provider_capacity += tmp_req.w
                else:
                    error("wrong deployment")
                    sys.exit(-1)

                alive.remove(tmp_req)
                tmp_req.deployed = -1
            else:
                j += 1

        if verbose:
            debug("\n")
            debug("current: ", req)
            debug("local_capacity = ", local_capacity, "provider_capacity = ", provider_capacity)


        action = None
    
        if req.w <= local_capacity:
            action = Environment.Actions.accept
        elif req.w <= provider_capacity:
            action = Environment.Actions.federate
        else:
            action = Environment.Actions.reject

        '''
        rnd = np.random.uniform(0,1)
        if rnd <= greediness:
            if req.w <= capacity:
                action = Environment.Actions.accept
            else:
                action = Environment.Actions.federate
        else:
            rnd = np.random.uniform(0,1)
            if (rnd < 0.5) and (req.w <= capacity): 
                action = Environment.Actions.accept
            else:
                action = Environment.Actions.federate
        '''
        
        if verbose:
            debug("action = ", action)

        if action == Environment.Actions.accept:
            #debug("accept")
            profit += req.rev
            accepted_num += 1
            req.deployed = 0
            alive.append(req)
            local_capacity -= req.w

        elif action == Environment.Actions.federate:
            #debug("federate")
            provider_domain = Environment.providers[1] # in this version, there is only one provider
            profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
            federate_num += 1
            req.deployed = 1
            alive.append(req)
            provider_capacity -= req.w

    
    return profit, accepted_num, federate_num


def test_policy(demands, policy):
    if verbose:
        debug("--------- test_policy -------------")
    
    profit = 0
    accepted_num = 0
    federate_num = 0
    all_alives = []
    local_capacity = Environment.domain.total_cpu
    provider_capacity = Environment.providers[1].quota

    for i in range(len(demands)):
        req = demands[i]
        
        if verbose:
            debug("current: ", req)

        if local_capacity < 0 or local_capacity > Environment.domain.total_cpu or provider_capacity < 0 or provider_capacity > Environment.providers[1].quota:
            error("local_capacity = ", local_capacity)
            error("provider_capacity = ", provider_capacity)
            error("Bug in the capacity")
            sys.exit()

        t = req.st

        j = 0
        local_domain_alives = [0] * Environment.total_classes
        provider_domain_alives = [0] * Environment.total_classes

        while j < len(all_alives):
            tmp_req = all_alives[j]
            print("tmp_req = ", tmp_req)
            if tmp_req.dt <= t:
                print("remove: ", tmp_req)
                if tmp_req.deployed == 0:
                    local_capacity += tmp_req.w
                elif tmp_req.deployed == 1:
                    provider_capacity += tmp_req.w
                else:
                    error("wrong deployment")
                    sys.exit(-1)

                all_alives.remove(tmp_req)
                tmp_req.deployed = -1

            else:
                print("update alives")
                if tmp_req.deployed == 0:
                    local_domain_alives[tmp_req.class_id] += 1
                elif tmp_req.deployed == 1:
                    provider_domain_alives[tmp_req.class_id] += 1

                j += 1
        
        debug("local_capacity = ", local_capacity, "provider_capacity = ", provider_capacity)
        debug("local_domain_alives = ", local_domain_alives)
        debug("provider_domain_alives = ", provider_domain_alives)

        req_index = req.class_id
        arrival_depart_events = [0] * Environment.total_classes
        arrival_depart_events[req_index] = 1
       
        state = State(Environment.total_classes)
        state.domains_alives = [tuple(local_domain_alives), tuple(provider_domain_alives)]
        state.arrivals_departures = tuple(arrival_depart_events)

        if verbose:
            debug("state = ", state)

        random_action = False
        if state in policy:
            action = policy[state]
        else:
            warning("Unknown state: ", state)
            action = 1 + int(np.random.uniform(0, Environment.total_actions - 1.00001))
            random_action = True
        
        if verbose:
            debug("Action = ", action)

        if action == None:
            print("None Action!!!!")
            va = Environment.get_valid_actions(state)
            action = va[np.random.randint(0, len(va))]

        if action == Environment.Actions.accept:
            if req.w > local_capacity:
                if random_action == False:
                    error("Error: w = ", req.w, "local_capacity = ", local_capacity)
                    sys.exit()
                else:
                    error("Invalid random action")
            else:
                
                if verbose:
                    debug("accept")
                
                profit += req.rev
                accepted_num += 1
                req.deployed = 0
                all_alives.append(req)
                local_capacity -= req.w

        elif action == Environment.Actions.federate:
            if req.w > provider_capacity:
                if random_action == False:
                    error("Error: w = ", req.w, "provider_capacity = ", local_capacity)
                    sys.exit()
                else:
                    error("Invalid random action")
            else:
                if verbose:
                    debug("federate")
            
                provider_domain = Environment.providers[1] # in this version, there is only one provider
                profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
                federate_num += 1
                req.deployed = 1
                all_alives.append(req)
                provider_capacity -= req.w

        elif action == Environment.Actions.reject:
            pass
            #debug("reject")
        else:
            error("Error in Actions in Policy")
            error("action = ", action)
            sys.exit()
        

    return profit, accepted_num, federate_num


def greedy_result(demands, beta, profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_greedy_random_policy(demands, beta)
    profit += p / demands_num
    accept += a / demands_num
    federate += f / demands_num

    return profit, accept, federate


def mdp_policy_result(demands, policy,  profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_policy(demands, policy)
    profit += p / demands_num
    accept += a / demands_num
    federate += f / demands_num

    return profit, accept, federate


if __name__ == "__main__":

    sim_time = 5
    episode_num = 2

    parser.parse_config("config.json")
    
    print("total_cpu = ", Environment.domain.total_cpu)
    
    dp_policy = DP.policy_iteration(0.99)
    #debug("********* Optimal Policy ***********")
    DP.print_policy(dp_policy)
    
    '''
    env = Environment.Env(Environment.domain.total_cpu, sim_time)
    ql_policy = QL.qLearning(env, episode_num)
    #debug("********* QL Policy ***********")
    DP.print_policy(ql_policy)
    '''

    greedy_profit = dp_profit = ql_profit = 0
    greedy_accept = dp_accept = ql_accept = 0
    greedy_federate = dp_federate = ql_federate = 0

    iterations = 1
    for i in range(iterations):
        
        demands = Environment.generate_req_set(sim_time)
        Environment.print_reqs(demands)

        greedy_profit, greedy_accept, greedy_federate = greedy_result(demands, 0, greedy_profit, greedy_accept, greedy_federate)
    
        dp_profit, dp_accept, dp_federate = mdp_policy_result(demands, dp_policy, dp_profit, dp_accept, dp_federate)

        #ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)


    print("Greedy Profit = ", greedy_profit / iterations)
    print("DP Profit = ", dp_profit / iterations)
    print("QL Profit = ", ql_profit / iterations)

    print("Greedy Accept = ", greedy_accept / iterations)
    print("DP Accept = ", dp_accept / iterations)
    print("QL Accept = ", ql_accept / iterations)

    print("Greedy Federate = ", greedy_federate / iterations)
    print("DP Federate = ", dp_federate / iterations)
    print("QL Federate = ", ql_federate / iterations)

