import json
import os
import sys
import networkx as nx
import DomainsGenerator as DG

# Global variable for the project absolute path
absPath = os.path.abspath(os.path.dirname(__file__))
graphsAbsPath = '/'.join(absPath.split('/')[:-2]) + '/graphs'


class MultiDomain(object):

    """Wrapper class to operate with the graphs associated to the multiple
    domains contained in a multi-domain scenario."""

    def __init__(self):
        """__init__
        """
        pass


    def __str__(self):
        """Returns the string representation for the multidomain
        :returns: TODO

        """
        header = '### MultiDomain ###\n'
        domains = '  - domains: ' + str(self.__domains if hasattr(self,
                '_MultiDomain__domains')\
                else str(None)) + '\n'
        meshDegree = '  - meshDegree: ' + str(self.__meshDegree if\
                hasattr(self, '_MultiDomain__meshDegree')\
                else str(None)) + '\n'
        fatTreeDegrees = '  - fatTreeDegrees: ' + str(self.__fatTreeDegrees\
                if hasattr(self, '_MultiDomain__fatTreeDegrees')\
                else str(None)) + '\n'
        meshLnkRes = '  - meshLnkRes: ' + str(self.__meshLnkRes\
                if hasattr(self, '_MultiDomain__meshLnkRes')\
                else str(None)) + '\n'
        fatLnkRes = '  - fatLnkRes: ' + str(self.__fatLnkRes\
                if hasattr(self, '_MultiDomain__fatLnkRes')\
                else str(None)) + '\n'
        servRes = '  - servRes: ' + str(self.__servRes\
                if hasattr(self, '_MultiDomain__servRes')\
                else str(None)) + '\n'
        foreignPods = '  - foreignPods: ' + str(self.__foreignPods\
                if hasattr(self, '_MultiDomain__servRes')\
                else str(None)) + '\n'

        return header + domains + meshDegree + fatTreeDegrees + meshLnkRes +\
            fatLnkRes + servRes + foreignPods


    def getDomainsViews(self):
        """Obtains the stored domains views' graphs
        :returns: list of networkx

        """
        return self.__domainsViews


    def getGlobalView(self):
        """Obtains the global view's graph
        :returns: networkx instance

        """
        return self.__globalView


    def getLnkRes(self, domain, A, B):
        """Obtains the resources available in a domain's link

        :domain: domain index, (-1 for global view link)
        :A: first node
        :B: second node
        :returns: dictionary with domain link
            False if an error ocurs

        """
        if not (-1 <= domain < self.__domains):
            print 'domain index not correct'
            return False

        view = self.__globalView if domain == -1 else\
            self.__domainsViews[domain]

        if not view.has_edge(A, B):
            print 'graph view don\'t have that link'
            return False

        lnksRes = nx.get_edge_attributes(view, 'res')
        if (A, B) in lnksRes:
            return lnksRes[(A, B)]
        else:
            return lnksRes[(B, A)]


    def getServerRes(self, domain, A):
        """Obtains the resources from a certain server

        :domain: domain index, (-1 for global view link)
        :A: server index
        :returns: dictionary with server resources from that domain
            False if an error ocurs

        """
        if not (-1 <= domain < self.__domains):
            print 'domain index not correct'
            return False

        view = self.__globalView if domain == -1 else\
            self.__domainsViews[domain]

        if not view.has_node(A):
            print 'graph view don\'t have that node'
            return False

        return nx.get_node_attributes(view, 'res')[A]


    def getCores(self):
        """Retrieves the core switches present in the global view
        :returns: dictionary indexed by the core nodes IDs

        """
        coreNodes = nx.get_node_attributes(self.__globalView, 'fatType')
        nodes = coreNodes.keys()
        for node in nodes:
            if coreNodes[node] != 'core':
                del coreNodes[node]

        return coreNodes


    def getAggregates(self):
        """Retrieves the aggregation switches present in the global view
        :returns: dictionary indexed by the agg nodes IDs

        """
        aggNodes = nx.get_node_attributes(self.__globalView, 'fatType')
        nodes = aggNodes.keys()
        for node in nodes:
            if aggNodes[node] != 'aggregate':
                del aggNodes[node]

        return aggNodes


    def getEdges(self):
        """Retrieves the edge switches present in the global view
        :returns: dictionary indexed by the edge nodes IDs

        """
        edgeNodes = nx.get_node_attributes(self.__globalView, 'fatType')
        nodes = edgeNodes.keys()
        for node in nodes:
            if edgeNodes[node] != 'edge':
                del edgeNodes[node]

        return edgeNodes


    def getServers(self, domain):
        """Retrieves the servers available under a certain domain

        :domain: domain index, (-1 for global view)
        :returns: list of server nodes of the networkx graph of the domain
            { 1: res:{'disk':_, 'cpu':_, 'mem':_}, ... }

        """
        
        domView = self.__domainsViews[domain] if domain != -1\
                else self.__globalView
        domNodes = nx.get_node_attributes(domView, 'fatType')
        servers = [ node for node in domNodes.keys() if domNodes[node] ==
                'server' ]

        serverNodes = dict()
        for server in servers:
            res = self.getServerRes(domain, server)
            serverNodes[server] = res

        return serverNodes


    def getCapableServers(self, domain, cpu, memory, disk):
        """Obtains the servers capable of deal with computational requirements
        under the given domain.

        :domain: domain index
        :cpu: cpu requirements
        :memory: memory requirements
        :disk: disk requirements
        :returns: dictionary of capable servers with the getServers() format

        """
        
        servers = self.getServers(domain)
        capable = dict()

        for server in servers.keys():
            res = self.getServerRes(domain, server)

            if res['cpu'] >= cpu and\
                    res['memory'] >= memory and\
                    res['disk'] >= disk:
                capable[server] = servers[server]

        return capable


    def isServerCapable(self, domain, server, cpu, memory, disk):
        """Determines if a server is capable to allocate resources for a
        certain domain.

        :domain: domain number
        :server: server node ID
        :cpu: cpu requirements
        :memory: memory requirements
        :disk: disk requirements
        :returns: True/False

        """
        serverRes = self.getServerRes(domain, server)
        return serverRes['cpu'] >= cpu and\
                serverRes['disk'] >= disk and\
                serverRes['memory'] >= memory


    def getPathDelay(self, domain, path):
        """Retrieves the path delay

        :domain: domain index
        :path: tuples list in the format of the NsMapper class search methods
            e.g.: [(node1, node2), (node2, node2), (node2, node3), ...]
        :returns: the path delay

        """
        delay = 0
        for nodesPair in path:
            if nodesPair[0] != nodesPair[1]:
                linkRes = self.getLnkRes(domain, nodesPair[0], nodesPair[1])
                delay += linkRes['delay']

        return delay


    @staticmethod
    def yieldMultiDomain(domains, meshDegree, fatTreeDegrees, foreignPods,
            meshLnkRes, fatLnkRes, servRes, meshProps=None, fatLnkProps=None,
            fatSrvProps=None):
        """Generates a MultiDomain based on the specified arguments

        :param domains: number of domains composing the graph
        :param meshDegree: connectivity degree of the mesh (0, 1)
        :param fatTreeDegrees: list of fat-tree degrees for each domain
        :param foreignPods: list of dictionaries with the foreign pods that
            each domain uses
        :param meshLnkRes: dictionary with mesh links resources thresholds
        :param fatLnkRes: dictionary with fat-tree link resources thresholds
        :param serverRes: dictionary with server resources thresholds
        :param meshProps: list of mesh proportions for resource sharing
        :param fatLnkProps: list of lists with fat tree shared link
            proportions
        :param fatSrvProps: list of lists with fat tree shared server
            proportions

        """

        multiDomain = MultiDomain()
        multiDomain.initialize(domains, meshDegree, fatTreeDegrees,
                foreignPods, meshLnkRes, fatLnkRes, servRes,
                meshProps=meshProps, fatLnkProps=fatLnkProps,
                fatSrvProps=fatSrvProps)
        
        return multiDomain
        

    @staticmethod
    def yieldRandMultiDomain():
        """Create a random MultiDomain graph instance
        :returns: Multidomain instance

        """
        properties = DG.DomainsGenerator.genProperties()

        multidomain = MultiDomain()
        multidomain.initialize(domains=properties['domains'],
                meshDegree=properties['meshDegree'],
                fatTreeDegrees=properties['fatTreeDegrees'],
                foreignPods=properties['foreignPods'],
                meshLnkRes=properties['meshLnkRes'],
                fatLnkRes=properties['fatLnkRes'],
                servRes=properties['servRes'])

        return multidomain
        


    def getProperties(self):
        """Obtains the set of properties from the MultiDomain instance
        :returns: dictionary with the set of properties

        """
        return {
            'domains': self.__domains,
            'meshDegree': self.__meshDegree,
            'fatTreeDegrees': self.__fatTreeDegrees,
            'foreignPods': self.__foreignPods,
            'meshLnkRes': self.__meshLnkRes,
            'fatLnkRes': self.__fatLnkRes,
            'servRes': self.__servRes
        }
        

    def setProperties(self, properties):
        """Sets the dictionary with the properties specified by argument

        :properties: dictionary with the same keys as the ones returned by
            getProperties() and the 'globalDomain' and 'domainsViews' are
            optional
        :returns: Nothing

        """
        self.__domains = properties['domains']
        self.__meshDegree = properties['meshDegree']
        self.__fatTreeDegrees = properties['fatTreeDegrees']
        self.__foreignPods = properties['foreignPods']
        self.__meshLnkRes = properties['meshLnkRes']
        self.__fatLnkRes = properties['fatLnkRes']
        self.__servRes = properties['servRes']

        if 'globalView' in properties.keys():
            self.__globalView = properties['globalView']
        if 'domainsViews' in properties.keys():
            self.__domainsViews = properties['domainsViews']


    def initialize(self, domains, meshDegree, fatTreeDegrees, foreignPods,
            meshLnkRes, fatLnkRes, servRes, meshProps=None, fatLnkProps=None,
            fatSrvProps=None):
        """Initializes a MultiDomain instance based on specified arguments

        :param domains: number of domains composing the graph
        :param meshDegree: connectivity degree of the mesh (0, 1)
        :param fatTreeDegrees: list of fat-tree degrees for each domain
        :param foreignPods: list with foreign pods dictionary.
        :param meshLnkRes: dictionary with mesh links resources thresholds
        :param fatLnkRes: dictionary with fat-tree link resources thresholds
        :param serverRes: dictionary with server resources thresholds
        :param meshProps: list of mesh proportions for resource sharing
        :param fatLnkProps: list of lists with fat tree shared link
            proportions
        :param fatSrvProps: list of lists with fat tree shared server
            proportions
        :returns: Nothing

        """

        if len(fatTreeDegrees) != domains:
            raise UnboundLocalError('number of domains don\'t match with\
 number of provided degrees')
        else:
            self.__domains = domains
            self.__meshDegree = meshDegree
            self.__fatTreeDegrees = fatTreeDegrees
            self.__foreignPods = foreignPods
            self.__meshLnkRes = meshLnkRes
            self.__fatLnkRes = fatLnkRes
            self.__servRes = servRes

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
                foreignPods[domain]))
        generator.issueMeshBw(globalView, domainsViews, shareProps=meshProps)
        generator.issueFatRes(globalView, domainsViews,
                lnkProps=fatLnkProps, srvProps=fatSrvProps)

        self.__globalView = globalView
        self.__domainsViews = domainsViews


    def write(self, storedName, absBasePath=None):
        """Stores the domains and global view graph

        :storedName: name of the directory that will contain the graph views
        :absBasePath: path under which the MultiDomain will be stored
        :returns: Nothing

        """
        basePath = graphsAbsPath + '/' + storedName + '/' if not absBasePath\
                else absBasePath + '/' + storedName + '/'
        if not os.path.exists(basePath):
            os.makedirs(basePath)

        nx.write_gml(self.__globalView, basePath + '/global.gml')
        
        for domain in range(len(self.__domainsViews)):
            nx.write_gml(self.__domainsViews[domain], basePath + 'domain' +
                    str(domain) + '.gml')

        with open(basePath + 'metadata.json', 'w') as f:
             json.dump(self.getProperties(), f)


    @staticmethod
    def read(storedName, absBasePath=None):
        """Generates a multidomain instance based on the global and domain
        graph views located under the graphs directory with storedName

        :storedName: name of the directory that will contain the graph views
        :absBasePath: path under which the MultiDomain will be stored
        :returns: MultiDomain instance

        """
        basePath = graphsAbsPath + '/' + storedName + '/' if not absBasePath\
                else absBasePath + '/' + storedName + '/'

        with open(basePath + 'metadata.json', 'r') as f:
            properties = json.load(f)

        domainsViews = []
        for domain in range(properties['domains']):
            domainsViews.append(nx.read_gml(basePath + 'domain' + str(domain)\
                + '.gml'))

        globalView = nx.read_gml(basePath + 'global.gml')

        properties['globalView'] = globalView
        properties['domainsViews'] = domainsViews

        multiDomain = MultiDomain()
        multiDomain.setProperties(properties)

        return multiDomain

        
    def incrLnkResource(self, domain, A, B, resource, incr):
        """Increments positively/negatively the (A,B) link resource

        :domain: domain number
        :A: first node of the link
        :B: second node of the link
        :resource: resource key
        :incr: integer increment
        :returns: Boolean indicating if the increment was successfull

        """
        
        if domain > self.__domains - 1:
            return False

        if resource != 'bw' and resource != 'delay':
            return False

        # Get the domain link (if it has it)
        domainView = self.__domainsViews[domain]
        if domainView.has_edge(A, B):
            globalRes = self.__globalView[A][B]
            domainRes = domainView[A][B]

            # Not enough resources available
            if incr < 0 and domainRes['res'][resource] < abs(incr):
                return False
            
            self.__globalView[A][B]['res'][resource] += incr
            domainView[A][B]['res'][resource] += incr
        else:
            return False

        return True
            

    def incrServerResource(self, domain, A, resource, incr):
        """Increments positively/negatively the server A resource

        :domain: domain number
        :A: server node
        :resource: resource key
        :incr: integer increment
        :returns: Boolean indicating if the increment was successfull

        """
        
        if domain > self.__domains - 1:
            return False

        if resource != 'memory' and resource != 'cpu' and resource != 'disk':
            return False

        # Get the server (if it has it)
        domainView = self.__domainsViews[domain]
        if domainView.has_node(A):
            globalRes = nx.get_node_attributes(self.__globalView, 'res')[A]
            domainRes = nx.get_node_attributes(domainView, 'res')[A]

            # Not enough resources available
            if incr < 0 and domainRes[resource] < abs(incr):
                return False
            
            globalRes[resource] += incr
            domainRes[resource] += incr

            nx.set_node_attributes(self.__globalView, 'res', {A: globalRes})
            nx.set_node_attributes(domainView, 'res', {A: domainRes})
        else:
            return False

        return True


    def getNodeNeighs(self, domain, node):
        """Obtains the neighbors of a node contained in a certain domain

        :domain: domain number
        :node: node ID contained in the domain
        :returns: a list of nodes with its resources, None in case of error

        """
        
        if domain > len(self.__domainsViews):
            return None

        domView = self.__domainsViews[domain]
        
        return domView.neighbors(node)


if __name__ == '__main__':
    # md = MultiDomain.yieldRandMultiDomain()
    md = MultiDomain()
    print md

