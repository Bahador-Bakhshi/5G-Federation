
import numpy as np
import sys

import graph
import requests


def instantiate_vnfs(topology, placement):
    if placement == None or len(placement) == 0:
        return
    else:
        print("Placement is not implemented yet")
        sys.exit(-1)


def route_path(topology, path, sfc):
    for i in range(len(path) - 1):
        bw = int(topology.edges[path[i], path[i+1]]["bw"]) - sfc.bw
        if bw < 0:
            print("Error, negative bw")
            sys.exit(-1)

        topology.edges[path[i], path[i+1]]["bw"] = bw


def deploy_request(topology, request):
    instantiate_vnfs(topology, request.placement)
    route_path(topology, request.path, request.sfc)


def free_vnfs(topology, placement):
    if placement == None or len(placement) == 0:
        pass
    else:
        print("Placement is not implemented yet")
        sys.exit(-1)


def free_path(topology, path, sfc):
    for i in range(len(path) - 1):
        bw = int(topology.edges[path[i], path[i+1]]["bw"]) + sfc.bw
        if bw > topology.edges[path[i], path[i+1]]["org_bw"]:
            print("Error, bw > org_bw")
            sys.exit(-1)

        topology.edges[path[i], path[i+1]]["bw"] = bw


def free(topology, request):
    free_vnfs(topology, request.placement)
    free_path(topology, request.path, request.sfc)


def is_empty(topology):
    for e in topology.edges:
        if topology.edges[e[0],e[1]]["bw"] != topology.edges[e[0],e[1]]["org_bw"]:
            return False

    return True

