import csv
import numpy as np
import argparse
import json
import math
from math import log
import random



def gen_arrivals(rate, time_interval):
    """Generate poisson arrivals with lambda=rate inside (0,time_interval)

    :rate: lambda of poisson process
    :time_interval: end of time interval
    :returns: list of arrival times

    """
    arrivals = [0]
    print(rate)
    while arrivals[-1] < time_interval:
        t = np.random.exponential(scale=float(1)/float(rate))
        arrivals += [arrivals[-1] + t]
    if arrivals[-1] > time_interval:
        arrivals = arrivals[:-1]

    arrivals = arrivals[1:]
    return arrivals


if __name__ == '__main__':
    small_arrivals = []
    big_arrivals = []

    
    # Parse args
    parser = argparse.ArgumentParser(description='Generate arrivals of' +\
                                                 'Services')
    parser.add_argument('configFile', type=str,
                        help='path to resources config file')
    parser.add_argument('--outCSV', type=str, default=None,
                        help='CSV path where results are stored')
    args = parser.parse_args()

    # Read config file
    config = None
    with open(args.configFile) as f:
        config = json.load(f)

    small_arrivals = gen_arrivals(config['smallResources']['rate'],
                                  config['daysRunning'])
    big_arrivals = gen_arrivals(config['bigResources']['rate'],
                                config['daysRunning'])

    # assign cpu, mem, disk, and lifetime for each one
    small_cpus, small_mems, small_disks, small_lifes = [], [], [], []
    small_profits = []
    for _ in small_arrivals:
        small_cpus += [math.ceil(abs(np.random.normal(config['smallResources']['cpu_mean'])))]
        small_disks += [math.ceil(abs(np.random.normal(config['smallResources']['disk_mean'])))]
        small_mems += [math.ceil(abs(np.random.normal(config['smallResources']['mem_mean'])))]
        small_lifes += [np.random.uniform(1.0, 4.0)]
        small_profits += [np.random.uniform(3.0, 5.0)]


    big_cpus, big_mems, big_disks, big_lifes, big_profits = [], [], [], [], []
    for _ in big_arrivals:
        big_cpus += [math.ceil(abs(np.random.normal(config['bigResources']['cpu_mean'])))]
        big_disks += [math.ceil(abs(np.random.normal(config['bigResources']['disk_mean'])))]
        big_mems += [math.ceil(abs(np.random.normal(config['bigResources']['mem_mean'])))]
        big_lifes += [np.random.uniform(5.0, 10.0)]
        big_profits += [np.random.uniform(5.0, 10.0)]

    # Write CSV only if asked
    if args.outCSV:
        with open(args.outCSV, mode='w') as f:
            arrival_writer = csv.writer(f, delimiter=',', quotechar='"',
                                         quoting=csv.QUOTE_MINIMAL)

            arrival_writer.writerow(['big', 'small', 'arrival_time', 'cpu', 'mem',
                                     'disk', 'lifetime', 'profit'])
            
            for i in range(len(small_arrivals)):
                arrival_writer.writerow(['0', '1', small_arrivals[i],
                        small_cpus[i], small_mems[i], small_disks[i],
                        small_lifes[i], small_profits[i]])
            for i in range(len(big_arrivals)):
                arrival_writer.writerow(['1', '0', big_arrivals[i], big_cpus[i],
                                big_mems[i], big_disks[i],
                                big_lifes[i], big_profits[i]])


    print("SMALL (last 5)")
    print("\tarrivals: " + str(small_arrivals[-5:]))
    print("\tcpus: " + str(small_cpus[-5:]))
    print("\tdisk: " + str(small_disks[-5:]))

    print("BIG (last 5)")
    print("\tarrivals: " + str(big_arrivals[-5:]))
    print("\tcpus: " + str(big_cpus[-5:]))
    print("\tdisk: " + str(big_disks[-5:]))
