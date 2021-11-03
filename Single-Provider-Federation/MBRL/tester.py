#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import MBQL
import MBRL
import RL
import heapq
import itertools 
import random
import Environment
import parser
import DP
from Environment import State, debug, error, warning, verbose

def greedy_policy(state):
    valid_actions = Environment.get_valid_actions(state)
        
    action = None
    if Environment.Actions.accept in valid_actions:
        action = Environment.Actions.accept
    elif Environment.Actions.federate in valid_actions:
        action = Environment.Actions.federate
    else:
        action = Environment.Actions.reject

    return action
 

def test_policy(policy, demands):
    total_reward = 0
    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, given_demands = demands)
    state = env.reset()

    i = 0
    last_total_reward = 0
    window = 10000

    while state != None:
        i += 1
        action = policy(state) 
        next_state, reward, done = env.step(state, action)
        
        global warmup
        if i > warmup:
            total_reward += reward

        if done:
            break

        state = next_state
        
        if i % window == 0:
            print("window = ", window, "gain = ", (total_reward - last_total_reward) / window)
            last_total_reward = total_reward

    print("---------------------------------------")
    return total_reward, 0, 0


def test_mb_policy(module, agent, demands):
    total_reward = 0
    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, given_demands = demands)
    module.init(env)
    state = env.reset()
 
    i = 0
    last_total_reward = 0
    window = 100
   
    while state != None:
        i += 1

        reward, next_state = agent(env, state)
        
        global warmup
        if i > warmup:
            total_reward += reward

        state = next_state

        if i % window == 0:
            print("window = ", window, "gain = ", (total_reward - last_total_reward) / window)
            last_total_reward = total_reward
    
    print("--------------------------------------")
    return total_reward, 0, 0


def greedy_result(demands, profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_policy(greedy_policy, demands)
    profit += p / (demands_num - warmup)
    accept += a / (demands_num - warmup)
    federate += f / (demands_num - warmup)

    return profit, accept, federate

def mf_result(mf_policy, demands, profit, accept, federate):
    demands_num = float(len(demands))
    
    def mf_policy_func(state):
        if state in mf_policy:
            return mf_policy[state]
        else:
            valid_actions = Environment.get_valid_actions(state)
            return np.random.choice(valid_actions)

    p, a, f = test_policy(mf_policy_func, demands)
    profit += p / (demands_num - warmup)
    accept += a / (demands_num - warmup)
    federate += f / (demands_num - warmup)

    return profit, accept, federate


def mb_result(module, agent, demands, profit, accept, federate):
    demands_num = float(len(demands))

    p, a, f = test_mb_policy(module, agent, demands)
    profit += p / (demands_num - warmup)
    accept += a / (demands_num - warmup)
    federate += f / (demands_num - warmup)

    return profit, accept, federate


if __name__ == "__main__":

    sim_time = 100
    episode_num = 50

    parser.parse_config("config.json")
    
    init_size = 2
    step = 3
    scale = 0
    
    '''
    if sim_num < 1000:
        iterations = 50
    elif sim_num < 10000:
        iterations = 20
    else:
        iterations = 5
    '''
    iterations = 20
    i = 0
    
    while i <= scale:
        #Environment.domain.total_cpu = init_size + i * step
        
        i += 1

        '''
        dp_policy_95 = DP.policy_iteration(0.99)
        print("------------ DP -------------")
        DP.print_policy(dp_policy_95)
        '''
        
        greedy_profit_00 = greedy_profit_50 = greedy_profit_100 = dp_profit_05 = dp_profit_30 = dp_profit_60 = dp_profit_95 = ql_profit = rl_profit = mbql_profit = mbrl_profit = mfrl_profit = 00
        greedy_accept_00 = greedy_accept_50 = greedy_accept_100 = dp_accept_05 = dp_accept_30 = dp_accept_60 = dp_accept_95 = ql_accept = rl_accept = mbql_accept = mbrl_accept = mfrl_accept = 0
        greedy_federate_00 = greedy_federate_50 = greedy_federate_100 = dp_federate_05 = dp_federate_30 = dp_federate_60 = dp_federate_95 = ql_federate = rl_federate = mbql_federate = mbrl_federate = mfrl_federate = 0

        for j in range(iterations):
            
            #env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time * 100)
            #rl_policy = RL.rLearning(env, episode_num, 1)

            demands = Environment.generate_req_set(sim_time)
            warmup = int(len(demands) * 0.3)
            print("# of demands = ", len(demands))

            greedy_profit_100, greedy_accept_100, greedy_federate_100 = greedy_result(demands, greedy_profit_100, greedy_accept_100, greedy_federate_100)
           
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

            #mbql_profit, mbql_accept, mbql_federate = mb_result(MBQL, MBQL.MBqLearning, demands, mbql_profit, mbql_accept, mbql_federate)
            MBRL.bg_explor_num  = 10
            MBRL.bg_explor_deep = 5
           
            MBRL.explor_num  = 5
            MBRL.explor_deep = 2
            
            MBRL.exploit_num  = 1
            MBRL.exploit_deep = 2
            mbrl_profit, mbrl_accept, mbrl_federate = mb_result(MBRL, MBRL.MBrLearning, demands, mbrl_profit, mbrl_accept, mbrl_federate)
            
            MBRL.explor_num = 0
            MBRL.explor_deep = 0
            #mfrl_profit, mfrl_accept, mfrl_federate = mb_result(MBRL, MBRL.MBrLearning, demands, mfrl_profit, mfrl_accept, mfrl_federate)
            
            '''
            dp_profit_95, dp_accept_95, dp_federate_95 = mdp_policy_result(demands, dp_policy_95, dp_profit_95, dp_accept_95, dp_federate_95)
            
            ql_profit, ql_accept, ql_federate = mdp_policy_result(demands, ql_policy, ql_profit, ql_accept, ql_federate)
            
            '''
            #rl_profit, rl_accept, rl_federate = mf_result(rl_policy, demands, rl_profit, rl_accept, rl_federate)


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
        print("MBRL Profit = ", mbrl_profit / iterations)
        print("MFRL Profit = ", mfrl_profit / iterations)
        print("RL Profit   = ", rl_profit / iterations)
        print("", flush=True)

        '''
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
        '''

    print("DONE!!!")
