#!/usr/bin/python3

import json
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys
import fig_plotter

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
DP_99 = []
QL_95  = []
QL_55  = []
QL_20  = []
RL  = []

for data in results:
    x.append(data["x"])
    greedy_000.append(data["greedy000"])
    greedy_050.append(data["greedy050"])
    greedy_100.append(data["greedy100"])
    DP_05.append(data["DP_05"])
    DP_30.append(data["DP_30"])
    DP_60.append(data["DP_60"])
    DP_99.append(data["DP_99"])
    QL_95.append(data["QL_95"])
    QL_55.append(data["QL_55"])
    QL_20.append(data["QL_20"])
    RL.append(data["RL"])

fig_plotter.plotter(x_label, y_label, x, greedy_000, greedy_050, greedy_100, DP_05, DP_30, DP_60, DP_99, QL_95, QL_55, QL_20, RL, str(sys.argv[1]))


