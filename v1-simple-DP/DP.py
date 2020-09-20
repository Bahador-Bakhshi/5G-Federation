#!/usr/bin/python3

import numpy as np
from collections import defaultdict
import sys

server_size = 5

lambda1 = 1.0
mu1 = 4.0
w1 = 2.0
r1 = 1.0

reject = 0
accept = 1
no_requst = 0

gamma = 0.1

def pr(state, action):
    prob = {}
    #reward = {}
    capacity = state[0]
    alive = state[1]
    requst = state[2]

    if action == reject:
        reward = 0
        if requst == no_requst:
            print("case: reject, no_req")
            ns = (capacity, alive, 1)
            p = lambda1 / (lambda1 + mu1)
            prob.update({ns: p})
            #r = 0
            #reward.update({ns: r})
            
            if alive > 0:
                ns = (capacity + w1, alive - 1, 0)
                p = mu1 / (lambda1 + mu1)
                prob.update({ns: p})
                #r = 0
                #reward.update({ns: r})
        else:
            print("case: reject, with req")
            ns = (capacity, alive, 1)
            p = lambda1 / (lambda1 + mu1)
            prob.update({ns: p})
            #r = 0
            #reward.update({ns: r})
            if alive > 0:
                ns = (capacity + w1, alive - 1, 0)
                p = mu1 / (lambda1 + mu1)
                prob.update({ns: p})
                #r = 0
                #reward.update({ns: r})
    elif action == accept:
        if requst == no_requst:
            print("case: accept, no_req")
            reward = -1 * np.inf
            ns = (capacity, alive, 1)
            p = lambda1 / (lambda1 + mu1)
            prob.update({ns: p})
            #r = -1 * np.inf
            #reward.update({ns: r})
            if alive > 0:
                ns = (capacity + w1, alive - 1, 0)
                p = mu1 / (lambda1 + mu1)
                prob.update({ns: p})
                #r = -1 * np.inf
                #reward.update({ns: r})
        else:
            if (alive + 1) * w1 <= server_size:
                print("case: accept, with req")
                reward = r1
                ns = (capacity - w1, alive + 1, 1)
                p = lambda1 / (mu1 + lambda1)
                prob.update({ns: p})
                #r = r1
                #reward.update({ns: r})
                if alive > 0:
                    ns = (capacity - w1 + w1, alive + 1 - 1, 0)
                    p = mu1 / (mu1 + lambda1)
                    prob.update({ns: p})
                    #r = r1
                    #reward.update({ns: r})
            else:
                print("case: try but cannot, with req")
                reward = -1 * np.inf
                ns = (capacity, alive, 1)
                p = lambda1 / (lambda1 + mu1)
                prob.update({ns: p})
                #r = -1 * np.inf
                #reward.update({ns: r})
                if alive > 0:
                    ns = (capacity + w1, alive - 1, 0)
                    p = mu1 / (lambda1 + mu1)
                    prob.update({ns: p})
                    #r = -1 * np.inf
                    #reward.update({ns: r})
    else:
        print("Error")
        sys.exit()

    print("State = ",state, ", action = ", action)
    print("\t Prob: ", prob)
    print("\t Reward: ", reward)

    return prob, reward


def generate_all_states(c, w):
    res = []
    for i in range (int(c / w) + 1):
        s = (c - i * w, i, 0)
        res.append(s)
        s = (c - i * w, i, 1)
        res.append(s)

    print("All States:", res)

    return res


def print_V(V, all_s):
    print("**************************")
    for s in all_s:
        if V[s] != 0:
            print("V[{}] = {}".format(s,V[s]))
    print("==========================")

if __name__ == "__main__":
    #state = (server capacity, number of alive demands, arrival or not)
    total_states = server_size * int (server_size /  w1) * 2
    total_actions = 2

    V = defaultdict(lambda: np.zeros(1))
    policy = {}
    all_possible_state = generate_all_states(server_size, w1)
    
    i = 0
    while True:
        i += 1
        if i > 20:
            break
       
        for s in all_possible_state:
            print_V(V, all_possible_state)
            improve = np.zeros(total_actions)
            for a in range(total_actions):
                p, r = pr(s, a)
                for ns in p.keys():
                    print("a  = ", a)
                    print("ns = ", ns)
                    print("p[ns] = ", p[ns])
                    print("r = ", r)
                    print("V[ns] = ", V[ns])
                    improve[a] += p[ns] * (r + gamma * V[ns])
                    print("improve[a] = ", improve[a])

            V[s] = max(improve)
            policy.update({s: np.argmax(improve)})
            print("Updated V[s] = ", V[s])


    print("Optimal Policy: ", policy)
