#import random
#import numpy as np
#from collections import deque
#from keras.models import Sequential
#from keras.layers import Dense, Dropout
#import tensorflow as tf
#from tensorflow import keras

import sys
import sklearn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import Adadelta
import numpy as np
import os
import gym
import itertools 
from collections import deque
from collections import defaultdict 

class Memory_Entity:
    def __init__(self, state, action, reward, next_state):
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state

    '''
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
    '''

    def __str__(self):
        return str(self.state) +","+ str(self.action) +","+ str(self.reward) +","+ str(self.next_state)


def print_deque(q):
    for e in q:
        print("\t", e)


class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate):
        self.fit_individual = False
        self.epochs = 100
        self.state_size = state_size
        self.lr = learning_rate
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.model = self._build_model()
        #self.target = self.model 
        self.target = self._build_model()
        self.history = []
        self.state_importance = None
    
    def reset_importance(self):
        self.state_importance = defaultdict(lambda: 0)

    def _build_model(self):  # Neural Net for Deep-Q learning Model

        keras.backend.clear_session()
        model = keras.models.Sequential()
        model.add(keras.layers.Dense(4, activation="elu", input_shape = [self.state_size]))
        model.add(keras.layers.Dense(4, activation="elu"))
        model.add(keras.layers.Dense(4, activation="elu"))
        model.add(keras.layers.Dense(self.action_size, activation="linear"))
   
        print("learning_rate = ", self.lr)
        model.compile(loss='mse', optimizer=Adadelta(lr=self.lr))
        
        print("Model Summary:")
        print(model.summary())

        '''
        model = Sequential()
        model.add(Dense(32, input_dim=self.state_size, activation='relu'))
        model.add(Dropout(rate=0.2))
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(rate=0.2))
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(rate=0.2))
        model.add(Dense(self.action_size, activation='linear'))
        '''

        return model

    def remember(self, state, action, reward, next_state):
        new_entry = Memory_Entity(state, action, reward, next_state)
        try:
            index = self.memory.index(new_entry) 
        except ValueError:
            print("Adding new_entry")
            self.memory.append(new_entry)
        except:
            print("Error")
            sys.exit(-1)


    def sample(self, batch_size):
        indices = np.random.randint(len(self.memory), size=batch_size)
        batch = [self.memory[index] for index in indices]
        states = np.array([experience.state for experience in batch])
        actions = np.array([experience.action for experience in batch])
        rewards = np.array([experience.reward for experience in batch])
        next_states = np.array([experience.next_state for experience in batch])
        return states, actions, rewards, next_states


    def act(self, state, epsilon):
        if np.random.rand() <= epsilon:
            return np.random.randint(self.action_size), True

        act_values = self.model.predict(np.array([state]))
        print("state = ", state, ", act_values = ", act_values)
        return np.argmax(act_values[0]), False


    def unify_q_values(self, states, actions, next_states, updated_target_Q_values):
        #for p in self.state_importance.keys():
        #    print("pair = ", p, ", importance = ", self.state_importance[p])

        for i in range(len(states)):
            for j in range(len(states)):
                if i != j:
                    '''
                    print("states[",i,"] = ", states[i])
                    print("states[",j,"] = ", states[j])
                    print("Q[",i,"] = ", updated_target_Q_values[i])
                    print("Q[",j,"] = ", updated_target_Q_values[j])
                    '''

                    if np.all(states[i] -  states[j] == 0): 
                        '''
                        print("Equal")
                        print("actions[",i,"] = ", actions[i])
                        print("actions[",j,"] = ", actions[j])
                        '''
                        if actions[i] != actions[j]:
                            updated_target_Q_values[i][actions[j]] = updated_target_Q_values[j][actions[j]]
                            updated_target_Q_values[j][actions[i]] = updated_target_Q_values[i][actions[i]]
                        else:
                            pair_i = tuple(zip(tuple(states[i]), tuple(next_states[i])))
                            importance_i = self.state_importance[pair_i]

                            pair_j = tuple(zip(tuple(states[j]), tuple(next_states[j])))
                            importance_j = self.state_importance[pair_j]

                            weighted_average = (importance_i * updated_target_Q_values[i][actions[i]] + importance_j * updated_target_Q_values[j][actions[j]]) / (1.0 * importance_i + importance_j)

                            updated_target_Q_values[i][actions[i]] = updated_target_Q_values[j][actions[j]] = weighted_average

                        for k in range(len(updated_target_Q_values[i])):
                            if k != actions[i] and k != actions[j]:
                                updated_target_Q_values[i][k] = updated_target_Q_values[j][k] = 0.5 * (updated_target_Q_values[i][k] + updated_target_Q_values[j][k])
                    '''
                    print("Q[",i,"] = ", updated_target_Q_values[i])
                    print("Q[",j,"] = ", updated_target_Q_values[j])
                    '''

    def train(self, batch_size, discount_rate):
        experiences = self.sample(batch_size)
        states, actions, rewards, next_states = experiences
        updated_target_Q_values = np.zeros(shape=(batch_size, self.action_size))

        individual_history = []

        for i in range(batch_size):
            #print("train: experience = ")
            #print("\t", states[i], actions[i], rewards[i], next_states[i])
   
            next_Q_values = self.model.predict(next_states[i][np.newaxis])
            #print("train: online next_Q_values = ", next_Q_values)
            
            best_next_actions = np.argmax(next_Q_values, axis=1)
            #print("train: best_next_actions = ", best_next_actions)
            
            next_mask = tf.one_hot(best_next_actions, self.action_size).numpy()
            next_best_Q_values = (self.target.predict(next_states[i][np.newaxis]) * next_mask).sum(axis=1)
            #print("train: traget next_best_Q_values = ", next_best_Q_values)

            observed_target_Q_values = (rewards[i] + discount_rate * next_best_Q_values)
            #print("train: observed_target_Q_values = ", observed_target_Q_values)
 
            old_Q_values = self.model.predict(states[i][np.newaxis])
            #print("train: old_Q_values = ", old_Q_values)
            
            updated_target_Q_values[i] = old_Q_values
            #print("train: updated_target_Q_values = ", updated_target_Q_values)
            
            updated_target_Q_values[i][actions[i]] = observed_target_Q_values[0]
            #print("train: updated_target_Q_values = ", updated_target_Q_values)
            
            if self.fit_individual:
                hist = self.model.fit(states[i][np.newaxis], updated_target_Q_values[i][np.newaxis], epochs=self.epochs, verbose=0)
                individual_history.append(hist.history["loss"][0])

        if self.fit_individual:
            self.history.append(individual_history)

        else:
            print("------------------------------------")
            print("states = ", states)
            print("actions= ", actions)
            print("before unifying: updated_target_Q_values = ", updated_target_Q_values)
            self.unify_q_values(states, actions, next_states, updated_target_Q_values)
            print("after unifying: updated_target_Q_values = ", updated_target_Q_values)

            hist = self.model.fit(states, updated_target_Q_values, epochs=self.epochs, verbose=0)
            print("after fit: ")
            for s in states:
                print(self.model.predict(s[np.newaxis]))

            self.history.append(hist)

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


