#!/usr/bin/python3

from amplpy import AMPL, DataFrame
import argparse
import csv
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Given arrivals CSV, ' + \
                                                 'it creates an AMPL .dat file')

    parser.add_argument('model', metavar='model', type=str,
                        help='Path to the AMPL model')
    parser.add_argument('arrivals', metavar='arrivals', type=str,
                        help='Path to the arrivals CSV file')
    parser.add_argument('out', metavar='out', type=str,
                        help='Path to the output where .dat is created')
    args = parser.parse_args()


    # Create the AMPL object
    ampl = AMPL()
    ampl.read(args.model)

    # Read the arrivals
    asked_cpu, asked_mem, asked_disk, asked_lifes = [], [], [], []
    times, profit_federate, profit_local, profit_reject = [], [], [], []
    leaves_cpu, leaves_mem, leaves_disk, leaves_time = [], [], [], []
    leaves_arrival = []
    with open(args.arrivals, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            times += [float(row[2])]
            asked_cpu += [float(row[3])]
            asked_mem += [float(row[4])]
            asked_disk += [float(row[5])]
            asked_lifes += [float(row[6])]
            profit_federate += [1]
            profit_local += [float(row[7])]
            profit_reject += [-float(row[7])]

            # Include the leaving
            leaves_time += [times[-1] + asked_lifes[-1]]
            leaves_arrival += [times[-1]]
            leaves_cpu += [asked_cpu[-1]]
            leaves_mem += [asked_mem[-1]]
            leaves_disk += [asked_disk[-1]]


    # create the events dictionary
    events = {}
    for i in range(len(times)):
        events[times[i]] = {
            'profit_federate': profit_federate[i],
            'profit_local': profit_local[i],
            'profit_reject': profit_reject[i],
            'asked_cpu': asked_cpu[i],
            'asked_mem': asked_mem[i],
            'asked_disk': asked_disk[i],
            'frees_mem': 0,
            'frees_cpu': 0,
            'frees_disk': 0,
            'frees_arrival': leaves_arrival[0]
        }
    for i in range(len(leaves_time)):
        events[leaves_time[i]] = {
            'profit_federate': 0,
            'profit_local': 0,
            'profit_reject': 0,
            'asked_cpu': 0,
            'asked_mem': 0,
            'asked_disk': 0,
            'frees_mem': leaves_mem[i],
            'frees_cpu': leaves_cpu[i],
            'frees_disk': leaves_disk[i],
            'frees_arrival': leaves_arrival[i]
        }

    # Set the ordered timestamps
    timestamps = times + leaves_time
    timestamps.sort()
    ampl.set['timestamps'] = timestamps

    # Set profits
    df = DataFrame(('timestamps'), 'profit_federate')
    df.setValues({t: events[t]['profit_federate'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'profit_local')
    df.setValues({t: events[t]['profit_local'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'profit_reject')
    df.setValues({t: events[t]['profit_reject'] for t in events.keys()})
    ampl.setData(df)

    # Set asked resources
    df = DataFrame(('timestamps'), 'asked_cpu')
    df.setValues({t: events[t]['asked_cpu'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'asked_mem')
    df.setValues({t: events[t]['asked_mem'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'asked_disk')
    df.setValues({t: events[t]['asked_disk'] for t in events.keys()})
    ampl.setData(df)

    # Set leavings
    df = DataFrame(('timestamps'), 'frees_cpu')
    df.setValues({t: events[t]['frees_cpu'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'frees_mem')
    df.setValues({t: events[t]['frees_mem'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'frees_disk')
    df.setValues({t: events[t]['frees_disk'] for t in events.keys()})
    ampl.setData(df)
    df = DataFrame(('timestamps'), 'frees_arrival')
    df.setValues({t: events[t]['frees_arrival'] for t in events.keys()})
    ampl.setData(df)
    ampl.exportData(datfile=args.out)

