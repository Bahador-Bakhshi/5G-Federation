
from __future__ import absolute_import, division, print_function

import sys
import base64
import imageio
import IPython
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import pyvirtualdisplay

import tensorflow as tf

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.networks import sequential
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.specs import tensor_spec
from tf_agents.utils import common
from tf_agents.environments import utils

import tf_environment
import parser
import environment
from graph import debug

# ## Hyperparameters
req_num = 0
num_iterations = 100000

initial_collect_steps = 10000
collection_per_train = 200
replay_buffer_max_length = 50000 

batch_size = 32  
learning_rate = 1e-3  

log_interval = 250
eval_interval = 500 
num_eval_episodes = 10 


def check_env(env):
    env.reset()
    
    #Some checks for env
    print('Observation Spec:')
    print(env.time_step_spec().observation)

    print('Reward Spec:')
    print(env.time_step_spec().reward)

    print('Action Spec:')
    print(env.action_spec())

    time_step = env.reset()
    print('Time step:')
    print(time_step)

    action = np.array(0, dtype=np.int32)

    next_time_step = env.step(action)
    print('Next time step:')
    print(next_time_step)


def create_env(topology, src_dst_list, sfcs_list):
    #env_validation_episodes = 5

    train_py_env = tf_environment.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num =  req_num)
    #utils.validate_py_environment(train_py_env, episodes = env_validation_episodes)
    eval_py_env = tf_environment.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num = req_num)
    #utils.validate_py_environment(eval_py_env, episodes= env_validation_episodes)

    train_env = tf_py_environment.TFPyEnvironment(train_py_env)
    eval_env = tf_py_environment.TFPyEnvironment(eval_py_env)

    return train_env, eval_env


def observation_and_action_constraint_splitter(obs):
	return obs['observations'], obs['valid_actions']


def create_DQN_agent(train_env):

    fc_layer_params = (64, 64, 64, 64)
    action_tensor_spec = tensor_spec.from_spec(train_env.action_spec())
    num_actions = action_tensor_spec.maximum - action_tensor_spec.minimum + 1

    # Define a helper function to create Dense layers configured with the right
    # activation and kernel initializer.
    def dense_layer(num_units):
        return tf.keras.layers.Dense(
                    num_units,
                    activation=tf.keras.activations.relu,
                    kernel_initializer=tf.keras.initializers.VarianceScaling(
                        scale=2.0, 
                        mode='fan_in', 
                        distribution='truncated_normal'
                    )
                )

    # QNetwork consists of a sequence of Dense layers followed by a dense layer
    # with `num_actions` units to generate one q_value per available action as
    # it's output.
    dense_layers = [dense_layer(num_units) for num_units in fc_layer_params]

    q_values_layer = tf.keras.layers.Dense(
                        num_actions,
                        activation=None,
                        kernel_initializer=tf.keras.initializers.RandomUniform(
                                                minval=-0.03, 
                                                maxval=0.03
                                    ),
                        bias_initializer=tf.keras.initializers.Constant(-0.2)
                    )

    q_net = sequential.Sequential(dense_layers + [q_values_layer])

    '''
    fc_layer_params = (100,)

    q_net = q_network.QNetwork(
            train_env.observation_spec(),
            train_env.action_spec(),
            fc_layer_params=fc_layer_params
        )
    '''

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    train_step_counter = tf.Variable(0)

    epsilon_fn = tf.keras.optimizers.schedules.PolynomialDecay(
                initial_learning_rate=1.0, 
                decay_steps= int (0.8 * num_iterations),
                end_learning_rate=0.01)
    
    agent = dqn_agent.DqnAgent(
                train_env.time_step_spec(),
                train_env.action_spec(),
                q_network=q_net,
                optimizer=optimizer,
                td_errors_loss_fn=common.element_wise_squared_loss,
                train_step_counter=train_step_counter,
                epsilon_greedy=lambda: epsilon_fn(train_step_counter), 
                observation_and_action_constraint_splitter=observation_and_action_constraint_splitter
            )

    agent.initialize()

    return agent


def create_policies():
    '''     
    Agents contain two policies: 

     -   `agent.policy` — The main policy that is used for evaluation and deployment.
     -   `agent.collect_policy` — A second policy that is used for data collection.
    '''

    eval_policy = agent.policy
    collect_policy = agent.collect_policy

    return eval_policy, collect_policy


def create_random_policy(train_env):
    random_policy = random_tf_policy.RandomTFPolicy(
                                    train_env.time_step_spec(),
                                    train_env.action_spec(),
                                    observation_and_action_constraint_splitter=observation_and_action_constraint_splitter
                                )

    return random_policy


