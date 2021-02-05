import os
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from simulation import simulator

if __name__ == '__main__':
    #check episode no
    greedy_fed_alpha = []
    greedy_no_fed_alpha = []
    ql_alpha = []
    
    step = .1
    i = step
    max_alpha = 1
    while i <= max_alpha:
        tmp_greedy_fed_alpha = 0
        tmp_greedy_no_fed_alpha = 0
        tmp_ql_alpha = 0

        for j in range(10):
            os.system("python3 arrivals.py load_config.json --outCSV test_data.csv")
            greedy_profit_fed, greedy_profit_no_fed, ql_profit = simulator(episodes = 100, alpha = i, discount = 0.75, configFile = "domain_config.json", inCSV = "test_data.csv")

            tmp_greedy_fed_alpha += greedy_profit_fed
            tmp_greedy_no_fed_alpha += greedy_profit_no_fed
            tmp_ql_alpha += ql_profit

        greedy_fed_alpha.append(tmp_greedy_fed_alpha / 10.0)
        greedy_no_fed_alpha.append(tmp_greedy_no_fed_alpha / 10.0)
        ql_alpha.append(tmp_ql_alpha / 10.0)

        i += step

    x = np.arange(step, max_alpha + 1, step)
    print(x)
    print(greedy_fed_alpha)
    print(greedy_no_fed_alpha)
    print(ql_alpha)

    fig, ax = plt.subplots()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.ylabel('Profit vs Episode')
    plt.plot(x, [v for v in greedy_fed_alpha], label='Greedy', color='C2', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in greedy_no_fed_alpha], label='No Fed', color='C3', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in ql_alpha], label='QL', color='C1', linestyle='dashed', linewidth=2)
    plt.legend(loc='best', handlelength=4)
    #plt.show()
    plt.savefig('profit_vs_episode.png')



