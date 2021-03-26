from itertools import islice

import networkx as nx
import numpy as np

debug = 1

def get_max_flow(topology, src, dst):
    flow_value, flow_dict = nx.maximum_flow(topology, src, dst, capacity="bw")
    return flow_value, flow_dict


def test_max_flow(topology):
    if debug > 2:
        print(topology.nodes)
    
    for u in range(len(topology.nodes)):
        for v in range(len(topology.nodes)):
            if u != v:
                flow_value, flow_dict = get_max_flow(topology, u + 1, v + 1)
                if debug > 1:
                    print("maxflow: src = ", u + 1, ", dst = ", v + 1, ", flow_value = ", flow_value)


WEIGHT_BIG_M = 1000000000.00
def link_weight_one(topology, sfc, feasibility_check):
    for e in topology.edges:
        topology.edges[e[0],e[1]]["routing_weight"] = 1 if feasibility_check(topology, e, sfc) else WEIGHT_BIG_M

    if debug > 2:
        print("link_weight_one: sfc.bw = ", sfc.bw)
        print(topology.edges(data = True))


def link_weight_capacity(topology, sfc, feasibility_check):
    for e in topology.edges:
        bw = topology.edges[e[0],e[1]]["bw"]
        topology.edges[e[0],e[1]]["routing_weight"] = 1.0 / bw if feasibility_check(topology, e, sfc) else WEIGHT_BIG_M
    
    if debug > 2:
        print(topology.edges(data=True))


def bw_feasibility(topology, e, sfc):
    return True if topology.edges[e[0], e[1]]["bw"] >=  sfc.bw else False


def get_path_weight(topology, path):
    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += topology.edges[path[i], path[i+1]]["routing_weight"]

    return total_weight


def get_path_bw(topology, path):
    e2e_bw = np.inf
    for i in range(len(path) - 1):
        link_bw = topology.edges[path[i], path[i+1]]["bw"]
        if link_bw < e2e_bw:
            e2e_bw = link_bw

    return e2e_bw


def shortest_path(topology, request, feasibility_check_function, weight_function):
    weight_function(topology, request.sfc, feasibility_check_function)
    path = nx.shortest_path(topology, source=request.src, target=request.dst, weight="routing_weight")

    if debug > 2:
        print("shortest_path: path = ", path)

    total_weight = get_path_weight(topology, path)
    if total_weight >= WEIGHT_BIG_M:
        return False, None
    else:
        return True, path


def k_shortest_paths(topology, request, k, feasibility_check_function, weight_function):
    weight_function(topology, request.sfc, feasibility_check_function)
    kpaths = list(islice(nx.shortest_simple_paths(topology, request.src, request.dst, weight="routing_weight"), k))

    if debug > 2:
        print("k_shortest_paths: kpaths = ", kpaths)
    res = []

    for path in kpaths:
        if debug > 2:
            print("k_shortest_paths: path = ", path)
        
        total_weight = get_path_weight(topology, path)
        
        if debug> 2:
            print("\t total_weight = ", total_weight)
        
        if total_weight >= WEIGHT_BIG_M:
            '''Path is not feasible '''
            pass
        else:
            res.append(path)
        
    if len(res) == 0:
        return False, None
    else:
        return True, res

