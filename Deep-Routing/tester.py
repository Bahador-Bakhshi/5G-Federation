#!/usr/bin/python3
import sys
import numpy as np

import gpu

import network
import requests
import environment
import traditionals
import parser
import kpath
import tf_agent

from graph import debug

class Tester_Agent:

    def __init__(self, topology, policy, observer):
        self.topology = topology
        self.policy = policy
        self.observer = observer
        self.env = environment.Environment(self.topology, self.observer)

    def test(self, requests):
        self.env.set_test_requests(requests)
        observation = self.env.reset()

        done = 0
        total_reward = 0

        while done == 0:
            action = self.policy(observation)
            observation, reward, done = self.env.step(action)
            total_reward += reward

        return total_reward


def main():
    topology = parser.generate_topo("topo_10_1.json")
    if debug > 3:
        print(topology.edges(data = True))
    parser.parse_sfc_config("config.json")

    src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(topology)
  
    tf_agent.req_num = req_num
    agent = tf_agent.main(topology, src_dst_list, sfcs_list)

    for i in range(20):
        all_requests = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)
    
        total_reward = tf_agent.evaluate_agent(topology, src_dst_list, sfcs_list, agent, all_requests)
        print("Total reward - Deep = ", total_reward)

        min_hop_count_tester = Tester_Agent(topology, traditionals.MinHopCount.policy, traditionals.MinHopCount.observer)
        total_reward = min_hop_count_tester.test(all_requests)
        print("Total reward - MHC  = ", total_reward)

        k_widest_tester = Tester_Agent(topology, kpath.WidestKpath.policy, kpath.WidestKpath.observer)
        total_reward = k_widest_tester.test(all_requests)
        print("Total reward - KPath= ", total_reward)

if __name__ == "__main__":
    main()

    
