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
from tester import test_greedy_random_policy, test_policy
from Environment import debug, error, warning

if __name__ == "__main__":

    sim_time = 50
    episode_num = 100

    parser.parse_config("config.json")

    init_size = 0.05
    step = 0.025
    scale = 20

    i = 0

    while i <= scale:
        m = init_size + i * step
        Environment.traffic_loads[1].lam = Environment.traffic_loads[0].lam
        Environment.traffic_loads[1].mu = Environment.traffic_loads[0].mu * m
        Environment.domain.services[1].cpu = int(Environment.domain.services[0].cpu / m)
        Environment.domain.services[1].revenue = int(Environment.domain.services[0].revenue * m)
        Environment.providers[0].federation_costs[Environment.domain.services[1]] = int(Environment.providers[0].federation_costs[Environment.domain.services[0]] / m)


        Environment.domain.total_cpu = 0.6 * (((Environment.traffic_loads[0].lam / Environment.traffic_loads[0].mu) * Environment.domain.services[0].cpu) + ((Environment.traffic_loads[1].lam / Environment.traffic_loads[1].mu) * Environment.domain.services[1].cpu)) 
        print("Environment.domain.total_cpu = ", Environment.domain.total_cpu)

        i += 1

        dp_policy = DP.policy_iteration()
        debug("********* Optimal Policy ***********")
        #DP.print_policy(dp_policy)
    

        greedy_profit_0 = greedy_profit_50 = greedy_profit_100 = dp_profit = ql_profit = 0

        iterations = 20
        for j in range(iterations):
            env = Environment.Env(Environment.domain.total_cpu, sim_time)
            ql_policy = QL.qLearning(env, episode_num)
            debug("********* QL Policy ***********")
            #DP.print_policy(ql_policy)
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit_0 += test_greedy_random_policy(demands, 0.0) / float(len(demands))
            greedy_profit_50 += test_greedy_random_policy(demands, 0.5) / float(len(demands))
            greedy_profit_100 += test_greedy_random_policy(demands, 1.0) / float(len(demands))

            dp_profit += test_policy(demands, dp_policy) / float(len(demands))
        
            ql_profit += test_policy(demands, ql_policy) / float(len(demands))

        print("multiplier = ", m)
        print("Greedy Profit = ", greedy_profit_0 / iterations)
        print("Greedy Profit = ", greedy_profit_50 / iterations)
        print("Greedy Profit = ", greedy_profit_100 / iterations)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)
