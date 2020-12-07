#!/usr/bin/python3

import json
from numpy import *
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("Usage: ", str(sys.argv[0]), "input_file")
    sys.exit()

res_file_handler = open(str(sys.argv[1])+".json")
res = json.load(res_file_handler)
res_file_handler.close()

x_label = res["x_label"]
results = res["results"]

x = []
DP_95 = []
QL_09  = []
QL_05  = []
RL  = []

gap = lambda a, b : (a - b) / a
for data in results:
    x.append(data["x"])
    DP_95_tmp = data["DP_95"]
    QL_09_tmp = data["QL_09"]
    QL_05_tmp = data["QL_05"]
    RL_tmp = data["RL"]
    
    QL_09_tmp = gap(DP_95_tmp, QL_09_tmp)
    QL_05_tmp = gap(DP_95_tmp, QL_05_tmp)
    RL_tmp = gap(DP_95_tmp, RL_tmp)
    DP_95_tmp = gap(DP_95_tmp, DP_95_tmp)

    DP_95.append(DP_95_tmp)
    QL_09.append(QL_09_tmp)
    QL_05.append(QL_05_tmp)
    RL.append(RL_tmp)

font = {
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
plt.rcParams["axes.labelweight"] = "bold"

fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Gap")
plt.xlabel(x_label)
axes = plt.gca()
axes.set_ylim([-0.01,0.25])

plt.plot(x, DP_95, label='DP', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, QL_09, label='QL-0.9', color='C5', linestyle='dashed', linewidth=1)
plt.plot(x, QL_05, label='QL-0.5', color='C6', linestyle='dashed', linewidth=1)
plt.plot(x, RL, label='RL', color='C9', linestyle='-.', linewidth=1)

plt.legend(loc='best', handlelength=4)

plt.savefig("gap_"+str(sys.argv[1])+".png")


