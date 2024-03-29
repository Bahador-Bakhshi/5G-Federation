import json
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

def plotter(x_label, y_label, x, greedy_000, greedy_050, greedy_100, DP_05, DP_30, DP_60, DP_99, QL_95, QL_55, QL_20, RL, output, no_greedy):

    font = {
            'weight' : 'bold',
            'size'   : 15
        }

    matplotlib.rc('font', **font)
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.labelsize"] = "18"

    fig, ax = plt.subplots()

    plt.grid(linestyle="--", linewidth=0.5)

    if x_label == "Episode":
        plt.xlabel(r'$n$')
    elif x_label == "LC":
        plt.xlabel(r'$\eta_{C^{l}}$')
    elif x_label == "PC":
        plt.xlabel(r'$\eta_{C^{p}}$')
    elif x_label == "FC":
        plt.xlabel(r'$\eta_{\Sigma}$')
    elif x_label == "Omega":
        plt.xlabel(r'$\eta_{\omega}$')
    elif x_label == "Theta":
        plt.xlabel(r'$\eta_{\theta}$')
    elif x_label == "Lambda":
        plt.xlabel(r'$\eta_{\lambda}$')
    else:
        print("Unknow axis X")
        sys.exit(-1)

    print("y_label = ", y_label)
    if y_label == "FR %":
        y_label = "DR %"

    plt.ylabel(y_label)

    plt.plot(x, DP_99, label='PI', color='k', linestyle='solid', linewidth=1.25, marker = '*')

    plt.plot(x, QL_95, label='QL-95', color='b', linestyle='dashed', linewidth=1.25, marker = '^')
    plt.plot(x, QL_55, label='QL-55', color='c', linestyle='dashed', linewidth=1.25, marker = '>')
    plt.plot(x, QL_20, label='QL-20', color='g', linestyle='dashed', linewidth=1.25, marker = 'v')

    plt.plot(x, RL, label='RL', color='r', linestyle='-.', linewidth=1.25, marker = 'D')

    if no_greedy == False:
        plt.plot(x, greedy_100, label='Greedy', color='y', linestyle='dashdot', linewidth=1.25, marker = '+')

    plt.legend(loc='best', handlelength=3, prop={'size': 12})

    x_ticks = [x[i] for i in range(0, len(x) + 1, 2)] #change 2 to 3 for "check_episode"
    ax.set_xticks(x_ticks)

    min_y = math.floor(min(min(DP_99), min(QL_95), min(QL_55), min(QL_20), min(RL), min(greedy_100)))
    max_y = math.ceil(max(max(DP_99), max(QL_95), max(QL_55), max(QL_20), max(RL), max(greedy_100)))
    max_yticks = 6
    step_y = (max_y - min_y) / (max_yticks * 1.0)
    print("float step = ", step_y)

    if step_y < 1:
        min_y = max(0, round(min_y - step_y / 3, 2))
        step_y = max(round(step_y, 2), 0.015)
        y_ticks = [min_y + i * step_y for i in range(max_yticks + 1)]
    else:
        min_y = max(0, int(min_y - step_y / 3))
        step_y = math.ceil(step_y + 0.1)
        y_ticks = [min_y + i * step_y for i in range(max_yticks + 1)]

        print("min = ", min_y)
        print("max = ", max_y)
        print("tick= ", y_ticks)
        print("step= ", step_y)
        #sys.exit(-1)

    ax.set_yticks(y_ticks)

    #plt.savefig(output+".eps", bbox_inches='tight')
    
    plt.savefig(output+".pdf", bbox_inches='tight', format="pdf",transparent=True)
    
    
    
    
    
    
