#!/usr/bin/python3

from TD import *
import DP

def print_p_q(Q):
    print("........................................")
    for state in Q:
        print(state)
        for action in Q[state]:
            print("\t", action)
            print("\t\t reward = ", Q[state][action][0])
            for ns in Q[state][action][1]:
                print("\t\t", ns,"->",Q[state][action][1][ns])
    print("........................................")
 
def get_all_a_val(Q, state, level):
    q_s_a = dict()
    for action in Q[state]:
        val = 0
        for ns in Q[state][action][1]:
            if Q[state][action][1][ns]["level"] >= level:
                val += Q[state][action][1][ns]["val"] * Q[state][action][1][ns]["pr"]
            else:
                if not(ns in Q):
                    add_new_state(Q, ns)
                new_value = get_v_s(Q, ns, level - 1)
                Q[state][action][1][ns]["val"] = new_value
                Q[state][action][1][ns]["level"] = level
                val += Q[state][action][1][ns]["val"] * Q[state][action][1][ns]["pr"]

        q_s_a [action] = val
    
    if verbose:
        print("get_all_a_val: s = ", state, "res = ", q_s_a)
    return q_s_a


def get_v_s(Q, state, level):
    all_q_a_vals = get_all_a_val(Q, state, level)
    best_action = max(all_q_a_vals, key=all_q_a_vals.get)
    res = all_q_a_vals[best_action]
    if verbose:
        print("get_v_s: s = ", state, "res = ", res)
    return res


def e_greedy(Q, state, epsilon, level):
    num_valid_actions = len(Q[state])
    probabilities = dict()
    for action in Q[state]:
        probabilities[action] = epsilon / num_valid_actions

    all_q_a_vals = get_all_a_val(Q, state, level)
    best_action = max(all_q_a_vals, key=all_q_a_vals.get)
    probabilities[best_action] += (1.0 - epsilon)

    selected_action = np.random.choice(list(probabilities.keys()), p = list(probabilities.values()))

    return selected_action


def add_new_state(Q, state):
    valid_actions = Environment.get_valid_actions(state)
    Q[state] = dict()
    for action in valid_actions:
        Q[state][action] = [0, dict()]
        next_states_probs, reward = DP.pr(state, action)
        Q[state][action][0] = reward
        for next_state in next_states_probs:
            Q[state][action][1][next_state] = {"pr": next_states_probs[next_state], "level": 0, "val": reward + np.random.uniform(0,1)}


def pLearning(env, num_episodes, dynamic, alpha0, epsilon0, gamma0, level):
    Q = dict()
    
    # Create an epsilon greedy policy function
    # appropriately for environment action space
    seen_states = set()

    discount_factor = gamma0
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
            
            if verbose:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("\nt =", t, "sate =", state)
                print_p_q(Q)
            
            if not (state in Q):
                add_new_state(Q, state)

            action = e_greedy(Q, state, epsilon, level)

            if verbose:
                print("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                print("next_state =", next_state, "reward =", reward, ", done =", done)
            
            if done:
                break

            if not (next_state in Q):
                add_new_state(Q, next_state)
            
            '''
            if Environment.is_active_state(state):
                discount_factor = gamma0
            else:
                discount_factor = 1.0
            '''

            next_state_value = get_v_s(Q, next_state, level)
            
            td_target = reward + discount_factor * next_state_value

            if verbose:
                print("td_target = ", td_target)
                
            td_delta = td_target - Q[state][action][1][next_state]["val"]
                    
            if verbose:
                print("td_delta = ", td_delta)

            Q[state][action][1][next_state]["val"] += alpha * td_delta
 
            seen_states.add(state)
            
            if verbose:
                print("seen_states = ", seen_states)
           
            state = next_state
    
    final_policy = {}
    for state in Q:
        final_policy[state] = e_greedy(Q, state, 0, 0)

    if verbose:
        print(final_policy)
    
    return final_policy




