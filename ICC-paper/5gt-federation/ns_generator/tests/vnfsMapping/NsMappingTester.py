import sys
import os
import random
import networkx as nx

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import NS
from vnfsMapping import NsMapping as NSm

class NsMappingTester(object):

    """Testing class for the NsMapping class"""

    def __init__(self):
        """TODO: to be defined1. """
        

    def genNS(self):
        """Generates the NS that will be used for testing methods.
        :returns: NS instance

        """
        chain = nx.Graph()
        chain.add_node('start')
        chain.add_node(1, memory=2, disk=3, cpu=4)
        chain.add_node(2, memory=2, disk=3, cpu=4)
        chain.add_node(3, memory=2, disk=3, cpu=4)
        chain.add_node(4, memory=2, disk=3, cpu=4)
        chain.add_node(5, memory=2, disk=3, cpu=4)
        chain.add_node(6, memory=2, disk=3, cpu=4)
        chain.add_node(7, memory=2, disk=3, cpu=4)
        chain.add_node(8, memory=2, disk=3, cpu=4)
        chain.add_node(9, memory=2, disk=3, cpu=4)

        chain.add_edge('start', 1, bw=2, delay=100)
        chain.add_edge(1, 2, bw=2, delay=100)
        chain.add_edge(1, 3, bw=2, delay=100)
        chain.add_edge(2, 4, bw=2, delay=100)
        chain.add_edge(3, 4, bw=2, delay=100)
        chain.add_edge(4, 5, bw=2, delay=100)
        chain.add_edge(4, 6, bw=2, delay=100)
        chain.add_edge(5, 7, bw=2, delay=100)
        chain.add_edge(6, 7, bw=2, delay=100)
        chain.add_edge(7, 8, bw=2, delay=100)
        chain.add_edge(7, 9, bw=2, delay=100)

        ns = NS.NS()
        ns.setChain(chain)
        ns.setSplitsNum(3)
        ns.setBranchNum(2)
        ns.setMaxSplitW(2)
        ns.setBranchHeads([8, 9])

        return ns


    def testMappingCreation(self):
        """Tests the creation of a NS mapping
        :returns: Nothing

        """
        ns = self.genNS()
        nsMapping = NSm.NsMapping(ns)

        print '###########################'
        print '## setLnkDelayAndRefresh ##'
        print '###########################'
        nsMapping.setLnkDelayAndRefresh('start', 1, 1)
        nsMapping.setLnkDelayAndRefresh(1, 2, 3)
        nsMapping.setLnkDelayAndRefresh(1, 3, 2)
        nsMapping.setLnkDelayAndRefresh(2, 4, 2)
        nsMapping.setLnkDelayAndRefresh(3, 4, 1)
        nsMapping.setLnkDelayAndRefresh(4, 5, 1)
        nsMapping.setLnkDelayAndRefresh(4, 6, 3)
        nsMapping.setLnkDelayAndRefresh(5, 7, 2)
        nsMapping.setLnkDelayAndRefresh(6, 7, 4)
        nsMapping.setLnkDelayAndRefresh(7, 8, 2)
        nsMapping.setLnkDelayAndRefresh(7, 9, 3)

        if nsMapping.getDelay() == 16 and nsMapping.getVnfDelay(1) == 1 and\
                nsMapping.getVnfDelay(2) == 4 and\
                nsMapping.getVnfDelay(3) == 3 and\
                nsMapping.getVnfDelay(4) == 6 and\
                nsMapping.getVnfDelay(5) == 7 and\
                nsMapping.getVnfDelay(6) == 9 and\
                nsMapping.getVnfDelay(7) == 13 and\
                nsMapping.getVnfDelay(8) == 15 and\
                nsMapping.getVnfDelay(9) == 16:
            print '  mapping creation: OK!'
        else:
            print '  mapping creation: ERR!'


    def testChangeVnfMapping(self):
        """Tests the changeVnfMapping() method
        :returns: TODO

        """
        ns = self.genNS()
        nsMapping = NSm.NsMapping(ns)

        print '######################'
        print '## changeVnfMapping ##'
        print '######################'
        nsMapping.setLnkDelayAndRefresh('start', 1, 1)
        nsMapping.setLnkDelayAndRefresh(1, 2, 3)
        nsMapping.setLnkDelayAndRefresh(1, 3, 2)
        nsMapping.setLnkDelayAndRefresh(2, 4, 2)
        nsMapping.setLnkDelayAndRefresh(3, 4, 1)
        nsMapping.setLnkDelayAndRefresh(4, 5, 1)
        nsMapping.setLnkDelayAndRefresh(4, 6, 3)
        nsMapping.setLnkDelayAndRefresh(5, 7, 2)
        nsMapping.setLnkDelayAndRefresh(6, 7, 4)
        nsMapping.setLnkDelayAndRefresh(7, 8, 2)
        nsMapping.setLnkDelayAndRefresh(7, 9, 3)
    
        nsMapping.changeVnfMapping(4, [2, 3], [5, 6], [3, 7], [1, 1])

        if nsMapping.getDelay() == 18 and nsMapping.getVnfDelay(4) == 10 and\
                nsMapping.getVnfDelay(5) == 11 and\
                nsMapping.getVnfDelay(6) == 11 and\
                nsMapping.getVnfDelay(7) == 15 and\
                nsMapping.getVnfDelay(8) == 17 and\
                nsMapping.getVnfDelay(9) == 18:
            print '  changed mapping: OK!'
        else:
            print '  changed mapping: ERR'

if __name__ == '__main__':
    tester = NsMappingTester()
    tester.testMappingCreation()
    tester.testChangeVnfMapping()

