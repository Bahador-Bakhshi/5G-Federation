
import networkx as nx

def get_max_flow(topology, src, dst):
    src = str(src)
    dst = str(dst)

    flow_value, flow_dict = nx.maximum_flow(topology, src, dst, capacity="bw")
    return flow_value, flow_dict

def test_max_flow(topology):
    print(topology.nodes)
    for u in range(len(topology.nodes)):
        for v in range(len(topology.nodes)):
            if u != v:
                flow_value, flow_dict = get_max_flow(topology, u + 1, v + 1)
                print("maxflow: src = ", u + 1, ", dst = ", v + 1, ", flow_value = ", flow_value, ", flow_dict = ", flow_dict)
