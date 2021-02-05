import os
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from simulation import simulator

if __name__ == '__main__':
    #check episode no
    greedy_fed_eps = []
    greedy_no_fed_eps = []
    ql_eps = []
    
    step = 10
    start = 5
    max_eps = 100
    i = start
    while i <= max_eps:
        tmp_greedy_fed_eps = 0
        tmp_greedy_no_fed_eps = 0
        tmp_ql_eps = 0

        for j in range(10):
            os.system("python3 arrivals.py load_config.json --outCSV test_data.csv")
            greedy_profit_fed, greedy_profit_no_fed, ql_profit = simulator(episodes = i, alpha = 0.65, discount = 0.5, configFile = "domain_config.json", inCSV = "test_data.csv")

            tmp_greedy_fed_eps += greedy_profit_fed
            tmp_greedy_no_fed_eps += greedy_profit_no_fed
            tmp_ql_eps += ql_profit

        greedy_fed_eps.append(tmp_greedy_fed_eps / 10.0)
        greedy_no_fed_eps.append(tmp_greedy_no_fed_eps / 10.0)
        ql_eps.append(tmp_ql_eps / 10.0)

        i += step

    x = np.arange(start, max_eps + 1, step)
    print(x)
    print(greedy_fed_eps)
    print(greedy_no_fed_eps)
    print(ql_eps)

    fig, ax = plt.subplots()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.ylabel('Profit vs Episode')
    plt.plot(x, [v for v in greedy_fed_eps], label='Greedy', color='C2', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in greedy_no_fed_eps], label='No Fed', color='C3', linestyle='dashdot', linewidth=2)
    plt.plot(x, [v for v in ql_eps], label='QL', color='C1', linestyle='dashed', linewidth=2)
    plt.legend(loc='best', handlelength=4)
    #plt.show()
    plt.savefig('profit_vs_episode.png')



