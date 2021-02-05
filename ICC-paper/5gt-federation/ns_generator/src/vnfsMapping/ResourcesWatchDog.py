from NS import NS
from MultiDomain import MultiDomain as MD

class ResourcesWatchDog(object):

    """Class to monitor the resources consumption during mapping"""

    def __init__(self, multiDomain, ns, domain):
        """Initializes the watch dog to with the multiDomain, NS and domain
        resources that is going to take care of

        :multiDomain: MultiDomain instance
        :ns: NS instance
        :domain: domain index

        """
        self.__multiDomain = multiDomain
        self.__ns = ns
        self.__domain = domain
        self.__watchingPaths = []
        self.__watchingVnfs = dict()
        

    def watch(self, vnf1, vnf2, path):
        """Consumes the resources along the path between vnf1 and vnf2, and
        the server resources for vnf2. ndB in the path is the server where
        vnf2 resources are located. ndB in the path is the server where
        vnf2 resources are located.
        WARNING: vnf1 and vnf2 must be consecutive vnfs

        :vnf1: id of vnf1
        :vnf2: id of vnf2
        :path: links between both vnfsvnfs  [(nd1, nd2), ..., (ndA, ndB)]
            if vnf2 is placed under same server as vnf2: [(nd1, nd1)]
        :returns: Nothing

        """
        nsLinkBw = self.__ns.getLink(vnf1, vnf2)['bw']

        # Decrease available bandwidth (if vnf1 and vnf2 under dif servers)
        if path[-1][0] != path[-1][-1]:
            for (nodeA, nodeB) in path:
                self.__multiDomain.incrLnkResource(self.__domain, nodeA,
                    nodeB, 'bw', -1 * nsLinkBw)

        # Alloc server resources
        if vnf2 not in self.__watchingVnfs:
            server = path[-1][-1]
            vnfRes = self.__ns.getVnf(vnf2)
            self.__incrServVNFsRes(vnfRes, server, decrease=True)
            self.__watchingVnfs[vnf2] = server

        # Add the watched path and server (vnf2)
        self.__watchingPaths.append((vnf1, vnf2, path))


    def changeConnection(self, vnf1, vnf2, newPath):
        """Changes the connection between vnf1 and vnf2, and links them using
        the newPath. It releases old path link resources, and consumes the new
        ones.
        WARNING: vnf1 and vnf2 must be consecutive vnfs
        WARNING: vnf2 should already be mapped to a server

        :vnf1: id of vnf1
        :vnf2: id of vnf2
        :newPath: links between both vnfs [(nd1, nd2), ..., (ndA, ndB)]
            if vnf2 is placed under same server as vnf2: [(nd1, nd1)]
        :returns: None in case there are no vnf1 and vnf2 connection being
            watched. True if link change can be performed

        """
        i, notFound, path = 0, True, None
        while notFound and i < len(self.__watchingPaths):
            vnfA, vnfB, path = self.__watchingPaths[i]
            notFound = vnfA != vnf1 and vnfB != vnf2
            i += 1

        if notFound:
            return None

        nsLinkBw = self.__ns.getLink(vnf1, vnf2)['bw']

        # Increase link resources in the previous path (if there are links)
        if path[-1][0] != path[-1][-1]:
            for (nodeA, nodeB) in path:
                self.__multiDomain.incrLnkResource(self.__domain, nodeA,
                    nodeB, 'bw', nsLinkBw)

        # Decrease link resources in the path (if there are links)
        if newPath[-1][0] != newPath[-1][-1]:
            for (nodeA, nodeB) in newPath:
                self.__multiDomain.incrLnkResource(self.__domain, nodeA,
                    nodeB, 'bw', -1 * nsLinkBw)

        # Realloc server resources (if vnf2 goes to new server)
        prevServer = self.__watchingVnfs[vnf2]
        if prevServer != newPath[-1][-1]:
            newServer = newPath[-1][-1]

            vnfRes = self.__ns.getVnf(vnf2)
            self.__incrServVNFsRes(vnfRes, prevServer)

            self.__incrServVNFsRes(vnfRes, newServer, decrease=True)
            self.__watchingVnfs[vnf2] = newServer

        del self.__watchingPaths[i - 1]
        self.__watchingPaths.append((vnf1, vnf2, newPath))

        return True


    def unWatch(self):
        """Releases all watched resources
        :returns: Nothing

        """
        # Release VNFs resources
        for vnf in self.__watchingVnfs.keys():
            server = self.__watchingVnfs[vnf]
            vnfRes = self.__ns.getVnf(vnf)
            self.__incrServVNFsRes(vnfRes, server)

        # Release link resources
        for (vnf1, vnf2, path) in self.__watchingPaths:
            # Ensure vnf1 and vnf2 are located under different servers
            if len(path) > 1 and path[-1][0] != path[-1][-1]:
                nsLinkBw = self.__ns.getLink(vnf1, vnf2)['bw']
                for (nodeA, nodeB) in path:
                    self.__multiDomain.incrLnkResource(self.__domain, nodeA,
                            nodeB, 'bw', nsLinkBw)

        self.__watchingVnfs = dict()
        self.__watchingPaths = []
                

    def __incrServVNFsRes(self, vnfRes, server, decrease=False):
        """Increases/decreases the vnf resources used in the server

        :vnfRes: dictionary with vnf resources
        :server: server id in the domain view
        :decrease: False/True to increase or decrease resources
        :returns: Nothing

        """
        coef = -1 if decrease else 1
        self.__multiDomain.incrServerResource(self.__domain, server,
                'cpu', coef * vnfRes['cpu'])
        self.__multiDomain.incrServerResource(self.__domain, server,
                'memory', coef * vnfRes['memory'])
        self.__multiDomain.incrServerResource(self.__domain, server,
                'disk', coef * vnfRes['disk'])
    


