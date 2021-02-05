import sys
import sklearn
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
import gym
import itertools 
from collections import deque
import matplotlib as mpl
import matplotlib.pyplot as plt

IS_COLAB = False

if not tf.config.list_physical_devices('GPU'):
    print("No GPU was detected. CNNs can be very slow without a GPU.")
    if IS_COLAB:
        print("Go to Runtime > Change runtime and select a GPU hardware accelerator.")


class Memory_Entity:
    def __init__(self, state, action, reward, next_state):
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state

    def entry_hash(self, entry):
        state_tuple = tuple(entry.state)
        action_tuple = entry.action
        reward_tuple = entry.reward
        next_state_tuple = tuple(entry.next_state)

        return hash((state_tuple, action_tuple, reward_tuple, next_state_tuple))

    def __hash__(self):
        return self.entry_hash(self)

    def __eq__(self, other):
        return self.entry_hash(self) == self.entry_hash(other)

    def __str__(self):
        return str(self.state) +","+ str(self.action) +","+ str(self.reward) +","+ str(self.next_state)


def print_deque(q):
    for e in q:
        print("\t", e)


batch_size = 16
discount_rate = 0.95
input_shape = [5] # server_size, a1, a2, r1, r2
n_outputs = 2
optimizer = keras.optimizers.Adam(lr=1e-3)
loss_fn = keras.losses.mean_squared_error

replay_memory = deque(maxlen=2000)

def tuple_to_array_state(state):
    res = np.array([state[0], state[1][0], state[1][1], state[2][0], state[2][1]])
    return res

def array_to_tuple_state(state):
    tmp1 = (state[1], state[2])
    tmp2 = (state[3], state[4])
    res =  (state[0], tmp1, tmp2)
    return res


def epsilon_greedy_policy(model, num_actions, state, epsilon=0):
    if np.random.rand() < epsilon:
        return np.random.randint(num_actions), True
    else:
        #print("State = ", state, ", shape = ", state.shape)
        Q_values = model.predict(state[np.newaxis])
        return np.argmax(Q_values[0]), False

def sample_experiences(batch_size):
    indices = np.random.randint(len(replay_memory), size=batch_size)
    batch = [replay_memory[index] for index in indices]
    states = np.array([experience.state for experience in batch])
    actions = np.array([experience.action for experience in batch])
    rewards = np.array([experience.reward for experience in batch])
    next_states = np.array([experience.next_state for experience in batch])
    return states, actions, rewards, next_states


def train_model(model, batch_size):
    experiences = sample_experiences(batch_size)
    states, actions, rewards, next_states = experiences
    print("train_model: experience = ", experiences)

    next_Q_values = model.predict(next_states)
    print("train_model: next_Q_values = ", next_Q_values)
    max_next_Q_values = np.max(next_Q_values, axis=1)

    target_Q_values = (rewards + discount_rate * max_next_Q_values)
    target_Q_values = target_Q_values.reshape(-1, 1)
    mask = tf.one_hot(actions, n_outputs)
    with tf.GradientTape() as tape:
        all_Q_values = model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))


def dqLearning(env, num_episodes, gamma0 = 0.9, epsilon0 = 0.8):
    keras.backend.clear_session()
    model = keras.models.Sequential([
        keras.layers.Dense(16, activation="elu", input_shape=input_shape),
        keras.layers.Dense(8, activation="elu"),
        keras.layers.Dense(n_outputs)
    ])
    print("Model Summary:")
    print(model.summary())

    for episode in range(num_episodes):
        print("episode = ", episode)
        state = tuple_to_array_state(env.reset())

        epsilon = max(epsilon0 - episode / 500, 0.01)
        gamma = max(gamma0 - episode / 500, 0.01)

        for iteration in itertools.count():
            print("\nt =", iteration, "sate =", state)

            action, random = epsilon_greedy_policy(model, env.action_space.n, state, epsilon)
            next_state, reward, done = env.step(array_to_tuple_state(state), action)
        
            if done:
                break

            next_state = tuple_to_array_state(next_state)
            print("next_state =", next_state, "reward =", reward, ", done =", done)
            
            new_entry = Memory_Entity(state, action, reward, next_state)
            
            #print("replay_memory = ")
            #print_deque(replay_memory)

            try:
                index = replay_memory.index(new_entry) 
                #print("new_entry_index = ", index)
            except ValueError:
                '''
                print("Checking deque elements - 1 ...")
                
                for e in replay_memory:
                    print("e = ", e)
                    print("new_entry = ", new_entry)
                    if e == new_entry:
                        print("e == new_entry")
                    else:
                        print("e !!! new_entry")
                '''
                print("Adding new_entry")
                replay_memory.append(new_entry)
                
                '''
                print("Checking deque elements - 2 ...")
                
                for e in replay_memory:
                    print("e = ", e)
                    print("new_entry = ", new_entry)
                    if e == new_entry:
                        print("e == new_entry")
                    else:
                        print("e !!! new_entry")
                '''
            except:
                print("Error")
                sys.exit(-1)

            state = next_state

    
        if episode > 5:
            train_model(model, batch_size)

    
    def policy_function(state):
        state = tuple_to_array_state(state)
        action, random = epsilon_greedy_policy(model, env.action_space.n, state, epsilon=0.05)
        return action, random

    return policy_function

