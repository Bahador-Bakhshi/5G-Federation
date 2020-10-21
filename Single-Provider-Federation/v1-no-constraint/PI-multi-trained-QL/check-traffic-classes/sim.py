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

    sim_time = 50
    episode_num = 100

    init_size = 1
    step = 1
    scale = 5

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


        dp_policy = DP.policy_iteration()
        debug("********* Optimal Policy ***********")
        DP.print_policy(dp_policy)
    
        env = Environment.Env(Environment.domain.total_cpu, sim_time)
        ql_policy = QL.qLearning(env, episode_num)
        debug("********* QL Policy ***********")
        DP.print_policy(ql_policy)
        
        greedy_profit_0 = greedy_profit_50 = greedy_profit_100 = dp_profit = ql_profit = 0

        iterations = 20
        for j in range(iterations):
            
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            greedy_profit_0 += test_greedy_random_policy(demands, 0.0) / float(len(demands))
            greedy_profit_50 += test_greedy_random_policy(demands, 0.5) / float(len(demands))
            greedy_profit_100 += test_greedy_random_policy(demands, 1.0) / float(len(demands))

            dp_profit += test_policy(demands, dp_policy) / float(len(demands))
        
            ql_profit += test_policy(demands, ql_policy) / float(len(demands))

        print("Greedy Profit_0.0 = ", greedy_profit_0 / iterations)
        print("Greedy Profit_0.5 = ", greedy_profit_50 / iterations)
        print("Greedy Profit_1.0 = ", greedy_profit_100 / iterations)
        print("DP Profit = ", dp_profit / iterations)
        print("QL Profit = ", ql_profit / iterations)
        print("", flush=True)
        i += 1
