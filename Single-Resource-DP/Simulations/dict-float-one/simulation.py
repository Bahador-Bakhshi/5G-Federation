import csv
import numpy as np
import argparse
import json
from environment import Env
import matplotlib as mpl
from matplotlib import pyplot as plt
import math
import os
from collections import defaultdict

FIND_BEST_Q=False # runs all combinations of alpha and discount
FEDERATED=True # federated domain to find best combinations in Q-learning
FEDERATED_MULTIPLIER=50 # federated_res=xFEDERATED_MULTIPLIER*local_res
BEST_FILE='/tmp/alpha-combs-x8.json' # file to store best combs


def greedy(env, big_cpus, big_disks, big_mems, big_time, big_lifes,
        big_profits, small_cpus, small_disks, small_mems, small_time,
        small_lifes, small_profits, federate=True):

    i, j = -1, -1
    current_time = 0
    i = -1
    j = -1
    arrival_cpu = 0
    arrival_mem = 0
    arrival_disk = 0
    arrival_length = 0
    env_capacity = []
    rewards = []
    total_profit = 0
    greedy_actions = {0: 0, 1: 0, 2:0}

    while True:
        if((i+1) >= len(small_time)):
            break

        # GET ARRIVAL INFORMATION
        if((j+1) < len(big_time) and big_time[j+1]<small_time[i+1]):
            j += 1
            current_time = float(big_time[j])
            arrival_cpu = big_cpus[j]
            arrival_mem = big_mems[j]
            arrival_disk = big_disks[j]
            arrival_profit = big_profits[j]
            arrival_length = big_lifes[j]
        else:
            i += 1
            current_time = float(small_time[i])
            arrival_cpu = small_cpus[i]
            arrival_mem = small_mems[i]
            arrival_disk = small_disks[i]
            arrival_profit = small_profits[i]
            arrival_length = small_lifes[i]


        # UPDATE ENVIRONMENT WITH LATEST TIME
        state, tot_profit, num_services = env.update_domain(current_time)

        # Choose greedily best current action
        now_profit = -math.inf
        now_action = None
        for action in [0, 1, 2]:
            action_profit = env.action_profit(action, arrival_cpu, arrival_mem,
                    arrival_disk, arrival_profit, current_time, arrival_length,
                    federate)
            #print('action_profit={}, now_profit={}'.format(action_profit, now_profit))
            if action_profit > now_profit:
                now_action = action
                now_profit = action_profit
        greedy_actions[now_action] += 1

        action = now_action
        #print("time:", current_time)
        #print("action:", action)
        now_cpu, now_memory, now_disk, now_profit = env.instantiate_service(action, arrival_cpu, arrival_mem, arrival_disk, arrival_profit, current_time, arrival_length)
        #updated_state = env.capacity_to_state(now_cpu, now_memory, now_disk)
        updated_state = env.calculate_state()
        total_profit += now_profit
        #print("Profit of step:", now_profit)
        #print("Profit total:", tot_profit)
        #print("Capacity:", str(now_cpu), str(now_memory), str(now_disk), "\n")

    print("Episode: greedy")
    print("Rewards:", tot_profit)
    print("Actions:", greedy_actions)

    return total_profit


