#!/usr/bin/python3

import json
from numpy import *
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

gap = lambda a, b : (a - b) / a
for data in results:
    x.append(data["x"])
    greedy_000_tmp = data["greedy000"]
    greedy_050_tmp = data["greedy050"]
    greedy_100_tmp = data["greedy100"]
    DP_05_tmp = data["DP_05"]
    DP_30_tmp = data["DP_30"]
    DP_60_tmp = data["DP_60"]
    DP_99_tmp = data["DP_99"]
    QL_95_tmp = data["QL_95"]
    QL_55_tmp = data["QL_55"]
    QL_20_tmp = data["QL_20"]
    RL_tmp = data["RL"]
    
    greedy_000_tmp = gap(DP_99_tmp, greedy_000_tmp)
    greedy_050_tmp = gap(DP_99_tmp, greedy_050_tmp)
    greedy_100_tmp = gap(DP_99_tmp, greedy_100_tmp)
    QL_95_tmp = gap(DP_99_tmp, QL_95_tmp)
    QL_55_tmp = gap(DP_99_tmp, QL_55_tmp)
    QL_20_tmp = gap(DP_99_tmp, QL_20_tmp)
    RL_tmp = gap(DP_99_tmp, RL_tmp)
    DP_05_tmp = gap(DP_99_tmp, DP_05_tmp)
    DP_30_tmp = gap(DP_99_tmp, DP_30_tmp)
    DP_60_tmp = gap(DP_99_tmp, DP_60_tmp)
    DP_99_tmp = gap(DP_99_tmp, DP_99_tmp)

    greedy_000.append(greedy_000_tmp)
    greedy_050.append(greedy_050_tmp)
    greedy_100.append(greedy_100_tmp)
    DP_05.append(DP_05_tmp)
    DP_30.append(DP_30_tmp)
    DP_60.append(DP_60_tmp)
    DP_99.append(DP_99_tmp)
    QL_95.append(QL_95_tmp)
    QL_55.append(QL_55_tmp)
    QL_20.append(QL_20_tmp)
    RL.append(RL_tmp)

fig_plotter.plotter(x_label, "Gap", x, greedy_000, greedy_050, greedy_100, DP_05, DP_30, DP_60, DP_99, QL_95, QL_55, QL_20, RL, "gap")

