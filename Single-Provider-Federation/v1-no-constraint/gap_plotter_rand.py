#!/usr/bin/python3

import json
from numpy import *
import math
import matplotlib.pyplot as plt


res_file_handler = open("res.json")
res = json.load(res_file_handler)
res_file_handler.close()

x_label = res["x_label"]
results = res["results"]

x = []
greedy_000 = []
greedy_050 = []
greedy_100 = []
DP = []
QL  = []

for data in results:
    x.append(data["x"])
    greedy_000_tmp = data["greedy000"]
    greedy_050_tmp = data["greedy050"]
    greedy_100_tmp = data["greedy100"]
    DP_tmp = data["DP"]
    QL_tmp = data["QL"]
    
    greedy_000_tmp = (DP_tmp - greedy_000_tmp) / DP_tmp
    greedy_050_tmp = (DP_tmp - greedy_050_tmp) / DP_tmp
    greedy_100_tmp = (DP_tmp - greedy_100_tmp) / DP_tmp
    QL_tmp = (DP_tmp - QL_tmp) / DP_tmp
    DP_tmp = 0.0

    greedy_000.append(greedy_000_tmp)
    greedy_050.append(greedy_050_tmp)
    greedy_100.append(greedy_100_tmp)
    DP.append(DP_tmp)
    QL.append(QL_tmp)


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Gap")
plt.xlabel(x_label)
plt.plot(x, DP, label='DP', color='C4', linestyle='solid', linewidth=1.5)
plt.plot(x, QL, label='QL', color='C0', linestyle='dashed', linewidth=1.5)
plt.plot(x, greedy_000, label='Greedy-0.0', color='C1', linestyle='dashdot', linewidth=1.5)
plt.plot(x, greedy_050, label='Greedy-0.5', color='C2', linestyle='dashdot', linewidth=1.5)
plt.plot(x, greedy_100, label='Greedy-1.0', color='C3', linestyle='dashdot', linewidth=1.5)
plt.legend(loc='best', handlelength=4)

plt.show()
plt.savefig("gap.png")
