#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import RL
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

    sim_time = 200

    parser.parse_config("config.json")

    
    init_size = 5
    step = 20
    scale = 15

    iterations = 10
    
    i = 0
    
    diff_count = 0
    while i <= scale:
        Environment.domain.total_cpu = init_size + i * step
        #episode_num = 300 * (int (Environment.domain.total_cpu / 100) + 1)
        i += 1

        episode_num = 50

        #dp_policy_05 = DP.policy_iteration(0.005)
        #dp_policy_30 = DP.policy_iteration(0.300)
        #dp_policy_60 = DP.policy_iteration(0.600)
        dp_policy_95 = DP.policy_iteration(0.9999)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_95)
    
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = rl_federate = 0

        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.total_cpu, sim_time)
            ql_policy = QL.qLearning(env, episode_num, 1, gamma = 0.5)
            print("---------- QL --------------")
            DP.print_policy(ql_policy)
        
            rl_policy = RL.rLearning(env, episode_num, 1)
            print("---------- RL --------------")
            DP.print_policy(rl_policy)
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            #greedy_profit_00, greedy_accept_00, greedy_federate_00 = greedy_result(demands, 0.0, greedy_profit_00, greedy_accept_00, greedy_federate_00)
            #greedy_profit_50, greedy_accept_50, greedy_federate_50 = greedy_result(demands, 0.5, greedy_profit_50, greedy_accept_50, greedy_federate_50)
            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            
            #dp_profit_05, dp_accept_05, dp_federate_05 = mdp_policy_result(demands, dp_policy_05, dp_profit_05, dp_accept_05, dp_federate_05)
            #dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            #dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)


            if ql_policy != dp_policy_95:
                diff_count += 1
            
            print("diff = ", diff_count)


        print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL Profit = ", ql_profit / iterations)
        print("RL Profit = ", rl_profit / iterations)
        print("", flush=True)

        print("Capacity_Accept = ", Environment.domain.total_cpu)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_95 Accept = ", dp_accept_95 / iterations)
        print("QL Accept    = ", ql_accept / iterations)
        print("RL Accept    = ", rl_accept / iterations)
        print("", flush=True)

        print("Capacity_Federate = ", Environment.domain.total_cpu)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_95 Federate = ", dp_federate_95 / iterations)
        print("QL Federate    = ", ql_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)

print("diff_count = ", diff_count)
print("DONE!!!")

