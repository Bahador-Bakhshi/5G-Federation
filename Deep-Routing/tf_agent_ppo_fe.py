
import numpy as np
import sys

import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import
from tf_agents.agents.ppo import ppo_clip_agent
from tf_agents.drivers import dynamic_episode_driver
from tf_agents.environments import suite_pybullet
from tf_agents.environments import tf_py_environment
from tf_agents.environments import parallel_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import actor_distribution_network
from tf_agents.networks import actor_distribution_rnn_network
from tf_agents.networks import value_network
from tf_agents.networks import value_rnn_network
from tf_agents.policies import policy_saver
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.system import system_multiprocessing as multiprocessing
from tf_agents.utils import common


import tf_environment_fe
import parser
import environment
import requests
from graph import debug

return_evaluation_demands = None
use_rnns = False
lstm_size = (20,)

actor_fc_layers = (128, 128, 128, 128, 128)
value_fc_layers = (128, 128, 128, 128, 128)

num_parallel_environments = 8
batch_size = num_parallel_environments
#sample_batch_size = 8
replay_buffer_capacity = 10000
collect_episodes_per_iteration = 1

learning_rate  = 1e-4
training_steps = 300
training_eval_interval = 10

'''
def train_agent(
        topology = None, 
        src_dst_list = None, 
        sfcs_list = None):
'''

#def train_agent(_):
def train_agent(*args, **kwargs):
    eval_py_env = tf_environment_fe.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num = req_num)
    
    def env_generator():
        return tf_environment_fe.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num = req_num)
    train_py_env = parallel_py_environment.ParallelPyEnvironment([lambda: env_generator()] * num_parallel_environments)
    
    tf_env = tf_py_environment.TFPyEnvironment(train_py_env)
    eval_tf_env = tf_py_environment.TFPyEnvironment(eval_py_env)

    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    
    if use_rnns:
        actor_net = actor_distribution_rnn_network.ActorDistributionRnnNetwork(
                        tf_env.observation_spec(),
                        tf_env.action_spec(),
                        input_fc_layer_params=actor_fc_layers,
                        output_fc_layer_params=None,
                        lstm_size=lstm_size)

        value_net = value_rnn_network.ValueRnnNetwork(
                        tf_env.observation_spec(),
                        input_fc_layer_params=value_fc_layers,
                        output_fc_layer_params=None)
    else:
        actor_net = actor_distribution_network.ActorDistributionNetwork(
                        tf_env.observation_spec(),
                        tf_env.action_spec(),
                        fc_layer_params=actor_fc_layers,
                        activation_fn=tf.keras.activations.tanh)

        value_net = value_network.ValueNetwork(
                        tf_env.observation_spec(),
                        fc_layer_params=value_fc_layers,
                        activation_fn=tf.keras.activations.tanh)
    
    global_step = tf.compat.v1.train.get_or_create_global_step()
    
    tf_agent = ppo_clip_agent.PPOClipAgent(
        tf_env.time_step_spec(),
        tf_env.action_spec(),
        optimizer,
        actor_net=actor_net,
        value_net=value_net,
        entropy_regularization=0.0,
        importance_ratio_clipping=0.2,
        normalize_observations=False,
        normalize_rewards=False,
        use_gae=True,
        #num_epochs=num_epochs,
        #debug_summaries=debug_summaries,
        #summarize_grads_and_vars=summarize_grads_and_vars,
        train_step_counter=global_step)
    
    tf_agent.initialize()

    eval_policy = tf_agent.policy
    collect_policy = tf_agent.collect_policy

    print("tf_agent.collect_data_spec = ",  tf_agent.collect_data_spec)

    replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(
        tf_agent.collect_data_spec,
        batch_size=batch_size,
        max_length=replay_buffer_capacity)

    collect_driver = dynamic_episode_driver.DynamicEpisodeDriver(
        tf_env,
        collect_policy,
        observers=[replay_buffer.add_batch], # + train_metrics,
        num_episodes=collect_episodes_per_iteration)
    
    '''
    dataset = replay_buffer.as_dataset(
                sample_batch_size=sample_batch_size, 
                num_steps=2
            ).prefetch(4)

    iterator = iter(dataset)
    '''

    collect_driver.run = common.function(collect_driver.run, autograph=False)
    tf_agent.train = common.function(tf_agent.train, autograph=False)

    training_counter = 0
    while training_counter < training_steps:
    
        collect_driver.run()
        trajectories = replay_buffer.gather_all()
        #trajectories, buffer_info = next(iterator)
        total_loss, _ = tf_agent.train(experience=trajectories)
        replay_buffer.clear()

        if training_counter % training_eval_interval == 0:
            print("step = ", training_counter," Return = ", evaluate_agent(topology, src_dst_list, sfcs_list, tf_agent, return_evaluation_demands))
            print("step = ", training_counter," Loss   = ", total_loss, flush=True)

        training_counter += 1

    global agent
    agent = tf_agent


def evaluate_agent(topology, src_dst_list, sfcs_list, agent, demands):

    test_py_env = tf_environment_fe.TF_Agent_Env_Wrapper(topology.copy(), src_dst_list, sfcs_list, req_num = req_num)
    test_env = tf_py_environment.TFPyEnvironment(test_py_env)

    num_episodes = 1
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


def main(this_topology, this_src_dst_list, this_sfcs_list):
    global topology, src_dst_list, sfcs_list, return_evaluation_demands
    global agent 
    
    topology = this_topology
    src_dst_list = this_src_dst_list
    sfcs_list = this_sfcs_list

    return_evaluation_demands = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)
   
    multiprocessing.handle_test_main(train_agent)

    print("\n\n\n\n-------------------------------------")

    return agent


if __name__ == '__main__':
    global topology, src_dst_list, sfcs_list, req_num

    topology = parser.generate_topo("topo_02_1.json")
    parser.parse_sfc_config("config_02.json")
    src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(topology)
    
    return_evaluation_demands = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)
    
    multiprocessing.handle_main(train_agent)

