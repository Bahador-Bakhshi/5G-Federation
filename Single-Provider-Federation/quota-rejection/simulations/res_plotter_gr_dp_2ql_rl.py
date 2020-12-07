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


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.xlabel(x_label)
plt.ylabel(y_label)

#plt.plot(x, DP_05, label='DP-0.05', color='C1', linestyle='solid', linewidth=1)
#plt.plot(x, DP_30, label='DP-0.30', color='C2', linestyle='solid', linewidth=1)
#plt.plot(x, DP_60, label='DP-0.60', color='C3', linestyle='solid', linewidth=1)
plt.plot(x, DP_95, label='DP', color='r', linestyle='solid', linewidth=2, marker = '*')

plt.plot(x, QL_09, label='QL-0.9', color='C5', linestyle='dashed', linewidth=1)
plt.plot(x, QL_05, label='QL-0.5', color='C6', linestyle='dashed', linewidth=1)
plt.plot(x, RL, label='RL', color='C9', linestyle='-.', linewidth=1)

#plt.plot(x, greedy_000, label='Greedy-0.0', color='C6', linestyle='dashdot', linewidth=1)
#plt.plot(x, greedy_050, label='Greedy-0.5', color='C7', linestyle='dashdot', linewidth=1)
plt.plot(x, greedy_100, label='Greedy', color='C8', linestyle='dashdot', linewidth=1)

plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig(str(sys.argv[1])+".png")

