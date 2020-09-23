#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import plotting
import QL
import heapq
import itertools 
import matplotlib 
import matplotlib.style 
import Environment
from Environment import Actions
from Environment import Env 
from Environment import compute_capacity
from Environment import generate_req_set

matplotlib.style.use('ggplot') 

gamma = 0.9 #TODO  FIXME !!!!!!!!!!!!!!!!!!!!!!!!!!!

server_size = Environment.server_size
lams = Environment.lams
mus  = Environment.mus
ws   = Environment.ws
rs   = Environment.rs
total_actions = Environment.total_actions
total_classes = Environment.total_classes

def arrival_after_reject(cs, arrival_index, total_rates):
    alives = cs[0]
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = lams[arrival_index] / total_rates
    return {ns: p}


def departure_after_reject(cs, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = mus[dep_index] / total_rates
    return {ns: p}


def arrival_after_accept(cs, accept_index, arrival_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = lams[arrival_index] / total_rates
    return {ns: p}


def departure_after_accept(cs, accept_index, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = mus[dep_index] / total_rates
    return {ns: p}


def get_total_rates(total_classes, state):
    alives = state[0]
    requests = state[1]
    capacity = compute_capacity(alives)
 
    total_rates = 0
    for j in range(total_classes):
        total_rates += lams[j]
        if alives[j] > 0:
            total_rates += mus[j]
    
    return total_rates

def pr(state, action):
    prob = {}
    alives = state[0]
    requests = state[1]
    capacity = compute_capacity(alives)

    total_rates = get_total_rates(total_classes, state)
    
    print("State = ", state, ", action = ", action)

    active = 0
    for i in range(len(requests)):
        if requests[i] > 0:
            active += 1
    if active > 1:
        print("Error in requests: ", requests)
        sys.exit()

    if action == Actions.no_action:
        if active != 0:
            print("Error in actions")
            sys.exit()

        print("No action")
        reward = 0
        
        for j in range(total_classes):
            prob.update(arrival_after_reject(state, j, total_rates))
            
        for j in range(total_classes):
            if alives[j] > 0:
                prob.update(departure_after_reject(state, j, total_rates))
 
    elif action == Actions.reject:
        print("Reject")
        reward = 0
        
        for j in range(total_classes):
            prob.update(arrival_after_reject(state, j, total_rates))
            
        for j in range(total_classes):
            if alives[j] > 0:
                prob.update(departure_after_reject(state, j, total_rates))
            
    elif action == Actions.accept:
        active = 0
        for i in range(len(requests)):
            if requests[i] > 0:
                active += 1

        if active == 0:
            print("Accept for no demand!!!")
            print("Invalid action")
            sys.exit()
            '''
            # cannot be accepted, it is like reject but -inf for reward
            reward = -1 * np.inf

            for j in range(total_classes):
                prob.update(arrival_after_reject(state, j, total_rates))
            
            for j in range(total_classes):
                if alives[j] > 0:
                    prob.update(departure_after_reject(state, j, total_rates))
            '''
        else:
            req_index = np.argmax(requests)
            
            print("alives = ", requests)
            print("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", ws[req_index])

            if capacity < ws[req_index]:
                print("Try to accept but no resource")
                #cannot be accepted, it is like reject but -inf for reward

                reward = -1 * np.inf

                for j in range(total_classes):
                    prob.update(arrival_after_reject(state, j, total_rates))
            
                for j in range(total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_reject(state, j, total_rates))
            else:
                print("Accepting")
                reward = rs[req_index]

                for j in range(total_classes):
                    prob.update(arrival_after_accept(state, req_index, j, total_rates))

                for j in range(total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_accept(state, req_index, j, total_rates))

    else:
        print("Error")
        sys.exit()

    tp = 0
    for i in prob.keys():
        tp += prob[i]
    if abs(tp - 1.0) > 0.0001:
        print("Error in p: ", prob)
        sys.exit()

    print("State = ", state, ", action = ", action)
    print("\t Prob: ", prob)
    print("\t Reward: ", reward)

    return prob, reward


def generate_all_states(c, w):
    res = []
    for i in range (int(c / w[0]) + 1):
        for j in range(int(c / w[1]) + 1):
            if i * w[0] + j * w[1] <= c:
                capacity = c - (i * w[0] + j * w[1])
                alives = (i , j)
                
                requests = (0, 0)
                s = (alives, requests)
                res.append(s)
                
                requests = (0, 1)
                s = (alives, requests)
                res.append(s)
                
                requests = (1, 0)
                s = (alives, requests)
                res.append(s)
                

    print("All States:", res)

    return res


def print_V(V, all_s):
    print("**************************")
    for s in all_s:
        if V[s] != 0:
            print("V[{}] = {}".format(s,V[s]))
    print("==========================")


def print_policy(policy):
    for s in policy:
        print(s, ": ", Actions(policy[s]))


def DP():
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(server_size, ws)
   
    loop = True
    while loop:
        max_diff = 0

        for s in all_possible_state:
            #print_V(V, all_possible_state)
            improve = np.zeros(total_actions)
            va = Environment.get_valid_actions(s)

            for a in va:
                p, r = pr(s, a)
                for ns in p.keys():
                    print("a  = ", a)
                    print("ns = ", ns)
                    print("p[ns] = ", p[ns])
                    print("r = ", r)
                    print("V[ns] = ", V[ns])
                    improve[a] += (p[ns] * (r + gamma * V[ns]))
                print("improve[a] = ", improve[a])
            
            new_val = -1 * np.inf
            best_action = None
            for a  in va:
                if improve[a] > new_val:
                    new_val = improve[a]
                    best_action = a

            print("new_val = ", new_val)
            print("best_action = ", best_action)

            policy.update({s: best_action})
            print("--------------------------------------")

            diff = abs(V[s] - new_val)
            if diff > max_diff:
                max_diff = diff

            V[s] = new_val
            print("Updated V[s] = ", V[s])

        if max_diff < 0.0001:
            loop = False

    return policy


def test_greedy_policy(demands):
    profit = 0
    accepted = []
    capacity = server_size
    for i in range(len(demands)):
        req = demands[i]
        print("current: ", req, ", capacity = ", capacity)
        t = req.st
       
        j = 0
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                print("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                j += 1

        if req.w <= capacity:
            print("accept")
            profit += req.rev
            accepted.append(req)
            capacity -= req.w
        else:
            print("reject")

        if capacity > server_size:
            print("Error in capacity: ", capacity, ", server_size = ", server_size)

    return profit

def test_policy(demands, policy):
    profit = 0
    accepted = []
    capacity = server_size
    for i in range(len(demands)):
        req = demands[i]
        print("current: ", req, ", capacity = ", capacity)
        t = req.st

        j = 0
        alives_list = [0] * total_classes
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                print("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                alives_list[tmp_req.class_id] += 1
                j += 1
            
        req_index = req.class_id
        arrival_list = [0] * total_classes
        arrival_list[req_index] = 1
        
        state = (tuple(alives_list), tuple(arrival_list))
        print("State = ", state)
        random_action = False
        if state in policy:
            action = policy[state]
        else:
            print("Unknown state")
            action = int(np.random.uniform(0,1.9999))
            random_action = True
        print("Action = ", action)

        if action == Actions.accept:
            if req.w > capacity:
                if random_action == False:
                    print("Error: w = ", req.w, "capacity = ", capacity)
                    sys.exit()
                else:
                    print("Invalid random action")
            else:
                print("accept")
                profit += req.rev
                accepted.append(req)
                capacity -= req.w

        elif action == Actions.reject:
            print("reject")
        else:
            print("Error in Actions in Policy")
            sys.exit()
        
        if capacity > server_size:
            print("Error in capacity: ", capacity, ", server_size = ", server_size)
            sys.exit()

    return profit

if __name__ == "__main__":
    sim_time = 10

    dp_policy = DP()
    print("********* Optimal Policy ***********")
    print_policy(dp_policy)

    env = Env(server_size, sim_time)
    ql_policy = QL.qLearning(env, 10)
    print("********* QL Policy ***********")
    print_policy(ql_policy)

    for i in range(10):

        demands = generate_req_set(total_classes, sim_time)
        #print_reqs(demands)
        greedy_profit = test_greedy_policy(demands)
        print("Greedy Profit = ", greedy_profit)

        dp_profit = test_policy(demands, dp_policy)
        print("DP Profit = ", dp_profit)
    
        ql_profit = test_policy(demands, ql_policy)
        print("QL Profit = ", ql_profit)



