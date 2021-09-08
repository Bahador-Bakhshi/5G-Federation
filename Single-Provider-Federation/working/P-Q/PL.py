#!/usr/bin/python3

from TD import *
import DP
import random 

theta = 2.0
rev_propag_level = 10

def print_q_entry(Q, state):
    print(state)
    for action in Q[state]["actions"]:
        print("\t", action)
        print("\t\t reward = ", Q[state]["actions"][action][0])
        print("\t\t visit  = ", Q[state]["actions"][action][2])
        print("\t\t value  = ", Q[state]["actions"][action][3])
        for ns in Q[state]["actions"][action][1]:
            print("\t\t", ns,"->",Q[state]["actions"][action][1][ns])
 
def print_p_q(Q):
    print("........................................")
    for state in Q:
        print_q_entry(Q, state)
    print("........................................")
 

def get_all_a_val(Q, state, level, r_not_q, rho, alpha, discount_factor):
    q_s_a = dict()
    for action in Q[state]["actions"]:
        val = 0
        for ns in Q[state]["actions"][action][1]:
            if Q[state]["actions"][action][1][ns]["level"] >= level:
                val += Q[state]["actions"][action][1][ns]["val"] * Q[state]["actions"][action][1][ns]["pr"]
            else:
                if not(ns in Q):
                    add_new_state(Q, ns, r_not_q, rho, level, alpha, discount_factor)
                new_value = get_v_s(Q, ns, level - 1, r_not_q, rho, alpha, discount_factor)
                Q[state]["actions"][action][1][ns]["val"] = new_value
                Q[state]["actions"][action][1][ns]["level"] = level
                val += Q[state]["actions"][action][1][ns]["val"] * Q[state]["actions"][action][1][ns]["pr"]

        q_s_a [action] = val
        #q_s_a [action] = max([x["val"] for x in Q[state]["actions"][action][1].values()])
        #q_s_a [action] = random.choices([x["val"] for x in Q[state]["actions"][action][1].values()], 
        #                       weights =[x["pr"]  for x in Q[state]["actions"][action][1].values()]
        #                 )[0]

    
    if verbose:
        print("get_all_a_val: s = ", state, "res = ", q_s_a)
    return q_s_a


def get_v_s(Q, state, level, r_not_q, rho, alpha, discount_factor):
    all_q_a_vals = get_all_a_val(Q, state, level, r_not_q, rho, alpha, discount_factor)
    best_action = max(all_q_a_vals, key=all_q_a_vals.get)
    res = all_q_a_vals[best_action]
    if verbose:
        print("get_v_s: s = ", state, "res = ", res)
    return res


def e_greedy(Q, state, epsilon, level, r_not_q, rho, alpha, discount_factor):
    num_valid_actions = len(Q[state]["actions"])
    probabilities = dict()
    for action in Q[state]["actions"]:
        probabilities[action] = epsilon / num_valid_actions

    all_q_a_vals = get_all_a_val(Q, state, level, r_not_q, rho, alpha, discount_factor)
    best_action = max(all_q_a_vals, key=all_q_a_vals.get)
    probabilities[best_action] += (1.0 - epsilon)

    selected_action = np.random.choice(list(probabilities.keys()), p = list(probabilities.values()))
    best_not_random =  best_action == selected_action
    
    return selected_action, best_not_random
    

def e_greedy_q_a(Q, state, epsilon, r_not_q, rho):
    num_valid_actions = len(Q[state]["actions"])
    probabilities = dict()
    for action in Q[state]["actions"]:
        probabilities[action] = epsilon / num_valid_actions

    all_q_a_vals = dict()
    for action in Q[state]["actions"]:
        all_q_a_vals[action] = Q[state]["actions"][action][3]

    best_action = max(all_q_a_vals, key=all_q_a_vals.get)
    probabilities[best_action] += (1.0 - epsilon)

    selected_action = np.random.choice(list(probabilities.keys()), p = list(probabilities.values()))
    best_not_random =  best_action == selected_action
    
    return selected_action, best_not_random


def init_new_entry(Q, state):
    if state in Q:
        return
    
    Q[state] = {"cnt_s": 0, "actions": dict(), "prev": set(), "old_vs": random.uniform(0,1)}


def fill_new_entry(Q, state, r_not_q, rho):
    valid_actions = Environment.get_valid_actions(state)
    for action in valid_actions:
        Q[state]["actions"][action] = [0, dict(), 0, random.uniform(0,0)] #reward, ns, visit, Q(s,a)
        next_states_probs, reward = DP.pr(state, action)
        Q[state]["actions"][action][0] = reward
        for next_state in next_states_probs:
            if r_not_q:
                #Q[state]["actions"][action][1][next_state] = {"pr": next_states_probs[next_state], "level": 0, "val": (reward - rho) + np.random.uniform(0,1)}
                Q[state]["actions"][action][1][next_state] = {"pr": next_states_probs[next_state], "level": 0, "val": np.random.uniform(0,0), "visit": 0}
            else:
                #Q[state]["actions"][action][1][next_state] = {"pr": next_states_probs[next_state], "level": 0, "val": reward + np.random.uniform(0,1)}
                Q[state]["actions"][action][1][next_state] = {"pr": next_states_probs[next_state], "level": 0, "val": np.random.uniform(0,0), "visit": 0}

            init_new_entry(Q, next_state)
            Q[next_state]["prev"].add((state, action, next_state))


