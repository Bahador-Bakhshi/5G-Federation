
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


def link_weight_one(topology):
    for e in topology.edges:
        topology.edges[e[0],e[1]]["routing_weight"] = 1


def shortest_path(topology, src, dst, weight_function):
    weight_function(topology)
    return nx.shortest_path(topology, source=src, target=dst, weight="routing_weight")

    
