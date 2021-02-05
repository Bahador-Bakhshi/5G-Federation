import csv
import numpy as np
import argparse
import json
from environment import Env
import matplotlib as mpl
from matplotlib import pyplot as plt
import math
from simulation import greedy, q_learning


fed_multiplier = 2 # multiplier to increase federation resources
fed_cpu_limit = 100 # limit of CPUs in federated domain
multiplier_alphas = { # alpha parameters based on the multiplier
    4: 1, # 0.34,
    8: 1
}
multiplier_discounts = { # discount parameters based on the multiplier
    4: 0.85, #0.0,
    8: 0.85
}



if __name__ == '__main__':
    small_arrivals = []
    big_arrivals = []
    big_cpus, big_mems, big_disks, big_time, big_lifes = [], [], [], [], []
    small_cpus, small_mems, small_disks, small_time = [], [], [], []
    small_lifes, small_profits, big_profits = [], [], []
        # Parse args
    parser = argparse.ArgumentParser(description='Increase federation' +\
            'resources and runs the Q-learning and greedy decisions')
    parser.add_argument('configFile', type=str,
                        help='path to resources config file')
    parser.add_argument('fedConfigFile', type=str,
                        help='path to federation resources config file')
    parser.add_argument('outJSON', type=str, default=None,
                        help='JSON path where results are stored')
    parser.add_argument('--inCSV', type=str, default=None,
                        help='CSV path where arrivals are')
    args = parser.parse_args()

    #config file for Administrative domain capacity
    domain_config = None
    with open(args.configFile) as f:
        domain_config = json.load(f)
    fed_domain_config = None
    with open(args.fedConfigFile) as f:
        fed_domain_config = json.load(f)


    print(domain_config["cpu"])
    # Write CSV only if asked
    if args.inCSV:
        with open(args.inCSV, mode='r') as f:
            arrival_reader = csv.DictReader(f)
            for row in arrival_reader:
                if float(row["big"]) > float(0):
                    big_cpus += [float(row["cpu"])]
                    big_disks += [float(row["disk"])]
                    big_mems += [float(row["mem"])]
                    big_time += [float(row["arrival_time"])]
                    big_lifes += [float(row['lifetime'])]
                    big_profits += [float(row['profit'])]
                else:
                    small_cpus += [float(row["cpu"])]
                    small_disks += [float(row["disk"])]
                    small_mems += [float(row["mem"])]
                    small_time += [float(row["arrival_time"])]
                    small_lifes += [float(row['lifetime'])]
                    small_profits += [float(row['profit'])]

    print("SMALL (last 5)")
    print("\tarrivals: " + str(small_time[-5:]))
    print("\tcpus: " + str(small_cpus[-5:]))
    print("\tdisk: " + str(small_disks[-5:]))

    # Environment initialization
    simTime = 30  # seconds
    # startSim = True
    # stepTime = 0.005  # seconds

    domain_cpu = int(domain_config["cpu"])
    domain_disk = int(domain_config["disk"])
    domain_memory = int(domain_config["mem"])
    fed_domain_cpu = int(fed_domain_config["cpu"])
    fed_domain_disk = int(fed_domain_config["disk"])
    fed_domain_memory = int(fed_domain_config["mem"])
    

    print("Domain:")
    print("\tcpu: " + str(domain_cpu))
    print("\tmemory: " + str(domain_memory))
    print("\tdisk: " + str(domain_disk))
    print("Federated domain:")
    print("\tcpu: " + str(fed_domain_cpu))
    print("\tmemory: " + str(fed_domain_memory))
    print("\tdisk: " + str(fed_domain_disk))


    episodes= 200
    alpha = 0.35
    discount = 0.0
    env = Env(domain_cpu,domain_memory,domain_disk,fed_domain_cpu,
            fed_domain_memory, fed_domain_disk)
    env.print_status()
    current_time = 0
    alpha = 0.75
    discount = 0.80
    sim_active = True
    i = -1
    j = -1
    print(i,j)
    arrival_cpu = 0
    arrival_mem = 0
    arrival_disk = 0
    arrival_length = 0
    env_capacity = []
    rewards = []
    total_actions_episode = 0
    print(env.get_profit())


    # TODO

    print('### GREEDY SOLUTION without federation ###')
    # Obtain the greedy solution
    env.reset()
    greedy_profit_no_fed = greedy(env, big_cpus, big_disks, big_mems, big_time,
            big_lifes, big_profits, small_cpus, small_disks, small_mems,
            small_time, small_lifes, small_profits, federate=False)

    increase_profits = {}
    multiplier = 1
    last_lap = False
    while fed_domain_cpu <= fed_cpu_limit or last_lap:
        print('##### MULTIPLIER {}'.format(multiplier))
        print('##### FED DOMAIN CPU {}'.format(fed_domain_cpu))
        print('multiplier: {}'.format(multiplier))
        print('alpha={},ds={}'.format(alpha,discount))
        print('federated_resources={}, local resources={}'.format(fed_domain_cpu,domain_cpu))

        # set Q-learning parameters
        if multiplier in multiplier_alphas:
            print('ENTROOOOO')
            alpha = multiplier_alphas[multiplier]
            discount = multiplier_discounts[multiplier]
        else:
            alpha = 0.75
            discount = 0.8
        env = Env(domain_cpu,domain_memory,domain_disk,fed_domain_cpu,
                fed_domain_memory, fed_domain_disk)

        # Obtain the greedy solution with federation
        print('### GREEDY SOLUTION with federation ###')
        env.reset()
        greedy_profit_fed = greedy(env, big_cpus, big_disks, big_mems, big_time,
                big_lifes, big_profits, small_cpus, small_disks, small_mems,
                small_time, small_lifes, small_profits, federate=True)

        # Q-LEARNING
        env.reset()
        episode_reward = q_learning(env, big_cpus, big_disks, big_mems, big_time,
                big_lifes, big_profits, small_cpus, small_disks, small_mems,
                small_time, small_lifes, small_profits, domain_cpu, domain_memory,
                domain_disk, alpha, discount, episodes)

        # Store increase step results
        increase_profits[multiplier] = {
            'greedy_fed': greedy_profit_fed,
            'greedy_no_fed': greedy_profit_no_fed,
            'q-learning': episode_reward[-1]
        }


        multiplier *= fed_multiplier
        fed_domain_cpu = multiplier * domain_cpu
        fed_domain_disk = multiplier * domain_disk
        fed_domain_memory = multiplier * domain_memory

        if last_lap: # quit the loop
            break
        elif fed_domain_cpu > fed_cpu_limit: # infty on last lap
            last_lap = True
            multiplier = math.inf
            fed_domain_cpu = math.inf
            fed_domain_disk = math.inf
            fed_domain_memory = math.inf
            
        # Environment doubles federation resources
        env = Env(domain_cpu,domain_memory,domain_disk,fed_domain_cpu,
                fed_domain_memory, fed_domain_disk)



    # Dump the results to a JSON file
    with open(args.outJSON, 'w') as outfile:
        json.dump(increase_profits, outfile)


    

