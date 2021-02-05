import sys
import os
import random
import networkx as nx

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import MultiDomain as MD
from vnfsMapping import NS
from vnfsMapping import NsMapper as NSM
from vnfsMapping import NsMapping as NSm
from vnfsMapping import NsGenerator as NSG


class NsMapperTester(object):

    """Class for testing the NsMapper"""

    def __init__(self):
        """TODO: to be defined1. """
        

    def __genMultiDomain(self):
        """Generates a multi domain view based on the graph showed for
        Dijkstra in wikipedia

        :returns: MultiDomain instance with a single domain view

        """
        graph = nx.Graph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4, res={'memory': 2, 'disk': 50, 'cpu': 4},\
			 fatType='server')
        graph.add_node(5, res={'memory': 2, 'disk': 50, 'cpu': 4},\
			 fatType='server')
        graph.add_node(6)
        graph.add_edge(1, 2, res={'bw': 300, 'delay': 7})
        graph.add_edge(1, 3, res={'bw': 300, 'delay': 9})
        graph.add_edge(1, 6, res={'bw': 100, 'delay': 14})
        graph.add_edge(2, 3, res={'bw': 100, 'delay': 10})
        graph.add_edge(2, 4, res={'bw': 200, 'delay': 15})
        graph.add_edge(3, 6, res={'bw': 300, 'delay': 2})
        graph.add_edge(3, 4, res={'bw': 200, 'delay': 11})
        graph.add_edge(4, 5, res={'bw': 250, 'delay': 6})
        graph.add_edge(5, 6, res={'bw': 250, 'delay': 9})

        multiDomain = MD.MultiDomain()
        multiDomain._MultiDomain__domains = 1
        multiDomain._MultiDomain__globalView = graph
        multiDomain._MultiDomain__domainsViews = [graph.copy()]

        return multiDomain
   

    def __genSquareMultiDomain(self):
        """Generates a square multi domain to test mapping algorithms under
        vnfs that are join points.
        :returns: MultiDomain instance

        """
        graph = nx.Graph()
        graph.add_node(1, res={'memory': 2, 'disk': 51, 'cpu': 4},\
			 fatType='server')
        graph.add_node(2, res={'memory': 2, 'disk': 52, 'cpu': 3},\
			 fatType='server')
        graph.add_node(3, res={'memory': 2, 'disk': 53, 'cpu': 2},\
			 fatType='server')
        graph.add_node(4, res={'memory': 2, 'disk': 54, 'cpu': 1},\
			 fatType='server')
        graph.add_node(6)
        graph.add_edge(1, 2, res={'bw': 300, 'delay': 1})
        graph.add_edge(1, 3, res={'bw': 300, 'delay': 1})
        graph.add_edge(3, 4, res={'bw': 300, 'delay': 1})
        graph.add_edge(2, 4, res={'bw': 300, 'delay': 1})

        multiDomain = MD.MultiDomain()
        multiDomain._MultiDomain__domains = 1
        multiDomain._MultiDomain__globalView = graph
        multiDomain._MultiDomain__domainsViews = [graph.copy()]

        return multiDomain


    def __genTabuMultiDomain(self):
        """Generates a MultiDomain instance on top ow which tabu search is
        tested.
        :returns: MultiDomain instance

        """
        graph = nx.Graph()

        # Base three down
        graph.add_node(1, res={'memory': 0, 'disk': 0, 'cpu': 4},\
			 fatType='server')
        graph.add_node(2, res={'memory': 10, 'disk': 0, 'cpu': 0},\
			 fatType='server')
        graph.add_node(3, res={'memory': 0, 'disk': 100, 'cpu': 0},\
			 fatType='server')

        # Top three left
        graph.add_node(4, res={'memory': 1, 'disk': 0, 'cpu': 1},\
			 fatType='server')
        graph.add_node(5, res={'memory': 1, 'disk': 1, 'cpu': 0},\
			 fatType='server')
        graph.add_node(6, res={'memory': 0, 'disk': 1, 'cpu': 1},\
			 fatType='server')

        # Top three middle
        graph.add_node(7, res={'memory': 1, 'disk': 0, 'cpu': 1},\
			 fatType='server')
        graph.add_node(8, res={'memory': 1, 'disk': 1, 'cpu': 0},\
			 fatType='server')
        graph.add_node(9, res={'memory': 0, 'disk': 1, 'cpu': 1},\
			 fatType='server')

        # Top three right
        graph.add_node(10, res={'memory': 1, 'disk': 0, 'cpu': 1},\
			 fatType='server')
        graph.add_node(11, res={'memory': 1, 'disk': 1, 'cpu': 0},\
			 fatType='server')
        graph.add_node(12, res={'memory': 0, 'disk': 1, 'cpu': 1},\
			 fatType='server')

        # Switch nodes
        graph.add_node(20)
        graph.add_node(21)
        graph.add_node(23)
        graph.add_node(24)
        graph.add_node(25)
        graph.add_node(26)
        graph.add_node(27)
        graph.add_node(28)
        graph.add_node(30)
        graph.add_node(31)
        graph.add_node(32)
        graph.add_node(33)
        graph.add_node(34)
        graph.add_node(35)

        # Links between nodes
        # Down links
        graph.add_edge(1, 20, res={'bw': 300, 'delay': 1})
        graph.add_edge(1, 21, res={'bw': 300, 'delay': 1})
        graph.add_edge(21, 3, res={'bw': 300, 'delay': 1})
        graph.add_edge(20, 2, res={'bw': 300, 'delay': 1})

        # Links between 3 and others
        graph.add_edge(3, 23, res={'bw': 300, 'delay': 15})
        graph.add_edge(3, 25, res={'bw': 300, 'delay': 20})
        graph.add_edge(3, 27, res={'bw': 300, 'delay': 30})
        graph.add_edge(23, 4, res={'bw': 300, 'delay': 15})
        graph.add_edge(25, 7, res={'bw': 300, 'delay': 20})
        graph.add_edge(27, 10, res={'bw': 300, 'delay': 30})

        # Links between 2 and others
        graph.add_edge(2, 24, res={'bw': 300, 'delay': 15})
        graph.add_edge(2, 26, res={'bw': 300, 'delay': 20})
        graph.add_edge(2, 28, res={'bw': 300, 'delay': 30})
        graph.add_edge(24, 4, res={'bw': 300, 'delay': 15}) 
        graph.add_edge(26, 7, res={'bw': 300, 'delay': 20})
        graph.add_edge(28, 10, res={'bw': 300, 'delay': 30})

        # Links between top left
        graph.add_edge(4, 30, res={'bw': 300, 'delay': 45})
        graph.add_edge(4, 31, res={'bw': 300, 'delay': 45})
        graph.add_edge(30, 5, res={'bw': 300, 'delay': 45})
        graph.add_edge(31, 6, res={'bw': 300, 'delay': 45})

        # Links between top middle
        graph.add_edge(7, 32, res={'bw': 300, 'delay': 30})
        graph.add_edge(7, 33, res={'bw': 300, 'delay': 30})
        graph.add_edge(32, 8, res={'bw': 300, 'delay': 30})
        graph.add_edge(33, 9, res={'bw': 300, 'delay': 30})

        # Links between top right
        graph.add_edge(10, 34, res={'bw': 300, 'delay': 1})
        graph.add_edge(10, 35, res={'bw': 300, 'delay': 1})
        graph.add_edge(34, 11, res={'bw': 300, 'delay': 1})
        graph.add_edge(35, 12, res={'bw': 300, 'delay': 1})


        multiDomain = MD.MultiDomain()
        multiDomain._MultiDomain__domains = 1
        multiDomain._MultiDomain__globalView = graph
        multiDomain._MultiDomain__domainsViews = [graph.copy()]

        return multiDomain


    def __genTabuNS(self):
        """Generates the NS chain used to test the tabu search
        :returns: NS instance

        """
        chain = nx.Graph()
        chain.add_node('start', memory=2, disk=3, cpu=4)
        chain.add_node(1, memory=0, disk=0, cpu=4)
        chain.add_node(2, memory=10, disk=0, cpu=0)
        chain.add_node(3, memory=0, disk=100, cpu=0)
        chain.add_node(4, memory=1, disk=0, cpu=1)
        chain.add_node(5, memory=0, disk=1, cpu=1)
        chain.add_node(6, memory=1, disk=1, cpu=0)

        chain.add_edge('start', 1, bw=0, delay=0)
        chain.add_edge(1, 2, bw=0, delay=3)
        chain.add_edge(1, 3, bw=0, delay=3)
        chain.add_edge(2, 4, bw=0, delay=70)
        chain.add_edge(3, 4, bw=0, delay=70)
        chain.add_edge(4, 5, bw=0, delay=200)
        chain.add_edge(4, 6, bw=0, delay=200)

        ns = NS.NS()
        ns.setChain(chain)
        ns.setSplitsNum(2)
        ns.setBranchNum(2)
        ns.setMaxSplitW(2)
        ns.setBranchHeads([5, 6])

        return ns


    def testConstrainedDijkstra(self):
        """Tests the constrained Dijkstra method
        :returns: Nothing

        """
        md = self.__genMultiDomain()
        mapper = NSM.NsMapper(md)
        err = False

        print '#########################'
        print '## constrainedDijkstra ##'
        print '#########################'

        path, delay = mapper.constrainedDijkstra(0, 1, [4, 5], delay=50,
                bw=190)
        if path != [(1, 3), (3, 4)] or delay != 20:
            print '  first search failed, got:' + str(path) + ' instead of:\
[(1, 3), (3, 4)]'
            err = True

        path, delay = mapper.constrainedDijkstra(0, 1, [4, 5], delay=50,
                bw=240)
        if path != [(1, 3), (3, 6), (6, 5)] or delay != 20:
            print '  second search failed, got:' + str(path) + ' instead of:\
[(1, 3), (3, 6), (6, 5)]'
            err = True

        # Unfeasible delays and bandwidths
        path, _ = mapper.constrainedDijkstra(0, 1, [4, 5], delay=50, bw=1000)
        if path is not None:
            print '  it should not have found any possible path'
            err = True

        path, _ = mapper.constrainedDijkstra(0, 1, [4, 5], delay=19, bw=0)
        if path is not None:
            print '  it should not have found any possible path'
            err = True

        if not err:
            print '  constrained Dijkstra works!'


    def testGreedy(self):
        """Tests the greedy mapping algorithm
        :returns: Nothing

        """
        md = self.__genMultiDomain()
        mapper = NSM.NsMapper(md)
        err = False

        print '############'
        print '## greedy ##'
        print '############'


        # Stress test server consumption
        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=1)
        chain.add_node(2, memory=0, disk=10, cpu=1)
        chain.add_edge('start', 1, bw=0, delay=90)
        chain.add_edge(1, 2, bw=0, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([2])

        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping.getPath('start', 1) == [(1, 3), (3, 4)] and\
                nsMapping.getPath(1, 2) == [(4, 4)] and\
                nsMapping.getServerMapping(1) == 4 and\
                nsMapping.getServerMapping(2) == 4 and\
                nsMapping.getDelay() == 20:
            print '  first server-stress mapping: OK'
        else:
            print '  first server-stress mapping: ERR'


        ns = NS.NS() # node 4 can only host one of the VNFs
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=2)
        chain.add_node(2, memory=0, disk=10, cpu=2)
        chain.add_edge('start', 1, bw=0, delay=90)
        chain.add_edge(1, 2, bw=0, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([2])
        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping.getPath('start', 1) == [(1, 3), (3, 4)] and\
                nsMapping.getPath(1, 2) == [(4, 5)] and\
                nsMapping.getServerMapping(1) == 4 and\
                nsMapping.getServerMapping(2) == 5 and\
                nsMapping.getDelay() == 26:
            print '  second server-stress mapping: OK\n'
        else:
            print '  second server-stress mapping: ERR'
        
        mapper.freeMappings()

        # Link stress testing
        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=0, cpu=0)
        chain.add_edge('start', 1, bw=200, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([1])

        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping.getPath('start', 1) == [(1, 3), (3, 4)] and\
            nsMapping.getServerMapping(1) == 4 and\
            nsMapping.getDelay() == 20:
            print '  first link-stress mapping: OK'
        else:
            print '  first link-stress mapping: ERR'

        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=0, cpu=4)
        chain.add_node(2, memory=0, disk=0, cpu=1)
        chain.add_edge('start', 1, bw=0, delay=90)
        chain.add_edge(1, 2, bw=250, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([2])
    
        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping.getPath('start', 1) == [(1, 3), (3, 4)] and\
                nsMapping.getPath(1, 2) == [(4, 5)] and\
                nsMapping.getServerMapping(1) == 4 and\
                nsMapping.getServerMapping(2) == 5 and\
                nsMapping.getDelay() == 26:
            print '  second link-stress mapping: OK'
        else:
            print '  second link-stress mapping: ERR'

        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=0)
        chain.add_node(2, memory=0, disk=10, cpu=0)
        chain.add_edge('start', 1, bw=50, delay=90)
        chain.add_edge(1, 2, bw=30000, delay=0)
        ns.setChain(chain)
        ns.setBranchHeads([2])
    
        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping.getPath('start', 1) == [(1, 3), (3, 6), (6, 5)] and\
                nsMapping.getPath(1, 2) == [(5, 5)] and\
                nsMapping.getServerMapping(1) == 5 and\
                nsMapping.getServerMapping(2) == 5 and\
                nsMapping.getDelay() == 20:
            print '  third link-stress mapping: OK'
        else:
            print '  third link-stress mapping: ERR'


        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=0, cpu=0)
        chain.add_edge('start', 1, bw=200, delay=19)
        ns.setChain(chain)
        ns.setBranchHeads([1])

        nsMapping = mapper.greedy(0, 1, ns)
        if nsMapping != None:
            print '  fourth link-stress mapping: ERR'
        else:
            print '  fourth link-stress mapping: OK'

        mapper.freeMappings()


        #################################
        ## Test joining VNF in a chain ##
        #################################
        print ''
        md = self.__genSquareMultiDomain()
        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=51, cpu=4)
        chain.add_node(2, memory=0, disk=52, cpu=3)
        chain.add_node(3, memory=0, disk=53, cpu=2)
        chain.add_node(4, memory=0, disk=54, cpu=1)
        chain.add_edge('start', 1, bw=100, delay=100)
        chain.add_edge(1, 2, bw=100, delay=100)
        chain.add_edge(1, 3, bw=100, delay=100)
        chain.add_edge(3, 4, bw=100, delay=100)
        chain.add_edge(2, 4, bw=100, delay=100)
        ns.setChain(chain)
        ns.setBranchHeads([4])

        mapper = NSM.NsMapper(md)
        nsMapping = mapper.greedy(0, 1, ns)
        link13 = md.getLnkRes(0, 1, 3)
        link12 = md.getLnkRes(0, 1, 2)
        link34 = md.getLnkRes(0, 3, 4)
        link24 = md.getLnkRes(0, 2, 4)
        serv1 = md.getServerRes(0, 1)
        serv2 = md.getServerRes(0, 2)
        serv3 = md.getServerRes(0, 3)
        serv4 = md.getServerRes(0, 4)

        mappingsOk = nsMapping.getServerMapping(1) == 1 and\
                nsMapping.getServerMapping(2) == 2 and\
                nsMapping.getServerMapping(3) == 3 and\
                nsMapping.getServerMapping(4) == 4
        linksOk = link12['bw'] == link13['bw'] == link34['bw'] ==\
                link24['bw'] == 200
        serversOk = serv1['disk'] == serv1['cpu'] ==\
                serv2['disk'] == serv2['cpu'] ==\
                serv3['disk'] == serv3['cpu'] ==\
                serv4['disk'] == serv4['cpu']

        if mappingsOk and linksOk and serversOk:
            print '  joint VNFs mapping: OK!'
        else:
            print '  joint VNFs mapping: ERR!'

        mapper.freeMappings()


    def testRandomWalk(self):
        """Tests the random walk to find paths for VNF allocation
        :returns: Nothing

        """
        md = self.__genMultiDomain()
        mapper = NSM.NsMapper(md)
        err = False

        print '#################'
        print '## Random walk ##'
        print '#################'

        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=0)
        chain.add_edge('start', 1, bw=250, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([1])

        path, delay = mapper.randomWalk(0, 1, {4: None, 5: None}, 90, 250)
        if path == None or (path == [(1, 3), (3, 6), (6, 5)] and delay == 20):
            print '  first mapping worked!'
        else:
            print '  first mapping did not work as expected'

        path, delay = mapper.randomWalk(0, 1, {4: None, 5: None}, 90, 200)
        if path == None or\
                (path == [(1, 3), (3, 6), (6, 5)] and delay == 20) or\
                (path == [(1, 2), (2, 4)] and delay == 22) or\
                (path == [(1, 3), (3, 4)] and delay == 20):
            print '  second mapping worked!'
        else:
            print '  second mapping did not work as expected'


    def testSmartRandomWalk(self):
        """Tests the backtracking random walk to find paths for VNF allocation
        :returns: Nothing

        """
        md = self.__genMultiDomain()
        mapper = NSM.NsMapper(md)
        err = False

        print '#######################'
        print '## Smart random walk ##'
        print '#######################'

        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=0)
        chain.add_edge('start', 1, bw=250, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([1])

        path, delay = mapper.smartRandomWalk(0, 1, {4: None, 5: None}, 20,
                250)
        if path == [(1, 3), (3, 6), (6, 5)] and delay == 20:
            print '  first mapping worked!'
        else:
            print '  first mapping did not work as expected'
        print '  given path=' + str(path) + ' delay=' + str(delay)

        path, delay = mapper.smartRandomWalk(0, 1, {4: None, 5: None}, 90,
                200)
        if (path == [(1, 3), (3, 6), (6, 5)] and delay == 11) or\
                (path == [(1, 2), (2, 4)] and delay == 22) or\
                (path == [(1, 3), (3, 4)] and delay == 20):
            print '  second mapping worked!'
        else:
            print '  second mapping did not work as expected'
        print '  given path=' + str(path) + ' delay=' + str(delay)

        path, delay = mapper.smartRandomWalk(0, 1, {4: None, 5: None}, 90,
                1000)
        if path == None:
            print '  third mapping worked!'
        else:
            print '  third mapping did not work as expected'
        print '  given path=' + str(path)


    def testBFS(self):
        """Tests the BFS algorithm to find paths between certain nodes-
        :returns: Nothing

        """
        md = self.__genMultiDomain()
        mapper = NSM.NsMapper(md)
        err = False

        print '#########'
        print '## BFS ##'
        print '#########'

        ns = NS.NS()
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=0, disk=10, cpu=0)
        chain.add_edge('start', 1, bw=250, delay=90)
        ns.setChain(chain)
        ns.setBranchHeads([1])

        path, delay = mapper.BFS(0, 1, {4: None, 5: None}, 20, 250)
        if path == [(1, 3), (3, 6), (6, 5)] and delay == 20:
            print '  first mapping worked!'
        else:
            print '  first mapping did not work as expected'

        path, _= mapper.BFS(0, 1, {4: None, 5: None}, 20, 250, depth=2)
        if path == None:
            print '  second mapping worked!'
        else:
            print '  second mapping did not work as expected'

        path, delay = mapper.BFS(0, 1, {4: None, 5: None}, 90, 200)
        if path == [(1, 2), (2, 4)] and delay == 22:
            print '  third mapping worked!'
        else:
            print '  third mapping did not work as expected'

        path, _ = mapper.BFS(0, 1, {4: None, 5: None}, 90, 200, depth=1)
        if path == None:
            print '  fourth mapping worked!'
        else:
            print '  fourth mapping did not work as expected'


    def greedyNsBunch(self, numNs):
        """Launches a bunch of NS requests to be mapped on top of an existing
        multiDomain. In case it is not already created, a multiDomain will be
        generated. Is just to check if some errors appear.

        :numNs: number of NSs to be within the bunch
        :returns: Nothing

        """
        # Create the NS requests bunch
        bwTh = {'min': 100, 'max': 200}
        delayTh = {'min': 5, 'max': 15}
        memoryTh = {'min': 1, 'max': 3}
        diskTh = {'min': 20, 'max': 100}
        cpuTh = {'min': 1, 'max': 4}
        nsGen = NSG.NSgenerator(bwTh, delayTh, memoryTh, diskTh, cpuTh)
        NSs = []
        for _ in range(numNs):
            ns = nsGen.yieldChain(2, 3, 3, 6)
            NSs.append(ns)

        # Generate/read the multiDomain
        md = None
        if not os.path.exists('graphs/greedyNsBunch') or\
                not os.path.isdir('graphs/greedyNsBunch'):
            print 'a escribir'
            md = MD.MultiDomain.yieldRandMultiDomain()
            md.write('greedyNsBunch')
        else:
            md = MD.MultiDomain.read('greedyNsBunch')

        # Execute the mappings
        failed = 0
        mapper = NSM.NsMapper(md)
        domains = len(md.getDomainsViews())
        print 'Multidomain has ' + str(domains) + ' domains'
        for ns in NSs:
            domain = random.randint(0, domains - 1)
            servers = md.getServers(domain).keys()
            entryS = random.randint(0, len(servers) - 1)
            print 'entryServer=' + str(servers[entryS]) + ', possibleEntryServers=' +\
                str(len(servers)) + ', domain=' + str(domain)
            print ns
            nsMapping = mapper.greedy(domain, servers[entryS], ns,
                    method='Dijkstra')
            if nsMapping == None:
                print 'nsMapping: None'
                failed += 1
            else:
                print nsMapping
                print '=======================\n'

        mapper.freeMappings()
    
        print '  successful requests: ' + str(numNs - failed)
        print '  failed requests: ' + str(failed)


    def testModifyMappedPath(self):
        """Test the modifyMappedPath method
        :returns: Nothing

        """
        print '######################'
        print '## modifyMappedPath ##'
        print '######################'

        # First NS example
        graph = nx.Graph()
        graph.add_node('start')
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge('start', 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        ns = NS.NS()
        ns.setChain(graph)
        ns.setBranchHeads([3])

        mapper = NSM.NsMapper(self.__genMultiDomain()) # the multiDomain does
                                                       # not matter
        mapping = {1: 3, 2: 5, 3: 6}
        path = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

        # Remap VNF1 to server 2
        newPath = mapper.modifyMappedPath(ns, 1, 2, mapping, path, [(0, 1), (1, 2)],
                [(2, 3), (3, 4), (4, 'A'), ('A', 5)])
        if newPath == [(0, 1), (1, 2), (2, 3), (3, 4), (4, 'A'), ('A', 5),
                (5, 6)]:
            print '  first remapping OK!'
        else:
            print '  first mapping BAD!, got newPath=' + str(newPath)

        # Remap VNF2 to server 3
        newPath = mapper.modifyMappedPath(ns, 2, 3, mapping, path, [(3, 3)],
                [(3, 4), (4, 'A'), ('A', 'B'), ('B', 5), (5, 6)])
        if newPath == [(1, 2), (2, 3), (3, 3), (3, 4), (4, 'A'),
                ('A', 'B'), ('B', 5), (5, 6)]:
            print '  second remapping OK!'
        else:
            print '  second mapping BAD!, got newPath=' + str(newPath)

        # Remap VNF3 to server 7
        newPath = mapper.modifyMappedPath(ns, 3, 7, mapping, path, [(5, 'C'),
            ('C', 'D'), ('D', 7)], [])
        if newPath == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 'C'), ('C', 'D'),
                ('D', 7)]:
            print '  third remapping OK!'
        else:
            print '  third mapping BAD!, got newPath=' + str(newPath)

        # Test if exceptions are risen properly
        errorCatched = False
        try:
            newPath = mapper.modifyMappedPath(ns, 1, 2, mapping, path,
                    [(0, 1), (1, 5)], [(2, 3), (3, 4), (4, 'A'), ('A', 5)])
        except Exception as e:
            errorCatched = True
            print '  raise last node in prevPath != new server: OK!'
        if not errorCatched:
            print '  raise last node in prevPath != new server: ERR!'

        errorCatched = False
        try:
            newPath = mapper.modifyMappedPath(ns, 1, 2, mapping, path,
                    [(0, 1), (1, 2)], [(10, 3), (3, 4), (4, 'A'), ('A', 5)])
        except Exception as e:
            errorCatched = True
            print '  raise first node in afterPath!= new server: OK!'
        if not errorCatched:
            print '  raise first node in afterPath!= new server: OK!'

        errorCatched = False
        try:
            newPath = mapper.modifyMappedPath(ns, 2, 3, mapping, path,
                    [(6, 3)], [(3, 4), (4, 'A'), ('A', 'B'), ('B', 5),
                    (5, 6)])
        except Exception as e:
            errorCatched = True
            print '  raise first node in prevPath != prev server: OK!'
        if not errorCatched:
            print '  raise first node in prevPath != prev server: OK!'

        errorCatched = False
        try:
            newPath = mapper.modifyMappedPath(ns, 2, 3, mapping, path,
                    [(3, 3)], [(3, 4), (4, 'A'), ('A', 'B'), ('B', 5),
                    (5, 8)])
        except Exception as e:
            errorCatched = True
            print '  raise last node in afterPath != next server: OK!'
        if not errorCatched:
            print '  raise last node in afterPath != next server: OK!'


        # Second NS example
        graph = nx.Graph()
        graph.add_node('start')
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge('start', 1)
        graph.add_edge(1, 2)
        ns = NS.NS()
        ns.setChain(graph)
        ns.setBranchHeads([2])

        mapping = {1: 1, 2: 3}
        path = [(1, 1), (1, 2), (2, 3)]

        # Remap VNF2 to server 1
        newPath = mapper.modifyMappedPath(ns, 2, 1, mapping, path, [(1, 1)],
                [])
        if newPath == [(1, 1), (1, 1)]:
            print '  fourth remapping OK!'
        else:
            print '  fourth mapping BAD!, got newPath=' + str(newPath)
        
        # Remap VNF1 to server 3
        newPath = mapper.modifyMappedPath(ns, 1, 3, mapping, path, [(1, 2),
            (2, 3)], [(3, 3)])
        if newPath == [(1, 2), (2, 3), (3, 3)]:
            print '  fifth remapping OK!'
        else:
            print '  fifth mapping BAD!, got newPath=' + str(newPath)
        

    def testTabu(self):
        """Tests the tabu search algorithm
        :returns: Nothing

        """
        md = self.__genTabuMultiDomain()
        ns = self.__genTabuNS()
        mapper = NSM.NsMapper(md)

        print '##########'
        print '## tabu ##'
        print '##########'

        # No tabu iterations (same as greedy)
        mapping = mapper.tabu(0, 1, ns, 10, 0)
        if mapping.getPath('start', 1) == [(1, 1)] and\
                mapping.getPath(1, 2) == [(1, 20), (20, 2)] and\
                mapping.getPath(1, 3) == [(1, 21), (21, 3)] and\
                mapping.getPath(2, 4) == [(2, 24), (24, 4)] and\
                mapping.getPath(3, 4) == [(3, 23), (23, 4)] and\
                mapping.getPath(4, 6) == [(4, 30), (30, 5)] and\
                mapping.getPath(4, 5) == [(4, 31), (31, 6)] and\
                mapping.getServerMapping(1) == 1 and\
                mapping.getServerMapping(2) == 2 and\
                mapping.getServerMapping(3) == 3 and\
                mapping.getServerMapping(4) == 4 and\
                mapping.getServerMapping(5) == 6 and\
                mapping.getServerMapping(6) == 5:
            print '  first tabu mapping 0 iterations: OK'
        else:
            print '  first tabu mapping 0 iterations: ERR'
        mapper.freeMappings()

        # 1 tabu iteration
        mapping = mapper.tabu(0, 1, ns, 10, 1)
        if mapping.getPath('start', 1) == [(1, 1)] and\
                mapping.getPath(1, 2) == [(1, 20), (20, 2)] and\
                mapping.getPath(1, 3) == [(1, 21), (21, 3)] and\
                mapping.getPath(2, 4) == [(2, 26), (26, 7)] and\
                mapping.getPath(3, 4) == [(3, 25), (25, 7)] and\
                mapping.getPath(4, 6) == [(7, 32), (32, 8)] and\
                mapping.getPath(4, 5) == [(7, 33), (33, 9)] and\
                mapping.getServerMapping(1) == 1 and\
                mapping.getServerMapping(2) == 2 and\
                mapping.getServerMapping(3) == 3 and\
                mapping.getServerMapping(4) == 7 and\
                mapping.getServerMapping(5) == 9 and\
                mapping.getServerMapping(6) == 8 and\
                mapping.getDelay() == 102:
            print '  second tabu mapping 1 iterations: OK'
        else:
            print '  second tabu mapping 1 iterations: ERR'
        mapper.freeMappings()

        # 2 tabu iteration
        mapping = mapper.tabu(0, 1, ns, 10, 2)
        if mapping.getPath('start', 1) == [(1, 1)] and\
                mapping.getPath(1, 2) == [(1, 20), (20, 2)] and\
                mapping.getPath(1, 3) == [(1, 21), (21, 3)] and\
                mapping.getPath(2, 4) == [(2, 28), (28, 10)] and\
                mapping.getPath(3, 4) == [(3, 27), (27, 10)] and\
                mapping.getPath(4, 6) == [(10, 34), (34, 11)] and\
                mapping.getPath(4, 5) == [(10, 35), (35, 12)] and\
                mapping.getServerMapping(1) == 1 and\
                mapping.getServerMapping(2) == 2 and\
                mapping.getServerMapping(3) == 3 and\
                mapping.getServerMapping(4) == 10 and\
                mapping.getServerMapping(5) == 12 and\
                mapping.getServerMapping(6) == 11 and\
                mapping.getDelay() == 64:
            print '  third tabu mapping 3 iterations: OK'
        else:
            print '  third tabu mapping 3 iterations: ERR'
        mapper.freeMappings()

        # 8 tabu iteration
        mapping = mapper.tabu(0, 1, ns, 10, 2)
        if mapping.getPath('start', 1) == [(1, 1)] and\
                mapping.getPath(1, 2) == [(1, 20), (20, 2)] and\
                mapping.getPath(1, 3) == [(1, 21), (21, 3)] and\
                mapping.getPath(2, 4) == [(2, 28), (28, 10)] and\
                mapping.getPath(3, 4) == [(3, 27), (27, 10)] and\
                mapping.getPath(4, 6) == [(10, 34), (34, 11)] and\
                mapping.getPath(4, 5) == [(10, 35), (35, 12)] and\
                mapping.getServerMapping(1) == 1 and\
                mapping.getServerMapping(2) == 2 and\
                mapping.getServerMapping(3) == 3 and\
                mapping.getServerMapping(4) == 10 and\
                mapping.getServerMapping(5) == 12 and\
                mapping.getServerMapping(6) == 11 and\
                mapping.getDelay() == 64:
            print '  fourth tabu mapping 8 iterations: OK'
        else:
            print '  fourth tabu mapping 8 iterations: ERR'
        mapper.freeMappings()



if __name__ == '__main__':
    tester = NsMapperTester()
    # tester.testConstrainedDijkstra()
    # tester.testGreedy()
    # tester.testRandomWalk()
    # tester.testSmartRandomWalk()
    # tester.testBFS()
    # tester.greedyNsBunch(100)
    # tester.testModifyMappedPath()
    tester.testTabu()


