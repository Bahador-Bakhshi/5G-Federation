#!/usr/bin/python3
import sys
import numpy as np

import gpu

import network
import requests
import environment_pps
import traditionals
import parser
import kpath
import tf_agent_ppo_pps

from graph import debug

class Tester_Agent:

    def __init__(self, topology, policy, observer):
        self.topology = topology.copy()
        network.reset_topology(self.topology)
        self.policy = policy
        self.observer = observer
        self.env = environment_pps.Environment(self.topology, self.observer)

    def test(self, requests):
        self.env.set_test_requests(requests)
        observation, _ = self.env.reset()

        done = 0
        total_reward = 0
        accept = 0
        while done == 0:
            action = self.policy(observation)
            observation, reward, done, _ = self.env.step(action)
            total_reward += reward
            if reward > 0:
                accept += 1

        print("accept = ", accept)
        return total_reward


def main():
    topology = parser.generate_topo("topo_10_1.json")
    if debug > 3:
        print(topology.edges(data = True))
    parser.parse_sfc_config("config.json")

    src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(topology)
  
    tf_agent_ppo_pps.req_num = req_num
    the_best_policy = tf_agent_ppo_pps.main(topology, src_dst_list, sfcs_list)
    
    org_lambdas = []
    for index in requests.traffic_config["traffic_rates"]:
        org_lambdas.append(index["lambda"])

    for i in range(4,5):
        scale = 0.2 + i * 0.2
        for index in range(len(requests.traffic_config["traffic_rates"])):
            requests.traffic_config["traffic_rates"][index]["lambda"] = org_lambdas[index] * scale
        
        print("lambdas = ", requests.traffic_config["traffic_rates"])

        total_reward_ddqn = total_reward_mhc = total_reward_kpath = 0.0
        for _ in range(20):
            all_requests = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)
            
            total_reward_ddqn += tf_agent_ppo_pps.evaluate_policy(topology, src_dst_list, sfcs_list, the_best_policy, all_requests, True)
            #print("Total reward - Deep = ", total_reward)

            min_hop_count_tester = Tester_Agent(topology, traditionals.MinHopCount.policy, traditionals.MinHopCount.observer)
            total_reward_mhc += min_hop_count_tester.test(all_requests)
            #print("Total reward - MHC  = ", total_reward)

            k_widest_tester = Tester_Agent(topology, kpath.WidestKpath.policy, kpath.WidestKpath.observer)
            total_reward_kpath += k_widest_tester.test(all_requests)
            #print("Total reward - KPath= ", total_reward)

        print("Total reward - Deep  = ", total_reward_ddqn / 20.0)
        print("Total reward - MHC   = ", total_reward_mhc / 20.0)
        print("Total reward - Kpath = ", total_reward_kpath / 20.0)

if __name__ == "__main__":
    main()

    
