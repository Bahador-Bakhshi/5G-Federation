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
from tester import test_greedy_policy, test_policy
from Environment import debug, error, warning

if __name__ == "__main__":

    sim_time = 100
    episode_num = 100

    parser.parse_config("config.json")

    init_size = 0.1
    step = 0.05
    scale = 20

    i = 0

    while i <= scale:
        m = init_size + i * step
        Environment.traffic_loads[1].lam = Environment.traffic_loads[0].lam
        Environment.traffic_loads[1].mu = Environment.traffic_loads[0].mu * m
        Environment.domain.services[1].cpu = int(Environment.domain.services[0].cpu / m)
        Environment.domain.services[1].revenue = int(Environment.domain.services[0].revenue * m)
        Environment.providers[0].federation_costs[Environment.domain.services[1]] = int(Environment.providers[0].federation_costs[Environment.domain.services[0]] / m)

        i += 1

        dp_policy = DP.DP()
        debug("********* Optimal Policy ***********")
        #DP.print_policy(dp_policy)
    
        env = Environment.Env(Environment.domain.total_cpu, sim_time)
        ql_policy = QL.qLearning(env, episode_num)
        debug("********* QL Policy ***********")
        #DP.print_policy(ql_policy)

        greedy_profit = dp_profit = ql_profit = 0

        iterations = 30
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit += test_greedy_policy(demands) / float(len(demands))

            dp_profit += test_policy(demands, dp_policy) / float(len(demands))
        
            ql_profit += test_policy(demands, ql_policy) / float(len(demands))

        print("multiplier = ", m)
        print("Greedy Profit = ", greedy_profit / iterations)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)