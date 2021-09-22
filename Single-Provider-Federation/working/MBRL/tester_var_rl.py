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

    sim_time = 10000
    #episode_num = 1000
    episode_num = 10

    parser.parse_config("config_var-3.json")
    
    iterations = 10
    i = 0
    
    env = Environment.Env(Environment.domain.total_cpu, Environment.providers[1].quota, sim_time)
    rl_policy = RL.rLearning(env, episode_num, 1)

    times = [5000]
    scale = len(times)
    while i < scale:
        
        sim_time = times[i]
        i += 1

        greedy_profit_100 = rl_profit = mbrl_000_profit = mbrl_011_profit = mbrl_100_profit = mbrl_111_profit = 0
        alaki1 = alaki2 = 0

        for j in range(iterations):
        
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            
            demands = Environment.generate_req_set(sim_time)
            warmup = int(len(demands) * 0.3)
            print("# of demands = ", len(demands))

            greedy_profit_100, alaki1, alaki2 = greedy_result(demands, greedy_profit_100, alaki1, alaki2)

            MBRL.bg_explor_num  = 0
            MBRL.bg_explor_deep = 0
           
            MBRL.explor_num  = 0
            MBRL.explor_deep = 0
            
            MBRL.exploit_num  = 0
            MBRL.exploit_deep = 0
            #mbrl_000_profit, alaki1, alaki2 = mb_result(MBRL, MBRL.MBrLearning, demands, mbrl_000_profit, alaki1, alaki2)
 

            MBRL.bg_explor_num  = 0
            MBRL.bg_explor_deep = 0
           
            MBRL.explor_num  = 3
            MBRL.explor_deep = 2
            
            MBRL.exploit_num  = 1
            MBRL.exploit_deep = 2
            #mbrl_011_profit, alaki1, alaki2 = mb_result(MBRL, MBRL.MBrLearning, demands, mbrl_011_profit, alaki1, alaki2)


            MBRL.bg_explor_num  = 5
            MBRL.bg_explor_deep = 3
           
            MBRL.explor_num  = 0
            MBRL.explor_deep = 0
            
            MBRL.exploit_num  = 0
            MBRL.exploit_deep = 0
            #mbrl_100_profit, alaki1, alaki2 = mb_result(MBRL, MBRL.MBrLearning, demands, mbrl_100_profit, alaki1, alaki2)

            MBRL.bg_explor_num  = 5
            MBRL.bg_explor_deep = 3
           
            MBRL.explor_num  = 3
            MBRL.explor_deep = 2
            
            MBRL.exploit_num  = 1
            MBRL.exploit_deep = 2
            #mbrl_111_profit, alaki1, alaki2 = mb_result(MBRL, MBRL.MBrLearning, demands, mbrl_111_profit, alaki1, alaki2)

            
            rl_profit, alaki1, alaki2 = mf_result(rl_policy, demands, rl_profit, alaki1, alaki2)


        print("Capacity_Profit = ", Environment.domain.total_cpu)
        print("Greedy Profit 100 = ", greedy_profit_100 / iterations)
        print("MBRL_000 Profit = ", mbrl_000_profit / iterations)
        print("MBRL_100 Profit = ", mbrl_100_profit / iterations)
        print("MBRL_011 Profit = ", mbrl_011_profit / iterations)
        print("MBRL_111 Profit = ", mbrl_111_profit / iterations)
        print("RL Profit   = ", rl_profit / iterations)
        print("", flush=True)

    print("DONE!!!")

