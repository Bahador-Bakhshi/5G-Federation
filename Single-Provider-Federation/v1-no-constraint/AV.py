#!/usr/bin/python3
import json
import gurobipy as gp
from gurobipy import GRB
import numpy as np
import pandas as pd
import sys
from enum import Enum
from enum import IntEnum
import DP
import Environment
import parser
from tester import test_policy, test_greedy_random_policy

accuracy = 0.000001
NM = -1000000

def average_reward_LP(states, actions, Pr, R):
    # Model
    m = gp.Model("AR_LP")

    # Create decision variables for each item
    x = m.addVars(states, actions, name="x")

    v = m.addVar(name="v")

    # The objective is to maximize the value
    # max z
    m.setObjective(v, GRB.MAXIMIZE)

    # Constraints
    
    # v = sum_s sum_a R(s,a) * x(s,a)
    m.addConstr((v == gp.quicksum(R[s][a] * x[s,a]  for s in states for a in actions)), name='c1')
   
    # sum_s sum_a x(s,a) = 1
    m.addConstr((1 == gp.quicksum(x[s,a]  for s in states for a in actions)), name='c2')

    # sum_a x(sp,a) = sum_s (sum_a x(s,a) * Pr(s,a,sp))
    m.addConstrs((gp.quicksum(x[sp,a] for a in actions) == gp.quicksum(x[s,a] * Pr[s][a][sp] for s in states for a in actions) for sp in states), name='c3')


    # Solve
    m.optimize()
    m.write("model.lp")
    
    X = [None] * len(states)
    for s in states:
        X[s] = [None] * len(actions)
        for a in actions:
            X[s][a] = 0

    for v in m.getVars():
        print(v.varName,"=", v.x)
    
    opt_df = pd.DataFrame.from_dict(x, orient="index", columns = ["variable_object"])
    opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["s", "a"])
    
    opt_df.reset_index(inplace=True)    
    opt_df["val"] =  opt_df["variable_object"].apply(lambda item: item.X)

    opt_df.drop(columns=["variable_object"], inplace=True)
    #opt_df.to_csv("./optimization_solution.csv")

    for index, row in opt_df.iterrows():
        X[int(row['s'])][int(row['a'])] = row['val']
    
    return X


def average_reward_IP(states, actions, Pr, R):
    # Model
    m = gp.Model("AR_LP")

    # Create decision variables for each item
    x = m.addVars(states, actions, name="x")
    y = m.addVars(states, actions, vtype = GRB.BINARY, name="y")

    v = m.addVar(name="v")

    # The objective is to maximize the value
    # max z
    m.setObjective(v, GRB.MAXIMIZE)

    # Constraints
    
    # v = sum_s sum_a R(s,a) * x(s,a)
    m.addConstr((v == gp.quicksum(R[s][a] * x[s,a]  for s in states for a in actions)), name='c1')
   
    # sum_s sum_a x(s,a) = 1
    m.addConstr((1 == gp.quicksum(x[s,a]  for s in states for a in actions)), name='c2')

    # sum_a x(sp,a) = sum_s (sum_a x(s,a) * Pr(s,a,sp))
    m.addConstrs((gp.quicksum(x[sp,a] for a in actions) == gp.quicksum(x[s,a] * Pr[s][a][sp] for s in states for a in actions) for sp in states), name='c3')

    # x[s,a] - accuracy <= y[s,a]
    m.addConstrs(((x[s,a] - accuracy) <= y[s,a] for s in states for a in actions), name='c4')

    # x[s,a] / accuracy > y[s,a]
    m.addConstrs(((x[s,a] / accuracy) >= y[s,a] for s in states for a in actions), name='c5')

    # sum_a y[s,a] = 1 for all s
    m.addConstrs((gp.quicksum(y[s,a] for a in actions) == 1 for s in states), name='c6')

    # Solve
    m.optimize()
    m.write("model.lp")
    
    X = [None] * len(states)
    for s in states:
        X[s] = [None] * len(actions)
        for a in actions:
            X[s][a] = 0

    #for v in m.getVars():
    #    print(v.varName,"=", v.x)
    
    opt_df = pd.DataFrame.from_dict(x, orient="index", columns = ["variable_object"])
    opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["s", "a"])
    
    opt_df.reset_index(inplace=True)    
    opt_df["val"] =  opt_df["variable_object"].apply(lambda item: item.X)

    opt_df.drop(columns=["variable_object"], inplace=True)
    #opt_df.to_csv("./optimization_solution.csv")

    for index, row in opt_df.iterrows():
        X[int(row['s'])][int(row['a'])] = row['val']
    
    return X


