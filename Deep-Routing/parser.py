
import json
import math
import numpy as np 
import networkx as nx

import requests
import graph
import network

def bandwidth(src, dst, links, channels):
    #print("----------------------------------------------\n")
    #print("src: ", src, ", dst: ", dst)

    link = next((item for item in links if ((item["source_id"] == src) and (item["destination_id"] == dst))), None)
    #print("link: ", link, "\n") 

    link_channel = link["channel_id"]
    #print("channel: ", link_channel, "\n")
    
    channel = next((item for item in channels if (item["channel_id"] == link_channel)), None)
    bw = channel["data_rate"]
    #print("bandwith: ", bw, "\n")
    return bw


def generate_topo(filename):
    topo_file = open(filename)
    topo_json = json.load(topo_file)
    topo_file.close()

    channels = topo_json["channels"]
    links = topo_json["connections"]
    nodes = topo_json["nodes"]

    topo = nx.DiGraph()
    x_coord = {}
    y_coord = {}
    for i in range(len(nodes)):
        topo.add_node(nodes[i]["node_id"])
        x_coord[nodes[i]["node_id"]] = nodes[i]["x-coord"]
        y_coord[nodes[i]["node_id"]] = nodes[i]["y-coord"]

    nx.set_node_attributes(topo, x_coord, "xcoord")
    nx.set_node_attributes(topo, y_coord, "ycoord")

    max_bw = 0
    for i in range(len(links)):
        src = links[i]["source_id"]
        dst = links[i]["destination_id"]
        bwd = bandwidth(src, dst, links, channels)
        bwd = int(bwd)
        if bwd > max_bw:
            max_bw = bwd
        topo.add_edge(src, dst, bw = bwd, org_bw = bwd)
        if not ((dst, src) in topo.edges):
            topo.add_edge(dst, src, bw = bwd, org_bw = bwd)
 
    network.topo_max_bw = max_bw
    return topo


def parse_sfc_config(filename):
    config_file = open(filename)
    requests.traffic_config = json.load(config_file)
    config_file.close()
    

def main():

    topo = generate_topo("topo_03_1.json")
    print(topo.edges(data = True))

    parse_sfc_config("config.json")
    src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(topo)

    all_requests = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)

    #requests.print_requests(all_requests)

    graph.test_max_flow(topo)

    print("Shortest path 1 --> 3: \n \t", graph.shortest_path(topo, 1, 3, graph.link_weight_one))
    print("Shortest path 1 --> 3: \n \t", graph.shortest_path(topo, 1, 3, graph.link_weight_capacity))


if __name__ == "__main__":
    main()
