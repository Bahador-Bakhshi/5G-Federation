import argparse
import json
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the profit as ' +\
            'federation resources increase')
    parser.add_argument('increaseJSON', type=str,
                        help='path to JSON with resources increase')
    args = parser.parse_args()

    
    profits = None
    with open(args.increaseJSON) as json_file:
        profits = json.load(json_file)


    # Store the bar values
    print(profits.keys())
    multipliers = list(profits.keys())
    # Filter out x4 and x8 because Q-learning was not properly trained
    multipliers = list(filter(lambda k: k not in ['8','4'],profits.keys()))
    multipliers.sort()
    greedy_no_fed, greedy_fed, q_learning = [], [], []
    for m in multipliers:
        greedy_no_fed += [profits[m]['greedy_no_fed'] / 353.1591274]
        greedy_fed += [profits[m]['greedy_fed'] / 353.1591274]
        q_learning += [profits[m]['q-learning'] / 353.1591274]

    # Plot
    fig, ax = plt.subplots()
    ind = np.arange(len(multipliers))
    width = 0.3         # the width of the bars

    patterns=['/','_','\\']
    p1 = ax.bar(ind, greedy_no_fed, width, bottom=0,
            color='C1',alpha=0.8, hatch=patterns.pop(0))
    p2 = ax.bar(ind + width, greedy_fed, width, bottom=0,
            color='C3', alpha=0.8, hatch=patterns.pop(0))
    p3 = ax.bar(ind + 2*width, q_learning, width, bottom=0,
            color='C0', alpha=0.8, hatch=patterns.pop(0))
    ax.grid(linestyle='--', linewidth=0.5)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(['x{}'.format(m) for m in (multipliers[:-1] +
        ['$\\infty$'])])
    ax.legend((p1[0], p2[0], p3[0]), ('no-federate', 'checker', 'Q-learning'),
            loc='best')
    ax.autoscale_view()
    plt.ylabel('$\\frac{r}{r_{OPT}}$', size=16)
    plt.xlabel('xN local resources', size=10)
    plt.ylim(0.5, 1)

    plt.show()


