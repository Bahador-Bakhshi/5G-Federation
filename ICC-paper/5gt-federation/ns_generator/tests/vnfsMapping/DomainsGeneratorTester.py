import sys
import os
import random
import itertools
import networkx as nx
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import DomainsGenerator as DG



class DomainsGeneratorTester(object):

    """Test the domain generation class"""

    def __init__(self):
        properties = DG.DomainsGenerator.genProperties()

        self.__domains = properties['domains']
        self.__meshDegree = properties['meshDegree']
        self.__fatTreeDegrees = properties['fatTreeDegrees']
        self.__foreignPods = properties['foreignPods']
        self.__meshLnkRes = properties['meshLnkRes']
        self.__fatLnkRes = properties['fatLnkRes']
        self.__servRes = properties['servRes']


    def getAttrNodes(self, graph, attr, value):
        """Gets graph nodes with a certain attribute value

        :graph: networkX grpah
        :attr: attribute string
        :value: attribute value
        :returns: list of nodes with attr=value

        """
        nodes = nx.get_node_attributes(graph, attr)
        return filter(lambda node: nodes[node] == value, nodes.keys())


    def testFatTree(self):
        """Tests the fat-tree generation
        :returns: True | False if test succeeds or not

        """

        print '#####################'
        print '### fat-tree test ###'
        print '#####################'


        generator = DG.DomainsGenerator(domains=1, meshDegree=0,
                fatTreeDegrees=[1], meshLnkRes=self.__meshLnkRes,
                fatLnkRes=self.__fatLnkRes, servRes=self.__servRes)

        for k in [4, 6, 8]:
            # Test k-ary tree generation
            print 'Checking ' + str(k) + '-ary fat-tree generation'
            generator.setFatTreeDegrees([k])
            globalView = generator.createGlobalView()

            coreNodes = self.getAttrNodes(globalView, 'fatType', 'core')
            aggNodes = self.getAttrNodes(globalView, 'fatType', 'aggregate')
            edgeNodes = self.getAttrNodes(globalView, 'fatType', 'edge')

            # Check nodes degree
            gwDegOk = globalView.degree(0) == k/2*k/2
            coreDegOk = reduce(lambda ok, node: ok and\
                    globalView.degree(node) == k+1, coreNodes)
            aggNodesOk = reduce(lambda ok, node: ok and\
                    globalView.degree(node) == k, aggNodes)
            edgeNodesOk = reduce(lambda ok, node: ok and\
                    globalView.degree(node) == k, edgeNodes)

            print '  gwDegOk: ' + str(gwDegOk)
            print '  coreDegOk: ' + str(coreDegOk)
            print '  aggNodesOk: ' + str(aggNodesOk)
            print '  edgeNodesOk: ' + str(edgeNodesOk)

            # Check shortest paths
            servers = self.getAttrNodes(globalView, 'fatType', 'server')
            pathLengths = dict()
            for (server1, server2) in itertools.combinations(servers, 2):
                length = nx.dijkstra_path_length(globalView, server1, server2)
                pathLengths[length] = 1 if length not in pathLengths.keys()\
                        else pathLengths[length] + 1

            len2Paths = k*k/2*len(list(itertools.combinations(range(k/2), 2)))
            len4Paths = k*( len(list(itertools.combinations(range(k/2*k/2),
                2))) - k/2*len(list(itertools.combinations(range(k/2), 2))) )
            len6Paths = len(list(itertools.combinations(range(k*k/2*k/2),
                2))) - len4Paths - len2Paths

            print '  len2Paths: ' + str(len2Paths)
            print '  len4Paths: ' + str(len4Paths)
            print '  len6Paths: ' + str(len6Paths)

            print '  ' + str(pathLengths)
            print '  path lengths ok?: ' + str(len2Paths == pathLengths[2]\
                    and len4Paths == pathLengths[4] and\
                    len6Paths == pathLengths[6])

    
    def domainsViewTester(self):
        """Test if each domain view of the global graph is correct
        :returns: TODO

        """

        print '\n########################'
        print '### domainsView test ###'
        print '########################'

        # Create the global and per domain graph views
        generator = DG.DomainsGenerator(domains=self.__domains,
                meshDegree=self.__meshDegree,
                fatTreeDegrees=self.__fatTreeDegrees,
                meshLnkRes=self.__meshLnkRes, fatLnkRes=self.__fatLnkRes,
                servRes=self.__servRes)
        globalView = generator.createGlobalView()
        print '       \ttheory\treal'
        for domain in range(self.__domains):
            domainView = generator.createDomainView(globalView, domain,
                    self.__foreignPods[domain])
            # Check if it has the correct number of nodes
            k = self.__fatTreeDegrees[domain]
            fatTreeNodes = k/2*k/2 + k*k + k*k*k/4
            sharedNodes = 0
            
            for shareDomain in self.__foreignPods[domain]:
                shareK = self.__fatTreeDegrees[int(shareDomain)]
                pods = self.__foreignPods[domain][shareDomain]
                sharedNodes += len(pods)* (shareK + shareK*shareK/4) # pod
                sharedNodes += shareK*shareK/4 # core switches

            theoryNodes = fatTreeNodes + self.__domains + sharedNodes

            print 'Domain' + str(domain) + '\t' + str(theoryNodes) + '\t' +\
                    str(len(domainView.nodes())) + ('\tok' if theoryNodes ==
                            len(domainView.nodes()) else '\terr')


    def testMeshBw(self):
        """Tests if the mesh links share bandwidth properly accross domains.
        :returns: None

        """

        print '\n########################'
        print '### issueMeshBw test ###'
        print '########################'

        print '(gwA,gwB): sum of domain bws for link (gwA,gwB) <= totalBW ->\
 True/False'

        # Generate the domain and subdomain views
        generator = DG.DomainsGenerator(domains=self.__domains,
                meshDegree=self.__meshDegree,
                fatTreeDegrees=self.__fatTreeDegrees,
                meshLnkRes=self.__meshLnkRes, fatLnkRes=self.__fatLnkRes,
                servRes=self.__servRes)
        globalView = generator.createGlobalView()
        domainsViews = []
        for domain in range(self.__domains):
            domainsViews.append(generator.createDomainView(globalView, domain,
                self.__foreignPods[domain]))
        generator.issueMeshBw(globalView, domainsViews)

        # Check bandwidth's sums
        for (gwA, gwB) in nx.get_edge_attributes(globalView, 'meshLink'):
            bwDomain = []
            for domain in range(self.__domains):
                bwDomain.append(domainsViews[domain][gwA][gwB]['res']['bw'])

            globalBw = globalView[gwA][gwB]['res']['bw']
            bwDomainSum = reduce(lambda x, y: x+y, bwDomain)
            bwDomainSumStr = ' + '.join([str(bw) for bw in bwDomain])
            sumStr = '(' + str(gwA) + ', ' + str(gwB) + '): ' + bwDomainSumStr\
                + ' = ' + str(bwDomainSum) + ' <= ' +\
                str(globalBw) + ' -> ' + str(bwDomainSum <= globalBw)
            print sumStr

    
    def testFatTreeRes(self):
        """Tests the assignment of resources to the fat-tree
        :returns: Nothing

        """
        print '\n########################'
        print '### issueFatRes test ###'
        print '########################'

        # Generate the domain and subdomain views
        generator = DG.DomainsGenerator(domains=self.__domains,
                meshDegree=self.__meshDegree,
                fatTreeDegrees=self.__fatTreeDegrees,
                meshLnkRes=self.__meshLnkRes, fatLnkRes=self.__fatLnkRes,
                servRes=self.__servRes)
        globalView = generator.createGlobalView()
        domainsViews = []
        for domain in range(self.__domains):
            domainsViews.append(generator.createDomainView(globalView, domain,
                self.__foreignPods[domain]))
        generator.issueFatRes(globalView, domainsViews)

        # Test fat-tree proportional assignment for edges
        exceeded = False
        for domain in range(self.__domains):
            for (A, B) in generator.getFatTreeEdges(globalView, domain):
                totalBw = globalView[A][B]['res']['bw']
                issuedBw = []
                issuedProps = []
                
                for localDom in range(self.__domains):
                    domainView = domainsViews[localDom]
                    resEdges = nx.get_edge_attributes(domainView, 'res')
                    if (A, B) in resEdges.keys():
                        issuedBw.append(domainView[A][B]['res']['bw'])
                        issuedProps.append(domainView[A][B]['res']['prop'])

                sumedIssued = reduce(lambda x,y: x+y, issuedBw)
                if sumedIssued > totalBw:
                    exceeded = True
                    strIssuedBw = [str(bw) for bw in issuedBw]
                    print '(' + str(A) + ',' + str(B) + '): ' +\
                            ' + '.join(strIssuedBw) + ' = ' +\
                            str(sumedIssued) + ' > ' + str(totalBw)

        if exceeded:
            print 'Error, above link exceeds bandwidth shared'
        else:
            print 'Fat-tree link resources shared properly - OK'

        # Test fat-tree proportional assignment for servers
        exceeded = False
        for domain in range(self.__domains):
            for server in generator.getFatTreeServers(globalView, domain):
                resourcesG = nx.get_node_attributes(globalView, 'res')[server]

                resources = dict()
                for localDom in range(self.__domains):
                    localView = domainsViews[localDom]
                    hasServer = nx.get_node_attributes(localView,
                            'res').has_key(server)

                    if hasServer:
                        resourcesL = nx.get_node_attributes(localView,
                                'res')[server]
                        for res in resourcesG.keys():
                            if not resources.has_key(res):
                                resources[res] = []
                            resources[res].append(resourcesL[res])

                # Check server resurces distribution
                for res in resourcesG.keys():
                    distRes = resources[res]
                    distResSum = reduce(lambda x,y: x+y, distRes)
                    globalRes = resourcesG[res]

                    if distResSum > globalRes:
                        print 'server' + str(server) + ' - ' + str(res) + ': '\
                                + ' + '.join([str(res) for res in distRes]) +\
                                ' = ' + str(distResSum) + ' > ' +\
                                str(globalRes)

        if exceeded:
            print 'Error, above server resurces sharing have been exceeded'
        else:
            print 'Server resources shared properly - OK'


if __name__ == '__main__':
    tester = DomainsGeneratorTester()
    tester.testFatTree()
    tester.domainsViewTester()
    tester.testMeshBw()
    tester.testFatTreeRes()

