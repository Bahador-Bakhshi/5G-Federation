import sys
import re
import networkx as nx
import networkx.algorithms.isomorphism as iso
import json
import os
import csv

# Global variable for the project absolute path
absPath = os.path.abspath(os.path.dirname(__file__))
nsAbsPath = '/'.join(absPath.split('/')[:-2]) + '/ns-chains'

# NOTE: ":D" is a market to now that code chunk supports MultiGraphs()

class NS(object):

    """Network Service class"""


    def __init__(self):
        """Creates empty NS instance

        """
        self.__serviceName = None
        self.__chain = None
        self.__nfpdsIdx = dict() # each path has its current index
        self.__nfpds = dict()
        self.__branches = None
        self.__splits = None
        self.__maxSplitW = None
        self.__prevNeighsCache = dict() # deprecated
        self.__nextNeighsCache = dict() # deprecated
        self.__branchHeads = dict()


    def __str__(self):
        """String representation with the NS chain
        :returns: string representation

        """

        vnfStr = "VNFs:"
        edges = {}

        for vnf in mg.nodes():
            vnfStr += "  " + str(vnf) + ", properties:"
            vnfStr += "    " + str(mg.getVnf(vnf))

        vnfStr += "VLs:"
        for edge in mg.edges_iter(keys = True):
            vnfStr += "  " + str(edge[0]) + "<-->" + str(edge[1]) +\
                    " index=" + str(edge[2])

        return vnfStr
        

    # :D
    @staticmethod
    def create(vnfs, links, nfpds):
        """Initializes a Network Service instance

        :vnfs: list of dictionaries with required resources for each VNF
            [{'vnf_name', 'id', 'memory', 'disk', 'cpu', 'processing_time'}, ...]
        :links: list of dictionaries with required resources for each link in
            the NS [{'idA', 'idB', 'bw', 'delay'}, ...]
            idA can be 'start' for the starting point
        :nfpds: dictionary of lists containing VNFs traversed at each Nfpd
        :returns: a NS instance

        """

        # Create NS chain graph
        chain = nx.MultiGraph()
        for vnf in vnfs:
            chain.add_node(vnf['id'], **vnf)
        
        for link in links:
            # Check if link endpoints are correct
            if not chain.has_node(link['idA']) or\
                not chain.has_node(link['idB']):
                raise UnboundLocalError('Link endpoint is a non-existing\
 VNF!')
            else:
                chain.add_edge(link['idA'], link['idB'], **link)

        ns = NS()
        ns.setChain(chain)
        ns.setNfpds(nfpds)

        return ns


    def getVNFsNumber(self):
        """Obtains the number of VNFs present in the NS chain
        :returns: number of nodes or -1 if the chain is not set yet

        """
        return self.__chain.number_of_nodes() -1 if self.__chain != None\
                else -1


    def initIter(self):
        """Initializes the iterator for each Nfpd
        :returns: Nothing

        """

        for nfpd in self.__nfpds.keys():
            self.__nfpdsIdx[nfpd] = -1


    def currIterId(self, nfpd):
        """Obtains the id for the current VNF in the iterator of a Nfpd
        :nfpd: ID of the Nfpd
        :returns: VNF id 

        """
        return self.__nfpds[self.__nfpdsIdx[nfpd]]

    
    # :D
    def prevVNF(self, vnfId, nfpd):
        """Obtains the previous vnf of a certain one

        :vnfId: VNF id from which to obtain the previous neighbours
        :nfpd: ID of the Nfpd
        :note: in case the VNF is traversed multiple times in nfpd, then the
        function gives the previous VNF before it is traversed for first time
        :returns: previous VNF id or None

        """

        if self.__nfpds[nfpd][0] == vnfId:
            return None

        i = 0
        prevNotFound = True

        while i < len(self.__nfpds[nfpd]) - 1 and prevNotFound:
            prevNotFound = self.__nfpds[nfpd][i + 1] != vnfId
            i += 1

        return None if prevNotFound else self.__nfpds[nfpd][i - 1]


    # :D
    def getNextVNF(self, vnfId, nfpd):
        """Obtains the next VNF neighbor in the nfpd path

        :vnfId: VNF id from which to obtain the next neighbours
        :nfpd: ID of the Nfpd
        :note: in case the VNF is traversed multiple times in nfpd, then the
        function gives the the next VNF after first time traversal
        :returns: None or next VNF id within the nfpd

        """

        i = 0
        notFound = True
        while i < len(self.__nfpds[nfpd]) and notFound:
            notFound = self.__nfpds[nfpd][i] != vnfId
            i += 1

        return None if notFound or i == len(self.__nfpds[nfpd])\
                else self.__nfpds[nfpd][i]


    def getPrevIdx(self, nfpd):
        """Obtains the previous VNF index in the iterator
        :nfpd: ID of the Nfpd
        :returns: None or the index

        """

        prevIdx = self.__nfpdsIdx[nfpd] - 1

        return prevIdx if prevIdx >= 0 else None


    # :D
    def iterNext(self, nfpd):
        """Retrieves the next VNFs id after current one and advances the
            iterator pointer to the next id
        :nfpd: ID of the Nfpd
        :returns: next VNF id or None if it is the last one

        """

        if self.__nfpdsIdx[nfpd] + 1 == len(self.__nfpds[nfpd]):
            return None

        self.__nfpdsIdx[nfpd] += 1

        return self.__nfpds[nfpd][self.__nfpdsIdx[nfpd]]


    # TODO - deprecated
    def getBranchNum(self):
        """Obtains the number of branches
        :returns: int, None if not set

        """

        return self.__branches


    # TODO - deprecated
    def getSplitsNum(self):
        """Obtains the number of splits
        :returns: int, None if not set

        """
        
        return self.__splits


    # TODO - deprecated
    def getMaxSplitW(self):
        """Obtains the maximum split within the chain
        :returns: int, None if not set

        """
        
        return self.__maxSplitW


    def setNfpds(self, nfpds):
        """It sets which are the Nfpds within the NS.

        :nfpds: dictionary of lists containing VNFs traversed at each Nfpd
        :returns: Nothing

        """
        
        self.__nfpds = nfpds


    def setServiceName(self, name):
        """Sets the service name

        :name: service name string
        :returns: Nothing

        """
        self.__serviceName = name


    def getServiceName(self):
        """Gets the service name
        :returns: string containing the service name

        """
        return self.__serviceName


    # TODO - deprecated
    def setBranchNum(self, branchNum):
        """Sets the number of branches in a NS chain

        :branchNum: number of branches in the chain

        """
        self.__branches = branchNum


    def setIterIdx(self, iterIdx, nfpd):
        """Sets the iterator index

        :iterIdx: iterator index
        :nfpd: ID of the Nfpd
        :returns: Nothing

        """
        self.__nfpdsIdx[nfpd] = iterIdx


    # TODO - deprecated
    def setSplitsNum(self, splits):
        """Sets the number of splits of the NS chain

        :splits: number of splits

        """
        self.__splits = splits


    def setChain(self, chain):
        """Sets the NS chain

        :chain: NS chain (networkx instance)
        :returns: Nothing

        """

        self.__chain = chain


    # TODO - deprecated
    def setMaxSplitW(self, maxSplitW):
        """Sets the maximum split width

        :maxSplitW: the split within the chain with the maximum width
        :returns: Nothing

        """
        
        self.__maxSplitW = maxSplitW


    # TODO - deprecated
    def addBranchHead(self, vnf):
        """Include the vnf in the branch heads list.
        
        :vnf: vnf id of the branch head
        :returns: Nothing"""
        self.__branchHeads[vnf] = True


    # TODO - deprecated
    def setBranchHeads(self, branchHeads):
        """Sets the branch heads of the NS chain
        
        :branchHeads: list with VNFs that are the branch heads
        :returns: Nothing"""
        for branchHead in branchHeads:
            self.__branchHeads[branchHead] = True


    # TODO - deprecated
    def getBranchHeads(self):
        """Returns the branch heads of the NS chain
        
        :returns: list of VNF id that are branch heads"""
        return [branchHead for branchHead in self.__branchHeads]


    # TODO - deprecated
    def isBranchHead(self, vnf):
        """Determines if the vnf is a branch head of the NS chain.
        
        :vnf: vnf id
        :returns: True/False"""
        return vnf in self.__branchHeads


    # :D
    def getLinks(self, A, B):
        """Gets the (A,B) links and their resources

        :A: first VNF
        :B: second VNF
        :returns: a dictionary with the link resources of each VL connecting A
        and B

        """

        if not self.__chain.has_edge(A, B):
            return None
        else:
            return self.__chain.get_edge_data(A, B)


    # :D
    def getLinksTo(self, B):
        """Gets all the links arriving to B

        :B: destination VNF id
        :note: for now it retrieves the first (A,B) link stored
        :returns: list of edges between (_, B), where each element is a
        dictionary with the multiple links connecting "_" and "B"

        """
        nodes = self.getChain().nodes()
        links = [self.getLink(node, B) for node in nodes]

        return filter(lambda l: l != None, links)


    def getChain(self):
        """Retrieves the NS chain
        :returns: networkx instance

        """
        return self.__chain


    def getVnf(self, vnf):
        """Obtains the requested resources of the VNF with id 'vnf'

        :vnf: VNF id
        :returns: dictionary of requested resources, None in case of error

        """
        
        if not self.__chain.has_node(vnf):
            return None

        resources = {'requirements': {}}
        resources['vnf_name'] = nx.get_node_attributes(self.__chain,
            'vnf_name')[vnf]
        resources['id'] = nx.get_node_attributes(self.__chain,
            'id')[vnf]
        resources['memory'] = nx.get_node_attributes(self.__chain,
            'memory')[vnf]
        resources['disk'] = nx.get_node_attributes(self.__chain,
            'disk')[vnf]
        resources['cpu'] = nx.get_node_attributes(self.__chain,
            'cpu')[vnf]
        resources['processing_time'] = nx.get_node_attributes(self.__chain,
            'processing_time')[vnf]

        return resources


    def split(self, clusters):
        """Splits the network service in the specified clusters, and generates
           a NS entity for every cluster.

        :clusters: dictionary with clusters and vnf numbers
                   {clusterNum: [vnf1, vnf2], clusterNum2: [vnf3, vnf4]}
        :returns: list of NS in ascendent ordered by respective cluster number
                  i.e., [NScls1, NScls2]

        """
        nsClusters = []
        for cls in clusters:
            vnfs = clusters[cls]
            notInCls = [v for v in self.getChain().nodes() if v not in vnfs]
            cluster = self.getChain().copy()
            for vnf in notInCls:
                cluster.remove_node(vnf)
            nsCluster = NS()
            nsCluster.setChain(cluster)
            nsClusters.append(nsCluster)

        return nsClusters
        
    
    def write(self, storedName, absPath=None, absName=None):
        """Writes the NS chain and saves it under the specified storedName
        directory

        :storedName: name of the directory under which the NS chain will be
            stored
        :absPath: optional parameter to specify the absolute path under which
            the NS will be stored
        :absName: optional param to specify absPath/name.gml where file is
                  stored. If absPath is specified, this one is the used param
        :returns: Nothing

        """
        basePath = None
        if not absPath:
            basePath = nsAbsPath + '/' + storedName + '/'
        else:
            basePath = absPath + '/' + storedName + '/'
        if not os.path.exists(basePath):
            os.makedirs(basePath)
        gmlPath = basePath + 'chain.gml' if not absName else absName
        jsonPath = basePath[:-5] + '.json'
        nx.write_gml(self.__chain, gmlPath)

        # Write the properties as well
        props = {
            'branches': self.__branches,
            'splits': self.__splits,
            'maxSplitW': self.__maxSplitW ,
            'branchHeads': self.__branchHeads
        }
        with open(jsonPath, 'w') as f:
            json.dump(props, f)


    @staticmethod
    def readCSV(vnfCSV, vlCSV):
        """Creates a network service based on the virtual links and vnfs CSV
           files

        :vnfCSV: path to the CSV file where the VNFs are present
        :vlCSV: path to the CSV file where the virtual links are present
        :returns: NS instance

        """
        nsG = nx.Graph()
        with open(vnfCSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nsG.add_node(row['idVNF'], row)

        with open(vlCSV) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nsG.add_edge(row['idVNFa'], row['idVNFb'], row)

        readNS = NS()
        readNS.setChain(nsG)

        return readNS
    

    def writeCSV(self, vlAbs, vnfAbs):
        """Saves the NS as two separate CSV files, one for the virtual links
        and another for theSaves the NS as two separate CSV files, one for the
        virtual links and another for the VNFs

        :vlAbs: absolute path filename to store the VLs CSV
        :vnfAbs: absolute path filename to store the VNFs CSV

        :returns: Nothing

        """
        csvChain = self.__prepareCSVchain()
        vnfs = csvChain.nodes()
        vls = csvChain.edges()

        # Write the VLs csv file
        if len(vls) > 0:
            with open(vlAbs, 'w') as csvfile:
                vl0 = csvChain.get_edge_data(vls[0][0], vls[0][1])
                writer = csv.DictWriter(csvfile, fieldnames = vl0.keys())
                writer.writeheader()

                for (vnf1, vnf2, data) in csvChain.edges(data=True):
                    writer.writerow(data)

        # Write the VNFs csv file
        if len(vnfs) > 0:
            with open(vnfAbs, 'w') as csvfile:
                prevChain = self.getChain()
                self.setChain(csvChain)
                firstVnf = csvChain.nodes()[0]
                props = self.getVnf(firstVnf).keys()
                if 'idVNF' not in props:
                    props += ['idVNF']
                writer = csv.DictWriter(csvfile, fieldnames = props)
                writer.writeheader()


                for vnf in csvChain.nodes():
                    vnfDat = dict(self.getVnf(vnf))
                    vnfDat['idVNF'] = vnfDat['id']
                    #del vnfDat['id']
                    writer.writerow(vnfDat)


    def __prepareCSVchain(self):
        """Prepares a networkX chain to write it for a CSV.
           It removes the 'start' VNF.
        :returns: networkX Graph instance

        """
        csvChain = self.getChain().copy()
        if 'start' in csvChain.nodes():
            csvChain.remove_node('start')

        # Set VL attributes
        idsA, idsB = {}, {}
        for (vnfA, vnfB, data) in csvChain.edges(data=True):
            idsA[vnfA,vnfB] = vnfA
            idsB[vnfA,vnfB] = vnfB
        nx.set_edge_attributes(csvChain, 'idVNFa', idsA)
        nx.set_edge_attributes(csvChain, 'idVNFb', idsB)

        # Set VNF attributes
        ids, cpus, disks, memories = {}, {}, {}, {},
        for (vnf, data) in csvChain.nodes(data=True):
            csvChain.node[vnf]['id'] = vnf
            ids[vnf] = vnf
            # It might be the case that requirements is not present
            reqs = data['requirements']
            if type(reqs) == dict and len(reqs) > 0:
                cpus[vnf] = data['requirements']['cpu']
                disks[vnf] = data['requirements']['storage']
                memories[vnf] = data['requirements']['memory']

        nx.set_node_attributes(csvChain, 'id', ids)
        # It might be the case that requirements is not present
        if len(cpus) > 0:
            nx.set_node_attributes(csvChain, 'cpu', cpus)
            nx.set_node_attributes(csvChain, 'disk', disks)
            nx.set_node_attributes(csvChain, 'memory', memories)

        return csvChain


    def compareVNFs(self, vnf1, vnf2):
        """Compares two VNFs

        :vnf1: VNF 1 obtained with the getVnf() method
        :vnf2: VNF 2 obtained with the getVnf() method
        :returns: True/False

        """
        
        return vnf1['memory'] == vnf2['memory'] and\
                vnf1['disk'] == vnf2['disk'] and\
                vnf1['cpu'] == vnf2['cpu'] and\
                vnf1['processing_time'] == vnf2['processing_time']


    # :D
    def compareLinks(self, link1, link2):
        """Compares two NS chain links

        :link1: link 1 obtained with getLinks()[n] method
        :link2: link 2 obtained with getLinks()[n] method
        :returns: True/False

        """
        
        return link1['bw'] == link2['bw'] and link1['delay'] == link2['delay']


    # :D
    def compare(self, ns):
        """Compares the NS chain with the other ones passed by argument.
        All nodes, links and properties must be the same

        :ns: other NS chain to compare with
        :returns: True/False

        """

        sChain = self.getChain()
        nsChain = ns.getChain()


        # Compare the VNFs
        if not self.getVNFsNumber() == ns.getVNFsNumber():
            return False
        for vnfId in sChain.nodes():
            if vnfId not in nsChain.nodes():
                return False
            for vnfReq in sChain[vnfId]:
                if vnfReq not in nsChain[vnfId]:
                    return False
                if sChain[vnfId][vnfReq] != nsChain[vnfId][vnfReq]:
                    return False

        # Compare the VLs
        for vnf in sChain.nodes():
            for vnfNeig in sChain.neighbors(vnf):
                if vnfNeig not in nsChain[vnf]:
                    return False
                for mVl in sChain[vnf][vnfNeig]:
                    existInNs = False
                    if mVl not in nsChain[vnf][vnfNeig]:
                        return False
                    else:
                        existInNs = sChain[vnf][vnfNeigh][mVl] ==\
                                nsChain[vnf][vnfNeigh][mVl]
                    if not existInNs:
                        return False
        
        return True


    # TODO - deprecated
    def toPimrc(self, pimrc=None):
        """Translates the NS instance into a PIMRC18 JSON format.
        If pimrc parameter is provided, the info. is incorporated there.

        :pimrc: PIMRC18 dictionary
        :returns: JSON in PIMRC18 format

        """
        if not pimrc:
            pimrc = {}
        if 'vnfs' not in pimrc:
            pimrc['vnfs'] = []
        if 'services' not in pimrc:
            pimrc['services'] = []
        if 'vnf_edges' not in pimrc:
            pimrc['vnf_edges'] = []

        # Generate service name
        service_nums = [-1]
        for service in pimrc['services']:
            if 's_gen_' in service['service_name']:
                service_nums.append(int(
                    service['service_name'].split('s_gen_')[-1]))
        serviceName = 's_gen_' + str(max(service_nums) + 1)
            
        # Generate the service dictionary
        service = {
            'service_name': serviceName,
            'max_latency': self.maxDelay(),
            'traversed_vnfs': {}
        }

		# Get the traversed links
        vnf_edges = filter(lambda ve: ve[0] != 'start' and ve[1] != 'start',
            self.getChain().edges(data=True))
        for vnf_edge in vnf_edges:
            link = dict(self.getLink(vnf_edge[0], vnf_edge[1]))
            vnfAname = self.getVnf(vnf_edge[0])['vnf_name']
            vnfBname = self.getVnf(vnf_edge[1])['vnf_name']
            link['source'] = vnfAname
            link['target'] = vnfBname
            del link['prob']
            pimrc['vnf_edges'].append(link)

        # Get the VNFs inside the NS
        networkx_vnfs = filter(lambda v: v != 'start',
            self.getChain().nodes())
        nsVnfs = [self.getVnf(v) for v in networkx_vnfs]
        pimrcVnfNames = [vnf['vnf_name'] for vnf in pimrc['vnfs']]

        for (vnf, vnfId) in zip(nsVnfs, networkx_vnfs):
            pass # TODO
        	# Check that the vnf is not there
            if vnf['vnf_name'] not in pimrcVnfNames:
                pimrc['vnfs'].append({
                    'vnf_name': vnf['vnf_name'],
                    'processing_time': vnf['processing_time'],
                    'requirements': vnf['requirements']
                })

            # Traversing prob - TODO only 1 link supposed (if more tha one, it
            # is a merging and will have probs=1)
            arrivingLinks = self.getLinksTo(vnfId)
            if 'v_gen_1' in vnf['vnf_name']:
                service['traversed_vnfs'][vnf['vnf_name']] = 1
            else:
                service['traversed_vnfs'][vnf['vnf_name']] =\
                    arrivingLinks[0]['prob']
        
        pimrc['services'].append(service)

        return pimrc

    
    # TODO - unused
    @staticmethod
    def read(storedName, absPath=None):
        """Reads a NS chain stored under the provided storedName directory

        :storedName: name of the directory under which the NS chain will be
            stored
        :absPath: optional parameter to specify the absolute path under which
            the NS will be stored
        :returns: a NS chain instance

        """
        
        basePath = 0
        if not absPath:
            basePath = nsAbsPath + '/' + storedName + '/'
        else:
            basePath = absPath + '/' + storedName + '/'
        props = None

        # Read from files
        with open(basePath + 'props.json', 'r') as f:
            props = json.load(f)
        chain = nx.read_gml(basePath + 'chain.gml', 'label')
        print "Nodes of read chain: " + str(chain.nodes())
        print "This are the chain edges: " + str(chain.edges())
        print "start 1 properties: " + str(chain['start']["1"])
        
        # Instance the NS chain
        ns = NS()
        ns.setChain(chain)
        ns.setBranchNum(props['branches'])
        ns.setSplitsNum(props['splits'])
        ns.setMaxSplitW(props['maxSplitW'])
        branchHeads = dict()
        # branchHeads keys (the vnfs) are stored as strings, convert to int
        for vnf in props['branchHeads']:
            branchHeads[int(vnf)] = props['branchHeads'][vnf]
        ns.setBranchHeads(branchHeads)
        
        return ns


    # TODO - deprecated
    def equal(self, ns):
        """Compares the NS with the one passed by argument

        :ns: NS instance
        :returns: True/False

        """
        same = True
        same = same and iso.is_isomorphic(self.getChain(), ns.getChain(),
                node_match=lambda n1Res, n2Res: n1Res == n2Res,
                edge_match=lambda ed1Res, ed2Res: ed1Res == ed2Res)
        same = same and self.__branches == ns._NS__branches
        same = same and self.__splits == ns._NS__splits
        same = same and self.__maxSplitW == ns._NS__maxSplitW
        same = same and self.__prevNeighsCache == ns._NS__prevNeighsCache
        same = same and self.__nextNeighsCache == ns._NS__nextNeighsCache
        same = same and self.__branchHeads == ns._NS__branchHeads

        return same


    def maxDelay(self):
        """Obtains the maximum delay to go from the first VNF to one of the
        last ones. It is the maximum delay of all existing Nfpds.
        :returns: maximum delay number

        """

        maxDel = sys.maxint

        for nfpd in self.__nfpds:
            currDel = 0
            for i in range(len(self.__nfpds[nfpd]) - 1):
                v1 = self.__nfpds[nfpd][i]
                v2 = self.__nfpds[nfpd][i + 1]
                currDel += max([l['delay'] for l in self.__getLinks(v1, v2)])

            if currDel < maxDelay:
                maxDelay = currDel

        return maxDel


    def avgDelay(self, processing=False):
        """Obtains the average delay of the service to reach last VNF. It is
        performed over all the existing Nfpds.
        :returns: average service delay
        :processing: boolean specifying if processing times must be taken into
        account

        """

        totalAvgDel = 0

        for nfpd in self.__nfpds:
            currDel = 0

            if processing:
                currDelay = self.__nfpd[0]['processing_time']

            for i in range(len(self.__nfpds[nfpd]) - 1):
                v1 = self.__nfpds[i]
                v2 = self.__nfpds[i + 1]
                allDelays = [l['delay'] for l in self.__getLinks(v1, v2)]

                currDel += reduce(lambda x, y: x + y, allDelays) / \
                        len(allDelays)

                if processing:
                    currDel += v2['processing_time']

            totalDel += currDel

        return totalAvgDel / len(self.__nfpds.keys())


