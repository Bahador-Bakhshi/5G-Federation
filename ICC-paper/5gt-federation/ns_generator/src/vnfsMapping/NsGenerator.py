import random
from time import sleep
import time
import networkx as nx
import NS
import os
import time 

# Global variable for the project absolute path
absPath = os.path.abspath(os.path.dirname(__file__))
nsAbsPath = '/'.join(absPath.split('/')[:-2]) + '/ns-chains'



class NSgenerator(object):

    """Generator of NS requests"""

    def __init__(self, linkTh, vnfTh):
        """Initializes the NS generator with required thresholds

        :linkTh: Threshold values for the links (follow PIMRC18 model), ex.:
            {'traffic': {'min', 'max'}, 'delay': {}}
        :vnfTh: Threshold values for the VNFs (follow PIMRC18 model), ex.:
            {
             'processing_time': {'min', 'max'},
             'requirements': {
               'cpu':     {'min', 'max'},
               'memory':  {'min', 'max'},
               'storage': {'min', 'max'}
             }
            }

        """
        self.__linkTh = linkTh
        self.__vnfTh = vnfTh

        self.__branches = None
        self.__split = None
        

    def __createLink(self, chain, vnfA, vnfB, prob=1):
        """Stablishes a link between VNFs with id vnfA and vnfB

        :chain: NS chain (networkX graph)
        :vnfA: id of vnfA
        :vnfB: id of vnfB
        :prob: probability of going from vnfA to vnfB
        :returns: Nothing

        """
        link_params = {'prob': prob}
        for linkTh_param in self.__linkTh:
            link_params[linkTh_param] = random.randint(
                self.__linkTh[linkTh_param]['min'],
                self.__linkTh[linkTh_param]['max'])
        chain.add_edge(vnfA, vnfB, **link_params)


    def genVnfName(self, vnfId):
        """Generates a VNF id based on the VNF IDinside the NS

        :vnfId: VNF id inside the NS chain
        :returns: Nothing

        """
        sleep(0.001)
        return 'v_gen_' + str(vnfId) + '_' + str(random.randint(1, 20)) +\
            '_'+ str(time.time())

    def __insertVNF(self, chain, branchHeads, predecesors, vnfId=None, prob=1):
        """Inserts a VNF in the current NS chain. It adds it after the
        predecesors VNF list

        :chain: NS chain (networkX graph)
        :branchHeads: list of all branches' heads
        :predecesors: list of VNFs predecesors
        :vnfId: (optional) id of inserted VNF, otherwise it'll have
            max(predecesors) + 1
        :returns: Nothing

        """

        vnf_params = {
            'requirements': {}
        }
        for vnf_param in self.__vnfTh['requirements']:
            vnf_params['requirements'][vnf_param] = random.randint(
                self.__vnfTh['requirements'][vnf_param]['min'],
                self.__vnfTh['requirements'][vnf_param]['max'])
        for vnf_param in self.__vnfTh:
            if vnf_param != 'requirements':
                vnf_params[vnf_param] = random.randint(
                self.__vnfTh[vnf_param]['min'],
                self.__vnfTh[vnf_param]['max'])

        # Add VNFs and links
        vnfId = max(branchHeads) + 1 if not vnfId else vnfId
        vnf_params['vnf_name'] = self.genVnfName(vnfId)
        chain.add_node(vnfId, **vnf_params)
        newBranchHeads = list(branchHeads)

        for predecesor in predecesors:
            newBranchHeads.remove(predecesor)
            self.__createLink(chain, predecesor, vnfId, prob=prob)

        return newBranchHeads + [vnfId]
    

    def __canSplit(self, remSplits, remBranches, remVNFs):
        """Checks if a split can be performed in the creation of the current NS
        chain.

        :remSplits: remaining splits to be performed
        :remBranches: remaining branches to create
        :remVNFs: remaining VNFs to be inserted in the NS chain
        :returns: True/False

        """

        if not remSplits > 0 or not remBranches > 0 or not remVNFs >= 2:
            return False
        else:
            return True
        

    def __canInsertVnf(self, branchHeads, remVNFs):
        """Checks if a VNF can be added to the current NS chain

        :branchHeads: list of all branches' heads
        :remVNFs: remaining VNFs to be inserted in the NS chain
        :returns: Nothing

        """

        return remVNFs > 0
        

    def __joinBranches(self, chain, branchHeads, remVNFs):
        """Randomly joins the branches present in the NS chain

        :chain: NS chain
        :branchHeads: list of all branches' heads
        :remVNFs: remaining VNFs to be inserted in the NS chain
        :returns: (number of joined branches, new branch heads)

        """
        
        newBranchHeads = None
        joinNum = 0

        if remVNFs == 1:
            newBranchHeads = self.__insertVNF(chain, branchHeads, branchHeads)
            joinNum = len(branchHeads)
        else:
            joinNum = random.randint(2, len(branchHeads))
            joinVNFs = list(branchHeads)
            
            for _ in range(len(joinVNFs) - joinNum):
                del joinVNFs[random.randint(0, len(joinVNFs) - 1)]
            newBranchHeads = self.__insertVNF(chain, branchHeads, joinVNFs)

        return (joinNum, newBranchHeads)


    def __splitChain(self, chain, branchHeads, splitWidth, remBranches, remVNFs):
        """Randomly splits a NS chain

        :chain: NS chain
        :branchHeads: list of all branches' heads
        :splitWidth: maximum number of branches coming out of a split
        :remBranches: number of remaining branches to be created
        :remVNFs: remaining VNFs to be inserted in the NS chain
        :returns: (list of new branch heads, number of new branches)

        """
        
        vnfIdx = random.randint(0, len(branchHeads) - 1)
        predecesor = branchHeads[vnfIdx]
        newVnfId = max(branchHeads)

        # Decide split length and insert new VNFs after the split
        newVnfs = []
        maxSplitW = min(splitWidth, remBranches + 1, remVNFs)
        splitW = random.randint(2, maxSplitW)
        probs = NSgenerator.arrayProbs(splitW)
        for i in range(1, splitW + 1):
            newVnfs.append(newVnfId + i)
            self.__insertVNF(chain, branchHeads, [predecesor],
                    vnfId=newVnfId + i, prob=probs[i-1])

        del branchHeads[vnfIdx]

        return branchHeads + newVnfs, splitW - 1


    def yieldChain(self, splits, splitWidth, branches, vnfs):
        """Yields a generated NS chain with a maximum number of splits,
        branches and a certain number a vnfs.

        :splits: maximum number of splits in the NS chain
        :splitWidth: maximum number of branches coming out of a split
        :branches: maximum number of branches in the NS chain
        :vnfs: number of VNFs that compose the chain
        :returns: a NS instance

        """
        
        branchHeads = []
        remVNFs = vnfs
        remSplits = splits
        remBranches = branches - 1
        maxBranches = 1
        maxSplits = 1
        maxSplitW = 0
        chain = nx.Graph()
        decisions = ['insert', 'join', 'split']

        branchHeads = self.__insertVNF(chain, [], [], vnfId=1)
        remVNFs -= 1

        while chain.number_of_nodes() < vnfs:
            random.shuffle(decisions)
            i, madeDecision = 0, False
            
            # Decide wether a new VNF is inserted, or if there is a split or a
            # join in the chain
            while not madeDecision and i < len(decisions):
                if decisions[i] == 'insert' and\
                        self.__canInsertVnf(branchHeads, remVNFs):
                    predecesor = branchHeads[random.randint(0, len(branchHeads)
                        - 1)]
                    branchHeads = self.__insertVNF(chain, branchHeads,
                        [predecesor])
                    remVNFs -= 1
                    madeDecision = True

                elif decisions[i] == 'join' and len(branchHeads) > 1:
                    joined, branchHeads = self.__joinBranches(chain,
                            branchHeads, remVNFs)
                    remVNFs -= 1
                    remBranches += joined - 1
                    madeDecision = True

                elif decisions[i] == 'split' and self.__canSplit(remSplits,
                        remBranches, remVNFs):
                    branchHeads, newBranches = self.__splitChain(chain,
                            branchHeads, splitWidth, remBranches, remVNFs)
                    remVNFs -= newBranches + 1
                    remBranches -= newBranches
                    remSplits -= 1
                    madeDecision = True

                    # Refresh counters
                    if branches - remBranches > maxBranches:
                        maxBranches = branches - remBranches
                    if splits - remSplits > maxSplits:
                        maxSplits = splits - remSplits
                    if maxSplitW < newBranches + 1:
                        maxSplitW = newBranches + 1

                i += 1

        # Add starting and ending link requirements and star/end points
        chain.add_node('start')
        self.__createLink(chain, 'start', 1)

        ns = NS.NS()
        ns.setChain(chain)
        ns.setBranchNum(maxBranches)
        ns.setSplitsNum(maxSplits)
        ns.setMaxSplitW(maxSplitW)
        ns.setBranchHeads(branchHeads)

        return ns

    
    @staticmethod
    def arrayProbs(n):
        """Creates an array of n random numbers summing 1
        For example, uniformProbs(3) -> [0.3, 0.5, 0.2]

        :n: number of entries in the array
        :returns: array of probabilities that sum 1

        """
        # Decide probabilities
        probs = [1 for _ in range(n)]
        if n > 1:
            for i in range(n):
                if i == 0:
                    probs[0] = random.uniform(0, 1)
                elif i == n - 1: # last element
                    assigned_probs = reduce(lambda x, y: x + y, probs[:i])
                    probs[i] = 1 - assigned_probs
                else: 
                    assigned_probs = reduce(lambda x, y: x + y, probs[:i])
                    probs[i] = random.uniform(0, 1 - assigned_probs)

        return probs


    @staticmethod
    def writeNsBunch(nsBunch, storedName, baseAbsPath=None):
        """Stores a NS bunch

        :nsBunch: list of NSs
        :storedName: name of the directory under which the NS chain will be
            stored
        :baseAbsPath: base absolute path under which the ns bunch will be
            stored
        :returns: Nothing

        """
        basePath = nsAbsPath + '/' + storedName if not baseAbsPath\
                else baseAbsPath + '/' + storedName

        nsCounter = 0
        for ns in nsBunch:
            ns.write('ns-' + str(nsCounter), absPath=basePath)
            nsCounter += 1


    @staticmethod
    def readNsBunch(storedName, baseAbsPath=None):
        """Reads a a bunch of generated NSs

        :storedName: directory under which the Nss of the bunch are stored
        :baseAbsPath: base absolute path under which the ns bunch will be
            stored
        :returns: list of NS instances, None in case there is an error
        """
        basePath = nsAbsPath + '/' + storedName if not baseAbsPath\
                else baseAbsPath + '/' + storedName
        if not os.path.exists(basePath):
            return None

        nsBunch = []
        numNSs = len(os.listdir(basePath))
        for nsNum in range(numNSs):
            nsBunch.append(NS.NS.read('ns-' + str(nsNum), absPath=basePath))

        return nsBunch


    @staticmethod
    def genNsBunch(numNs, bwTh, delayTh, memoryTh, diskTh, cpuTh, splits,
            splitWidth, branches, vnfs):
        """Generate a bunch of NS instances based on the specified parameters.

        :numNs: number of NS to be generated
        :bwTh: links bw thresholds - dictionaty {'min':_, 'max': _}
        :delayTh: links delay thresholds - dictionaty {'min':_, 'max': _}
        :memoryTh: links memory thresholds - dictionaty {'min':_, 'max': _}
        :diskTh: servers disks thresholds - dictionaty {'min':_, 'max': _}
        :cpuTh: servers cpu thresholds - dictionaty {'min':_, 'max': _}
        :splits: maximum number of splits within the generated NS chains
        :splitWidth: maximum number of VNFs that can come up from a split in
            the generated NS chains
        :branches: maximum number of branches in the generated NS chains
        :vnfs: maximum number of VNFs within the generated NS chains
        :returns: a list of the generated NS chains

        """
        nsBunch = []
        nsGen = NSgenerator(bwTh, delayTh, memoryTh, diskTh, cpuTh)

        for _ in range(numNs):
            ns = nsGen.yieldChain(splits, splitWidth, branches, vnfs)
            nsBunch.append(ns)

        return nsBunch



