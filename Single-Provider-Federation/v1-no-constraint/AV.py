#!/usr/bin/python3
import json
import gurobipy as gp
from gurobipy import GRB
import numpy as np
import pandas as pd
import sys
from enum import Enum
from enum import IntEnum
from  DP import *
import Environment
import parser
from tester import test_policy, test_greedy_random_policy

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


def discounted_reward_LP(states, actions, Pr, R, gamma):
    # Model
    m = gp.Model("DR_LP")
    
    d = [0] * len(states)
    d[0] = 1.0

    # Create decision variables for each item
    x = m.addVars(states, actions, name="x")

    v = m.addVar(name="v")

    # The objective is to maximize the value
    # max z
    m.setObjective(v, GRB.MAXIMIZE)

    # Constraints
    
    # v = sum_s sum_a R(s,a) * x(s,a)
    m.addConstr((v == gp.quicksum(R[s][a] * x[s,a]  for s in states for a in actions)), name='c1')
   
    # sum_a x(sp,a) = sum_s (sum_a x(s,a) * Pr(s,a,sp))
    m.addConstrs((gp.quicksum(x[sp,a] for a in actions) == d[sp] + gamma * gp.quicksum(x[s,a] * Pr[s][a][sp] for s in states for a in actions) for sp in states), name='c3')


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


def generate_policy(X, states, actions):
    policy = {}
    for s in states:
        ps = X[s]
        action = None
        last_pr = NM
        for a in actions:
            if ps[a] > accuracy:
                if (action != None) and (abs(last_pr - ps[a]) < accuracy):
                    print("Error!!! Multiple actions with pr > 0")
                    print("s = ", s, "action = ", action, "a = ", a, "last_pr = ", last_pr, "ps[a] = ", ps[a])
                    #sys.exit()
                
                if ps[a] > last_pr:
                    action = a
                    last_pr = ps[a]

        policy.update({s: action})

    return policy



def average_reward_policy():
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)

    #Treate everything as integer since Gurobi needs it 
    num_states, tuple_to_num, num_to_tuple = state_tuple_to_num(all_possible_state)
   
    num_actions = action_enum_to_num(Environment.Actions)

    Pr, R = compute_Pr_R(num_states, num_actions, tuple_to_num, num_to_tuple, Environment.Actions)
    
    print("Before Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    
    Pr, R, reduce_num_to_num = correct_mdp(Pr, R, num_actions, num_to_tuple, tuple_to_num, Environment.Actions)
    
    print("After Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    
    new_states = range(len(Pr))
    X = average_reward_LP(new_states, num_actions, Pr, R)
    print(X)
    policy = generate_policy(X, new_states, num_actions)
    print(policy)

    policy_tuple = {}
    for s in policy.keys():
        a = policy[s]
        state_tuple = num_to_tuple[reduce_num_to_num[s]]
        action_code = None if a == None else Environment.Actions(a)
        policy_tuple.update({state_tuple: action_code})

    return policy_tuple


def discounted_reward_policy(gamma):
    policy = {}
    all_possible_state = generate_all_states(Environment.domain.total_cpu, Environment.traffic_loads)

    #Treate everything as integer since Gurobi needs it 
    num_states, tuple_to_num, num_to_tuple = state_tuple_to_num(all_possible_state)
    print("------------ num_to_tuple -------------")
    print(num_to_tuple)
   
    num_actions = action_enum_to_num(Environment.Actions)

    Pr, R = compute_Pr_R(num_states, num_actions, tuple_to_num, num_to_tuple, Environment.Actions)
    
    print("Before Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    

    Pr, R, reduce_num_to_num = correct_mdp(Pr, R, num_actions, num_to_tuple, tuple_to_num, Environment.Actions)
    
    print("After Correction")
    print("---------- Pr ------------")
    print(Pr)
    print("---------- R -------------")
    print(R)
    
    new_states = range(len(Pr))
    X = discounted_reward_LP(new_states, num_actions, Pr, R, gamma)
    print(X)
    policy = generate_policy(X, new_states, num_actions)
    print(policy)

    policy_tuple = {}
    for s in policy.keys():
        a = policy[s]
        state_tuple = num_to_tuple[reduce_num_to_num[s]]
        action_code = None if a == None else Environment.Actions(a)
        policy_tuple.update({state_tuple: action_code})

    return policy_tuple

   

def policy_diff(p1, p2):
    for s in p1.keys():
        #if p1[s] != None and p2[s] != None and p1[s] != p2[s]:
        if p1[s] != p2[s]:
            print("Diff: s = ", s, "p1[s] = ", p1[s], "!= p2[s] = ", p2[s])


def policy_modifier(policy):
    greedy_policy = gen_greedy_policy()
    for s in policy.keys():
        if policy[s] == None:
            policy.update({s: greedy_policy[s]})




if __name__ == "__main__":


    parser.parse_config("config.json")

    init_size = 2
    step = 20
    scale = 0

    i = 0
    sim_time = 100000
    iterations = 1
    while i <= scale:

        #Environment.domain.total_cpu = init_size + i * step
        demands = Environment.generate_req_set(sim_time)
        i += 1
        
        '''
        gamma = 0.995
        
        pi_policy = policy_iteration(gamma)
        print("*********** PI **********")
        print_policy(pi_policy)
        
        #dr_policy = discounted_reward_policy(gamma)
        #dr_policy.update({((0,1),(0,1)): Environment.Actions.accept})
        #print("*********** DR **********")
        #print_policy(dr_policy)

        #av_policy = average_reward_policy()
        #print("*********** AV **********")
        #print_policy(av_policy)

        gr_policy = gen_greedy_policy()
        print("*********** GR **********")
        print_policy(gr_policy)
        
        print("", flush=True)
        print("Checking diff")
        policy_diff(pi_policy, gr_policy)

        av_profit = gr_profit = dr_profit = pi_profit = 0
        for j in range(iterations):
        
            demands = Environment.generate_req_set(sim_time)
            Environment.print_reqs(demands)

            #p, a, f = test_greedy_random_policy(demands, 1.0)
            p, a, f = test_policy(demands, gr_policy)
            gr_profit += (p / float(len(demands)))
            p, a, f = test_policy(demands, pi_policy)
            pi_profit += (p / float(len(demands)))
            
            #p, a, f = test_policy(demands, av_policy)
            #av_profit += (p / float(len(demands)))
            
            #p, a, f = test_policy(demands, dr_policy)
            #dr_profit += (p / float(len(demands)))


        print("GR Profit = ", gr_profit / iterations) 
        print("AV Profit = ", av_profit / iterations)
        print("DR Profit = ", dr_profit / iterations)
        print("PI Profit = ", pi_profit / iterations)
        '''
