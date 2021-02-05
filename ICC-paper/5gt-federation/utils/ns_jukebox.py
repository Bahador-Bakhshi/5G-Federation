import sys
import os
import json
import argparse

# Import NsGenerator based on relative path
absPath = os.path.abspath(os.path.dirname(__file__))
srcGen= '/'.join(absPath.split('/')[:-1]) + '/ns_generator/src'
sys.path.append(srcGen)
from vnfsMapping.NsGenerator import NSgenerator


if __name__ == '__main__':
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Generate network service ' +\
            'graphs.')
    parser.add_argument('config', metavar='cfg', type=str,
                        help='path to config file for the generator')
    parser.add_argument('numNSs', type=int,
                        help='number of graphs to generate')
    parser.add_argument('out', type=str,
                        help='path to store the generated graphs')
    args = parser.parse_args()
    

    # Read config file for the generation
    cfg = None
    with open(args.config, 'r') as cfgJson:
        cfg = json.load(cfgJson)
    generator = NSgenerator(cfg['linkTh'], cfg['vnfTh'])

    # Generate the NS graphs
    generated = []
    for i in range(args.numNSs):
        print "Generating " + str(i) + "-th NS for config " + args.config
        ns = generator.yieldChain(
                splits = cfg['splits'],
                splitWidth = cfg['splitWidth'],
                branches = cfg['branches'],
                vnfs = cfg['vnfs'])
        generated.append(ns)
        vlAbs = args.out + '/vls-' + str(i) + '.csv'
        vnfAbs = args.out + '/vnfs-' + str(i) + '.csv'
        ns.writeCSV(vlAbs, vnfAbs)
        print "  VNF CSV at: " + vlAbs
        print "  VL CSV at: " + vnfAbs
        

         


