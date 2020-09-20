import os
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from simulation import simulator

if __name__ == '__main__':
    #check episode no
    greedy_fed_gamma = []
    greedy_no_fed_gamma = []
    ql_gamma = []
    
    step = 0.1
    i = step
    max_gamma = 1
    while i <= max_gamma:
        tmp_greedy_fed_gamma = 0
        tmp_greedy_no_fed_gamma = 0
        tmp_ql_gamma = 0

        for j in range(10):
            os.system("python3 arrivals.py load_config.json --outCSV test_data.csv")
            greedy_profit_fed, greedy_profit_no_fed, ql_profit = simulator(episodes = 100, alpha = 0.35, discount = i, configFile = "domain_config.json", inCSV = "test_data.csv")

            tmp_greedy_fed_gamma += greedy_profit_fed
            tmp_greedy_no_fed_gamma += greedy_profit_no_fed
            tmp_ql_gamma += ql_profit

        greedy_fed_gamma.append(tmp_greedy_fed_gamma / 10.0)
        greedy_no_fed_gamma.append(tmp_greedy_no_fed_gamma / 10.0)
        ql_gamma.append(tmp_ql_gamma / 10.0)

        i += step

    x = np.arange(step, max_gamma + 1, step)
    print(x)
    print(greedy_fed_gamma)
    print(greedy_no_fed_gamma)
    print(ql_gamma)

    fig, ax = plt.subplots()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.ylabel('Profit vs Episode')
    plt.plot(x, [v for v in greedy_fed_gamma], label='Greedy', color='C2', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in greedy_no_fed_gamma], label='No Fed', color='C3', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in ql_gamma], label='QL', color='C1', linestyle='dashed', linewidth=2)
    plt.legend(loc='best', handlelength=4)
    #plt.show()
    plt.savefig('profit_vs_episode.png')



