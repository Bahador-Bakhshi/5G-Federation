import json
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

def plotter():
    font = {
            'weight' : 'bold',
            'size'   : 15
        }

    matplotlib.rc('font', **font)
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.labelsize"] = "18"

    fig, ax = plt.subplots()

    plt.grid(linestyle="--", linewidth=0.5)

    plt.xlabel('% of learning period')
    plt.ylabel('Average Profit')

    X = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
 
    MFRL    = [32.54769777, 32.34704197, 32.35968621, 34.05037297, 35.27343658, 36.716724, 37.98891066, 39.38006103, 40.74047934, 42.02829461]
    MB_Full = [32.68831797, 32.60475304, 32.35968621, 35.20544098, 37.36696232, 39.87699175, 42.27996921, 44.54401671, 46.93844256, 49.40515261]
    MB_DTP  = [32.52556692, 32.59392947, 32.41813453, 34.70740598, 36.60856674, 38.85594332, 40.8817007, 43.54743094, 45.45189978, 47.82142008]
    MB_BGEX = [32.13649886, 32.5505782, 32.8538967, 34.84099003, 36.97873461, 39.06340425, 41.13747648, 43.92959815, 45.96110205, 48.52424226]
    RL_Offline = [56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134, 56.8322134]
    
    
    plt.plot(X, MFRL, label='MFRL', color='k', linestyle='solid', linewidth=1.25, marker = '*')

    plt.plot(X, MB_BGEX, label='MB-BGEX', color='b', linestyle='dashed', linewidth=1.25, marker = '^')
    plt.plot(X, MB_DTP, label='MB-DTP', color='c', linestyle='dashed', linewidth=1.25, marker = '>')
    plt.plot(X, MB_Full, label='MB-Full', color='g', linestyle='dashed', linewidth=1.25, marker = 'v')

    plt.plot(X, RL_Offline, label='RL-Offline', color='r', linestyle='-.', linewidth=1.25, marker = 'D')

    plt.legend(loc='best', handlelength=3, prop={'size': 12})

    '''
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
    '''
    
    #plt.savefig(output+".eps", bbox_inches='tight')
    
    plt.savefig("stop_learning.pdf", bbox_inches='tight', format="pdf",transparent=True)
    
    
    
if __name__ == "__main__":
    plotter()
    
    
