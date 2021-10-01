import json
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

def plotter():
    font = {
            'weight' : 'bold',
            'size'   : 12
        }

    matplotlib.rc('font', **font)
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.labelsize"] = "15"

    fig, ax = plt.subplots()

    plt.grid(linestyle="--", linewidth=0.5)

    plt.xlabel('# of variable service types')
    plt.ylabel('Average Profit')

    X = [0, 1, 2, 3]
 
    MFRL    = [37.10400639, 39.95489138, 41.5367551, 45.2879642]
   
    MB_BGEX = [43.63102333, 46.92739621, 48.95666589, 52.39837265]
    MB_DTP  = [50.00439925, 52.1621353, 57.05615117, 64.18598042]
    MB_Full = [50.00002159, 53.45814054, 57.96062222, 65.03075777]

    RL_Offline = [55.51622754, 58.3429547, 61.93517684, 69.2524923]
    
    plt.plot(X, RL_Offline, label='RL-Offline', color='tab:red', linestyle='-.', linewidth=1.25, marker = 'D')
    
    plt.plot(X, MB_Full, label='MB-Full', color='tab:green', linestyle='dashed', linewidth=1.25, marker = 'v')
    plt.plot(X, MB_DTP, label='MB-DTP', color='c', linestyle='dashed', linewidth=1.25, marker = '>')
    plt.plot(X, MB_BGEX, label='MB-BGEX', color='tab:blue', linestyle='dashed', linewidth=1.25, marker = '^')

    plt.plot(X, MFRL, label='MFRL', color='tab:orange', linestyle='solid', linewidth=1.25, marker = '*')

    plt.legend(loc='best', ncol=3, handlelength=2, prop={'size': 10})
    
    x_ticks = X
    ax.set_xticks(x_ticks)
    
    ax.set_ylim(35,75)
    ax.set_aspect(0.037)



    plt.savefig("var_traffic.pdf", bbox_inches='tight', format="pdf",transparent=True)
    
    
    
if __name__ == "__main__":
    plotter()
    
    
