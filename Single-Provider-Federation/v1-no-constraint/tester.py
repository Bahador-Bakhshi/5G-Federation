#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import plotting
import QL
import heapq
import itertools 
import matplotlib 
import matplotlib.style 
import Environment
import parser
import DP
from Environment import debug, error, warning

def test_greedy_policy(demands):
    profit = 0
    accepted = []
    capacity = Environment.domain.total_cpu
    for i in range(len(demands)):
        req = demands[i]
        debug("current: ", req, ", capacity = ", capacity)
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

        if req.w <= capacity:
            debug("accept")
            profit += req.rev
            accepted.append(req)
            capacity -= req.w
        else:
            debug("federate")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            profit += req.rev - provider_domain.federation_costs[Environment.domain.services[req.class_id]]

        if capacity > Environment.domain.total_cpu:
            error("Error in capacity: ", capacity, ", server_size = ", Environment.domain.total_cpu)
            sys.exit()

        debug("profit = ", profit)
    
    return profit


def test_policy(demands, policy):
    profit = 0
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
                    sys.exit()
                else:
                    error("Invalid random action")
            else:
                debug("accept")
                profit += req.rev
                accepted.append(req)
                capacity -= req.w

        elif action == Environment.Actions.federate:
            debug("federate")
            provider_domain = Environment.providers[0] # in this version, there is only one provider
            profit += req.rev - provider_domain.federation_costs[Environment.domain.services[req.class_id]]

        elif action == Environment.Actions.reject:
            debug("reject")
        else:
            error("Error in Actions in Policy")
            error("action = ", action)
            sys.exit()
        
        if capacity > Environment.domain.total_cpu:
            error("Error in capacity: ", capacity, ", server_size = ", Environment.domain.total_cpu)
            sys.exit()

        debug("profit = ", profit)

    return profit



if __name__ == "__main__":

    sim_time = 250

    parser.parse_config("config.json")

    dp_policy = DP.DP()
    debug("********* Optimal Policy ***********")
    DP.print_policy(dp_policy)
    
    env = Environment.Env(Environment.domain.total_cpu, sim_time)
    ql_policy = QL.qLearning(env, 2)
    warning("********* QL Policy ***********")
    #DP.print_policy(ql_policy)

    greedy_profit = dp_profit = ql_profit = 0

    iterations = 50
    for i in range(iterations):
        
        demands = Environment.generate_req_set(sim_time)
        Environment.print_reqs(demands)

        greedy_profit += test_greedy_policy(demands) / float(len(demands))

        dp_profit += test_policy(demands, dp_policy) / float(len(demands))
        
        ql_profit += test_policy(demands, ql_policy) / float(len(demands))


    print("Greedy Profit = ", greedy_profit / iterations)
    print("DP Profit = ", dp_profit / iterations)
    print("QL Profit = ", ql_profit / iterations)
