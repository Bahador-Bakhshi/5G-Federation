#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import heapq
import itertools 
import random
import Environment
import parser
import QL
import RL
import DP
from Environment import State, debug, error, warning, verbose
from tester import test_greedy_random_policy, test_policy, greedy_result, mdp_policy_result


if __name__ == "__main__":

    sim_time = 250
    episode_num = 100

    best_QL_alpha   = 0.9
    best_QL_epsilon = 0.9
    best_QL_gamma   = 0.9

    best_RL_alpha   = 0.1
    best_RL_epsilon = 0.9
    best_RL_beta    = 0.1

    parser.parse_config("config.json")

    
    init_size = 0.0
    step = 0.3
    scale = 10

    iterations = 10
    
    
    org_fed_cost = [None for j in range(len(Environment.providers))]
    for j in range(len(Environment.providers)):
        if j == 0:
            pass #local domain
        else:
            org_fed_cost[j] = {}
            for k in Environment.domain.services:
                org_fed_cost[j][k] = Environment.providers[j].federation_costs[k]
    
    i = 0
   
    while i <= scale:
        cost_scale = init_size + i * step
        i += 1

        for j in range(len(Environment.providers)):
            if j == 0:
                pass #local domain
            else:
                for k in Environment.domain.services:
                    Environment.providers[j].federation_costs[k] = org_fed_cost[j][k] * cost_scale
 
        
        #dp_policy_05 = DP.policy_iteration(0.005)
        #dp_policy_30 = DP.policy_iteration(0.300)
        #dp_policy_60 = DP.policy_iteration(0.600)
        dp_policy_95 = DP.policy_iteration(0.99)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_95)
    
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_09_profit = ql_05_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_09_accept = ql_05_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_09_federate = ql_05_federate = rl_federate = 0

        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time)
            
            ql_09_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, best_QL_gamma)
            print("---------- QL-0.9 --------------")
            DP.print_policy(ql_09_policy)
        
            ql_05_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, 0.5)
            print("---------- QL-0.5 --------------")
            DP.print_policy(ql_05_policy)
       
            rl_policy = RL.rLearning(env, episode_num, 1, best_RL_alpha, best_RL_epsilon, best_RL_beta)
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
            
            ql_09_profit, ql_09_accept, ql_09_federate = mdp_policy_result(demands, ql_09_policy, ql_09_profit, ql_09_accept, ql_09_federate)
            
            ql_05_profit, ql_05_accept, ql_05_federate = mdp_policy_result(demands, ql_05_policy, ql_05_profit, ql_05_accept, ql_05_federate)
            
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)



        print("Scale_Profit = ", cost_scale)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL_09 Profit = ", ql_09_profit / iterations)
        print("QL_05 Profit = ", ql_05_profit / iterations)
        print("RL Profit = ", rl_profit / iterations)
        print("", flush=True)

        print("Scale_Accept = ", cost_scale)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_95 Accept = ", dp_accept_95 / iterations)
        print("QL_09 Accept    = ", ql_09_accept / iterations)
        print("QL_05 Accept    = ", ql_05_accept / iterations)
        print("RL Accept    = ", rl_accept / iterations)
        print("", flush=True)

        print("Scale_Federate = ", cost_scale)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_95 Federate = ", dp_federate_95 / iterations)
        print("QL_09 Federate    = ", ql_09_federate / iterations)
        print("QL_05 Federate    = ", ql_05_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)

print("DONE!!!")

