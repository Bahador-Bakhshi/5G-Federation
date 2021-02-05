import time
import sys
import random
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../')))
import MultiDomainConfReader as MDR
import NsBunchConfReader as NSBR
from utils import createRandMultiDomain
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import MultiDomain
from vnfsMapping import NS
from vnfsMapping import NsMapper as NSM

absPath = os.path.abspath(os.path.dirname(__file__))
configPath = '/'.join(absPath.split('/')[:-2]) + '/simulation-configs'



usage = """
Script usage:
    sim.py greedy method [d=n]
    sim.py tabu initial method [d=n] [i=n] [b=n]

    algorithm={greedy, tabu}
    initial={greedy}
    method={Dijkstra, random, BFScutoff, backtrackingCutoff}
    d stands for depth
    i stands for iterations (tabu)
    b stands for blocks (tabu)

    WARNING: if iterations is specified, blockings must be specified
"""

supportedAlgs = ['greedy', 'tabu']
supportedMethods = ['Dijkstra', 'random', 'BFScutoff', 'backtrackingCutoff']


def parseArgs(args):
    """Parse the command line arguments

    :args: command line arguments
    :returns: dictionary with parameters, string with explanaition in case of
        error

    """
    blocks = None
    iters = None
    depth = None
    algorithm = None
    method = None
    initial = None
    methodIdx = 2

    if len(args) != 4 and len(args) != 7:
        return usage
    algorithm = args[1]

    if args[1] not in supportedAlgs:
        return usage
    if args[1] == 'tabu':
        initial = args[2]
        methodIdx = 3
    method = args[methodIdx]

    if method not in supportedMethods:
        return usage

    for i in range(methodIdx + 1, len(args)):
        arg, value = args[i].split('=')
        if arg == 'd':
            depth = int(value)
        elif arg == 'i':
            iters = int(value)
        elif arg == 'b':
            blocks = int(value)
        else:
            return usage

    if (iters == None and blocks != None) or\
            (iters != None and blocks == None):
        return usage

    if (args[2] == 'bfs' or args[2] == 'dfs') and not depth:
        return usage

    if args[1] == 'tabu' and (not iters or not blocks):
        return usage


    return {
        'algorithm': algorithm,
        'initial': initial,
        'method': method,
        'depth': depth,
        'iters': iters,
        'blocks': blocks
    }













if __name__ == '__main__':
    simName = 'tabuPerfection'
    argums = parseArgs(sys.argv)

    if type(argums) == str:
        print argums
        sys.exit()

    if not os.path.exists(configPath + '/tabuPerfection/multiDomain.json'):
        meshLnkRes =  {
            "bw": {
                "min": 9000,
                "max": 9000
            },
            "delay": {
                "min": 1,
                "max": 5
            }
        }
        fatLnkRes =  {
            "bw": {
                "min": 5000,
                "max": 5000
            },
            "delay": {
                "min": 1,
                "max": 5
            }
        }
        servRes =  {
            "memory": {
                "min": 200,
                "max": 200
            },
            "cpu": {
                "min": 200,
                "max": 200
            },
            "disk": {
                "min": 200,
                "max": 200
            }
        }
        pods = {
            'min': 1,
            'max': 4
        }
        domains = 20
        meshProps = [1 for _ in range(domains)]

        createRandMultiDomain(domains, [4], meshLnkRes["bw"],
                meshLnkRes["delay"], fatLnkRes["bw"], fatLnkRes["delay"],
                servRes['memory'], servRes['cpu'], servRes['disk'], 9, pods,
                meshProps, configPath + '/' + simName + '/multiDomain.json')

    # Create the readers
    multiDomainR = MDR.MultiDomainConfReader(simName)
    nsBunchR = NSBR.NsBunchConfReader(simName)
    
    # Obtain multidomain and nsBunch
    md = multiDomainR.readDumped()
    if not md:
        print 'not created yet'
        md = multiDomainR.read()
    nsBunch, entryPoints = nsBunchR.readDumped(multiDomain=md)
    if not nsBunch:
        nsBunch, entryPoints = nsBunchR.read(multiDomain=md)

    mapper = NSM.NsMapper(md)


    print '#req\ttime (sec)\tavg. time (sec)\tmapping'

    # Variables
    fails = 0
    success = 0
    improved = 0
    startTime = time.time()
    i = 0
    aggTime = 0
    windowSize = 10
    window = []
    currAvg = 0

    # Mapping loop
    for ns, entryPoint in zip(nsBunch, entryPoints):
        chainStart = chainEnd = 0
        nsmapping = None

        # Launch mapping
        if argums['algorithm'] == 'greedy':
            chainStart = time.time()
            nsmapping = mapper.greedy(entryPoint['domain'],
                    entryPoint['server'], ns, method=argums['method'],
                    depth=argums['depth'])
            chainEnd = time.time()
        elif argums['algorithm'] == 'tabu':
            chainStart = time.time()
            nsmapping = mapper.tabu(entryPoint['domain'], entryPoint['server'],
                    ns, argums['blocks'], argums['iters'],
                    initial=argums['initial'], method=argums['method'],
                    depth=argums['depth'])
            chainEnd = time.time()

        # Window average
        if len(window) < windowSize:
            window.append(chainEnd - chainStart)
            currAvg = 0
        else:
            window = window[1:] + [chainEnd - chainStart]
            currAvg = reduce(lambda t1, t2: t1 + t2, window) / len(window)

        # Success rate
        if nsmapping != None:
            success += 1
            improved += 1 if nsmapping.hasImproved() else 0
        else:
            fails += 1

        print '%d\t%.3f\t%.3f\t%s' % (i, chainEnd - chainStart, currAvg,
                'OK' if nsmapping != None else 'ERR')
        sys.stdout.flush()
        aggTime += chainEnd - chainStart
        i += 1
    endTime = time.time()
    
    print '\n---- Final results ----'
    print str(len(nsBunch)) + ' NS requests'
    print str(fails) + ' failed requests'
    print str(success) + ' success requests'
    print str(improved) + ' improved requests'
    print '%.3f %s' % (aggTime, 'ellapsed time')