def q_learning(env, big_cpus_test, big_disks_test, big_mems_test, big_time_test,
        big_lifes_test, big_profits_test, small_cpus_test, small_disks_test, small_mems_test,
        small_time_test, small_lifes_test, small_profits_test, 
        domain_cpu, domain_memory,  domain_disk, alpha, discount, episodes):
    
    sim_active = True
    i = -1
    j = -1
   
    arrival_cpu = 0
    arrival_mem = 0
    arrival_disk = 0
    arrival_length = 0
    env_capacity = []
    rewards = []
    total_actions_episode = 0
    #print(env.get_profit())
    env.reset()

    #print('\n\n### Q-LEARNING SOLUTION ###')
    #tot_states = env.get_tot_states()
    tot_actions = 3
    tot_profit = 0
    #print("tot_states = ", tot_states)
    #Q = np.zeros(shape=(tot_states, tot_actions), dtype=np.int)
    Q = defaultdict(lambda: np.zeros(tot_actions))

    state = env.calculate_state()
    #print("total_length:",tot_states)
    #print("Q length: ",len(Q))
    #print("Initial State:", str(state))
    #print("Reverse calculate (state):", str(env.state_to_capacity(state)))
    #print("TRIAL CAPACITY TO STATE [4,15,9] =", str(env.capacity_to_state(4,15,9)))
    #print("Reverse calculate (state):", str(env.state_to_capacity(state)))

    episode_reward = []
    actions = []
    num_services = 0

    for episode in range(episodes + 1):
        #print("==========================================")
        test_episod = False;
        if episode == episodes:
            test_episod = True

        env.reset()
        sim_active = True

        #if test_episod:
        big_cpus = big_cpus_test
        big_disks = big_disks_test
        big_mems = big_mems_test
        big_time = big_time_test
        big_lifes = big_lifes_test
        big_profits = big_profits_test
        small_cpus = small_cpus_test
        small_disks = small_disks_test
        small_mems = small_mems_test
        small_time = small_time_test
        small_lifes = small_lifes_test
        small_profits = small_profits_test
        #else:
        #    big_cpus, big_disks, big_mems, big_time, big_lifes, big_profits, small_cpus, small_disks, small_mems, small_time, small_lifes, small_profits = generate_train_data()
 
        while True:
            #print(Q)

            if((i+1) >= len(small_time)):
                episode_reward.append(tot_profit)
                i=-1
                j=-1
                env.reset()
                sim_active = False
                break

            #   GET ARRIVAL INFORMATION
            if((j+1) < len(big_time) and big_time[j+1]<small_time[i+1]):
                j += 1
                current_time = float(big_time[j])
                arrival_cpu = big_cpus[j]
                arrival_mem = big_mems[j]
                arrival_disk = big_disks[j]
                arrival_profit = big_profits[j]
                arrival_length = big_lifes[j]
            else:
                i += 1
                current_time = float(small_time[i])
                arrival_cpu = small_cpus[i]
                arrival_mem = small_mems[i]
                arrival_disk = small_disks[i]
                arrival_profit = small_profits[i]
                arrival_length = small_lifes[i]

            #if test_episod:
            #print("Current demand: cpu = ", arrival_cpu, ", mem = ", arrival_mem, "disk = ", arrival_disk, "profit = ", arrival_profit, "length  = ", arrival_length)

            # UPDATE ENVIRONMENT WITH LATEST TIME
            state, tot_profit, num_services = env.update_domain(current_time)
            #print("current state = ", state)

            if test_episod == True:
                seen = False
                if state in Q:
                   seen = True
                
                #print("seen: ", seen) 
                if seen:
                    action = np.argmax(Q[state])
                else:
                    action = np.argmax(Q[state] + np.random.randn(1, tot_actions))
            else:
                action = np.argmax(Q[state] + np.random.randn(1, tot_actions) * (1 / float(episode + 1)))
                actions.append(action)
            
            #print("time:", current_time)
            #print("action:", action)
            
            now_cpu, now_memory, now_disk, now_profit = env.instantiate_service(action, arrival_cpu, arrival_mem, arrival_disk, arrival_profit, current_time, arrival_length)
            #updated_state = env.capacity_to_state(now_cpu, now_memory, now_disk)
            updated_state = env.calculate_state()
            
            #print("Profit of step:", now_profit)
            #print("Profit total:", tot_profit+now_profit)
            #print("Capacity:", str(now_cpu), str(now_memory), str(now_disk))
            #print("Updated State", str(updated_state), "\n")
            #print("Reverse calculate (state):", str(env.state_to_capacity(updated_state)), "\n")

            #print('state={}, action={}, updated_state={}'.format(state, action, updated_state))
            if test_episod == False:
                Q[state][action] += alpha * (now_profit + discount * np.max(Q[updated_state]) - Q[state][action])
            
            #print('Q[{},{}]={}', state, action, Q[state,action])
            unique, counts = np.unique(actions, return_counts=True)
            total_actions_episode = dict(zip(unique, counts))
            rewards.append(tot_profit)

        if test_episod == True:
            print("****    The TEST episode    ****")
        print("Episode:", episode)
        print("Rewards:", episode_reward[episode-1])
        print("Actions:", total_actions_episode)
        print("Num.Services:", num_services)

    ql_profit = episode_reward[episodes]
    print("Profit:", ql_profit)
    return ql_profit, episode_reward[:episodes - 1]

def generate_train_data():
    big_cpus, big_mems, big_disks, big_time, big_lifes = [], [], [], [], []
    small_cpus, small_mems, small_disks, small_time = [], [], [], []
    small_lifes, small_profits, big_profits = [], [], []
   
    os.system("python3 arrivals.py load_config.json --outCSV train_data.csv")
    with open("train_data.csv", mode='r') as f:
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

 
    return big_cpus, big_disks, big_mems, big_time, big_lifes, big_profits, small_cpus, small_disks, small_mems, small_time, small_lifes, small_profits


