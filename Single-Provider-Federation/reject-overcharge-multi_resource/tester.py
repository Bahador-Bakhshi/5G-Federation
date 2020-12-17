#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import RL
import DP
import heapq
import itertools 
import random
import Environment
import parser
from Environment import State, debug, error, warning, verbose, check_feasible_deployment, update_capacities, should_not_overcharge


def test_greedy_random_policy(demands, greediness):
    if verbose:
        debug("-------- test_greedy_random_policy -------")
        Environment.print_reqs(demands)
    
    profit = 0
    accepted_num = 0
    federate_num = 0
    alive = []
    provider_domain = Environment.providers[1]
    local_capacities = Environment.domain.capacities.copy()
    provider_capacities = provider_domain.quotas.copy()
    provider_capacities = [x * provider_domain.reject_threshold for x in provider_capacities]

    for i in range(len(demands)):
        req = demands[i]

        for j in range(len(local_capacities)):
            if local_capacities[j] < 0 or local_capacities[j] > Environment.domain.capacities[j] or provider_capacities[j] < 0 or provider_capacities[j] > provider_domain.quotas[j] * provider_domain.reject_threshold:
                error("Bug in capacities")
                error("local_capacity = ", local_capacities)
                error("provider_capacity = ", provider_capacities)
                sys.exit()

        t = req.st
       
        j = 0
        while j < len(alive):
            tmp_req = alive[j]
            if tmp_req.dt <= t:
                if tmp_req.deployed == 0: #local domain
                    update_capacities(tmp_req, local_capacities, 1)
                elif tmp_req.deployed == 1: #the provider # 1
                    update_capacities(tmp_req, provider_capacities, 1)
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
            debug("local_capacity = ", local_capacities, "provider_capacity = ", provider_capacities)

        action = None
    
        overcharging = -1
        if check_feasible_deployment(req, local_capacities):
            action = Environment.Actions.accept
        elif should_not_overcharge(req, provider_capacities, provider_domain.quotas, provider_domain.reject_threshold):
            action = Environment.Actions.federate
            overcharging = 0
        elif check_feasible_deployment(req, provider_capacities):
            action = Environment.Actions.federate
            overcharging = 1
        else:
            action = Environment.Actions.reject

        if verbose:
            debug("action = ", action)
            debug("overcharging = ", overcharging)

        if action == Environment.Actions.accept:
            #debug("accept")
            profit += req.rev
            accepted_num += 1
            req.deployed = 0
            alive.append(req)
            update_capacities(req, local_capacities, -1)

        elif action == Environment.Actions.federate:
            federation_cost_scale = 0
            
            if overcharging:
                federation_cost_scale = provider_domain.overcharge
            else:
                federation_cost_scale = 1

            profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service] * federation_cost_scale
            federate_num += 1
            req.deployed = 1
            alive.append(req)
            update_capacities(req, provider_capacities, -1)
        
        else: #reject
            pass
 
    while len(alive) > 0:
        tmp_req = alive[0]
        if tmp_req.deployed == 0: #local domain
            update_capacities(tmp_req, local_capacities, 1)
        elif tmp_req.deployed == 1: #the provider # 1
            update_capacities(tmp_req, provider_capacities, 1)
        else:
            error("wrong deployment")
            sys.exit(-1)

        alive.remove(tmp_req)
        tmp_req.deployed = -1

    return profit, accepted_num, federate_num


