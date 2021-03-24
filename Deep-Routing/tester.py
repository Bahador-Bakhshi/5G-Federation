#!/bin/python3
import sys
import numpy as np

import network
import requests
import environment
import traditionals
import parser
import kpath
import tf_agent

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
    topology = parser.generate_topo("topo_03_1.json")
    print(topology.edges(data = True))
    parser.parse_sfc_config("config.json")

    src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(topology)
    
    agent = tf_agent.main(topology, src_dst_list, sfcs_list)

    '''
    all_requests = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)

    min_hop_count_tester = Tester_Agent(topology, traditionals.MinHopCount.policy, traditionals.MinHopCount.observer)
    total_reward = min_hop_count_tester.test(all_requests)
    print("Total reward = ", total_reward)

    k_widest_tester = Tester_Agent(topology, kpath.WidestKpath.policy, kpath.WidestKpath.observer)
    total_reward = k_widest_tester.test(all_requests)
    print("Total reward = ", total_reward)
    '''

if __name__ == "__main__":
    main()

    
