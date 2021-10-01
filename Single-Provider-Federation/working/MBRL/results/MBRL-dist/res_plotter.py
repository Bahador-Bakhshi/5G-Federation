import json
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import sys

def plotter():
    font = {
            'weight' : 'bold',
            'size'   : 8
        }

    matplotlib.rc('font', **font)
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.labelsize"] = "13"
    matplotlib.rcParams['hatch.linewidth'] = 0.3

    D = [('Poisson', 42.09220511, 48.43800928, 48.18082863, 49.41549366, 58.54997673),
         ('Uniform', 41.82511832, 49.18577047, 49.18173626, 49.65339127, 59.82769006),
         ('Normal', 49.49815857, 49.49815857, 64.23149834, 64.58627939, 68.58670071)
        ] 
    

    dist    = [x[0] for x in D] 
    MFRL    = [x[1] for x in D] 
    MB_BGEX = [x[2] for x in D] 
    MB_DTP  = [x[3] for x in D]     
    MB_Full = [x[4] for x in D]     
    RL_Off  = [x[5] for x in D]     

    ind = np.arange(len(dist))
    width=0.17

    ax = plt.subplot()

    ax.barh(ind + (1 + 0.5) * width, RL_Off, width, align='center', color='tab:red', label='RL-Offline', linewidth = 0.1, edgecolor="white", hatch="///") 
    ax.barh(ind + (0 + 0.5) * width, MB_Full, width, align='center', color='tab:green', label='MB-Full', linewidth = 0.1, edgecolor="white", hatch="+++") 
    ax.barh(ind - (0 + 0.5) * width, MB_DTP, width, align='center', color='c', label='MB-DTP', linewidth = 0.1, edgecolor="white", hatch="xxx") 
    ax.barh(ind - (1 + 0.5) * width, MB_BGEX, width, align='center', color='tab:blue', label='MB-BGEX', linewidth = 0.1, edgecolor="white", hatch="|||") 
    ax.barh(ind - (2 + 0.5) * width, MFRL, width, align='center', color='tab:orange', label='MFRL', linewidth = 0.1, edgecolor="white", hatch="\\\\\\") 


    plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=True) # labels along the left edge are on
    
    ax.set(yticks=ind + (1 + 0.5) * width, yticklabels=dist, ylim=[2*width - 1, len(dist)])
    #ax.set_yticks([])
    ax.set_yticklabels(dist)
    plt.yticks(rotation=90)
    plt.xlabel('Average Profit')
    plt.xticks(fontsize=12)
    
    ax.legend(loc='best', handlelength=1, handletextpad=0.1, ncol=5, prop={'size': 9.5})   
    #ax.legend(handletextpad=0.1)
    
    ax.set_aspect(8.5)
     
    plt.savefig("dist.pdf", bbox_inches='tight', format="pdf",transparent=True)
    
    
    
if __name__ == "__main__":
    plotter()
    
    