def test_policy(demands, policy):
    if verbose:
        debug("--------- test_policy -------------")
        Environment.print_reqs(demands)
    
    profit = 0
    accepted_num = 0
    federate_num = 0
    all_alives = []
    provider_domain = Environment.providers[1]
    local_capacities = Environment.domain.capacities.copy()
    provider_capacities = provider_domain.quotas.copy()
    provider_capacities = [x * provider_domain.reject_threshold for x in provider_capacities]

    for i in range(len(demands)):
        req = demands[i]
        
        if verbose:
            debug("current: ", req)

        for j in range(len(local_capacities)):
            if local_capacities[j] < 0 or local_capacities[j] > Environment.domain.capacities[j] or provider_capacities[j] < 0 or provider_capacities[j] > Environment.providers[1].quotas[j] * provider_domain.reject_threshold:
                error("Bug in the capacity")
                error("local_capacity = ", local_capacities)
                error("provider_capacity = ", provider_capacities)
                sys.exit()

        t = req.st

        j = 0
        local_domain_alives = [0] * Environment.total_classes
        provider_domain_alives = [0] * Environment.total_classes

        while j < len(all_alives):
            tmp_req = all_alives[j]
            if tmp_req.dt <= t:
                if tmp_req.deployed == 0:
                    update_capacities(tmp_req, local_capacities, 1)
                elif tmp_req.deployed == 1:
                    update_capacities(tmp_req, provider_capacities, 1)
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
            debug("local_capacity = ", local_capacities, "provider_capacity = ", provider_capacities)
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
            if not check_feasible_deployment(req, local_capacities):
                if random_action == False:
                    error("Error: w = ", req.cap, "local_capacity = ", local_capacity)
                    sys.exit()
                else:
                    error("Invalid random action")
                    continue
            else:
                
                if verbose:
                    debug("accept")
                
                profit += req.rev
                accepted_num += 1
                req.deployed = 0
                all_alives.append(req)
                update_capacities(req, local_capacities, -1)

        elif action == Environment.Actions.federate:
            overcharging = -1

            if should_not_overcharge(req, provider_capacities, provider_domain.quotas, provider_domain.reject_threshold):
                overcharging = 0
            elif check_feasible_deployment(req, provider_capacities):
                overcharging = 1
            else:
                if random_action:
                    error("Invalid random action")
                    continue
                else:
                    error("Invalid federation, not enough resource")
                    sys.exit(-1)
            
            if verbose:
                debug("federating")
                debug("overcharging = ", overcharging)
            
            if overcharging:
                profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service] * provider_domain.overcharge
            else:
                profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]

            federate_num += 1
            req.deployed = 1
            all_alives.append(req)
            update_capacities(req, provider_capacities, -1)

        elif action == Environment.Actions.reject:
            if verbose:
                debug("reject")
        
        else:
            error("Error in Actions in Policy")
            error("action = ", action)
            sys.exit()

    while len(all_alives) > 0:
        if verbose:
            debug("all_alives = ", all_alives)

        tmp_req = all_alives[0]
        if tmp_req.deployed == 0:
            update_capacities(tmp_req, local_capacities, 1)
        elif tmp_req.deployed == 1:
            update_capacities(tmp_req, provider_capacities, 1)
        else:
            error("wrong deployment")
            sys.exit(-1)

        all_alives.remove(tmp_req)
        tmp_req.deployed = -1

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

    episode_len = 5000
    episode_num = 100

    best_QL_alpha   = 0.9
    best_QL_epsilon = 0.9
    best_QL_gamma   = 0.9

    best_RL_alpha   = 0.1
    best_RL_epsilon = 0.9
    best_RL_beta    = 0.01

    parser.parse_config("config.json")

    
    init_size = 5
    step = 15
    scale = 0

    iterations = 1
    
    i = 0
    
    while i <= scale:
        i += 1

        #dp_policy_05 = DP.policy_iteration(0.005)
        #dp_policy_30 = DP.policy_iteration(0.300)
        #dp_policy_60 = DP.policy_iteration(0.600)
        dp_policy_95 = DP.policy_iteration(0.99)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_95)
    
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_09_profit = ql_05_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_09_accept = ql_05_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_09_federate = ql_05_federate = rl_federate = 0

        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
            
            ql_09_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, best_QL_gamma)
            print("---------- QL-0.9 --------------")
            DP.print_policy(ql_09_policy)
        
            ql_05_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, 0.5)
            print("---------- QL-0.5 --------------")
            DP.print_policy(ql_05_policy)
        
            rl_policy = RL.rLearning(env, episode_num, 1, best_RL_alpha, best_RL_epsilon, best_RL_beta)
            print("---------- RL --------------")
            DP.print_policy(rl_policy)

            demands = Environment.generate_req_set(episode_len)
            Environment.print_reqs(demands)

            #greedy_profit_00, greedy_accept_00, greedy_federate_00 = greedy_result(demands, 0.0, greedy_profit_00, greedy_accept_00, greedy_federate_00)
            #greedy_profit_50, greedy_accept_50, greedy_federate_50 = greedy_result(demands, 0.5, greedy_profit_50, greedy_accept_50, greedy_federate_50)
            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            
            #dp_profit_05, dp_accept_05, dp_federate_05 = mdp_policy_result(demands, dp_policy_05, dp_profit_05, dp_accept_05, dp_federate_05)
            #dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            #dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            ql_09_profit, ql_09_accept, ql_09_federate = mdp_policy_result(demands, ql_09_policy, ql_09_profit, ql_09_accept, ql_09_federate)
            
            ql_05_profit, ql_05_accept, ql_05_federate = mdp_policy_result(demands, ql_05_policy, ql_05_profit, ql_05_accept, ql_05_federate)
            
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)

        #print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL_09 Profit = ", ql_09_profit / iterations)
        print("QL_05 Profit = ", ql_05_profit / iterations)
        print("RL Profit = ", rl_profit / iterations)
        print("", flush=True)
        '''
        #aprint("Capacity_Accept = ", Environment.domain.total_cpu)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_95 Accept = ", dp_accept_95 / iterations)
        print("QL_09 Accept    = ", ql_09_accept / iterations)
        print("QL_05 Accept    = ", ql_05_accept / iterations)
        print("RL Accept    = ", rl_accept / iterations)
        print("", flush=True)

        #print("Capacity_Federate = ", Environment.domain.total_cpu)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_95 Federate = ", dp_federate_95 / iterations)
        print("QL_09 Federate    = ", ql_09_federate / iterations)
        print("QL_05 Federate    = ", ql_05_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)
        '''
    print("DONE!!!")




