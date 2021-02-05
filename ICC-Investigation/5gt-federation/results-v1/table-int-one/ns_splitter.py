import networkx as nx
import sys
import os
import json
import argparse
from hac import GreedyAgglomerativeClusterer
import re

# Import NsGenerator based on relative path
absPath = os.path.abspath(os.path.dirname(__file__))
srcGen= '/'.join(absPath.split('/')[:-1]) + '/ns_generator/src'
sys.path.append(srcGen)
from vnfsMapping.NsGenerator import NSgenerator
from vnfsMapping.NS import NS


if __name__ == '__main__':
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Performs the clustering ' +\
            'of a specified network service graph.')
    parser.add_argument('vnfCSV', type=str,
                help='path to the CSV with VNFs of te NS graph vnfs-n.csv')
    parser.add_argument('vlCSV', type=str,
                help='path to the CSV with VLs of te NS graph vls-n.csv')
    parser.add_argument('out', type=str,
                help='path to store the generated clusters')
    args = parser.parse_args()

    # Get the NS number
    m = re.search('vls-(\d+).csv', args.vlCSV)
    nsNum = m.group(1)
    
    # Create the NS and set weights to be traffic
    readNS = NS.readCSV(vnfCSV = args.vnfCSV, vlCSV = args.vlCSV)
    nsG = readNS.getChain()
    weights = {}
    for (vnfA, vnfB, data) in nsG.edges(data=True):
        weights[vnfA, vnfB] = float(data['traffic'])
    nx.set_edge_attributes(nsG, 'weight', weights)

    # Perform the clustering
    clusterer = GreedyAgglomerativeClusterer()
    dendoVnf = clusterer.cluster(nsG)
    clustering = {}
    for n in range(2, len(nsG) + 1):
        clustering[n] = {}
        for vnf in nsG.nodes():
            cId = [i for i in range(n) if vnf in dendoVnf.clusters(n)[i]][0]
            if cId not in clustering[n]:
                clustering[n][cId] = []
            clustering[n][cId].append(vnf)

    # Split the network service graph
    for numCls in clustering:
        print "Splitting in " + str(numCls) + " clusters"
        clusters = clustering[numCls].keys()
        clusters.sort()
        nsClusters = readNS.split(clusters = clustering[numCls])
        for (nsCluster, clsNum) in zip(nsClusters, clusters):
            naming = "ns-" + str(nsNum) + "-clusters-" + str(numCls) +\
                    "-cluster" + str(clsNum) + "-"
            vlAbs = args.out + "/" + naming + "vls.csv"
            vnfAbs = args.out + "/" + naming + "vnfs.csv"
            nsCluster.writeCSV(vlAbs, vnfAbs)
            print "  VLs of cluster " + str(clsNum) + " written at " + vlAbs
            print "  VNFs of cluster " + str(clsNum) + " written at " + vnfAbs
            
            


