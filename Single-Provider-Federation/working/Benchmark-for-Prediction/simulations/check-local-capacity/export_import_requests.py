#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import csv
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


def load_reqs(reqs_file_name = "./requests.csv"):

    all_req = []

    with open(reqs_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            elif len(row) > 0:
                c1 = int(row[0])
                c2 = int(row[1])
                c3 = int(row[2])
                ts = float(row[3])
                dt = float(row[4])
                rev = int(row[5])
                class_id = int(row[6])
            
                req = Environment.Request(ts, dt, rev, class_id)
                req.cap = [c1,c2,c3].copy()
                all_req.append(req)

            line_count += 1

    return all_req

if __name__ == "__main__":

    sim_num = 100000
    episode_num = 1

    parser.parse_config("config.json")

    env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), episode_num)
   
    demands = Environment.generate_req_set(sim_num)
    print_reqs_csv(demands)
    
    '''
    
    demands = load_reqs(reqs_file_name = "./requests.csv")

    Environment.print_reqs(demands)
    
    '''
