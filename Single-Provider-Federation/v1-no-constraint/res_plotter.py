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
greedy = []
DP = []
QL  = []

for data in results:
    x.append(data["x"])
    greedy.append(data["greedy"])
    DP.append(data["DP"])
    QL.append(data["QL"])


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Normalized Profit")
plt.xlabel(x_label)
plt.plot(x, DP, label='DP', color='C3', linestyle='solid', linewidth=1.5)
plt.plot(x, QL, label='QL', color='C0', linestyle='dashed', linewidth=1.5)
plt.plot(x, greedy, label='Greedy', color='C2', linestyle='dashdot', linewidth=1.5)
plt.legend(loc='best', handlelength=4)

plt.show()
plt.savefig("res.png")
