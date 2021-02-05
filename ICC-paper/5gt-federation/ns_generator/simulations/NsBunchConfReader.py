import sys
import os
import random
import json
import random
import networkx as nx
import MultiDomainConfReader as MDCR

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../src')))
from vnfsMapping import MultiDomain as MD
from vnfsMapping import NS
from vnfsMapping import NsMapper as NSM
from vnfsMapping import NsMapping as NSm
from vnfsMapping import NsGenerator as NSG

# 
absPath = os.path.abspath(os.path.dirname(__file__))
configPath = '/'.join(absPath.split('/')[:-1]) + '/simulation-configs'



class NsBunchConfReader(object):

    """Class to read NS bunch configuration files"""

    def __init__(self, simName):
        """Initialize the reader instance

        :simName: name of the simulation

        """
        self.__simName = simName
        

    def __readConfig(self):
        """Reads the configuration file for the NsBunch
        :returns: dictionary, None in case of error

        """
        filePath = configPath + '/' + self.__simName + '/nsBunch.json'
        if not os.path.exists(filePath):
            return None

        nsBunchProperties = None
        with open(filePath) as f:
            nsBunchProperties = json.load(f)

        return nsBunchProperties


    def readDumped(self, multiDomain=None):
        """Reads an already dumped NS bunch based in the configuration file
        of the simulation.
        :multiDomain: MultiDomain instance, if not provided, it will be
            read/created from the simulation files under the directory
        :returns: [NS bunch list, entryPoint list]
            [None, None] if no Ns bunch have been created

        """
        if not os.path.exists(configPath + '/' + self.__simName +\
                '/nsBunch'):
            return None, None

        nsBunch = NSG.NSgenerator.readNsBunch('nsBunch',
                baseAbsPath=configPath + '/' + self.__simName)
        entryPoints = self.__genEntryPoints(len(nsBunch),
                multiDomain=multiDomain)

        return nsBunch, entryPoints


    def __genEntryPoints(self, requests, multiDomain=None):
        """Generates the entry points list. This implies writting the JSON file
        or reading it, if it has already been created.

        :requests: number of requests to obtain entry points from
        :multiDomain: MultiDomain instance, if not provided, it will be
            read/created from the simulation files under the directory
        :returns: list of dictionaries { 'domain':_, 'server':_ }

        """
        entryPoints = None

        # Generate where the requests will be launched
        mdCfgReader = MDCR.MultiDomainConfReader(self.__simName)
        mdProperties = mdCfgReader.readConfFields()

        entryPointsPath = configPath + '/' + self.__simName +\
                '/entryPoints.json'

        # Retrieve the multiDomain instance
        md = None
        if not multiDomain:
            md = mdCfgReader.readDumped()
            if not md:
                md = mdCfgReader.read()
        else:
            md = multiDomain

        ############
        # Generate #
        ############
        if not os.path.exists(entryPointsPath):
            # Generate NS request entry points 
            nsEntryPoints = []
            for _ in range(requests):
                domain = random.randint(0, mdProperties['domains'] - 1)
                serverDicts = md.getServers(domain)
                servers = serverDicts.keys()
                server = servers[random.randint(0, len(servers) - 1)]
                nsEntryPoints.append({ "domain": domain, "server": server })
            # Dump them
            with open(entryPointsPath, 'w') as entryOut:
                json.dump(nsEntryPoints, entryOut)
        ########
        # Read #
        ########
        else:
            with open(entryPointsPath) as f:
                nsEntryPoints = json.load(f)

        return nsEntryPoints


    def read(self, multiDomain=None):
        """Reads the configuration file to generate the NS bunch
        based on the config file of the simulation. After generating the
        NS bunch, it is stored as a list of GML files with its properties.
        :multiDomain: multiDomain on top of which the the NS bunch are mapped
        :returns: [list of NS instances, list of entry points]
            [None, None] in case of error

        """
        nsBunchProperties = self.__readConfig()
        if not nsBunchProperties:
            return None, None

        nsBunch = NSG.NSgenerator.genNsBunch(
                nsBunchProperties['numNs'],
                nsBunchProperties['bwTh'],
                nsBunchProperties['delayTh'],
                nsBunchProperties['memoryTh'],
                nsBunchProperties['diskTh'],
                nsBunchProperties['cpuTh'],
                nsBunchProperties['splits'],
                nsBunchProperties['splitWidth'],
                nsBunchProperties['branches'],
                nsBunchProperties['vnfs'])

        NSG.NSgenerator.writeNsBunch(nsBunch, 'nsBunch',
                baseAbsPath=configPath + '/' + self.__simName)
        entryPoints = self.__genEntryPoints(nsBunchProperties['numNs'],
                multiDomain=multiDomain)

        return nsBunch, entryPoints


