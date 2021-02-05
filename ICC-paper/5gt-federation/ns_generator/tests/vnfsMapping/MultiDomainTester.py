import sys
import os
import random
import itertools
import networkx as nx
import NsMapperTester as NSMT
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import MultiDomain as MD
from vnfsMapping import DomainsGenerator as DG


class MultiDomainTester(object):

    """Class to test the MultiDomain's functionalities"""

    def __init__(self):
        """__init__ """
        self.__multiDomain = MD.MultiDomain.yieldRandMultiDomain()

    
    def testGetPathDelay(self):
        """Tests the path delay retrieval
        :returns: Nothing

        """
        print '\n#######################'
        print '### getPathDelay test ###'
        print '#########################'

        nsMapperTester = NSMT.NsMapperTester()
        md = nsMapperTester._NsMapperTester__genMultiDomain()

        delay = md.getPathDelay(0, [(1, 3), (3, 6), (6, 5), (5, 5)])
        if delay != 20:
            print '  first retrieved delay is not 20, it is:' + str(delay)
        else:
            print '  first retrieved delay is OK!'

        delay = md.getPathDelay(0, [(1, 3), (3, 4), (4, 4), (4, 5), (5, 5)])
        if delay != 26:
            print '  second retrieved delay is not 20, it is:' + str(delay)
        else:
            print '  second retrieved delay is OK!'


    def testIncrLnkResource(self):
        """Tests the increment of link resources
        :returns: Nothing

        """
        resources = ['bw', 'delay']
        globalView = self.__multiDomain.getGlobalView()
        domainsViews = self.__multiDomain.getDomainsViews()

        print '\n###########################'
        print '### incrLnkResource test ###'
        print '############################'

        # Test arguments checking
        if self.__multiDomain.incrLnkResource(len(domainsViews), 1, 2,
                'delay', 0):
            print '  domains outside range - ERR'

        if self.__multiDomain.incrLnkResource(0, 1, 2, 'bla', 0):
            print '  increment of non-existing resource - ERR'

        # Test resurces decrement
        domain = random.randint(0, len(domainsViews) - 1)
        domainView = domainsViews[domain]
        edge = nx.get_edge_attributes(domainView, 'meshLink').keys()[0]
        globalRes = nx.get_edge_attributes(globalView, 'res')[edge]
        domainRes = nx.get_edge_attributes(domainView, 'res')[edge]

        for resource in resources:
            print '  # Testing resurce: ' + resource
            globalAm = globalRes[resource]
            domainAm = domainRes[resource]

            # Decrement more than what domain has
            if self.__multiDomain.incrLnkResource(domain, edge[0], edge[1],
                resource, -1 * (domainAm + 1)):
                print '  Trying to decrement more than it has: ERR'
            else:
                print '  Trying to decrement more than it has: OK'

            # Decrement, increment, and check coherence
            am = domainAm / 2
            if not self.__multiDomain.incrLnkResource(domain, edge[0],
                edge[1], resource, -1 * am):
                print '  Trying to decrement less than it has: ERR'
            else:
                print '  Trying to decrement less than it has: OK'

            nowGlobal = self.__multiDomain.getLnkRes(-1, edge[0],
                    edge[1])[resource]
            nowDomain = self.__multiDomain.getLnkRes(domain, edge[0],
                    edge[1])[resource]

            if (globalAm - nowGlobal) == (domainAm - nowDomain):
                print '  Resource coherence: OK'
            else:
                print '  Resource coherence: ERR'
            
            self.__multiDomain.incrLnkResource(domain, edge[0], edge[1], resource,
                am)
            nowGlobal = self.__multiDomain.getLnkRes(-1, edge[0],
                    edge[1])[resource]
            nowDomain = self.__multiDomain.getLnkRes(domain, edge[0],
                    edge[1])[resource]

            if (nowGlobal == globalAm) and (nowDomain == domainAm):
                print '  Resource restore: OK\n'
            else:
                print '  Resource restore: ERR\n'


    def testIncrServerResource(self):
        """Tests the incrServerResource method
        :returns: Nothing

        """
        resources = ['memory', 'cpu', 'disk']
        globalView = self.__multiDomain.getGlobalView()
        domainsViews = self.__multiDomain.getDomainsViews()

        print '\n##############################'
        print '### incrServerResource test ###'
        print '###############################'

        # Test resurces decrement
        domain = random.randint(0, len(domainsViews) - 1)
        domainView = domainsViews[domain]
        servers = nx.get_node_attributes(domainView, 'fatType')
        server = None
        for serverIt in servers.keys():
            if servers[serverIt] == 'server':
                server = serverIt

        for resource in resources:
            print '  # Testing resurce: ' + resource
            globalAm = self.__multiDomain.getServerRes(-1, server)[resource]
            domainAm = self.__multiDomain.getServerRes(domain ,
                    server)[resource]

            # Argument checking
            if self.__multiDomain.incrServerResource(len(domainsViews), 0,
                    'disk', 0):
                print '  domains outside range - ERR'
            if self.__multiDomain.incrServerResource(0, 1, 'bla', 0):
                print '  increment of non-existing resource - ERR'

            # Decrement mor than what the domain has
            if not self.__multiDomain.incrServerResource(domain, server,
                resource, -1 * (domainAm + 1)):
                print '  Trying to decrement more than it has: OK'
            else:
                print '  Trying to decrement more than it has: ERR'

            # Decrement, increment, and check coherence
            am = domainAm / 2
            if not self.__multiDomain.incrServerResource(domain, server,
                    resource, -1 * am):
                print '  Trying to decrement less than it has: ERR'
            else:
                print '  Trying to decrement less than it has: OK'

            nowGlobal = self.__multiDomain.getServerRes(-1, server)[resource]
            nowDomain = self.__multiDomain.getServerRes(domain,
                server)[resource]

            if (globalAm - nowGlobal) == (domainAm - nowDomain):
                print '  Resource coherence: OK'
            else:
                print '  Resource coherence: ERR'

            self.__multiDomain.incrServerResource(domain, server,
                resource, am)
            nowGlobal = self.__multiDomain.getServerRes(-1, server)[resource]
            nowDomain = self.__multiDomain.getServerRes(domain,
                server)[resource]

            if (nowGlobal == globalAm) and (nowDomain == domainAm):
                print '  Resource restore: OK\n'
            else:
                print '  Resource restore: ERR\n'


    def __compareMeshLnkRes(self, meshLnkResA, meshLnkResB):
        """Compares 2 meshLnkRes objects

        :meshLnkResA: first mesh link res
        :meshLnkResB: second mesh link res
        :returns: True/False

        """
        allEq = True
        for resource in meshLnkResA.keys():
            allEq = allEq and meshLnkResA[resource]['min']\
                    == meshLnkResB[resource]['min']
            allEq = allEq and meshLnkResA[resource]['max']\
                    == meshLnkResB[resource]['max']

        return allEq


    def __compareFatLnkRes(self, fatLnkResA, fatLnkResB):
        """Compares 2 fatLinkRes objects

        :fatLnkResA: object A
        :fatLnkResB: objectB
        :returns: True/False

        """
        allEq = True
        for resource in fatLnkResA.keys():
            allEq = allEq and fatLnkResA[resource]['min']\
                    == fatLnkResB[resource]['min']
            allEq = allEq and fatLnkResA[resource]['max']\
                    == fatLnkResB[resource]['max']

        return allEq


    def __compareServRes(self, servResA, servResB):
        """Compares server resources
        :fatLnkResA: object A
        :fatLnkResB: objectB
        :returns: True/False

        """
        allEq = True
        for resource in servResA.keys():
            allEq = allEq and servResA[resource]['min']\
                    == servResB[resource]['min']
            allEq = allEq and servResA[resource]['max']\
                    == servResB[resource]['max']

        return allEq


    def testWriteRead(self):
        """Tests the read and write functions for a MultiDomain instance
        :returns: Nothing

        """
        print '\n########################'
        print '### read & write test ###'
        print '#########################'

        # Recollect info before writting
        globalView = self.__multiDomain.getGlobalView()
        domainsViews = self.__multiDomain.getDomainsViews()

        beforeNodes = [domainView.number_of_nodes() for domainView in domainsViews]
        beforeNodes.insert(0, globalView.number_of_nodes())
        
        beforeEdges = [domainView.number_of_edges() for domainView in domainsViews]
        beforeEdges.insert(0, globalView.number_of_edges())

        beforeProperties = self.__multiDomain.getProperties()

        # Write and read
        self.__multiDomain.write('testMultiDomain')
        multiDomain = MD.MultiDomain.read('testMultiDomain')

        # Check info after read/write
        globalView = multiDomain.getGlobalView()
        domainsViews = multiDomain.getDomainsViews()
        afterProperties = multiDomain.getProperties()

        afterNodes = [domainView.number_of_nodes() for domainView in domainsViews]
        afterNodes.insert(0, globalView.number_of_nodes())
        
        afterEdges = [domainView.number_of_edges() for domainView in domainsViews]
        afterEdges.insert(0, globalView.number_of_edges())

        sameNodes = [nodesB == nodesA for (nodesB, nodesA) in zip(beforeNodes,
            afterNodes)]
        sameNodes = reduce(lambda okA, okB: okA and okB, sameNodes)
        sameEdges = [edgesB == edgesA for (edgesB, edgesA) in zip(beforeEdges,
            afterEdges)]
        sameEdges = reduce(lambda okA, okB: okA and okB, sameEdges)

        print '  same nodes before and after: ' + str(sameNodes)
        print '  same edges before and after: ' + str(sameEdges)

        # Check if properties remain the same
        print '  domains equal: ' + str(beforeProperties['domains'] ==
            afterProperties['domains'])
        print '  meshDegree equal: ' + str(beforeProperties['meshDegree'] ==
            afterProperties['meshDegree'])

        sameDegrees = [degB == degA for (degB, degA) in
                zip(beforeProperties['fatTreeDegrees'],
                    afterProperties['fatTreeDegrees'])]
        sameDegrees = reduce(lambda okA, okB: okA and okB, sameDegrees)
        print '  fatTreeDegrees equal: ' + str(sameDegrees)

        # Compare the mesh fat and serv resources
        print '  fatLnkRes equal before and after: ' +\
            str(self.__compareFatLnkRes(beforeProperties['fatLnkRes'],
                afterProperties['fatLnkRes']))
        print '  meshLinkRes equal before and after: ' +\
            str(self.__compareMeshLnkRes(beforeProperties['meshLnkRes'],
                afterProperties['meshLnkRes']))
        print '  servRes equal before and after: ' +\
            str(self.__compareServRes(beforeProperties['servRes'],
                afterProperties['servRes']))

        
if __name__ == '__main__':
    mdTester = MultiDomainTester()
    mdTester.testGetPathDelay()
    # mdTester.testIncrLnkResource()
    # mdTester.testIncrServerResource()
    # mdTester.testWriteRead()

