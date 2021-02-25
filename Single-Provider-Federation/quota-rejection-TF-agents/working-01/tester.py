#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import DDQL
import RL
import heapq
import itertools 
import random
import Environment
import parser
import DP
import TF_Agent
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
            if tmp_req.dt <= t:
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
                if tmp_req.deployed == 0:
                    local_domain_alives[tmp_req.class_id] += 1
                elif tmp_req.deployed == 1:
                    provider_domain_alives[tmp_req.class_id] += 1

                j += 1
       
        if verbose:
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

        action, random_action = policy(state)
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

def print_policy_function(policy):
    all_possible_state = DP.generate_all_states()
    for s in all_possible_state:
        print(s,": ", policy(s))


if __name__ == "__main__":


    sim_num = 2000
    episode_num = 500

    parser.parse_config("config.json")

    scale = 0
    iterations = 20
    i = 0
    
    while i <= scale:
        i += 1     
        dp_policy_95 = DP.policy_iteration(0.99)
        '''
        print("------------ DP -------------")
        print_policy_function(dp_policy_95)
        '''
        
        for j in range(iterations):
            '''
            env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_num)
            ql_policy = DDQL.ddqLearning(env, episode_num)
            print("----------- DDQL ------------")
            print_policy_function(ql_policy)
            '''
            greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = rl_profit = 0
            greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = rl_accept = 0
            greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = rl_federate = 0

            demands = Environment.generate_req_set(sim_num)

            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            agent = TF_Agent.main()
            ql_profit, ql_accept, ql_federate = TF_Agent.evaluate_agent(agent, demands)
            

            print("Capacity_Profit = ", Environment.domain.total_cpu)
            print("Greedy Profit 00  = ", greedy_profit_00 / 1)
            print("Greedy Profit 50  = ", greedy_profit_50 / 1)
            print("Greedy Profit 100 = ", greedy_profit_100 / 1)
            print("DP_05 Profit = ", dp_profit_05 / 1)
            print("DP_30 Profit = ", dp_profit_30 / 1)
            print("DP_60 Profit = ", dp_profit_60 / 1)
            print("DP_95 Profit = ", dp_profit_95 / 1)
            print("QL Profit = ", ql_profit / 1)
            print("RL Profit = ", rl_profit / 1)
            print("", flush=True)

            print("Capacity_Accept = ", Environment.domain.total_cpu)
            print("Greedy Accept 00 = ", greedy_accept_00 / 1)
            print("Greedy Accept 50  = ", greedy_accept_50 / 1)
            print("Greedy Accept 100 = ", greedy_accept_100 / 1)
            print("DP_05 Accept = ", dp_accept_05 / 1)
            print("DP_30 Accept = ", dp_accept_30 / 1)
            print("DP_60 Accept = ", dp_accept_60 / 1)
            print("DP_95 Accept = ", dp_accept_95 / 1)
            print("QL Accept    = ", ql_accept / 1)
            print("RL Accept    = ", rl_accept / 1)
            print("", flush=True)

            print("Capacity_Federate = ", Environment.domain.total_cpu)
            print("Greedy Federate 00  = ", greedy_federate_00 / 1)
            print("Greedy Federate 50  = ", greedy_federate_50 / 1)
            print("Greedy Federate 100 = ", greedy_federate_100 / 1)
            print("DP_05 Federate = ", dp_federate_05 / 1)
            print("DP_30 Federate = ", dp_federate_30 / 1)
            print("DP_60 Federate = ", dp_federate_60 / 1)
            print("DP_95 Federate = ", dp_federate_95 / 1)
            print("QL Federate    = ", ql_federate / 1)
            print("RL Federate    = ", rl_federate / 1)
            print("", flush=True)

    print("DONE!!!")
