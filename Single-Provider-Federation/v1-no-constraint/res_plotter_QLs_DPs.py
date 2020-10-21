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
DP_05 = []
DP_30 = []
DP_60 = []
DP_95 = []
QL_dynamic  = []
QL_static  = []

for data in results:
    x.append(data["x"])
    DP_05.append(data["DP_05"])
    DP_30.append(data["DP_30"])
    DP_60.append(data["DP_60"])
    DP_95.append(data["DP_95"])
    QL_dynamic.append(data["QL-Dynamic"])
    QL_static.append(data["QL-Static"])


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.plot(x, DP_05, label='DP-0.5', color='C1', linestyle='solid', linewidth=1)
plt.plot(x, DP_30, label='DP-3.0', color='C2', linestyle='solid', linewidth=1)
plt.plot(x, DP_60, label='DP-6.0', color='C3', linestyle='solid', linewidth=1)
plt.plot(x, DP_95, label='DP-9.5', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, QL_dynamic, label='QL-Dynamic', color='C6', linestyle='dashed', linewidth=1)
plt.plot(x, QL_static, label='QL-Static', color='C7', linestyle='dashdot', linewidth=1)

plt.legend(loc='best', handlelength=4)

#plt.show()
plt.savefig(str(sys.argv[1])+".png")
