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

    sim_num = 5000

    best_QL_alpha   = 0.75
    best_QL_epsilon = 0.75
    best_QL_gamma   = 0.75

    best_RL_alpha   = 0.8
    best_RL_epsilon = 1.0
    best_RL_beta    = 0.3

    parser.parse_config("config.json")

    
    init_size = 100
    step = 300
    scale = 10

    iterations = 20
    
    i = 0
 
    #dp_policy_05 = DP.policy_iteration(0.005)
    #dp_policy_30 = DP.policy_iteration(0.300)
    #dp_policy_60 = DP.policy_iteration(0.600)
    dp_policy_99 = DP.policy_iteration(0.99)
    print("------------ DP -------------")
    DP.print_policy(dp_policy_99)
    
    while i <= scale:
        episode_num = init_size + i * step
        i += 1
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_99 = ql_09_profit = ql_05_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_99 = ql_09_accept = ql_05_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_99 = ql_09_federate = ql_05_federate = rl_federate = 0
        greedy_reject_00 = greedy_reject_50 = greedy_reject_100 = dp_reject_05 = dp_reject_30 = dp_reject_60 = dp_reject_99 = ql_09_reject = ql_05_reject = rl_reject = 0
        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
            
            ql_09_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, best_QL_gamma)
            print("---------- QL-0.9 --------------")
            DP.print_policy(ql_09_policy)
        
            ql_05_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, 0.4)
            print("---------- QL-0.5 --------------")
            DP.print_policy(ql_05_policy)
        
            rl_policy = RL.rLearning(env, episode_num, 1, best_RL_alpha, best_RL_epsilon, best_RL_beta)
            print("---------- RL --------------")
            DP.print_policy(rl_policy)

            demands = Environment.generate_req_set(sim_num)
            Environment.print_reqs(demands)

            #greedy_profit_00, greedy_accept_00, greedy_federate_00 = greedy_result(demands, 0.0, greedy_profit_00, greedy_accept_00, greedy_federate_00)
            #greedy_profit_50, greedy_accept_50, greedy_federate_50 = greedy_result(demands, 0.5, greedy_profit_50, greedy_accept_50, greedy_federate_50)
            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            
            #dp_profit_05, dp_accept_05, dp_federate_05 = mdp_policy_result(demands, dp_policy_05, dp_profit_05, dp_accept_05, dp_federate_05)
            #dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            #dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_99, dp_accept_99, dp_federate_99 = mdp_policy_result(demands, dp_policy_99, dp_profit_99, dp_accept_99, dp_federate_99)
            
            ql_09_profit, ql_09_accept, ql_09_federate = mdp_policy_result(demands, ql_09_policy, ql_09_profit, ql_09_accept, ql_09_federate)
            
            ql_05_profit, ql_05_accept, ql_05_federate = mdp_policy_result(demands, ql_05_policy, ql_05_profit, ql_05_accept, ql_05_federate)
            
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)



        print("Episode_Profit = ", episode_num)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_99 Profit = ", dp_profit_99 / iterations)
        print("QL_09 Profit = ", ql_09_profit / iterations)
        print("QL_05 Profit = ", ql_05_profit / iterations)
        print("RL Profit = ", rl_profit / iterations)
        print("", flush=True)

        print("Episode_Accept = ", episode_num)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_99 Accept = ", dp_accept_99 / iterations)
        print("QL_09 Accept = ", ql_09_accept / iterations)
        print("QL_05 Accept = ", ql_05_accept / iterations)
        print("RL Accept    = ", rl_accept / iterations)
        print("", flush=True)

        print("Episode_Federate = ", episode_num)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_99 Federate = ", dp_federate_99 / iterations)
        print("QL_09 Federate = ", ql_09_federate / iterations)
        print("QL_05 Federate = ", ql_05_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)

        print("Episode_Reject = ", episode_num)
        print("Greedy Reject 00  = ", 1.0 - ((greedy_federate_00 + greedy_accept_00)/ iterations))
        print("Greedy Reject 50  = ", 1.0 - ((greedy_federate_50 + greedy_accept_50)/ iterations))
        print("Greedy Reject 100 = ", 1.0 - ((greedy_federate_100+ greedy_accept_100) / iterations))
        print("DP_05 Reject = ", 1.0 - ((dp_federate_05 + dp_accept_05) / iterations))
        print("DP_30 Reject = ", 1.0 - ((dp_federate_30 + dp_accept_30) / iterations))
        print("DP_60 Reject = ", 1.0 - ((dp_federate_60 + dp_accept_60) / iterations))
        print("DP_99 Reject = ", 1.0 - ((dp_federate_99 + dp_accept_99) / iterations))
        print("QL_09 Reject = ", 1.0 - ((ql_09_federate + ql_09_accept) / iterations))
        print("QL_05 Reject = ", 1.0 - ((ql_05_federate + ql_05_accept) / iterations))
        print("RL Reject    = ", 1.0 - ((rl_federate + rl_accept) / iterations))
        print("", flush=True)

print("DONE!!!")

