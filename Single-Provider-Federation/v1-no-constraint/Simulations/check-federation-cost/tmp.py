#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import QL
import heapq
import itertools 
import matplotlib 
import matplotlib.style 
import Environment
import parser
import DP
from tester import test_greedy_policy, test_policy
from Environment import debug, error, warning

if __name__ == "__main__":

    sim_time = 70
    episode_num = 150

    parser.parse_config("config.json")

    init_mult = 0
    step = 0.25
    scale = 25

    i = 0

    org_fed_cost = [None for j in range(len(Environment.providers))]
    for j in range(len(Environment.providers)):
        org_fed_cost[j] = {}
        for k in Environment.domain.services:
            org_fed_cost[j][k] = Environment.providers[j].federation_costs[k]

    while i <= scale:
        for j in range(len(Environment.providers)):
            for k in Environment.domain.services:
                Environment.providers[j].federation_costs[k] = org_fed_cost[j][k] * (init_mult + i * step)
        i += 1


        print("Costs Scale = ", init_mult + i * step)
