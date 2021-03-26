
import numpy as np
import sys

import graph
import requests

from graph import debug

topo_max_bw = 0

def instantiate_vnfs(topology, placement):
    if placement == None or len(placement) == 0:
        return True
    else:
        print("Placement is not implemented yet")
        sys.exit(-1)


def route_path(topology, path, sfc):
    if debug > 2:
        print("route_path: ")
        print("\t", topology.edges(data=True))
        print("\t path   = ", path)
        print("\t sfc.bw = ", sfc.bw)

    if graph.get_path_bw(topology, path) < sfc.bw:
        return False

    for i in range(len(path) - 1):
        bw = int(topology.edges[path[i], path[i+1]]["bw"]) - sfc.bw
        if bw < 0:
            print("Error, negative bw")
            sys.exit(-1)

        topology.edges[path[i], path[i+1]]["bw"] = bw
    
    if debug > 2:
        print("\t", topology.edges(data=True))
        print("-------------------------------------")
    
    return True 

def deploy_request(topology, request):
    feasible_placement = instantiate_vnfs(topology, request.placement)
    feasible_routing = route_path(topology, request.path, request.sfc)
    
    #FIXME
    #XXX
    #FIXME
    # Undo if onw of them is not feasible !!!!

    return feasible_placement and feasible_routing


def free_vnfs(topology, placement):
    if placement == None or len(placement) == 0:
        pass
    else:
        print("Placement is not implemented yet")
        sys.exit(-1)


def free_path(topology, path, sfc):
    if debug > 2:
        print("free_path: ")
        print("\t", topology.edges(data=True))
        print("\t path   = ", path)
        print("\t sfc.bw = ", sfc.bw)

    for i in range(len(path) - 1):
        bw = int(topology.edges[path[i], path[i+1]]["bw"]) + sfc.bw
        if bw > topology.edges[path[i], path[i+1]]["org_bw"]:
            print("Error, bw > org_bw")
            sys.exit(-1)

        topology.edges[path[i], path[i+1]]["bw"] = bw

    if debug > 2:
        print("\t", topology.edges(data=True))
        print("-------------------------------------")

def free(topology, request):
    free_vnfs(topology, request.placement)
    free_path(topology, request.path, request.sfc)


def is_empty(topology):
    for e in topology.edges:
        if topology.edges[e[0],e[1]]["bw"] != topology.edges[e[0],e[1]]["org_bw"]:
            return False

    return True

