import heapq
import networkx as nx
import random
import sys
from sets import Set
from ResourcesWatchDog import ResourcesWatchDog as WD
from NS import NS
from MultiDomain import MultiDomain as MD
from NsMapping import NsMapping as NSm

class NsMapper(object):

    """A class to map NS chains in the MultiDomain graphs"""

    def __init__(self, multiDomain):
        """Initialize a NS mapper with the multi-domain graph where it will
        perform the mapping algorithms

        :multiDomain: MultiDomain instance

        """
        self.__multiDomain = multiDomain
        self.__watchDogs = []

        # Node types integers
        self.__gwType = 1
        self.__coreType = 2
        self.__aggType = 3
        self.__edgeType = 4
        self.__serverType = 5

        # Cache variables
        self.__cores = None
        self.__aggregates = None
        self.__edges = None
        

    def __nodeType(self, node):
        """Obtains the type of node within the MultiDomain.

        :node: node number/ID
        :returns: the node type as the integers defined as properties

        """
        if 0 <= node <= self.__multiDomain.getProperties()['domains'] - 1:
            return self.__gwType

        # Check if it is a core
        if self.__cores == None: 
            self.__cores = self.__multiDomain.getCores()
        elif node in self.__cores:
            return self.__coreType

        # Check if it is an aggregate
        elif self.__aggregates == None:
            self.__aggregates = self.__multiDomain.getAggregates()
        elif node in self.__aggregates:
            return self.__aggType

        # Check if it is an edge
        elif self.__edges == None:
            self.__edges = self.__multiDomain.getEdges()
        elif node in self.__edges:
            return self.__edgeType

        return self.__serverType


    def __isForbidden(self, typesList):
        """Checks if there is a forbidden move in the last visited nodes.

        :typesList: list of node types 
        :returns: True/False

        """
        isForbidden = False

        if len(typesList) >= 3:
            # Core, GW, core
            if typesList[-3] == self.__coreType and\
                    typesList[-2] == self.__gwType and\
                    typesList[-1] == self.__coreType:
                isForbidden = True
            # Agg, edge, agg
            elif typesList[-3] == self.__aggType and\
                    typesList[-2] == self.__edgeType and\
                    typesList[-1] == self.__aggType:
                isForbidden = True
            # Core, agg, core
            elif typesList[-3] == self.__coreType and\
                    typesList[-2] == self.__aggType and\
                    typesList[-1] == self.__coreType:
                isForbidden = True

        return isForbidden


    def getLastWatchDog(self):
        """Retrieves the last watch dog in the list
        :returns: ReourcesWatchDog instance, None if there are no watchdogs

        """
        return None if len(self.__watchDogs) < 1 else self.__watchDogs[-1]


    def constrainedDijkstra(self, domain, serverS, serversE, delay, bw):
        """Finds a path acomplishing network constraints from the start server
        serverS to one of the multiple end serversE. Aggregated delay is
        ensured to be less than the given as parameter, and the bw is ensured
        along the path.
        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE)], delay]
        """
        
        delays = { serverS: 0 }
        prev = {}
        Q = []
        heapq.heappush(Q, (0, serverS))

        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        # Main loop
        while Q:
            nodeDelay, node = heapq.heappop(Q)

            # Lower node delay is higher than the limit => impossible to map
            # TODO - I think this situation isn't encountered: edges filtered
            if nodeDelay > delay:
                return None

            # Found end server (iterate through prevs to obtain path)
            if node in serversE:
                path = []
                filledPath = False
                
                while not filledPath:
                    path.insert(0, (prev[node], node))
                    node = prev[node]
                    if node == serverS:
                        filledPath = True
                
                return path, nodeDelay

            neighbors = self.__multiDomain.getNodeNeighs(domain, node)
            for neighbor in neighbors:
                linkRes = self.__multiDomain.getLnkRes(domain, node, neighbor)

                # Check if link satisfies requirements
                if linkRes['bw'] >= bw\
                       and delays[node] + linkRes['delay'] <= delay:

                    # New neighbor
                    if neighbor not in delays:
                        delays[neighbor] = delays[node] + linkRes['delay']
                        heapq.heappush(Q, (delays[neighbor], neighbor))
                        prev[neighbor] = node

                    # Already visited, better path
                    elif delays[node] + linkRes['delay'] < delays[neighbor]:
                        neighIdx = Q.index((delays[neighbor], neighbor))
                        delays[neighbor] = delays[node] + linkRes['delay']
                        Q[neighIdx] = (delays[neighbor], neighbor)
                        heapq.heapify(Q)
                        prev[neighbor] = node

        return None, None


    def randomWalk(self, domain, serverS, serversE, delay, bw):
        """Performs a random walk to find a path from serverS to a serverE
        under delay and bw constraints.

        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE)], delay]

        """
        path = []
        inPath = { serverS: True }
        keepWalking = True
        node = serverS
        aggDelay = 0

        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        while keepWalking:
            neighbors = self.__multiDomain.getNodeNeighs(domain, node)
            neighbors = filter(lambda neigh: neigh not in inPath, neighbors)
            random.shuffle(neighbors)

            # Search a reachable neighbor
            foundNeigh = False
            neighbor = None
            i = 0
            while not foundNeigh and i < len(neighbors):
                neighbor = neighbors[i]
                linkRes = self.__multiDomain.getLnkRes(domain, node, neighbor)
                if linkRes['bw'] >= bw and delay >= linkRes['delay'] +\
                        aggDelay:
                    foundNeigh = True
                    aggDelay += linkRes['delay']
                    inPath[neighbor] = True
                i += 1

            # Stop if neighbor inside final ones or no reachable neighbor
            keepWalking = False if not foundNeigh or neighbor in serversE\
                    else True
            path += [(node, neighbor)] if foundNeigh else []
            node = neighbor

        # Check if final server have been reached
        if len(path) < 1 or path[-1][-1] not in serversE:
            path = None

        return path, aggDelay


    def smartRandomWalk(self, domain, serverS, serversE, delay, bw,
            depth=None):
        """Performs a random walk to find a path from serverS to a serverE
        under delay and bw constraints. This random walk performs backtracking
        operations to avoid deadend roads

        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :depth: parameter that controls the recursion depth
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE)], delay]

        """
        def recursive(node, aggDelay, chain, st='', depth=None):
            """Recursive function to perform the backtracking approach of the
            random walks.

            :node: starting node
            :aggDelay: aggregated delay in the current path search
            :chain: set with current chain composed
            :st: string to be concatenated in debug printing
            :depth: parameter that controls the recursion depth
            :returns: [None, None] if no mapping was founded,
                [ [], delay ] if node==serverE,
                [(serverS, node1), ..., (serverN, serverE), delay]

            """
            if node in serversE:
                return [], aggDelay
            elif depth == 0:
                return None, None

            # Get neighbors not inside current chain
            neighbors = self.__multiDomain.getNodeNeighs(domain, node)
            neighbors = filter(lambda neigh: neigh not in chain, neighbors)
            random.shuffle(neighbors)

            for neighbor in neighbors:
                linkRes = self.__multiDomain.getLnkRes(domain, node, neighbor)
                if linkRes['bw'] >= bw and delay >= linkRes['delay'] +\
                        aggDelay:
                    # Link requirements ok, keep recursion!
                    nextChain = Set(chain)
                    nextChain.add(neighbor)
                    newDepth = None if not depth else depth - 1
                    path, pathDelay = recursive(neighbor,
                            aggDelay + linkRes['delay'], nextChain, st + '  ',
                            depth=newDepth)

                    if path != None:
                        return [(node, neighbor)] + path, pathDelay

            return None, None

        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        return recursive(serverS, 0, Set([serverS]), depth=depth)


    def cutoffSmartRandomWalk(self, domain, serverS, serversE, delay, bw,
            depth=None):
        """Performs a random walk to find a path from serverS to a serverE
        under delay and bw constraints. This random walk performs backtracking
        operations to avoid deadend roads. As well it avoids forbidden moves
        to speed up the search.

        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :depth: parameter that controls the recursion depth
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE)], delay]

        """
        reached = dict()

        def recursive(node, aggDelay, chain, nodesList, typesList, st='',
                depth=None):
            """Recursive function to perform the backtracking approach of the
            random walks.

            :node: starting node
            :aggDelay: aggregated delay in the current path search
            :chain: set with current chain composed
            :nodesList: list with the nodes visited in order
            :typesList: a list with the node types of the chain
            :st: string to be concatenated in debug printing
            :depth: parameter that controls the recursion depth
            :returns: [None, None] if no mapping was founded,
                [ [], delay ] if node==serverE,
                [(serverS, node1), ..., (serverN, serverE), delay]

            """
            # print '  nodesList: ' + str(nodesList)
            if node in serversE:
                return [], aggDelay
            elif depth == 0:
                return None, None

            # Get neighbors not inside current chain, and give priority to ones
            # that are not GWs
            # print 'domain: ' + str(domain)
            neighbors = self.__multiDomain.getNodeNeighs(domain, node)
            gws, others, othersTypes, gwsTypes = [], [], [], []
            for neigh in neighbors:
                if neigh not in chain:
                    neighType = self.__nodeType(neigh)
                    if neighType == self.__gwType:
                        gws.append(neigh)
                        gwsTypes.append(neighType)
                    else:
                        others.append(neigh)
                        othersTypes.append(neighType)

            neighbors = others + gws
            neighTypes = othersTypes + gwsTypes
            targetNeighs, targetTypes = [], []

            # print ' neighbors: ' + str(neighbors)

            # Refreshed reached and fill target nodes
            for neighbor, neighType in zip(neighbors, neighTypes):
                isForbidden = self.__isForbidden(typesList + [neighType])

                if not isForbidden:
                    linkRes = self.__multiDomain.getLnkRes(domain, node,
                            neighbor)
                    beVisited = neighbor not in reached or\
                        (neighbor in reached and\
                        reached[neighbor] > aggDelay + linkRes['delay'])
                    
                    # print 'linkRes[bw]=' + str(linkRes['bw'])
                    # print 'bw=' + str(bw)
                    # print 'linkRes[delay]=' + str(linkRes['delay'])
                    # print 'delay=' + str(delay)
                    # print '--------------------------------------------'

                    if linkRes['bw'] >= bw and delay >= linkRes['delay'] +\
                            aggDelay and beVisited:
                        # Link requirements ok, keep recursion!
                        reached[neighbor] = aggDelay + linkRes['delay']
                        targetNeighs += [neighbor]
                        targetTypes += [neighType]

            # Run recursively through target nodes
            for neighbor, neighType in zip(targetNeighs, targetTypes):
                nextChain = Set(chain)
                nextChain.add(neighbor)
                newDepth = None if not depth else depth - 1
                path, pathDelay = recursive(neighbor,
                        aggDelay + linkRes['delay'], nextChain,
                        nodesList + [neighbor],
                        typesList + [neighType], st + '  ',
                        depth=newDepth)

                if path != None:
                    return [(node, neighbor)] + path, pathDelay

            return None, None


        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        serverSType = self.__nodeType(serverS)
        return recursive(serverS, 0, Set([serverS]), [serverS],
                [serverSType], depth=depth)


    def BFS(self, domain, serverS, serversE, delay, bw, depth=None):
        """Performs a BFS to find possible paths from serverS to any serverE
        under the delay and bw requirements.

        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :depth: specify limit depth for searching
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE), delay]

        """
        toVisit = [(serverS, 0, [], Set([serverS]))]
        keepVisiting = True
        i = 0

        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        while keepVisiting:
            nextToVisit = []
            keepVisiting = False if depth != None and i > depth else True

            # Visit and add neighbors
            while len(toVisit) > 0 and keepVisiting:
                # Get curr node and neighbors
                node, aggDelay, chain, chainSet = toVisit[0]
                if node in serversE:
                    return chain, aggDelay
                del toVisit[0]
                neighbors = self.__multiDomain.getNodeNeighs(domain, node)
                neighbors = filter(lambda neigh: neigh not in chainSet,
                        neighbors)

                # Insert neighbors
                for neighbor in [n for n in neighbors if n not in chainSet]:
                    linkRes = self.__multiDomain.getLnkRes(domain, node, neighbor)
                    if linkRes['bw'] >= bw and\
                            aggDelay + linkRes['delay'] <= delay:
                        newChainSet = Set(chainSet)
                        newChainSet.add(neighbor)
                        nextToVisit += [(neighbor,
                            aggDelay + linkRes['delay'],
                            list(chain) + [(node, neighbor)], newChainSet)]

            toVisit = nextToVisit
            keepVisiting = len(toVisit) > 0
            i += 1
    
        return None, None


    def BFScutoff(self, domain, serverS, serversE, delay, bw, depth=None):
        """Performs a BFS to find possible paths from serverS to any serverE
        under the delay and bw requirements. This implementetion prevents the
        algorithm going through forbidden moves.

        :domain: domain number
        :serverS: starting server id
        :serversE: possible ending servers ids in a dictionary {idA: _, ...}
        :delay: required delay for the path (the final path will have less)
        :bw: required bw for the path (each link will have enough bw)
        :depth: specify limit depth for searching
        :returns: [None, None] if no mapping was founded,
            [ [(serverS, node1), ..., (serverN, serverE), delay]

        """
        serverSType = self.__nodeType(serverS)
        toVisit = [(serverS, 0, [], [serverSType], Set([serverS]))]
        keepVisiting = True
        i = 0
        reached = { serverS: 0 }

        # Check if serverS is within serversE
        if serverS in serversE:
            return [(serverS, serverS)], 0

        while keepVisiting:
            nextToVisit = []
            keepVisiting = False if depth != None and i > depth else True

            # Visit and add neighbors
            while len(toVisit) > 0 and keepVisiting:
                # Get curr node and neighbors
                node, aggDelay, chain, types, chainSet = toVisit[0]
                if node in serversE:
                    return chain, aggDelay
                del toVisit[0]
                neighbors = self.__multiDomain.getNodeNeighs(domain, node)
                neighbors = filter(lambda neigh: neigh not in chainSet,
                        neighbors)

                # Insert neighbors
                for neighbor in [n for n in neighbors if n not in chainSet]:
                    neighType = self.__nodeType(neighbor)
                    isForbidden = self.__isForbidden(types + [neighType])

                    if not isForbidden:
                        linkRes = self.__multiDomain.getLnkRes(domain, node,
                                neighbor)
                        beVisited = neighbor not in reached or\
                            (neighbor in reached and\
                            reached[neighbor] > aggDelay + linkRes['delay'])

                        if linkRes['bw'] >= bw and\
                                aggDelay + linkRes['delay'] <= delay and\
                                beVisited:
                            reached[neighbor] = aggDelay + linkRes['delay']
                            newChainSet = Set(chainSet)
                            newChainSet.add(neighbor)
                            nextToVisit += [(neighbor,
                                aggDelay + linkRes['delay'],
                                list(chain) + [(node, neighbor)],
                                types + [neighType], newChainSet)]

            toVisit = nextToVisit
            keepVisiting = len(toVisit) > 0
            i += 1
    
        return None, None


    def greedy(self, domain, entryServer, ns, method='Dijkstra', depth=None):
        """Performs a greedy mapping for the NS chain passed as argument

        :domain: entry domain for the NS chain
        :entryServer: server entry point for the NS
        :ns: NS chain instance
        :method: search method between VNFs - ['Dijkstra', 'BFS',
            'BFScutoff', 'backtracking', 'backtrackingCutoff', 'random']
        :depth: maximum search depth for 'BFS'
        :returns: NsMapping instance or None in case the mapping couldn't be
            performed

        """
        ns.initIter()
        vnfS = ns.currIterId()
        serverS = entryServer
        nextVNFs = ns.iterNext()
        watchDog = WD(self.__multiDomain, ns, domain)
        nsMapping = NSm(ns)

        while nextVNFs or vnfS != 'end':
            for vnf in nextVNFs:
                res = ns.getVnf(vnf)
                link = ns.getLink(vnfS, vnf)

                # VNF already mapped, force path to reach mapped server
                capable = None
                mappedServer = nsMapping.getServerMapping(vnf)
                if mappedServer != None:
                    capable = { mappedServer: True }
                else:
                    capable = self.__multiDomain.getCapableServers(domain,
                            res['cpu'], res['memory'], res['disk'])
                    # print '  serverS in capable?: ' + str(serverS in capable)
                    # print '  capable servers: ' + str(len(capable))

                # If last VNF server can contain it, place it there
                path, pathDelay = None, 0
                if method == 'Dijkstra':
                    path, pathDelay = self.constrainedDijkstra(domain,
                            serverS, capable, link['delay'], link['bw'])
                elif method == 'BFS':
                    path, pathDelay = self.BFS(domain, serverS,
                            capable, link['delay'], link['bw'],
                            depth=depth)
                elif method == 'BFScutoff':
                    path, pathDelay = self.BFScutoff(domain, serverS,
                            capable, link['delay'], link['bw'],
                            depth=depth)
                elif method == 'backtracking':
                    path, pathDelay = self.smartRandomWalk(domain, serverS,
                            capable, link['delay'], link['bw'],
                            depth=depth)
                elif method == 'backtrackingCutoff':
                    path, pathDelay = self.cutoffSmartRandomWalk(domain,
                            serverS, capable, link['delay'], link['bw'],
                            depth=depth)
                else:
                    path, pathDelay = self.randomWalk(domain, serverS,
                            capable, link['delay'], link['bw'])

                if not path:
                    watchDog.unWatch() # free previously allocated resources
                    return None
                else:
                    # print '  mapped vnf: ' + str(vnf)
                    nsMapping.setPath(vnfS, vnf, path)
                    nsMapping.setLnkDelayAndRefresh(vnfS, vnf, pathDelay)
                    watchDog.watch(vnfS, vnf, path)
 
            # Next VNFs
            vnfS = ns.currIterId()
            serverS = nsMapping.getServerMapping(vnfS)
            if vnfS != 'end':
                nextVNFs = ns.iterNext()

        # Add the watch dog to the list of mapped NSs
        self.__watchDogs.append(watchDog)

        return nsMapping


    def popurri(self, domain, entryServer, ns, method='Dijkstra', depth=None):
        """Popurri mapping is performed by choosing randomly servers and
        placing VNFs in those servers. Then a routing is performed between the
        chosen servers.

        :domain: entry domain for the NS chain
        :entryServer: server entry point for the NS
        :ns: NS chain instance
        :method: search method between VNFs - ['Dijkstra', 'BFS',
            'backtracking', 'random']
        :depth: maximum search depth for 'BFS'
        :returns: [(node1, node2), ..., (nodeN, nodeN+1)] path or empty list

        """
        pass





    def __reviseBlocks(self, domain, ns, vnf, prevServer, newServer, blocks):
        """TABU SEARCH AUXILIARY METHOD
        It revises the blocked movements after the remapping of the vnf from a
        prevServer to a newServer. It refreshes whether other vnfs will be able
        to use the freed server and the new server where the vnf is mapped.

        :domain: entry domain for the NS chain
        :ns: NS chain instance
        :vnf: VNF id
        :prevServer: previously used server ID
        :newServer: newly used server ID
        :blocks: dictionary with blocking movements
        :returns: Nothing

        """
        # Refresh capabilities
        origIterId = ns.currIterId()
        ns.initIter()
        ns.iterNext()
        currVnf = ns.currIterId()
        while currVnf != 'end':
            vnfRes = ns.getVnf(currVnf)
            if currVnf != vnf:
                if prevServer not in blocks[currVnf] and\
                    self.__multiDomain.isServerCapable(domain,
                            prevServer, vnfRes['cpu'],
                            vnfRes['memory'], vnfRes['disk']):
                    blocks[currVnf][prevServer] = False
                if newServer in blocks[currVnf] and not\
                    self.__multiDomain.isServerCapable(domain,
                            newServer, vnfRes['cpu'],
                            vnfRes['memory'], vnfRes['disk']):
                    del blocks[currVnf][newServer]

            ns.iterNext()
            currVnf = ns.currIterId()
        ns.setIterIdx(origIterId)


    def tabu(self, domain, entryServer, ns, block, iters, initial='greedy',
            method='Dijkstra', depth=None):
        """Performs a tabu search to map the NS in the underneath domain view.

        :domain: entry domain for the NS chain
        :entryServer: server entry point for the NS
        :ns: NS chain instance
        :block: number of rounds the last VNF placement will be blocked
        :iters: number of iterations over the whole the NS chain
        :initial: method used to obtain the initial solution
        :method: search method between VNFs - ['Dijkstra', 'BFS',
            'BFScutoff', 'backtracking', 'backtrackingCutoff', 'random']
        :depth: maximum search depth for 'BFS'
        :returns: NsMapping instance or None in case of error

        """
        initialSol = None
        mappings = None
        blocks = dict()
        iterators = dict()
        currSol, bestDelay = None, None
        vnfsNum = ns.getVNFsNumber()
        currVnf = None
        currServer = None
        nsMapping, bestNsMapping = None, None

        if initial == 'greedy':
            nsMapping = self.greedy(domain, entryServer, ns, method=method,
                    depth=depth)
            if not nsMapping:
                return None
            bestNsMapping = nsMapping.copy()
        else:
            # TODO - other methods to retrieve an initial solution
            pass

        if initialSol == []:
            return []

        # Initialize blocking and iterators dictionaries
        ns.initIter()
        ns.iterNext()
        vnf = ns.currIterId()
        while vnf != 'end':
            vnfRes = ns.getVnf(vnf)
            capable = self.__multiDomain.getCapableServers(domain,
                    vnfRes['cpu'], vnfRes['memory'], vnfRes['disk'])
            blocks[vnf] = dict()
            for server in capable:
                if server != nsMapping.getServerMapping(vnf):
                    blocks[vnf][server] = False
            blocks[vnf][nsMapping.getServerMapping(vnf)] = block

            ns.iterNext()
            vnf = ns.currIterId()

        ###############
        ## Main loop ##
        ###############
        ns.initIter()
        for _ in range(iters * vnfsNum):
            # Obtain current VNFs to force their new mapping
            ns.iterNext()
            currVnf = ns.currIterId()
            if currVnf == 'end':
                ns.initIter()
                ns.iterNext()
                currVnf = ns.currIterId()
            currServer = nsMapping.getServerMapping(currVnf)

            # Obtain info. to perform new mapping
            currCapables = dict()
            for server in blocks[currVnf].keys():
                if not blocks[currVnf][server]:
                    currCapables[server] = True

            # Obtain servers where previous vnfs are mapped
            prevMappings = []
            prevDelays = []
            prevServers = []
            prevVnfs = ns.prevVNFs(currVnf)
            for vnf in prevVnfs:
                prevServers += [nsMapping.getServerMapping(vnf)
                        if vnf != 'start' else entryServer]


            ###################
            ## Previous VNFs ##
            ###################
            keepSearch, i = True, 0
            while keepSearch and i < len(prevVnfs):
                prevVnf = prevVnfs[i]
                prevServer = prevServers[i]
                linkRes = ns.getLink(prevVnf, currVnf)

                # Perform the new mapping
                path, pathDelay = None, None
                if method == 'Dijkstra':
                    path, pathDelay = self.constrainedDijkstra(domain,
                            prevServer, currCapables, linkRes['delay'],
                            linkRes['bw'])
                elif method == 'BFS':
                    path, pathDelay = self.BFS(domain, prevServer,
                            currCapables, linkRes['delay'], linkRes['bw'],
                            depth=depth)
                elif method == 'BFScutoff':
                    path, pathDelay = self.BFScutoff(domain, prevServer,
                            currCapables, linkRes['delay'], linkRes['bw'],
                            depth=depth)
                elif method == 'backtracking':
                    path, pathDelay = self.smartRandomWalk(domain, prevServer,
                             currCapables, linkRes['delay'], linkRes['bw'],
                             depth=depth)
                elif method == 'backtrackingCutoff':
                    path, pathDelay = self.cutoffSmartRandomWalk(
                            domain, prevServer, currCapables,
                            linkRes['delay'], linkRes['bw'], depth=depth)
                elif method == 'random':
                    path, pathDelay = self.randomWalk(domain, prevServer,
                            currCapables, linkRes['delay'], linkRes['bw'])

                if path == None:
                    keepSearch = False
                else:
                    currCapables = [path[-1][-1]]
                    prevMappings.append(path)
                    prevDelays.append(pathDelay)
                    i += 1

            # currCapables=[endServer] if a path prev---curr has been found
            mappedServer = None
            if len(currCapables) == 1:
                mappedServer = currCapables[0]
                blocks[currVnf][mappedServer] = block + 1

            # Search path from new vnf to next ones
            prevSuccess = len(prevMappings) == len(prevVnfs) and\
                    None not in prevMappings
            afterVnfs = ns.getNextVNFs(currVnf)
            afterMappings, afterDelays, afterServers = [], [], []

            if prevSuccess and afterVnfs != []:
                # Obtain servers where next vnfs are mapped
                for vnf in afterVnfs:
                    afterServers += [nsMapping.getServerMapping(vnf)]

                ################
                ## After VNFs ##
                ################
                keepSearch, i = True, 0
                while keepSearch and i < len(afterVnfs):
                    linkRes = ns.getLink(currVnf, afterVnfs[i])

                    afterPath = None
                    if method == 'Dijkstra':
                        afterPath, afterDelay = self.constrainedDijkstra(
                                domain, mappedServer, [afterServers[i]],
                                linkRes['delay'], linkRes['bw'])
                    elif method == 'BFS':
                        afterPath, afterDelay = self.BFS(domain, mappedServer,
                                [afterServers[i]], linkRes['delay'],
                                linkRes['bw'], depth=depth)
                    elif method == 'BFScutoff':
                        afterPath, afterDelay = self.BFScutoff(domain,
                                mappedServer, [afterServers[i]], linkRes['delay'],
                                linkRes['bw'], depth=depth)
                    elif method == 'backtracking':
                        afterPath, afterDelay = self.smartRandomWalk(domain,
                                mappedServer, [afterServers[i]],
                                linkRes['delay'], linkRes['bw'], depth=depth)
                    elif method == 'backtrackingCutoff':
                        afterPath, afterDelay = self.cutoffSmartRandomWalk(
                                domain, mappedServer, [afterServers[i]],
                                linkRes['delay'], linkRes['bw'], depth=depth)
                    elif method == 'random':
                        afterPath, afterDelay = self.randomWalk(domain,
                                mappedServer, [afterServers[i]],
                                linkRes['delay'], linkRes['bw'])
                    
                    if afterPath == None:
                        keepSearch = False
                    else:
                        afterMappings.append(afterPath)
                        afterDelays.append(afterDelay)
                        i += 1

            # All remappings successfully performed
            if prevSuccess and len(afterMappings) == len(afterVnfs):
                
                # Update resources usage
                lastWatchDog = self.getLastWatchDog()
                for prevVnf, prevMap in zip(prevVnfs, prevMappings):
                    lastWatchDog.changeConnection(prevVnf, currVnf, prevMap)
                    nsMapping.setPath(prevVnf, currVnf, prevMap)
                for afterVnf, afterMap in zip(afterVnfs, afterMappings):
                    lastWatchDog.changeConnection(currVnf, afterVnf, afterMap)
                    nsMapping.setPath(currVnf, afterVnf, afterMap)

                # Update mapping object
                nsMapping.changeVnfMapping(currVnf, prevVnfs, afterVnfs,
                        prevDelays, afterDelays)
                if nsMapping.getDelay() < bestNsMapping.getDelay():
                    # print 'MEJORA: ' + str(bestNsMapping.getDelay()) +\
                    #         ' better than: ' + str(nsMapping.getDelay())
                    # sys.stdout.flush()
                    nsMapping.notifyImprovement()
                    bestNsMapping = nsMapping.copy()

                # New server may not be used by other vnfs, previous may yes
                self.__reviseBlocks(domain, ns, currVnf, currServer,
                        mappedServer, blocks)

                blocks[currVnf][mappedServer] = block + 1

            # Decrement blocking counters
            for vnf in blocks.keys():
                for server in blocks[vnf].keys():
                    blocked = blocks[vnf][server]
                    blocks[vnf][server] = blocked - 1 if blocked else False

        return bestNsMapping


    # TODO - is this neccesary?
    def modifyMappedPath(self, ns, vnf, server, mapping,
            path, prevPath, afterPath):
        """Obtain a new mapping path taking into account that vnf is placed
        under the new server.

        :ns: NS instance
        :vnf: VNF index that have been remapped
        :server: new server where the vnf is placed
        :mapping: dictionary with vnf server mappings { vnf1: serverA, ... }
        :path: list with ns placed path [(1, 2), (2, 4), (4, 6), (6, 6), ...]
        :prevPath: nodes path until the VNF server is reached
        :afterPath: nodes path to reach next mapped server from VNF server
        :returns: the path corresponding to the new mapping
        :raise: UnboundLocalError in case previous and after paths are not ok

        """
        vnfs = len(mapping.keys())
        if prevPath[-1][-1] != server:
            raise UnboundLocalError('modifyMappedPath: last node in prevPath\
 is not the new mapped server')
        elif vnf < vnfs and afterPath[0][0] != server:
            raise UnboundLocalError('modifyMappedPath: first node in afterPath\
 is not the new mapped server')
        elif vnf > 1 and mapping[vnf - 1] != prevPath[0][0]:
            raise UnboundLocalError('modifyMappedPath:: first node in prevPath\
 is not the server where previous vnf is mapped')
        elif vnf < vnfs and mapping[vnf + 1] != afterPath[-1][-1]:
            raise UnboundLocalError('modifyMappedPath:: last node in\
 afterPath is not the server where next vnf is mapped')

        # Aux variables
        pathIdx = 0
        positions = dict()
        iterIdx = ns.currIterId()
        ns.initIter()
        ns.iterNext()
        currVnf = ns.currIterId()

        # Obtain the positions of each placement within the path chain
        while currVnf != 'end' and currVnf != vnf + 2:
            while mapping[currVnf] != path[pathIdx][-1]:
                pathIdx += 1

            positions[currVnf] = pathIdx
            ns.iterNext()
            currVnf = ns.currIterId()

        # Copy until previous path
        newPath = []
        if vnf > 1:
            newPath = path[0:positions[vnf - 1] + 1]
    
        # Copy new previous and after paths
        newPath += prevPath + afterPath

        # Copy remaining path tail
        if vnf != vnfs:
            newPath += path[positions[vnf + 1]+1:]

        return newPath


    def freeMappings(self):
        """Frees all the resources mapped to NSs
        :returns: Nothing

        """
        for watchDog in self.__watchDogs:
            watchDog.unWatch()