def generate_policy(X, states, actions):
    policy = {}
    for s in states:
        ps = X[s]
        action = None
        last_pr = NM
        for a in actions:
            if ps[a] >= accuracy:
                if (action != None) and (abs(last_pr - ps[a]) < accuracy):
                    print("Error!!! Multiple actions with pr > 0")
                    sys.exit()
                
                if ps[a] > last_pr:
                    action = a
                    last_pr = ps[a]

        policy.update({s: action})


    return policy


def state_tuple_to_num(tuple_states):
    index = 0
    num_states = []
    tuple_to_num = {}
    num_to_tuple = {}

    for s in tuple_states:
        num_states.append(index)
        tuple_to_num.update({s: index})
        num_to_tuple.update({index: s})
        index += 1

    return num_states, tuple_to_num, num_to_tuple


def action_enum_to_num(Actions):
    num_actions = [e.value for e in Actions]
    return num_actions


def compute_Pr_R(states, actions, tuple_to_num, num_to_tuple, Actions):

    Pr = [None] * len(states)
    for s in states:
        Pr[s] = [None] * len(actions)
        for a in actions:
            Pr[s][a] = [None] * len(states)
            for ns in states:
                Pr[s][a][ns] = 0
    
    R = [None] * len(states)
    for s in states:
        R[s] = [None] * len(actions)
        for a in actions:
            R[s][a] = NM

    for s in states:
        state_tuple = num_to_tuple[s]
        va_tuple = Environment.get_valid_actions(state_tuple)
        va = action_enum_to_num(va_tuple)
        for a in va:
            action_code = Actions(a)

            p, r = DP.pr(state_tuple, action_code)

            R[s][a] = r

            for ns_tuple in p.keys():
                ns = tuple_to_num[ns_tuple]
                Pr[s][a][ns] = p[ns_tuple] 
    
    return Pr, R


def average_reward_policy():
    policy = {}
    all_possible_state = DP.generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)

    #Treate everything as integer since Gurobi needs it 
    num_states, tuple_to_num, num_to_tuple = state_tuple_to_num(all_possible_state)
   
    num_actions = action_enum_to_num(Environment.Actions)

    Pr, R = compute_Pr_R(num_states, num_actions, tuple_to_num, num_to_tuple, Environment.Actions)
    '''
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    '''
    X = average_reward_LP(num_states, num_actions, Pr, R)
    print(X)
    policy = generate_policy(X, num_states, num_actions)
    print(policy)

    policy_tuple = {}
    for s in policy.keys():
        a = policy[s]
        state_tuple = num_to_tuple[s]
        action_code = None if a == None else Environment.Actions(a)
        policy_tuple.update({state_tuple: action_code})

    return policy_tuple


if __name__ == "__main__":


    parser.parse_config("config.json")
    
    init_size = 5
    step = 5
    scale = 10

    i = 0
    sim_time = 100
    while i <= scale:
        Environment.domain.total_cpu = init_size + i * step
        i += 1
       
        pi_policy = DP.policy_iteration(0.05)
        print("*********** PI **********")
        DP.print_policy(pi_policy)
        
        vi_policy = DP.policy_iteration(0.999)
        print("*********** VI **********")
        DP.print_policy(vi_policy)
        
        av_policy = average_reward_policy()
        print("*********** AV **********")
        DP.print_policy(av_policy)

        
        pi_profit = vi_profit = av_profit = 0
        iterations = 20
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            p, a, f = test_policy(demands, pi_policy)
            pi_profit += (p / float(len(demands)))
            p, a, f = test_policy(demands, vi_policy)
            vi_profit += (p / float(len(demands)))
            p, a, f = test_policy(demands, av_policy)
            av_profit += (p / float(len(demands)))


        print("PI Profit = ", pi_profit / iterations)
        print("VI Profit = ", vi_profit / iterations) 
        print("AV Profit = ", av_profit / iterations) 
