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

    sim_num = 4000
    episode_num = 2500


    best_QL_alpha   = 1.0
    best_QL_epsilon = 1.0
    QL_gamma_95   = 0.95
    QL_gamma_55   = 0.55
    QL_gamma_20   = 0.20

    best_RL_alpha   = 1.0
    best_RL_epsilon = 1.0
    best_RL_beta    = 1.0

    parser.parse_config("config.json")

    init_size = 1
    step = 0.2
    scale = 0

    iterations = 10

    org_domain_capacity = Environment.domain.capacities.copy()

    i = 0
    
    while i <= scale:
        capacity_scale = init_size + i * step
        Environment.domain.capacities = [int(x * capacity_scale) for x in org_domain_capacity]
        i += 1


        dp_policy_99 = DP.policy_iteration(0.99)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_99)
 
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_99 = ql_95_profit = ql_55_profit = ql_20_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_99 = ql_95_accept = ql_55_accept = ql_20_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_99 = ql_95_federate = ql_55_federate = ql_20_federate = rl_federate = 0
        greedy_reject_00 = greedy_reject_50 = greedy_reject_100 = dp_reject_05 = dp_reject_30 = dp_reject_60 = dp_reject_99 = ql_95_reject = ql_55_reject = ql_20_reject = rl_reject = 0
        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
            
            '''
            ql_95_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, QL_gamma_95, "QL_95")
            print("---------- QL-0.95 --------------")
            DP.print_policy(ql_95_policy)
        
            ql_55_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, QL_gamma_55, "QL_55")
            print("---------- QL-0.55 --------------")
            DP.print_policy(ql_55_policy)
        
            ql_20_policy = QL.qLearning(env, episode_num, 1, best_QL_alpha, best_QL_epsilon, QL_gamma_20, "QL_20")
            print("---------- QL-0.20 --------------")
            DP.print_policy(ql_20_policy)
            '''

            rl_policy = RL.rLearning(env, episode_num, 1, best_RL_alpha, best_RL_epsilon, best_RL_beta, "RL")
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
            
            '''
            ql_95_profit, ql_95_accept, ql_95_federate = mdp_policy_result(demands, ql_95_policy, ql_95_profit, ql_95_accept, ql_95_federate)
            
            ql_55_profit, ql_55_accept, ql_55_federate = mdp_policy_result(demands, ql_55_policy, ql_55_profit, ql_55_accept, ql_55_federate)
            
            ql_20_profit, ql_20_accept, ql_20_federate = mdp_policy_result(demands, ql_20_policy, ql_20_profit, ql_20_accept, ql_20_federate)
            '''

            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)



        print("Scale_Profit = ", capacity_scale)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_99 Profit = ", dp_profit_99 / iterations)
        print("QL_95 Profit = ", ql_95_profit / iterations)
        print("QL_55 Profit = ", ql_55_profit / iterations)
        print("QL_20 Profit = ", ql_20_profit / iterations)
        print("RL Profit = ", rl_profit / iterations)
        print("", flush=True)

        print("Scale_Accept = ", capacity_scale)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_99 Accept = ", dp_accept_99 / iterations)
        print("QL_95 Accept = ", ql_95_accept / iterations)
        print("QL_55 Accept = ", ql_55_accept / iterations)
        print("QL_20 Accept = ", ql_20_accept / iterations)
        print("RL Accept    = ", rl_accept / iterations)
        print("", flush=True)

        print("Scale_Federate = ", capacity_scale)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_99 Federate = ", dp_federate_99 / iterations)
        print("QL_95 Federate = ", ql_95_federate / iterations)
        print("QL_55 Federate = ", ql_55_federate / iterations)
        print("QL_20 Federate = ", ql_20_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)

        print("Scale_Reject = ", capacity_scale)
        print("Greedy Reject 00  = ", 1.0 - ((greedy_federate_00 + greedy_accept_00)/ iterations))
        print("Greedy Reject 50  = ", 1.0 - ((greedy_federate_50 + greedy_accept_50)/ iterations))
        print("Greedy Reject 100 = ", 1.0 - ((greedy_federate_100+ greedy_accept_100) / iterations))
        print("DP_05 Reject = ", 1.0 - ((dp_federate_05 + dp_accept_05) / iterations))
        print("DP_30 Reject = ", 1.0 - ((dp_federate_30 + dp_accept_30) / iterations))
        print("DP_60 Reject = ", 1.0 - ((dp_federate_60 + dp_accept_60) / iterations))
        print("DP_99 Reject = ", 1.0 - ((dp_federate_99 + dp_accept_99) / iterations))
        print("QL_95 Reject = ", 1.0 - ((ql_95_federate + ql_95_accept) / iterations))
        print("QL_55 Reject = ", 1.0 - ((ql_55_federate + ql_55_accept) / iterations))
        print("QL_20 Reject = ", 1.0 - ((ql_20_federate + ql_20_accept) / iterations))
        print("RL Reject    = ", 1.0 - ((rl_federate + rl_accept) / iterations))
        print("", flush=True)

print("DONE!!!")