def simulator(episodes, alpha, discount, configFile, inCSV):
    small_arrivals = []
    big_arrivals = []
    big_cpus, big_mems, big_disks, big_time, big_lifes = [], [], [], [], []
    small_cpus, small_mems, small_disks, small_time = [], [], [], []
    small_lifes, small_profits, big_profits = [], [], []
    
    #config file for Administrative domain capacity
    domain_config = None
    with open(configFile) as f:
        domain_config = json.load(f)

    # Read demands from inCSV
    if inCSV:
        with open(inCSV, mode='r') as f:
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

    print("BIG (last 5)")
    print("\tarrivals: " + str(big_time[-5:]))
    print("\tcpus: " + str(big_cpus[-5:]))
    print("\tdisk: " + str(big_disks[-5:]))
    
    # Environment initialization
    simTime = 30  # seconds
    # startSim = True
    # stepTime = 0.005  # seconds

    domain_cpu = int(domain_config["cpu"])
    domain_disk = int(domain_config["disk"])
    domain_memory = int(domain_config["mem"])

    print("Domain:")
    print("\tcpu: " + str(domain_cpu))
    print("\tmemory: " + str(domain_memory))
    print("\tdisk: " + str(domain_disk))


    env = Env(domain_cpu,domain_memory,domain_disk)
    env.print_status()
    current_time = 0
    
    # Obtain the greedy solution with federation
    env.reset()
    print('### GREEDY SOLUTION with federation ###')
    greedy_profit_fed = greedy(env, big_cpus, big_disks, big_mems, big_time, big_lifes, big_profits, 
                                    small_cpus, small_disks, small_mems, small_time, small_lifes, small_profits, 
                                federate=True)

    # Obtain the greedy solution
    print('\n### GREEDY SOLUTION without federation ###')
    env.reset()
    greedy_profit_no_fed = greedy(env, big_cpus, big_disks, big_mems, big_time, big_lifes, big_profits, 
                                       small_cpus, small_disks, small_mems, small_time, small_lifes, small_profits, 
                                   federate=False)

    print('\n### QL SOLUTION ###')
    ql_profit, episode_reward = q_learning(env, 
                                    big_cpus, big_disks, big_mems, big_time, big_lifes, big_profits, 
                                    small_cpus, small_disks, small_mems, small_time, small_lifes, small_profits, 
                                domain_cpu, domain_memory, domain_disk, #!!! they are in env, why again?!
                                alpha, discount, episodes)
  

    '''
    # If find best is with a federated setup
    if FEDERATED:
        env = Env(domain_cpu,domain_memory,domain_disk,
                domain_cpu*FEDERATED_MULTIPLIER,
                domain_memory*FEDERATED_MULTIPLIER,
                domain_disk*FEDERATED_MULTIPLIER)

    # Look for the best (alpha,discount) combination
    if FIND_BEST_Q:
        q_experiments = {}
        for alpha_ in range(0, 105, 5):
            for discount_ in range(0, 105, 5):
                alpha = alpha_ / 100
                discount = discount_ / 100
                print('PAIR ({},{})'.format(alpha,discount))
                episode_reward2 = q_learning(env, big_cpus, big_disks, big_mems, big_time,
                        big_lifes, big_profits, small_cpus, small_disks, small_mems,
                        small_time, small_lifes, small_profits, domain_cpu, domain_memory,
                        domain_disk, alpha, discount, episodes)
                q_experiments[(alpha,discount)] = episode_reward2[-1]
        (best_alpha, best_discount) = [(k[0],k[1]) for (k,v) in
                q_experiments.items() if v == max(q_experiments.values())][0]
        print('best setup: alpha={},discount={}'.format(best_alpha, best_discount))
        with open(BEST_FILE, 'w') as outfile:
            dump_dict = {}
            for k in q_experiments.keys():
                dump_dict[str(k)] = q_experiments[k]
            json.dump(dump_dict, outfile)
    '''
    
    '''
    x = np.arange(0, len(episode_reward), 1)
    fig, ax = plt.subplots()
    ax.plot(x, episode_reward)
    plt.show()
    '''

    '''
    opt_profit = 0
    max_profit = max(ql_profit, opt_profit)
    max_profit = max(max_profit, greedy_profit_fed)
    max_profit = max(max_profit, greedy_profit_no_fed)
    max_profit = max(max_profit, opt_profit)
    '''
    '''
    max_profit = greedy_profit_fed

    x = np.arange(0, 2, 1)
    fig, ax = plt.subplots()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.ylabel('normalized test profit')
    plt.plot(x, [ql_profit/max_profit for _ in range(len(x))],
            label='QL Test', color='C2', linestyle='dashdot', linewidth=2)
    plt.plot(x, [greedy_profit_fed/max_profit for _ in range(len(x))],
            label='checker', color='C3', linestyle='dashdot', linewidth=2)
    plt.plot(x, [greedy_profit_no_fed/max_profit for _ in range(len(x))],
            label='no-federate', color='C1', linestyle='dashed', linewidth=2)
    plt.legend(loc='best', handlelength=4)
    plt.show()

    x = np.arange(0, len(episode_reward), 1)
    fig, ax = plt.subplots()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.xlabel('episodes')
    plt.ylabel('rewards')
    plt.plot(x, [er for er in episode_reward], label='QL-Train-Reward',
            color='C0', linewidth=2)
    plt.legend(loc='best', handlelength=4)
    plt.show()
    '''

    return greedy_profit_fed, greedy_profit_no_fed, ql_profit


if __name__ == '__main__':

    # Parse args
    parser = argparse.ArgumentParser(description='Generate arrivals of' + 'Services')
    parser.add_argument('configFile', type=str, help='path to resources config file')
    parser.add_argument('--inCSV', type=str, default=None, help='CSV path where results are stored')
    args = parser.parse_args()

    greedy_profit_fed, greedy_profit_no_fed, ql_profit = simulator(episodes = 10, alpha = 0.5, discount = 0.4, configFile = args.configFile, inCSV = args.inCSV)

    print("Greedy Profit = ", greedy_profit_fed)
    print("Greedy No Fed Profit = ", greedy_profit_no_fed)
    print("QL Profit = ", ql_profit)
