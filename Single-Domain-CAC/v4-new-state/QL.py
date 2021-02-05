import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys 
from collections import defaultdict 
import plotting 

matplotlib.style.use('ggplot') 


def print_Q(Q):
    for s, s_a in Q.items():
        print("{}: {}".format(s, s_a))
    print("*********************")


def print_policy(Q):
    for s, s_a in Q.items():
        print("{}: {}".format(s, np.argmax(s_a)))


def Q_change(Q, old_Q):
    total = 0
    for s, s_a in Q.items():
        try:
            old_s_a = old_Q[s]
            for i in range(len(old_s_a)):
                if s_a[i] != -1 * np.inf and old_s_a[i] != -1 * np.inf:
                    total += abs(s_a[i] - old_s_a[i])
        except:
            #print(s)
            pass
    return total


def copy_Q(Q):
    copy = defaultdict(lambda: np.zeros(env.action_space.n))
    for s, s_a in Q.items():
        copy_s_a = [0] * len(s_a)
        for i in range(len(s_a)):
            copy_s_a[i] = s_a[i]
        copy[s] = copy_s_a

    return copy


def createEpsilonGreedyPolicy(Q, epsilon, num_actions): 
    """ 
    Creates an epsilon-greedy policy based 
    on a given Q-function and epsilon. 
	
    Returns a function that takes the state 
    as an input and returns the probabilities 
    for each action in the form of a numpy array 
    of length of the action space(set of possible actions). 
    """
    def policyFunction(state): 
        print_Q(Q)
        Action_probabilities = np.ones(num_actions, dtype = float) * epsilon / num_actions 
				
        best_action = np.argmax(Q[state]) 
        Action_probabilities[best_action] += (1.0 - epsilon) 
        return Action_probabilities 

    return policyFunction 


def qLearning(env, num_episodes, discount_factor = 0.9,	alpha = 0.5, epsilon = 0.8):
    """
    Q-Learning algorithm: Off-policy TD control.
    Finds the optimal greedy policy while improving
    following an epsilon-greedy policy"""

    # Action value function
    # A nested dictionary that maps
    # state -> (action -> action-value).
    
    # FIXME TODO
    #Q = defaultdict(lambda: np.zeros(env.action_space.n))
    Q = defaultdict(lambda: np.random.uniform(0, 10, env.action_space.n))

    # Keeps track of useful statistics
    stats = plotting.EpisodeStats(
        episode_lengths = np.zeros(num_episodes),
    	episode_rewards = np.zeros(num_episodes),
        episode_q_change = np.zeros(num_episodes))

    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, epsilon, env.action_space.n)

    # For every episode
    for ith_episode in range(num_episodes):
        print("=======================================================")
        old_Q = copy_Q(Q)
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            print("\nt =", t, "sate =", state)

            # get probabilities of all actions from current state
            action_probabilities = policy(state)

            # choose action according to
            # the probability distribution
            action = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            print("action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            print("next_state =", next_state, "reward =", reward, ", done =", done)

            # Update statistics
            stats.episode_rewards[ith_episode] += reward
            stats.episode_lengths[ith_episode] = t

            if Q[state][action] != -1 * np.inf:
                # TD Update
                best_next_action = np.argmax(Q[next_state])
                td_target = reward + discount_factor * Q[next_state][best_next_action]
                td_delta = td_target - Q[state][action]
                Q[state][action] += alpha * td_delta
            else:
                if reward != -1 * np.inf:
                    print("Error in invalid actions!!!")
                    sys.exit()

            state = next_state


            # done is True if episode terminated
            if done:
                #print_Q(Q)
                #print("Total Changes =", Q_change(Q, old_Q))
                stats.episode_q_change[ith_episode] = Q_change(Q, old_Q)
                break

    
    final_policy = {}
    for i in Q:
        final_policy[i] = np.argmax(Q[i])

    #print(final_policy)
    return final_policy

