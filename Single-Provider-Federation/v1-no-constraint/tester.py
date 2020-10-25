#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import heapq
import itertools 
import random
import Environment
import parser
import DP
from Environment import debug, error, warning

def test_greedy_random_policy(demands, greediness):
    profit = 0
    accepted_num = 0
    federate_num = 0
    accepted = []
    capacity = Environment.domain.total_cpu
    for i in range(len(demands)):
        req = demands[i]
        debug("current: ", req, ", capacity = ", capacity)
        if capacity < 0:
            error("Bug in capacity")
            sys.exit()
        t = req.st
       
        j = 0
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                debug("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                j += 1

        action = None
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

        if action == Environment.Actions.accept:
            debug("accept")
            profit += req.rev
            accepted_num += 1
            accepted.append(req)
            capacity -= req.w
        else:
            debug("federate")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
            federate_num += 1

        if capacity > Environment.domain.total_cpu:
            error("Error in capacity: ", capacity, ", server_size = ", Environment.domain.total_cpu)
            sys.exit()

        debug("profit = ", profit, ", accepted_num = ", accepted_num, ", federate_num = ", federate_num)
    
    return profit, accepted_num, federate_num


def test_policy(demands, policy):
    profit = 0
    accepted_num = 0
    federate_num = 0
    accepted = []
    capacity = Environment.domain.total_cpu
    for i in range(len(demands)):
        req = demands[i]
        debug("current: ", req, ", capacity = ", capacity)
        t = req.st

        j = 0
        alives_list = [0] * Environment.total_classes
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                debug("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                alives_list[tmp_req.class_id] += 1
                j += 1
            
        req_index = req.class_id
        arrival_list = [0] * Environment.total_classes
        arrival_list[req_index] = 1
        
        state = (tuple(alives_list), tuple(arrival_list))
        debug("State = ", state)
        random_action = False
        if state in policy:
            action = policy[state]
        else:
            warning("Unknown state: ", state)
            action = 1 + int(np.random.uniform(0, Environment.total_actions - 1.00001))
            random_action = True
        debug("Action = ", action)

        if action == Environment.Actions.accept:
            if req.w > capacity:
                if random_action == False:
                    error("Error: w = ", req.w, "capacity = ", capacity)
                    #sys.exit()
                else:
                    error("Invalid random action")
            else:
                debug("accept")
                profit += req.rev
                accepted_num += 1
                accepted.append(req)
                capacity -= req.w

        elif action == Environment.Actions.federate:
            debug("federate")
            print("State = ", state)
            print("current: ", req, ", capacity = ", capacity)
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            profit += req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
            federate_num += 1

        elif action == Environment.Actions.reject:
            debug("reject")
        else:
            error("Error in Actions in Policy")
            error("action = ", action)
            sys.exit()
        
        if capacity > Environment.domain.total_cpu:
            error("Error in capacity: ", capacity, ", server_size = ", Environment.domain.total_cpu)
            sys.exit()


        debug("profit = ", profit, ", accepted_num = ", accepted_num, ", federate_num = ", federate_num)
    
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
    
    dp_policy = DP.policy_iteration(0.3)
    debug("********* Optimal Policy ***********")
    DP.print_policy(dp_policy)
    
    env = Environment.Env(Environment.domain.total_cpu, sim_time)
    ql_policy = QL.qLearning(env, episode_num)
    debug("********* QL Policy ***********")
    DP.print_policy(ql_policy)
    
    greedy_profit = dp_profit = ql_profit = 0
    greedy_accept = dp_accept = ql_accept = 0
    greedy_federate = dp_federate = ql_federate = 0

    iterations = 2
    for i in range(iterations):
        
        demands = Environment.generate_req_set(sim_time)
        Environment.print_reqs(demands)

        greedy_profit, greedy_accept, greedy_federate = greedy_result(demands, 0, greedy_profit, greedy_accept, greedy_federate)
    
        dp_profit, dp_accept, dp_federate = mdp_policy_result(demands, dp_policy, dp_profit, dp_accept, dp_federate)

        ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)


    print("Greedy Profit = ", greedy_profit / iterations)
    print("DP Profit = ", dp_profit / iterations)
    print("QL Profit = ", ql_profit / iterations)

    print("Greedy Accept = ", greedy_accept / iterations)
    print("DP Accept = ", dp_accept / iterations)
    print("QL Accept = ", ql_accept / iterations)

    print("Greedy Federate = ", greedy_federate / iterations)
    print("DP Federate = ", dp_federate / iterations)
    print("QL Federate = ", ql_federate / iterations)

