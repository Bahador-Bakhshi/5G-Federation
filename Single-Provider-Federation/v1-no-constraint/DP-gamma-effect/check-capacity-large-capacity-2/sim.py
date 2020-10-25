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

    sim_time = 50
    episode_num = 100

    parser.parse_config("config.json")

    init_size = 25
    step = 25
    scale = 39

    iterations = 10
    
    i = 0

    while i <= scale:
        Environment.domain.total_cpu = init_size + i * step
        i += 1
        
        dp_policy_01 = DP.policy_iteration(0.01)
        dp_policy_30 = DP.policy_iteration(0.30)
        dp_policy_60 = DP.policy_iteration(0.99)
        dp_policy_99 = DP.policy_iteration(0.99)
    
        
        greedy_profit_100 = dp_profit_01 = dp_profit_30 = dp_profit_60 = dp_profit_99 = 0
        greedy_accept_100 = dp_accept_01 = dp_accept_30 = dp_accept_60 = dp_accept_99 = 0
        greedy_federate_100 = dp_federate_01 = dp_federate_30 = dp_federate_60 = dp_federate_99 = 0

        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            dp_profit_01, dp_accept_01, dp_federate_01 = mdp_policy_result(demands, dp_policy_01, dp_profit_01, dp_accept_01, dp_federate_01)
            dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_99, dp_accept_99, dp_federate_99 = mdp_policy_result(demands, dp_policy_99, dp_profit_99, dp_accept_99, dp_federate_99)
            

        print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_01 Profit = ", dp_profit_01 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_99 Profit = ", dp_profit_99 / iterations)
        print("", flush=True)

        print("Capacity_Accept = ", Environment.domain.total_cpu)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_01 Accept = ", dp_accept_01 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_99 Accept = ", dp_accept_99 / iterations)
        print("", flush=True)

        print("Capacity_Federate = ", Environment.domain.total_cpu)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_01 Federate = ", dp_federate_01 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_99 Federate = ", dp_federate_99 / iterations)
        print("", flush=True)


print("DONE!!!")
