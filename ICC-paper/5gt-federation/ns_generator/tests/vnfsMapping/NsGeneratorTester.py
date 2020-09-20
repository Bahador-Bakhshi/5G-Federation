import sys
import time
import os
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../src')))
from vnfsMapping import NsGenerator as NsG


class NsGeneratorTester(object):

    """Test class for the NsGenerator"""

    def __init__(self):
        """TODO: to be defined1. """


    def __getNsInfo(self, ns):
        """Retrieves the NS chain information

        :ns: NS instance
        :returns: (vnfs, branches, splits, maxSplitW)

        """
        vnfs = ns.getVNFsNumber()
        branches = ns.getBranchNum()
        splits = ns.getSplitsNum()
        maxSplitW = ns.getMaxSplitW()

        return (vnfs, branches, splits, maxSplitW)


    
    def testYield(self):
        """Tests the yield method that generates NS chains
        :returns: Nothing

        """
        
        bwTh = {'min': 100, 'max': 200}
        delayTh = {'min': 100, 'max': 200}
        memoryTh = {'min': 500, 'max': 1000}
        diskTh = {'min': 100, 'max': 200}
        cpuTh = {'min': 100, 'max': 200}
        nsGen = NsG.NSgenerator(bwTh, delayTh, memoryTh, diskTh, cpuTh)
        
        print '###############'
        print '## testYield ##'
        print '###############'

        failFlag = False

        # Test with different chain sizes
        for vnfs in range(10, 31):
            for branches in range(1, vnfs - 1): # load balancer
                for splits in range(1, 2 * branches):
                    for splitW in range(2, 5):

                        ns = nsGen.yieldChain(splits, splitW, branches, vnfs)
                        genVnfs, genBranches, genSplits, genSplitW =\
                                self.__getNsInfo(ns)

                        print '  generated with maxs: vnfs=' +\
                            str(vnfs)+ ' branches=' + str(branches) +\
                            ' splits=' + str(splits) + ' maxSplitW=' +\
                            str(splitW)

                        if genVnfs > vnfs or genBranches > branches\
                                or genSplits > splits or genSplitW > splitW:
                            failFlag = True

                            ch = ns._NS__chain
                            print '  ' + str(genVnfs) + ' > ' +\
                                str(vnfs) + ': ' + str(genVnfs > vnfs)
                            print '  ' + str(genBranches) + ' > ' +\
                                str(branches) + ': ' +\
                                str(genBranches > branches)
                            print '  ' + str(genSplits) + ' > ' +\
                                str(splits) + ': ' + str(genSplits > splits)
                            print '  ' + str(genSplitW) + ' > ' +\
                                str(splitW) + ': ' + str(genSplitW > splitW)
                        else:
                            print '  successful generation!'
                        print ''

        if not failFlag:
            print '  no failure on chain generation!'


    def testNsBunchWriteRead(self):
        """Tests the write and read of NS bunch
        :returns: Nothing

        """
        print '##########################'
        print '## testNsBunchWriteRead ##'
        print '##########################'

        numNs = 20
        bwTh = { 'min': 100, 'max': 100 }
        delayTh = { 'min': 100, 'max': 100 }
        memoryTh = { 'min': 100, 'max': 100 }
        diskTh = { 'min': 100, 'max': 100 }
        cpuTh = { 'min': 100, 'max': 100 }
        splits = 4
        splitWidth = 2
        branches = 3
        vnfs = 10
        nsBunch = NsG.NSgenerator.genNsBunch(numNs, bwTh, delayTh, memoryTh, diskTh,
                cpuTh, splits, splitWidth, branches, vnfs)

        NsG.NSgenerator.writeNsBunch(nsBunch, 'testNsBunchWriteRead')
        readNsBunch = NsG.NSgenerator.readNsBunch('testNsBunchWriteRead')

        allEqual = True
        for i in range(len(readNsBunch)):
            allEqual = allEqual and nsBunch[i].equal(readNsBunch[i])
        if allEqual:
            print '  read/write NsBunch: OK'
        else:
            print '  read/write NsBunch: ERR'


if __name__ == '__main__':
    tester = NsGeneratorTester()
    tester.testYield()
    tester.testNsBunchWriteRead()


