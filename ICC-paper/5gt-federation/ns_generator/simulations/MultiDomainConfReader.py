import sys
import os
import random
import json
import networkx as nx
import time

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



class MultiDomainConfReader(object):

    """Class to read MultiDomain configuration files"""

    def __init__(self, simName):
        """Initialize the reader instance

        :simName: name of the simulation

        """
        self.__simName = simName
        


    def readDumped(self):
        """Reads an already dumped MultiDomain based in the configuration file
        of the simulation.
        :returns: MultiDomain instance, None if no MultiDomain has been mapped

        """
        if not os.path.exists(configPath + '/' + self.__simName +\
                '/multiDomain'):
            return None

        return MD.MultiDomain.read('multiDomain', absBasePath=configPath +\
                '/' + self.__simName)


    def readConfFields(self):
        """Returns the dictionary with the configuration fields
        :returns: dictionary

        """
        filePath = configPath + '/' + self.__simName + '/multiDomain.json'
        if not os.path.exists(filePath):
            return None

        mdProperties = None
        with open(filePath) as f:
            mdProperties = json.load(f)

        return mdProperties


    def read(self):
        """Reads the configuration file to generate a MultiDomain instance
        based on the config file of the simulation. After generating the
        MultiDomain, it is stored as a GML file with its properties.
        :returns: MultiDomain instance, None in case of error

        """
        mdProperties = self.readConfFields()
        if not mdProperties:
            return None

        print '  -> start multidomain generation at: ' + time.strftime("%a,\
 %d %b %Y %H:%M:%S +0000", time.gmtime())
        md = MD.MultiDomain.yieldMultiDomain(
                mdProperties['domains'],
                mdProperties['meshDegree'],
                mdProperties['fatTreeDegrees'],
                mdProperties['foreignPods'],
                mdProperties['meshLnkRes'],
                mdProperties['fatLnkRes'],
                mdProperties['servRes'],
                meshProps=mdProperties['meshProps'],
                fatLnkProps=mdProperties['fatLnkProps'],
                fatSrvProps=mdProperties['fatSrvProps'])

        print '  -> finished multidomain generation at: ' +\
                time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        print 'foreignPods[16]: ' + str(md.getProperties()['foreignPods'][16])
        md.write('multiDomain', absBasePath=configPath + '/' + self.__simName)
        print '  -> finished multidomain write at: ' +\
                time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

        return md


