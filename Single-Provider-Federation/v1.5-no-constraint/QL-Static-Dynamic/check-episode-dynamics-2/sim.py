#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import heapq
import itertools 
import matplotlib 
import matplotlib.style 
import Environment
import parser
import DP
from tester import greedy_result, mdp_policy_result
from Environment import debug, error, warning

if __name__ == "__main__":

    sim_time = 80

    parser.parse_config("config.json")

    dp_policy_05 = DP.policy_iteration(0.005)
    dp_policy_30 = DP.policy_iteration(0.300)
    dp_policy_60 = DP.policy_iteration(0.600)
    dp_policy_95 = DP.policy_iteration(0.995)
    
    init_size = 5
    step = 5
    scale = 10
    iterations = 10

    i = 0

    while i <= scale:
        ep = init_size + i * step
        i += 1

        dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = ql_static_profit = 0
        dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = ql_static_accept = 0
        dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = ql_static_federate = 0

        for j in range(iterations):

            env = Environment.Env(Environment.domain.total_cpu, sim_time)
            ql_policy = QL.qLearning(env, ep, 1)
            ql_static_policy = QL.qLearning(env, ep, 0)

            demands = Environment.generate_req_set(sim_time * 5)
            Environment.print_reqs(demands)

            dp_profit_05, dp_accept_05, dp_federate_05 = mdp_policy_result(demands, dp_policy_05, dp_profit_05, dp_accept_05, dp_federate_05)
            dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)
            ql_static_profit, ql_static_accept, ql_static_federate = mdp_policy_result(demands, ql_static_policy, ql_static_profit, ql_static_accept, ql_static_federate)

        print("Episode_Profit = ", ep)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL Dynamic Profit =", ql_profit / iterations)
        print("QL Static  Profit =", ql_static_profit / iterations)
        print("", flush=True)

        print("Episode_Accept = ", ep)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_95 Accept = ", dp_accept_95 / iterations)
        print("QL Dynamic Accept =", ql_accept / iterations)
        print("QL Static  Accept =", ql_static_accept / iterations)
        print("", flush=True)

        print("Episode_Federate = ", ep)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_95 Federate = ", dp_federate_95 / iterations)
        print("QL Dynamic Federate =", ql_federate / iterations)
        print("QL Static  Federate =", ql_static_federate / iterations)
        print("", flush=True)


print("DONE!!!")
