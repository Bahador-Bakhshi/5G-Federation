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
QL  = []

for data in results:
    x.append(data["x"])
    greedy_100.append(data["greedy100"])
    DP_05.append(data["DP_01"])
    DP_30.append(data["DP_30"])
    DP_60.append(data["DP_60"])
    DP_95.append(data["DP_99"])


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.plot(x, DP_05, label='DP-0.01', color='C1', linestyle='solid', linewidth=1)
plt.plot(x, DP_30, label='DP-0.30', color='C2', linestyle='solid', linewidth=1)
plt.plot(x, DP_60, label='DP-0.60', color='C3', linestyle='solid', linewidth=1)
plt.plot(x, DP_95, label='DP-0.99', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, greedy_100, label='Greedy-1.0', color='C8', linestyle='dashdot', linewidth=1)

plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig(str(sys.argv[1])+".png")