def compute_avg_return(environment, policy, num_episodes=3):

  total_return = 0.0
  for _ in range(num_episodes):

    time_step = environment.reset()
    episode_return = 0.0

    while not time_step.is_last():
      action_step = policy.action(time_step)
      time_step = environment.step(action_step.action)
      episode_return += time_step.reward
    total_return += episode_return

  avg_return = total_return / num_episodes
  return avg_return.numpy()[0]


def create_replay_buffer(agent, train_env):
    replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(
                                data_spec=agent.collect_data_spec,
                                batch_size=train_env.batch_size,
                                max_length=replay_buffer_max_length
                            )

    return replay_buffer


def collect_step(environment, policy, buffer):
  time_step = environment.current_time_step()
  action_step = policy.action(time_step)
  next_time_step = environment.step(action_step.action)
  traj = trajectory.from_transition(time_step, action_step, next_time_step)

  # Add trajectory to the replay buffer
  buffer.add_batch(traj)


def create_collect_driver(train_env, agent, replay_buffer):
    replay_buffer_observer = replay_buffer.add_batch
    driver = dynamic_step_driver.DynamicStepDriver(
                train_env,
                agent.collect_policy,
                observers=[replay_buffer_observer], #FIXME + train_metrics,
                num_steps=collection_per_train
            )

    return driver


def create_init_collect_driver(train_env, agent, replay_buffer):
    initial_collect_policy = create_random_policy(train_env)
    replay_buffer_observer = replay_buffer.add_batch

    driver = dynamic_step_driver.DynamicStepDriver(
                train_env,
                initial_collect_policy,
                observers=[replay_buffer_observer], 
                num_steps=initial_collect_steps
            )

    return driver


def create_iterator(replay_buffer):
    dataset = replay_buffer.as_dataset(
                num_parallel_calls=3, 
                sample_batch_size=batch_size, 
                num_steps=2
            ).prefetch(3)
    
    iterator = iter(dataset)
    return iterator


def train(agent, train_env, eval_env):
    try:
        get_ipython().run_line_magic('time', '')
    except:
        pass

    replay_buffer = create_replay_buffer(agent, train_env)
    if debug > 1:
        print("replay_buffer is created ")
    
    init_driver = create_init_collect_driver(train_env, agent, replay_buffer)
    if debug > 1:
        print("init_driver is created")
    
    init_driver.run()
    if debug > 1:
        print("init_driver run")
    
    iterator = create_iterator(replay_buffer)
    if debug > 1:
        print("iterator is created")

    collect_driver = create_collect_driver(train_env, agent, replay_buffer)
    if debug > 1:
        print("collect_driver is created")

    agent.train = common.function(agent.train)
    collect_driver.run = common.function(collect_driver.run)

    # Reset the train step
    agent.train_step_counter.assign(0)

    # Evaluate the agent's policy once before training.
    #avg_return = compute_avg_return(eval_env, agent.policy, num_eval_episodes)
    #print("avg_return at begging = ", avg_return)
    #returns = [avg_return]
    returns = []

    for _ in range(num_iterations):
    
        time_step = None
        policy_state = None 

        time_step, policy_state = collect_driver.run(time_step, policy_state)
        trajectories, buffer_info = next(iterator)
        train_loss = agent.train(trajectories)

        step = agent.train_step_counter.numpy()

        if step % log_interval == 0:
            print('step = {0}: loss = {1}'.format(step, train_loss), flush = True)

        if step % eval_interval == 0:
            avg_return = compute_avg_return(eval_env, agent.policy, num_eval_episodes)
            print('step = {0}: Average Return = {1}'.format(step, avg_return))
            returns.append(avg_return)


def main(topology, src_dst_list, sfcs_list):
    train_env, eval_env = create_env(topology, src_dst_list, sfcs_list)

    #check_env(train_env)
    #sys.exit(-1)

    agent = create_DQN_agent(train_env)
    train(agent, train_env, eval_env)
    return agent


def evaluate_agent(topology, src_dst_list, sfcs_list, agent, demands):
    print("------------- Evaluating -------------")
    test_py_env = tf_environment.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num=req_num, requests=demands)
    test_env = tf_py_environment.TFPyEnvironment(test_py_env)

    num_episodes = 10
    total_return = 0
    for _ in range(num_episodes):
        time_step = test_env.reset()
        episode_return = 0

        while not time_step.is_last():
            action_step = agent.policy.action(time_step)
            time_step = test_env.step(action_step.action)
            episode_return += time_step.reward
        
        total_return += episode_return
    

    #aavg_return = total_return / num_episodes
    #avg_return = avg_return.numpy()[0] / len(demands)
    #return avg_return, 0, 0
    
    return (total_return.numpy()[0])/num_episodes


if __name__ == "__main__":
    parser.parse_config("config.json")
    agent = main()
    demands = Environment.generate_req_set(req_num)
    evaluate_agent(agent, demands)

