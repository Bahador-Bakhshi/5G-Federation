import sys
sys.path.append('../../src/vnfsMapping/')
from NsGenerator import *


if __name__ == '__main__':
    vnfTh = {
        'processing_time': {'min': 2, 'max': 10},
        'requirements': {
            'cpu': {'min': 2, 'max': 10},
            'memory': {'min': 2, 'max': 10},
            'storage': {'min': 2, 'max': 10}
        }
    }

    linkTh = {
        'traffic': {'min': 12, 'max': 30},
        'delay': {'min': 2, 'max': 14}
    }

    ns_gen = NSgenerator(linkTh, vnfTh)
    ns = ns_gen.yieldChain(splits=2, splitWidth=3, branches=5, vnfs=8)

    print ns


    print '======== Testing arrayProbs ========='
    probs = NSgenerator.arrayProbs(5)
    print 'sum(probs) = ' + str(reduce(lambda x, y: x + y, probs))
    print 'probs = ' + str(probs)


    print '\n======== Printing PIMRC18 conversion ==========='
    print ns.toPimrc()



