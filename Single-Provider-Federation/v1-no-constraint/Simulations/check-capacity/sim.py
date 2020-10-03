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

    init_size = 20
    step = 20
    scale = 50

    i = 0

    while i <= scale:
        Environment.domain.total_cpu = init_size + i * step
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

        print("Capacity = ", Environment.domain.total_cpu)
        print("Greedy Profit = ", greedy_profit / iterations)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)
