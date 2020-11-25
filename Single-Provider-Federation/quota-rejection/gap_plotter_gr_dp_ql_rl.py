#!/usr/bin/python3

import json
from numpy import *
import math
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
greedy_000 = []
greedy_050 = []
greedy_100 = []
DP_05 = []
DP_30 = []
DP_60 = []
DP_95 = []
QL  = []
RL  = []

gap = lambda a, b : (a - b) / a
for data in results:
    x.append(data["x"])
    greedy_000_tmp = data["greedy000"]
    greedy_050_tmp = data["greedy050"]
    greedy_100_tmp = data["greedy100"]
    DP_05_tmp = data["DP_05"]
    DP_30_tmp = data["DP_30"]
    DP_60_tmp = data["DP_60"]
    DP_95_tmp = data["DP_95"]
    QL_tmp = data["QL"]
    RL_tmp = data["RL"]
    
    greedy_000_tmp = gap(DP_95_tmp, greedy_000_tmp)
    greedy_050_tmp = gap(DP_95_tmp, greedy_050_tmp)
    greedy_100_tmp = gap(DP_95_tmp, greedy_100_tmp)
    QL_tmp = gap(DP_95_tmp, QL_tmp)
    RL_tmp = gap(DP_95_tmp, RL_tmp)
    DP_05_tmp = gap(DP_95_tmp, DP_05_tmp)
    DP_30_tmp = gap(DP_95_tmp, DP_30_tmp)
    DP_60_tmp = gap(DP_95_tmp, DP_60_tmp)
    DP_95_tmp = gap(DP_95_tmp, DP_95_tmp)

    greedy_000.append(greedy_000_tmp)
    greedy_050.append(greedy_050_tmp)
    greedy_100.append(greedy_100_tmp)
    DP_05.append(DP_05_tmp)
    DP_30.append(DP_30_tmp)
    DP_60.append(DP_60_tmp)
    DP_95.append(DP_95_tmp)
    QL.append(QL_tmp)
    RL.append(RL_tmp)

fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Gap")
plt.xlabel(x_label)

#plt.plot(x, DP_05, label='DP-0.05', color='C1', linestyle='solid', linewidth=1)
#plt.plot(x, DP_30, label='DP-0.30', color='C2', linestyle='solid', linewidth=1)
#plt.plot(x, DP_60, label='DP-0.60', color='C3', linestyle='solid', linewidth=1)
plt.plot(x, DP_95, label='DP', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, QL, label='QL', color='C5', linestyle='dashed', linewidth=1)
plt.plot(x, RL, label='RL', color='C9', linestyle='-.', linewidth=1)

#plt.plot(x, greedy_000, label='Greedy-0.0', color='C6', linestyle='dashdot', linewidth=1)
#plt.plot(x, greedy_050, label='Greedy-0.5', color='C7', linestyle='dashdot', linewidth=1)
plt.plot(x, greedy_100, label='Greedy', color='C8', linestyle='dashdot', linewidth=1)

plt.legend(loc='best', handlelength=4)

plt.savefig("gap_"+str(sys.argv[1])+".png")


