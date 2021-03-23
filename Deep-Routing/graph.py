
import networkx as nx

def get_max_flow(topology, src, dst):
    flow_value, flow_dict = nx.maximum_flow(topology, src, dst, capacity="bw")
    return flow_value, flow_dict


def test_max_flow(topology):
    print(topology.nodes)
    for u in range(len(topology.nodes)):
        for v in range(len(topology.nodes)):
            if u != v:
                flow_value, flow_dict = get_max_flow(topology, u + 1, v + 1)
                #print("maxflow: src = ", u + 1, ", dst = ", v + 1, ", flow_value = ", flow_value, ", flow_dict = ", flow_dict)
                print("maxflow: src = ", u + 1, ", dst = ", v + 1, ", flow_value = ", flow_value)


WEIGHT_BIG_M = 1000000000.00
def link_weight_one(topology, sfc, feasibility_check):
    for e in topology.edges:
        topology.edges[e[0],e[1]]["routing_weight"] = 1 if feasibility_check(topology, e, sfc) else WEIGHT_BIG_M


    print("link_weight_one: sfc.bw = ", sfc.bw)
    print(topology.edges(data = True))


def link_weight_capacity(topology, sfc, feasibility_check):
    for e in topology.edges:
        bw = topology.edges[e[0],e[1]]["bw"]
        topology.edges[e[0],e[1]]["routing_weight"] = 1.0 / bw if feasibility_check(topology, e, sfc) else WEIGHT_BIG_M
    
    print(topology.edges(data=True))


def bw_feasibility(topology, e, sfc):
    return True if topology.edges[e[0], e[1]]["bw"] >=  sfc.bw else False


def shortest_path(topology, request, feasibility_check_function, weight_function):
    weight_function(topology, request.sfc, feasibility_check_function)
    path = nx.shortest_path(topology, source=request.src, target=request.dst, weight="routing_weight")

    print("shortest_path: path = ", path)

    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += topology.edges[path[i], path[i+1]]["routing_weight"]
        print("shortest_path: total_weight = ", total_weight)

    if total_weight >= WEIGHT_BIG_M:
        return False, None
    else:
        return True, path

    
