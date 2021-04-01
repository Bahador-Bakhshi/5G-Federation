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
greedy_000 = []
greedy_050 = []
greedy_100 = []
DP_05 = []
DP_30 = []
DP_60 = []
DP_95 = []
QL_09  = []
QL_05  = []
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
    QL_09_tmp = data["QL_09"]
    QL_05_tmp = data["QL_05"]
    RL_tmp = data["RL"]
    
    greedy_000_tmp = gap(DP_95_tmp, greedy_000_tmp)
    greedy_050_tmp = gap(DP_95_tmp, greedy_050_tmp)
    greedy_100_tmp = gap(DP_95_tmp, greedy_100_tmp)
    QL_09_tmp = gap(DP_95_tmp, QL_09_tmp)
    QL_05_tmp = gap(DP_95_tmp, QL_05_tmp)
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
    QL_09.append(QL_09_tmp)
    QL_05.append(QL_05_tmp)
    RL.append(RL_tmp)


font = {
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.labelsize"] = "15"

fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Gap")
if x_label == "episode":
    plt.xlabel(r'$n$')
elif x_label == "LC":
    plt.xlabel(r'$LC$')
elif x_label == "PC":
    plt.xlabel(r'$PC$')
elif x_label == "zeta":
    plt.xlabel(r'$\zeta$')
elif x_label == "l":
    plt.xlabel(r'$\ell$')
else:
    print("Unknow axis X")
    sys.exit(-1)

plt.plot(x, DP_95, label='DP', color='k', linestyle='solid', linewidth=2, marker = '*')

plt.plot(x, QL_09, label='QL-0.9', color='g', linestyle='dashed', linewidth=2, marker = 's')
plt.plot(x, QL_05, label='QL-0.5', color='b', linestyle='dashed', linewidth=2, marker = 'D')
plt.plot(x, RL, label='RL', color='r', linestyle='-.', linewidth=2, marker = 'o')

plt.plot(x, greedy_100, label='Greedy', color='y', linestyle='dashdot', linewidth=2, marker = '+')

plt.legend(loc='best', handlelength=4)

plt.savefig("gap_"+str(sys.argv[1])+".png")


