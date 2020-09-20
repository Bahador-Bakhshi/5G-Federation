import sys
import json
sys.path.append('../../src/vnfsMapping/')
from AbsFatTreeGen import *
from NS import *
from NsGenerator import *


if __name__ == '__main__':
    # Host capabilities
    linksProps = {
        'delay': 0.001,
        'capacity': 1000
    }
    serverProps = {
        'capabilities': {
            'storage': 1000,
            'cpu': 16,
            'memory': 128
        }
    }

    # VNF requirements
    vnfTh = {
        'processing_time': {'min': 2, 'max': 10},
        'requirements': {
            'cpu': {'min': 1, 'max': 3},
            'memory': {'min': 2, 'max': 20},
            'storage': {'min': 2, 'max': 100}
        }
    }
    linkTh = {
        'traffic': {'min': 12, 'max': 30},
        'delay': {'min': 2, 'max': 14}
    }


    # Generate a PIMRC18 base scenario
    fat_tree_gen = AbsFatTreeGen()
    NET_fat_tree = fat_tree_gen.yieldFatTree(4, linksProps, serverProps,
        abstraction='NET')
    scenario = AbsFatTreeGen.NETtoPimrc(NET_fat_tree, linksProps, serverProps)

    ns_gen = NSgenerator(linkTh, vnfTh)
    for _ in range(3):
        ns = ns_gen.yieldChain(splits=2, splitWidth=3, branches=5, vnfs=8)
        ns.toPimrc(pimrc=scenario)

    sup_th = {'min': 0.3, 'max': 1}
    cost_th = {'min': 1, 'max': 20}
    scenario = AbsFatTreeGen.PimrcGenCosts(scenario, sup_th, cost_th)

    with open('out/base_pimrc18_scenario.json', 'w') as fp:
        json.dump(scenario, fp, indent=2, sort_keys=True)

