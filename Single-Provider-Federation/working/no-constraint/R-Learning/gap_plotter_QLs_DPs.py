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
results = res["results"]

x = []
DP_05 = []
DP_30 = []
DP_60 = []
DP_95 = []
QL_static  = []
QL_dynamic  = []

gap = lambda a, b : (a - b) / a

for data in results:
    x.append(data["x"])
    DP_05_tmp = data["DP_05"]
    DP_30_tmp = data["DP_30"]
    DP_60_tmp = data["DP_60"]
    DP_95_tmp = data["DP_95"]
    QL_dynamic_tmp = data["QL-Dynamic"]
    QL_static_tmp  = data["QL-Static"]
    
    QL_dynamic_tmp = gap(DP_95_tmp, QL_dynamic_tmp)
    QL_static_tmp = gap(DP_95_tmp, QL_static_tmp)
    DP_05_tmp = gap(DP_95_tmp, DP_05_tmp)
    DP_30_tmp = gap(DP_95_tmp, DP_30_tmp)
    DP_60_tmp = gap(DP_95_tmp, DP_60_tmp)
    DP_95_tmp = gap(DP_95_tmp, DP_95_tmp)

    DP_05.append(DP_05_tmp)
    DP_30.append(DP_30_tmp)
    DP_60.append(DP_60_tmp)
    DP_95.append(DP_95_tmp)
    QL_dynamic.append(QL_dynamic_tmp)
    QL_static.append(QL_static_tmp)


fig, ax = plt.subplots()
plt.grid(linestyle="--", linewidth=0.5)
plt.ylabel("Gap")
plt.xlabel(x_label)

plt.plot(x, DP_05, label='DP-0.05', color='C1', linestyle='solid', linewidth=1)
plt.plot(x, DP_30, label='DP-0.30', color='C2', linestyle='solid', linewidth=1)
plt.plot(x, DP_60, label='DP-0.60', color='C3', linestyle='solid', linewidth=1)
plt.plot(x, DP_95, label='DP-0.95', color='C4', linestyle='solid', linewidth=1)

plt.plot(x, QL_dynamic, label='QL-Dynamic', color='C6', linestyle='dashed', linewidth=1)
plt.plot(x, QL_static, label='QL-Static', color='C7', linestyle='dashdot', linewidth=1)

plt.legend(loc='best', handlelength=4)

plt.savefig("gap_"+str(sys.argv[1])+".png")


