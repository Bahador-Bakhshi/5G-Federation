#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import heapq
import itertools 
import random
import Environment
import parser
import QL
import RL
import DP
from Environment import State, debug, error, warning, verbose
from tester import test_greedy_random_policy, test_policy, greedy_result, mdp_policy_result

def print_reqs_csv(reqs):
    print("c1, c2, c3, st, dt, rev, class_id")
    for r in reqs:
        print(r.cap[0],",",r.cap[1],",",r.cap[2],",",r.st,",",r.dt,",",r.rev,",",r.class_id)

def load_reqs()

if __name__ == "__main__":

    sim_num = 4
    episode_num = 1

    parser.parse_config("config.json")

    env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
   
    demands = Environment.generate_req_set(sim_num)
    print_reqs_csv(demands)


