import csv
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys


def load_trace(trace_file_name, output):
    exp = []

    PI = []
    RL = []
    Gr = []

    with open(trace_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            elif len(row) > 0:
                exp.append(row[0])

                PI.append(float(row[1])/1000)
                RL.append(float(row[2])/1000)
                Gr.append(float(row[3])/1000)

            line_count += 1
    print("PI = ", PI)
    print("RL = ", RL)
    print("Gr = ", Gr)
    #sys.exit(-1)
    
    font = {
            'weight' : 'bold',
            'size'   : 8
    }

    matplotlib.rc('font', **font)
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["axes.labelsize"] = "10"

    fig, ax = plt.subplots()
    plt.grid(axis="y", linestyle="dotted", linewidth=0.4)

    ax.set_xlabel("Experiments")
    labels = exp.copy()
    ticks = [x for x in range(len(exp))]
    plt.xticks(ticks, labels)

    ax.set_ylabel(r"Total Profit ($10^3$)")
    width = 0.2

    exp_PI = [x - width for x in range(len(exp))]
    exp_RL  = [x for x in range(len(exp))]
    exp_Gr   = [x + width for x in range(len(exp))]
    
    #plt.bar(exp_PI, PI, width, label='PI', color='tab:orange')
    #plt.bar(exp_RL, RL, width, label='RL', color='tab:green')
    #plt.bar(exp_Gr, Gr, width, label='Greedy', color='tab:blue')

    plt.bar(exp_PI, PI, width, label='PI', color='k')
    plt.bar(exp_RL, RL, width, label='RL', color='r')
    plt.bar(exp_Gr, Gr, width, label='Greedy', color='y')
    
    plt.ylim(0, 8.5)
    #ax.tick_params(axis='y')

    #plt.legend(handlelength=1, ncol=2, handleheight=2.4, labelspacing=0.00)
    plt.legend(loc='best', ncol=3, handlelength=3, prop={'size': 7})

    ax.set_aspect(0.5)

    plt.savefig(output+".pdf", bbox_inches='tight', format="pdf",transparent=True)

load_trace("results.csv", "experiment_resutls")


