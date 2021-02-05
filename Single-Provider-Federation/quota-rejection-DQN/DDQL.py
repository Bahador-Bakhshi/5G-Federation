import sys
import sklearn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import optimizers
import numpy as np
import os
import gym
import itertools 
from collections import deque
from collections import defaultdict 
import Environment

class Memory_Entity:
    def __init__(self, state, action, reward, next_state):
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state

    def __str__(self):
        return str(self.state) +","+ str(self.action) +","+ str(self.reward) +","+ str(self.next_state)


def print_deque(q):
    for e in q:
        print("\t", e)


class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate):
        self.fit_individual = True
        self.epochs = 1
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
        model.add(keras.layers.Dense(16, activation="elu", input_shape = [self.state_size]))
        model.add(keras.layers.Dense(16, activation="elu"))
        model.add(keras.layers.Dense(16, activation="elu"))
        model.add(keras.layers.Dense(16, activation="elu"))
        model.add(keras.layers.Dense(self.action_size))
   
        print("learning_rate = ", self.lr)
        model.compile(loss='mse', optimizer=optimizers.Adam(lr=self.lr))
        
        print("Model Summary:")
        print(model.summary())

        return model


    def remember(self, state, action, reward, next_state):
        new_entry = Memory_Entity(object_to_array_state(state), action, reward, object_to_array_state(next_state))
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
        va = Environment.get_valid_actions(state)
        valid_action_size = len(va)

        if np.random.rand() <= epsilon:
            rand_index = np.random.randint(valid_action_size)
            return va[rand_index], True

        act_values = self.model.predict(np.array([object_to_array_state(state)]))
        
        #print("1) state = ", state, ", act_values = ", act_values)
        for a in Environment.Actions:
            if not (a in va):
                act_values[0][a] = -1 * np.inf

        print("2) state = ", state, ", act_values = ", act_values)

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
            print("train: experience = ")
            print("\t", states[i], actions[i], rewards[i], next_states[i])
   
            next_Q_values = self.model.predict(next_states[i][np.newaxis])
            va = Environment.get_valid_actions(array_to_object_state(next_states[i]))
            for a in Environment.Actions:
                if not (a in va):
                    next_Q_values[0][a] = -1 * np.inf
            print("train: online next_Q_values = ", next_Q_values)
            
            best_next_actions = np.argmax(next_Q_values, axis=1)
            print("train: best_next_actions = ", best_next_actions)
            
            next_mask = tf.one_hot(best_next_actions, self.action_size).numpy()
            next_best_Q_values = (self.target.predict(next_states[i][np.newaxis]) * next_mask).sum(axis=1)
            print("train: traget next_best_Q_values = ", next_best_Q_values)

            observed_target_Q_values = (rewards[i] + discount_rate * next_best_Q_values)
            print("train: observed_target_Q_values = ", observed_target_Q_values)
 
            old_Q_values = self.model.predict(states[i][np.newaxis])
            print("train: old_Q_values = ", old_Q_values)
            
            updated_target_Q_values[i] = old_Q_values
            #print("train: updated_target_Q_values = ", updated_target_Q_values)
            
            updated_target_Q_values[i][actions[i]] = observed_target_Q_values[0]
            print("train: updated_target_Q_values = ", updated_target_Q_values)
            
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


def object_to_array_state(state):
    res = np.zeros(Environment.State.state_fields_num)
    index = 0
    for i in range(len(state.domains_alives)):
        for j in range(len(state.domains_alives[i])):
            res[index] = state.domains_alives[i][j]
            index += 1

    for i in range(len(state.arrivals_departures)):
        res[index] = state.arrivals_departures[i]
        index += 1

    #print("state --> array: state = ", state, ", array = ", res)
    return res


def array_to_object_state(state):
    res = Environment.State(Environment.total_classes)
    index = 0
    
    for i in range(len(res.domains_alives)):
        tmp_list = [0] * Environment.total_classes
        for j in range(len(res.domains_alives[i])):
            tmp_list[j] = state[index]
            index += 1
            
        res.domains_alives[i] = tuple(tmp_list)

    tmp_list = [0] * Environment.total_classes
    for i in range(len(res.arrivals_departures)):
        tmp_list[i] = state[index]
        index += 1

    res.arrivals_departures = tuple(tmp_list)
    
    print("array --> state: array = ", state, ", state = ", res)
    return res


def ddqLearning(env, num_episodes, gamma0 = 0.9, epsilon0 = 0.8):
    batch_size   = 32
    learning_rate= 0.005

    agent = DQNAgent(3 * Environment.total_classes, len(Environment.Actions), learning_rate)

    for episode in range(num_episodes):
        print("episode = ", episode)
        state = env.reset()
        agent.reset_importance()

        epsilon = max(epsilon0 - episode / 500, 0.01)
        gamma = max(gamma0 - episode / 500, 0.01)

        for iteration in itertools.count():
            print("t =", iteration, "sate =", state)

            action, random = agent.act(state, epsilon)
            print("action = ", action, ", random = ", random)
            next_state, reward, done = env.step(state, action)
        
            if done:
                break

            print("next_state =", next_state, "reward =", reward, ", done =", done)
           
            agent.remember(state, action, reward, next_state)
            state_pair = tuple(zip(tuple(object_to_array_state(state)), tuple(object_to_array_state(next_state))))

            agent.state_importance[state_pair] = agent.state_importance[state_pair] + 1

            state = next_state
    
        if episode > 20:
            agent.train(batch_size, gamma)

        if episode % 50 == 0:
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
        action, random = agent.act(state, epsilon=0.05)
        return action, random

    return policy_function

