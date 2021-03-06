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

    sim_time = 500
    episode_num = 100

    init_size = 1
    step = 1
    scale = 10
    
    iterations = 20

    i = 0

    while i <= scale:
        tc = init_size + i * step
        total_load = 0

        Environment.domain = Environment.Local_Domain(0)
        for j in range(tc):
            service = Environment.NFV_NS(j, np.random.randint(1, 11), np.random.randint(1, 11))
            Environment.domain.add_service(service)
       
        Environment.providers = []
        provider = Environment.Providers(0)
        for j in range(tc):
            provider.add_fed_cost(j, 1 + np.random.randint(0, Environment.domain.services[j].revenue))
        Environment.providers.append(provider)

        Environment.traffic_loads = []
        for j in range(tc):
            Environment.traffic_loads.append(Environment.Traffic_Load(j, np.random.randint(1, 11), np.random.randint(1, 11)))

        Environment.total_classes = len(Environment.traffic_loads)

        for j in range(tc):
            total_load += (Environment.traffic_loads[j].lam / Environment.traffic_loads[j].mu) * Environment.domain.services[j].cpu

        Environment.domain.total_cpu = int(0.4 * total_load)
        
        for j in range(tc):
            print("tc = ", j)
            print("\t lam =", Environment.traffic_loads[j].lam)
            print("\t mu  =", Environment.traffic_loads[j].mu)
            print("\t cpu =", Environment.domain.services[j].cpu)
            print("\t rev =", Environment.domain.services[j].revenue)
            print("\t cost=", Environment.providers[0].federation_costs[Environment.domain.services[j]])
        
        print("Environment.domain.total_cpu = ", Environment.domain.total_cpu)

        dp_policy_05 = DP.policy_iteration(0.005)
        dp_policy_30 = DP.policy_iteration(0.300)
        dp_policy_60 = DP.policy_iteration(0.600)
        dp_policy_95 = DP.policy_iteration(0.995)
    
        env = Environment.Env(Environment.domain.total_cpu, sim_time)
        #ql_policy = QL.qLearning(env, episode_num)
 
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = 0

        for j in range(iterations):
            
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit_00, greedy_accept_00, greedy_federate_00 = greedy_result(demands, 0.0, greedy_profit_00, greedy_accept_00, greedy_federate_00)
            greedy_profit_50, greedy_accept_50, greedy_federate_50 = greedy_result(demands, 0.5, greedy_profit_50, greedy_accept_50, greedy_federate_50)
            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, 1.0, greedy_profit_100, greedy_accept_100, greedy_federate_100)

            
            dp_profit_05, dp_accept_05, dp_federate_05 = mdp_policy_result(demands, dp_policy_05, dp_profit_05, dp_accept_05, dp_federate_05)
            dp_profit_30, dp_accept_30, dp_federate_30 = mdp_policy_result(demands, dp_policy_30, dp_profit_30, dp_accept_30, dp_federate_30)
            dp_profit_60, dp_accept_60, dp_federate_60 = mdp_policy_result(demands, dp_policy_60, dp_profit_60, dp_accept_60, dp_federate_60)
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            #ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)


        print("Class_Num_Profit = ", tc)
        print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL Profit = ", ql_profit / iterations)
        print("", flush=True)


        print("Class_Num_Accept = ", tc)
        print("Capacity_Accept = ", Environment.domain.total_cpu)
        print("Greedy Accept 00  = ", greedy_accept_00 / iterations)
        print("Greedy Accept 50  = ", greedy_accept_50 / iterations)
        print("Greedy Accept 100 = ", greedy_accept_100 / iterations)
        print("DP_05 Accept = ", dp_accept_05 / iterations)
        print("DP_30 Accept = ", dp_accept_30 / iterations)
        print("DP_60 Accept = ", dp_accept_60 / iterations)
        print("DP_95 Accept = ", dp_accept_95 / iterations)
        print("QL Accept    = ", ql_accept / iterations)
        print("", flush=True)


        print("Class_Num_Federate = ", tc)
        print("Greedy Federate 00  = ", greedy_federate_00 / iterations)
        print("Greedy Federate 50  = ", greedy_federate_50 / iterations)
        print("Greedy Federate 100 = ", greedy_federate_100 / iterations)
        print("DP_05 Federate = ", dp_federate_05 / iterations)
        print("DP_30 Federate = ", dp_federate_30 / iterations)
        print("DP_60 Federate = ", dp_federate_60 / iterations)
        print("DP_95 Federate = ", dp_federate_95 / iterations)
        print("QL Federate    = ", ql_federate / iterations)
        print("", flush=True)

        
        i += 1

print("DONE !!!")
