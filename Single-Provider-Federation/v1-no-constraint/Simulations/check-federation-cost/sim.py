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

    sim_time = 70
    episode_num = 150

    parser.parse_config("config.json")

    init_mult = 0
    step = 0.25
    scale = 25

    i = 0

    org_fed_cost = [None for j in range(len(Environment.providers))]
    for j in range(len(Environment.providers)):
        org_fed_cost[j] = {}
        for k in Environment.domain.services:
            org_fed_cost[j][k] = Environment.providers[j].federation_costs[k]

    while i <= scale:
        for j in range(len(Environment.providers)):
            for k in Environment.domain.services:
                Environment.providers[j].federation_costs[k] = org_fed_cost[j][k] * (init_mult + i * step)
        i += 1

        dp_policy = DP.DP()
        debug("********* Optimal Policy ***********")
        #DP.print_policy(dp_policy)
    
        env = Environment.Env(Environment.domain.total_cpu, sim_time)
        ql_policy = QL.qLearning(env, episode_num)
        debug("********* QL Policy ***********")
        #DP.print_policy(ql_policy)
        
        greedy_profit = dp_profit = ql_profit = 0

        iterations = 50
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit += test_greedy_policy(demands) / float(len(demands))

            dp_profit += test_policy(demands, dp_policy) / float(len(demands))
        
            ql_profit += test_policy(demands, ql_policy) / float(len(demands))

        print("Costs = ")
        for k in Environment.domain.services:
            print("\t ", Environment.providers[0].federation_costs[k])
        print("Greedy Profit = ", greedy_profit / iterations)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)
