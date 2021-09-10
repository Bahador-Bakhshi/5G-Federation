#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import MBQL
import RL
import heapq
import itertools 
import random
import Environment
import parser
import DP
from Environment import State, debug, error, warning, verbose

def test_greedy_policy(demands):
    total_reward = 0
    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, given_demands = demands)
    state = env.reset()

    i = 0
    last_total_reward = 0
    window = 100

    while state != None:
        i += 1
        valid_actions = Environment.get_valid_actions(state)
        
        action = None
        if Environment.Actions.accept in valid_actions:
            action = Environment.Actions.accept
        elif Environment.Actions.federate in valid_actions:
            action = Environment.Actions.federate
        else:
            action = Environment.Actions.reject
       
        next_state, reward, done = env.step(state, action)

        total_reward += reward

        if done:
            break

        state = next_state
        
        if i % window == 0:
            print("window = ", window, "gain = ", (total_reward - last_total_reward) / window)
            last_total_reward = total_reward

    print("---------------------------------------")
    return total_reward, 0, 0


def test_mbql_policy(demands):
    total_reward = 0
    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, given_demands = demands)
    MBQL.init(env)
    state = env.reset()
 
    i = 0
    last_total_reward = 0
    window = 100
   
    while state != None:
        i += 1

        reward, next_state = MBQL.MBqLearning(env, state)
        total_reward += reward

        state = next_state

        if i % window == 0:
            print("window = ", window, "gain = ", (total_reward - last_total_reward) / window)
            last_total_reward = total_reward
    
    print("--------------------------------------")
    return total_reward, 0, 0


def greedy_result(demands, profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_greedy_policy(demands)
    profit += p / demands_num
    accept += a / demands_num
    federate += f / demands_num

    return profit, accept, federate


def mbql_result(demands, profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_mbql_policy(demands)
    profit += p / demands_num
    accept += a / demands_num
    federate += f / demands_num

    return profit, accept, federate


if __name__ == "__main__":

    sim_num = 1000000

    parser.parse_config("config.json")

    
    init_size = 2
    step = 3
    scale = 0

    iterations = 5
    
    i = 0
    
    while i <= scale:
        #Environment.domain.total_cpu = init_size + i * step
        
        i += 1

        '''
        dp_policy_95 = DP.policy_iteration(0.99)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_95)
        '''
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = rl_profit = mbql_profit = 0
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = rl_accept = mbql_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = rl_federate = mbql_federate = 0

        for j in range(iterations):
            
            '''
            env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_num)
            ql_policy = QL.qLearning(env, episode_num, 1)
            print("---------- QL --------------")
            DP.print_policy(ql_policy)
        
            rl_policy = RL.rLearning(env, episode_num, 1)
            print("---------- RL --------------")
            DP.print_policy(rl_policy)
            '''

            demands = Environment.generate_req_set(sim_num)

            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, greedy_profit_100, greedy_accept_100, greedy_federate_100)
            
            mbql_profit, mbql_accept, mbql_federate = mbql_result(demands, mbql_profit, mbql_accept, mbql_federate)
            
            '''
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)
            
            rl_profit, rl_accept, rl_federate = mdp_policy_result(demands, rl_policy, rl_profit, rl_accept, rl_federate)
            '''


        print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 00  = ", greedy_profit_00 / iterations)
        print("Greedy Profit 50  = ", greedy_profit_50 / iterations)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("DP_05 Profit = ", dp_profit_05 / iterations)
        print("DP_30 Profit = ", dp_profit_30 / iterations)
        print("DP_60 Profit = ", dp_profit_60 / iterations)
        print("DP_95 Profit = ", dp_profit_95 / iterations)
        print("QL Profit   = ", ql_profit / iterations)
        print("MBQL Profit = ", mbql_profit / iterations)
        print("RL Profit   = ", rl_profit / iterations)
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
        print("MBQL Accept  = ", mbql_accept / iterations)
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
        print("MBQL Federate  = ", mbql_federate / iterations)
        print("RL Federate    = ", rl_federate / iterations)
        print("", flush=True)

    print("DONE!!!")