def update_new_entry(Q, state, alpha, discount_factor, level, r_not_q, rho):
    for action in Q[state]["actions"]:
        reward = Q[state]["actions"][action][0]
        for ns in Q[state]["actions"][action][1].keys():
            if ns in Q and len(Q[ns]["actions"]) > 0:
                update_values(Q, state, action, ns, reward, alpha, discount_factor, level, r_not_q, rho)


def add_new_state(Q, state, r_not_q, rho, level, alpha, discount_factor):
    init_new_entry(Q, state)
    fill_new_entry(Q, state, r_not_q, rho)
    update_new_entry(Q, state, alpha, discount_factor, level, r_not_q, rho)


def update_values(Q, state, action, next_state, reward, alpha, discount_factor, level, r_not_q, rho):
    next_state_value = get_v_s(Q, next_state, level, r_not_q, rho, alpha, discount_factor)
            
    if r_not_q:
        td_target = (reward - rho) + next_state_value
    else:
        td_target = reward + discount_factor * next_state_value

    if verbose:
        print("td_target = ", td_target)
                
    td_delta = td_target - Q[state]["actions"][action][1][next_state]["val"]
                    
    if verbose:
        print("td_delta = ", td_delta)

    Q[state]["actions"][action][1][next_state]["val"] += alpha * td_delta
    
    return next_state_value


def reverse_propagete(Q, state, alpha, discount_factor, level, r_not_q, rho, r_level):
    r_level -= 1
    for (prev_state, prev_action, this_state) in Q[state]["prev"]:
        update_values(Q, prev_state, prev_action, this_state, Q[prev_state]["actions"][prev_action][0], alpha, discount_factor, level, r_not_q, rho)

        new_vs = get_v_s(Q, prev_state, level, r_not_q, rho, alpha, discount_factor)
        old_vs = Q[prev_state]["old_vs"]
        Q[prev_state]["old_vs"] = new_vs

        if r_level > 0:
            if (old_vs != new_vs) and ((old_vs == 0 and new_vs != 0) or abs(new_vs - old_vs) / abs(old_vs) >= theta):
                if verbose:
                    print("state = ", prev_state)
                    print("\t old = ", old_vs)
                    print("\t new = ", new_vs)
                reverse_propagete(Q, prev_state, alpha, discount_factor, level, r_not_q, rho, r_level)



