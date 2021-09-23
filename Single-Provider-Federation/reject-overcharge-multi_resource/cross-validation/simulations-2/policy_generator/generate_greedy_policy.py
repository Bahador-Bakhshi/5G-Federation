#!/usr/bin/python3

import numpy as np
import math
import csv
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

DP_POLICY_FILE = "./Policy-DP-2-proc"

if __name__ == "__main__":

    parser.parse_config("config.json")

    with open(DP_POLICY_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",",row[6])
            elif len(row) > 0:
                l1 = int(row[0])
                l2 = int(row[1])

                f1 = int(row[2])
                f2 = int(row[3])

                a1 = int(row[4])
                a2 = int(row[5])

                state = Environment.State(2)

                state.domains_alives = [(l1,l2),(f1,f2)]
                state.arrivals_departures = (a1,a2)

                valid_actions = Environment.get_valid_actions(state)

                if Environment.Actions.accept in valid_actions:
                    print("{},{},{},{},{},{},accept".format(l1,l2,f1,f2,a1,a2))
                elif Environment.Actions.federate in valid_actions:
                    print("{},{},{},{},{},{},federate".format(l1,l2,f1,f2,a1,a2))
                else:
                    print("{},{},{},{},{},{},reject".format(l1,l2,f1,f2,a1,a2))
                
            line_count += 1

