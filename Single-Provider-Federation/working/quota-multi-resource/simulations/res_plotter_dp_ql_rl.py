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
greedy_100 = []
DP_95 = []
QL_09  = []
QL_05  = []
RL  = []

for data in results:
    x.append(data["x"])
    greedy_100.append(data["greedy100"])
    DP_95.append(data["DP_95"])
    QL_09.append(data["QL_09"])
    QL_05.append(data["QL_05"])
    RL.append(data["RL"])


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.xlabel(x_label)
plt.ylabel(y_label)
axes = plt.gca()
axes.set_ylim([45,75])


plt.plot(x, DP_95, label='DP', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, QL_09, label='QL-0.9', color='C5', linestyle='dashed', linewidth=1)
plt.plot(x, QL_05, label='QL-0.5', color='C6', linestyle='dashed', linewidth=1)
plt.plot(x, RL, label='RL', color='C9', linestyle='-.', linewidth=1)

plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig(str(sys.argv[1])+".png")

