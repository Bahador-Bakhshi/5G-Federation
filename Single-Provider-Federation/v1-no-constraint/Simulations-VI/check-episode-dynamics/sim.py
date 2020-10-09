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

    sim_time = 100

    parser.parse_config("config.json")

    dp_policy = DP.DP()
    debug("********* Optimal Policy ***********")
    #DP.print_policy(dp_policy)
    
    init_size = 5
    step = 10
    scale = 15

    i = 0

    while i <= scale:
        ep = init_size + i * step
        i += 1

        dp_profit = ql_profit = ql_static_profit= 0

        iterations = 20
        for j in range(iterations):
            env = Environment.Env(Environment.domain.total_cpu, sim_time)
            ql_policy = QL.qLearning(env, ep)
            ql_static_policy = QL.qLearning(env, ep, 0)

            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            dp_profit += test_policy(demands, dp_policy) / float(len(demands))
            ql_profit += test_policy(demands, ql_policy) / float(len(demands))
            ql_static_profit += test_policy(demands, ql_static_policy) / float(len(demands))

        print("episode = ", ep)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)
        print("QL Static Profit = ", ql_static_profit / iterations)
