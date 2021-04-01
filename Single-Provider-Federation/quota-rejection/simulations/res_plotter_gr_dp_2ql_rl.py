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
y_label = res["y_label"]
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

for data in results:
    x.append(data["x"])
    greedy_000.append(data["greedy000"])
    greedy_050.append(data["greedy050"])
    greedy_100.append(data["greedy100"])
    DP_05.append(data["DP_05"])
    DP_30.append(data["DP_30"])
    DP_60.append(data["DP_60"])
    DP_95.append(data["DP_95"])
    QL_09.append(data["QL_09"])
    QL_05.append(data["QL_05"])
    RL.append(data["RL"])


font = {
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.labelsize"] = "15"

fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)

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

plt.ylabel(y_label)

plt.plot(x, DP_95, label='DP', color='k', linestyle='solid', linewidth=2, marker = '*')

plt.plot(x, QL_09, label='QL-0.9', color='g', linestyle='dashed', linewidth=2, marker = 's')
plt.plot(x, QL_05, label='QL-0.5', color='b', linestyle='dashed', linewidth=2, marker = 'D')
plt.plot(x, RL, label='RL', color='r', linestyle='-.', linewidth=2, marker = 'o')

plt.plot(x, greedy_100, label='Greedy', color='y', linestyle='dashdot', linewidth=2, marker = '+')

plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig(str(sys.argv[1])+".png")

