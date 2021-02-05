import sys
import json
sys.path.append('../../src/vnfsMapping/')
from AbsFatTreeGen import *


if __name__ == '__main__':
    linksProps = {
        'delay': 0.001,
        'capacity': 1000
    }
    serverProps = {
        'capabilities': {
            'cpu': 1000,
            'storage': 16,
            'memory': 128
        }
    }

    fat_tree_gen = AbsFatTreeGen()
    NET_fat_tree = fat_tree_gen.yieldFatTree(4, linksProps, serverProps,
        abstraction='NET')
    nx.write_gml(NET_fat_tree, "out/test_NET_fat_tree_k4.gml")
    scenario = AbsFatTreeGen.NETtoPimrc(NET_fat_tree, linksProps, serverProps)
    with open('out/test_NET_fat_tree_k4.json', 'w') as fp:
        json.dump(scenario, fp)

    print '==== Testing PIMRC18 conversion ===='
    print scenario

