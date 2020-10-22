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
DP = []
QL_dynamic  = []
QL_static  = []

for data in results:
    x.append(data["x"])
    DP.append(data["DP"])
    QL_dynamic.append(data["QL-Dynamic"])
    QL_static.append(data["QL-Static"])


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Average Profit")
plt.xlabel(x_label)
plt.plot(x, DP, label='DP', color='C4', linestyle='solid', linewidth=1.5)
plt.plot(x, QL_dynamic, label='QL-Dynamic', color='C0', linestyle='dashed', linewidth=1.5)
plt.plot(x, QL_static, label='QL-Static', color='C1', linestyle='dashdot', linewidth=1.5)
plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig("res.png")