def tuple_to_array_state(state):
    res = np.array([state[0], state[1][0], state[1][1], state[2][0], state[2][1]])
    return res


def array_to_tuple_state(state):
    tmp1 = (state[1], state[2])
    tmp2 = (state[3], state[4])
    res =  (state[0], tmp1, tmp2)
    return res


def ddqLearning(env, num_episodes, gamma0 = 0.9, epsilon0 = 0.8):
    features_num = 5
    actions_num  = 2
    batch_size   = 8
    learning_rate= 0.001

    agent = DQNAgent(features_num, actions_num, learning_rate)

    for episode in range(num_episodes):
        print("episode = ", episode)
        state = tuple_to_array_state(env.reset())
        agent.reset_importance()

        epsilon = max(epsilon0 - episode / 500, 0.01)
        gamma = max(gamma0 - episode / 500, 0.01)

        for iteration in itertools.count():
            print("\nt =", iteration, "sate =", state)

            action, random = agent.act(state, epsilon)
            next_state, reward, done = env.step(array_to_tuple_state(state), action)
        
            if done:
                break

            next_state = tuple_to_array_state(next_state)
            print("next_state =", next_state, "reward =", reward, ", done =", done)
           
            agent.remember(state, action, reward, next_state)
            state_pair = tuple(zip(tuple(state), tuple(next_state)))

            agent.state_importance[state_pair] = agent.state_importance[state_pair] + 1

            state = next_state
    
        if episode > 10:
            agent.train(batch_size, gamma)

        if episode % 15 == 0:
            agent.target.set_weights(agent.model.get_weights()) 
   

        loss_sum = 0
        if agent.fit_individual:
            print("agent.history = ", agent.history)
            for h in agent.history:
                print("h = ", h)
                for v in h:
                    loss_sum = loss_sum + v
        else:
            for h in agent.history:
                for v in h.history['loss']:
                    loss_sum = loss_sum + v

        agent.history = []
        print("loss = ", loss_sum / 1000.0)

    def policy_function(state):
        state = tuple_to_array_state(state)
        action, random = agent.act(state, epsilon=0.05)
        return action, random

    return policy_function

