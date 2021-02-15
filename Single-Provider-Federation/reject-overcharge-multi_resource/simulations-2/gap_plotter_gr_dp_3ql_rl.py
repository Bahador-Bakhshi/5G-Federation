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
DP_99 = []
QL_95  = []
QL_55  = []
QL_20  = []
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
    DP_99_tmp = data["DP_99"]
    QL_95_tmp = data["QL_95"]
    QL_55_tmp = data["QL_55"]
    QL_20_tmp = data["QL_20"]
    RL_tmp = data["RL"]
    
    greedy_000_tmp = gap(DP_99_tmp, greedy_000_tmp)
    greedy_050_tmp = gap(DP_99_tmp, greedy_050_tmp)
    greedy_100_tmp = gap(DP_99_tmp, greedy_100_tmp)
    QL_95_tmp = gap(DP_99_tmp, QL_95_tmp)
    QL_55_tmp = gap(DP_99_tmp, QL_55_tmp)
    QL_20_tmp = gap(DP_99_tmp, QL_20_tmp)
    RL_tmp = gap(DP_99_tmp, RL_tmp)
    DP_05_tmp = gap(DP_99_tmp, DP_05_tmp)
    DP_30_tmp = gap(DP_99_tmp, DP_30_tmp)
    DP_60_tmp = gap(DP_99_tmp, DP_60_tmp)
    DP_99_tmp = gap(DP_99_tmp, DP_99_tmp)

    greedy_000.append(greedy_000_tmp)
    greedy_050.append(greedy_050_tmp)
    greedy_100.append(greedy_100_tmp)
    DP_05.append(DP_05_tmp)
    DP_30.append(DP_30_tmp)
    DP_60.append(DP_60_tmp)
    DP_99.append(DP_99_tmp)
    QL_95.append(QL_95_tmp)
    QL_55.append(QL_55_tmp)
    QL_20.append(QL_20_tmp)
    RL.append(RL_tmp)


font = {
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
plt.rcParams["axes.labelweight"] = "bold"

fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)

if x_label == "episode":
    plt.xlabel(r'$n$')
elif x_label == "LC":
    plt.xlabel(r'$\eta_{C^{l}}$')
elif x_label == "PC":
    plt.xlabel(r'$\eta_{C^{p}}$')
elif x_label == "FC":
    plt.xlabel(r'$\eta_{\Sigma}$')
elif x_label == "Omega":
    plt.xlabel(r'$\eta_{\omega}$')
elif x_label == "Theta":
    plt.xlabel(r'$\eta_{\theta}$')
elif x_label == "Lambda":
    plt.xlabel(r'$\eta_{\lambda}$')
else:
    print("Unknow axis X")
    sys.exit(-1)

plt.ylabel("Gap")


plt.plot(x, DP_99, label='DP', color='k', linestyle='solid', linewidth=2, marker = '*')

plt.plot(x, QL_95, label='QL-0.95', color='c', linestyle='dashed', linewidth=2, marker = '^')
plt.plot(x, QL_55, label='QL-0.55', color='m', linestyle='dashed', linewidth=2, marker = '>')
plt.plot(x, QL_20, label='QL-0.20', color='y', linestyle='dashed', linewidth=2, marker = 'v')

plt.plot(x, RL, label='RL', color='r', linestyle='-.', linewidth=2, marker = 'D')

plt.plot(x, greedy_100, label='Greedy', color='g', linestyle='dashdot', linewidth=2, marker = '+')

plt.legend(loc='best', handlelength=4)


plt.savefig("gap_"+str(sys.argv[1])+".png")


