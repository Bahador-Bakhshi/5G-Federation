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
import load_events
import load_policy
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

    iterations = 1

    org_domain_capacity = Environment.domain.capacities.copy()

    dp_policy_99 = load_policy.load_policy("Policy-DP-proc", len(Environment.traffic_loads))
    print("------------ DP -------------")
    DP.print_policy(dp_policy_99)
    
    rl_policy = load_policy.load_policy("Policy-RL-proc", len(Environment.traffic_loads))
    print("---------- RL --------------")
    DP.print_policy(rl_policy)
    
    i = 0
    
    while i <= scale:
        capacity_scale = init_size + i * step
        Environment.domain.capacities = [int(x * capacity_scale) for x in org_domain_capacity]
        i += 1

        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_99 = ql_95_profit = ql_55_profit = ql_20_profit = rl_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_99 = ql_95_accept = ql_55_accept = ql_20_accept = rl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_99 = ql_95_federate = ql_55_federate = ql_20_federate = rl_federate = 0
        greedy_reject_00 = greedy_reject_50 = greedy_reject_100 = dp_reject_05 = dp_reject_30 = dp_reject_60 = dp_reject_99 = ql_95_reject = ql_55_reject = ql_20_reject = rl_reject = 0
        
        for j in range(iterations):
            
            env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
            
            demands = load_events.get_event_reqs()
            Environment.print_reqs(demands)
            
            print("================= GREEDY =================")
            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)
            
            print("================ MDP ===================")
            dp_profit_99, dp_accept_99, dp_federate_99 = mdp_policy_result(demands, dp_policy_99, dp_profit_99, dp_accept_99, dp_federate_99)
            print("================ RL ====================")
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)


        print("Scale_Profit = ", capacity_scale)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations * len(demands))
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations * len(demands))
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations * len(demands))
        print("DP_05 Profit = ", dp_profit_05 / iterations * len(demands))
        print("DP_30 Profit = ", dp_profit_30 / iterations * len(demands))
        print("DP_60 Profit = ", dp_profit_60 / iterations * len(demands))
        print("DP_99 Profit = ", dp_profit_99 / iterations * len(demands))
        print("QL_95 Profit = ", ql_95_profit / iterations * len(demands))
        print("QL_55 Profit = ", ql_55_profit / iterations * len(demands))
        print("QL_20 Profit = ", ql_20_profit / iterations * len(demands))
        print("RL Profit = ", rl_profit / iterations * len(demands))
        print("", flush=True)

        print("Scale_Accept = ", capacity_scale)
        print("Greedy Accept 00 = ", greedy_accept_00 / iterations * len(demands))
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations * len(demands))
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations * len(demands))
        print("DP_05 Accept = ", dp_accept_05 / iterations * len(demands))
        print("DP_30 Accept = ", dp_accept_30 / iterations * len(demands))
        print("DP_60 Accept = ", dp_accept_60 / iterations * len(demands))
        print("DP_99 Accept = ", dp_accept_99 / iterations * len(demands))
        print("QL_95 Accept = ", ql_95_accept / iterations * len(demands))
        print("QL_55 Accept = ", ql_55_accept / iterations * len(demands))
        print("QL_20 Accept = ", ql_20_accept / iterations * len(demands))
        print("RL Accept    = ", rl_accept / iterations * len(demands))
        print("", flush=True)

        print("Scale_Federate = ", capacity_scale)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations * len(demands))
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations * len(demands))
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations * len(demands))
        print("DP_05 Federate = ", dp_federate_05 / iterations * len(demands))
        print("DP_30 Federate = ", dp_federate_30 / iterations * len(demands))
        print("DP_60 Federate = ", dp_federate_60 / iterations * len(demands))
        print("DP_99 Federate = ", dp_federate_99 / iterations * len(demands))
        print("QL_95 Federate = ", ql_95_federate / iterations * len(demands))
        print("QL_55 Federate = ", ql_55_federate / iterations * len(demands))
        print("QL_20 Federate = ", ql_20_federate / iterations * len(demands))
        print("RL Federate    = ", rl_federate / iterations * len(demands))
        print("", flush=True)

        print("Scale_Reject = ", capacity_scale)
        print("Greedy Reject 00  = ", 1.0 - ((greedy_federate_00 + greedy_accept_00)/ iterations * len(demands)))
        print("Greedy Reject 50  = ", 1.0 - ((greedy_federate_50 + greedy_accept_50)/ iterations * len(demands)))
        print("Greedy Reject 100 = ", 1.0 - ((greedy_federate_100+ greedy_accept_100) / iterations * len(demands)))
        print("DP_05 Reject = ", 1.0 - ((dp_federate_05 + dp_accept_05) / iterations * len(demands)))
        print("DP_30 Reject = ", 1.0 - ((dp_federate_30 + dp_accept_30) / iterations * len(demands)))
        print("DP_60 Reject = ", 1.0 - ((dp_federate_60 + dp_accept_60) / iterations * len(demands)))
        print("DP_99 Reject = ", 1.0 - ((dp_federate_99 + dp_accept_99) / iterations * len(demands)))
        print("QL_95 Reject = ", 1.0 - ((ql_95_federate + ql_95_accept) / iterations * len(demands)))
        print("QL_55 Reject = ", 1.0 - ((ql_55_federate + ql_55_accept) / iterations * len(demands)))
        print("QL_20 Reject = ", 1.0 - ((ql_20_federate + ql_20_accept) / iterations * len(demands)))
        print("RL Reject    = ", 1.0 - ((rl_federate + rl_accept) / iterations * len(demands)))
        print("", flush=True)

print("DONE!!!")