def pLearning(env, num_episodes, dynamic, alpha0, epsilon0, gamma0, level, r_not_q):
    Q = dict()
    
    # Create an epsilon greedy policy function
    # appropriately for environment action space
    seen_states = set()

    discount_factor = gamma0
    rho = 1.0
    decay = 0.025

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            alpha = alpha0 / (1.0 + ith_episode * decay)
            epsilon = epsilon0 / (1.0 + ith_episode * decay)
        if verbose:
            print("alpha = ", alpha, "epsilon = ", epsilon, "gamma = ", gamma0)
        
        state = env.reset()

        for t in itertools.count():
            if t % 400 == 0:
                print("PL: episode = ", ith_episode,", step = ", t, flush=True)
           
            if verbose:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("\nt =", t, "sate =", state)
                print_p_q(Q)
            
            if not (state in Q):
                add_new_state(Q, state, r_not_q, rho, level, alpha, discount_factor)
            elif len(Q[state]["actions"]) == 0:
                fill_new_entry(Q, state, r_not_q, rho)
                update_new_entry(Q, state, alpha, discount_factor, level, r_not_q, rho)
            
            Q[state]["cnt_s"] += 1
            
            action, best_not_random = e_greedy(Q, state, epsilon, level, r_not_q, rho, alpha, discount_factor)
            #action, best_not_random = e_greedy_q_a(Q, state, epsilon, r_not_q, rho)

            Q[state]["actions"][action][2] += 1

            if verbose:
                print("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                print("next_state =", next_state, "reward =", reward, ", done =", done)
            
            if done:
                break

            if not (next_state in Q):
                add_new_state(Q, next_state, r_not_q, rho, level, alpha, discount_factor)
            elif len(Q[next_state]["actions"]) == 0:
                fill_new_entry(Q, next_state, r_not_q, rho)
                update_new_entry(Q, next_state, alpha, discount_factor, level, r_not_q, rho)
            
            Q[state]["actions"][action][1][next_state]["visit"] += 1
            
            '''
            if Environment.is_active_state(state):
                discount_factor = gamma0
            else:
                discount_factor = 1.0
            '''
            next_state_value = update_values(Q, state, action, next_state, reward, alpha, discount_factor, level, r_not_q, rho)
            
            if r_not_q:
                print("Error")
                sys.exit(-1)
            else:
                next_state_q_s = [x[3] for x in Q[next_state]["actions"].values()]
                before_update_value = Q[state]["actions"][action][3]
                Q[state]["actions"][action][3] += alpha * (reward + discount_factor * max(next_state_q_s) - Q[state]["actions"][action][3])

            new_vs = get_v_s(Q, state, level, r_not_q, rho, alpha, discount_factor)
            old_vs = Q[state]["old_vs"]
            Q[state]["old_vs"] = new_vs

            if (old_vs != new_vs) and ((old_vs == 0 and new_vs != 0) or abs(new_vs - old_vs) / abs(old_vs) >= theta):
                if verbose:
                    print("state = ", state)
                    print("\t --> old = ", old_vs)
                    print("\t --> new = ", new_vs)
                reverse_propagete(Q, state, alpha, discount_factor, level, r_not_q, rho, rev_propag_level)

            if len(Q[next_state]["actions"]) == 0:
                print("Error")
                print("state = ", state)
                print("next_state = ", next_state)
                sys.exit(-1)

            '''
            if Q[state]["actions"][action][2] > 10000 and max([x[2] for x in Q[next_state]["actions"].values()]) > 10000:
                check_values = get_all_a_val(Q, state, level, r_not_q, rho)
                diff = (Q[state]["actions"][action][3] - check_values[action]) / (Q[state]["actions"][action][3] if Q[state]["actions"][action][3] > 0 else 0.0001)
                print("diff = ", diff)
                if abs(diff) > 0.001:
                    print("\t check_values = ", check_values[action])
                    print("\t Q[s,a]       = ", Q[state]["actions"][action][3])
                    print("\t before_update= ", before_update_value)
                    print_q_entry(Q, state)
                    print_q_entry(Q, next_state)
            '''

            if r_not_q and best_not_random:
                td_target = reward - Q[state]["actions"][action][1][next_state]["val"] + next_state_value
                td_delta = td_target - rho
                rho += alpha * td_delta
 
            seen_states.add(state)
            
            if verbose:
                print("seen_states = ", seen_states)
           
            '''
            for _ in range(min(0, int(0.1 * len(Q)))):
                #updating_s = random.choices(list(Q.keys()), weights=[val["cnt_s"] for val in Q.values()], k=1)[0]
                updating_s = random.choices(list(Q.keys()), k=1)[0]
                #updating_a = random.choices(list(Q[updating_s]["actions"].keys()), weights=[val[2] for val in Q[updating_s]["actions"].values()], k=1)[0]
                updating_a = random.choices(list(Q[updating_s]["actions"].keys()), k=1)[0]
                #updating_ns = random.choices(list(Q[updating_s]["actions"][updating_a][1].keys()), weights=[val["pr"] for val in Q[updating_s]["actions"][updating_a][1].values()], k=1)[0]
                updating_ns = random.choices(list(Q[updating_s]["actions"][updating_a][1].keys()), k=1)[0]
                updating_reward = Q[updating_s]["actions"][updating_a][0]

                if not(updating_ns is Q):
                    #add_new_state(Q, updating_ns, r_not_q, rho
                    continue

                update_values(Q, updating_s, updating_a, updating_ns, updating_reward, alpha, level, r_not_q, rho)
            '''

            state = next_state
    
    final_policy = {}
    for state in Q:
        if len(Q[state]["actions"]) > 0:
            final_policy[state], _ = e_greedy(Q, state, 0, 0, r_not_q, rho, alpha, discount_factor)

    if verbose:
        print(final_policy)
   
    print("Final rho = ", rho)
    check_probabilities(Q)

    return final_policy


def check_probabilities(Q):
    for state in Q:
        for a in Q[state]["actions"]:
            total_visit = 0.0
            for ns in Q[state]["actions"][a][1]:
                total_visit += Q[state]["actions"][a][1][ns]["visit"]
            
            if total_visit == 0:
                total_visit = 1.0
            
            total_diff = 0
            for ns in Q[state]["actions"][a][1]:
                pr =  Q[state]["actions"][a][1][ns]["pr"]
                avg_visit = Q[state]["actions"][a][1][ns]["visit"] / total_visit
                pr_diff = pr - avg_visit
                total_diff += abs(pr_diff
                        )
                print("pr = ", pr, "avg_visit = ", avg_visit, "pr_diff = ", pr_diff)
            
            print(state, a,": total_visit = ", total_visit, ", total_diff = ", total_diff) 
