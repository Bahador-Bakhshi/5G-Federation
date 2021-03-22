
import numpy as np


traffic_config = None

class VNF:

    def __init__(self, vnf_type, cpu, ram):
        self.vnf_type = vnf_type
        self.cpu = cpu
        self.ram = ram 

ingress_vnf = VNF(-1, 0, 0)
egress_vnf  = VNF(-2, 0, 0)

class Virtual_Link:

    def __init__(self, src, dst, bw):
        self.src = src
        self.dst = dst
        self.bw = bw


class SFC_per_link_bw:

    def __init__(self, vnfs, vlinks):
        self.vnfs = vnfs
        self.vlinks = vlinks


class SFC_e2e_bw:

    def __init__(self, sfc_id, vnfs, bw):
        self.sfc_id = sfc_id
        self.bw = bw
        
        self.vnfs = vnfs.copy()
        self.vnfs.insert(0, ingress_vnf)
        self.vnfs.append(egress_vnf)
        
        self.vlinks = []
        for i in range(len(self.vnfs) - 1):
            self.vlinks.append(Virtual_Link(self.vnfs[i], self.vnfs[i+1], bw))
        

class Request:

    def __init__(self, src, dst, sfc, t_start, t_end):
        self.src = src
        self.dst = dst
        self.sfc = sfc
        self.t_start = t_start
        self.t_end   = t_end


def generate_vnfs():
    type_num = traffic_config["max_vnf_types"]
    vnfs_list = []
    
    for i in range(type_num):
        cpu = np.random.choice(np.arange(traffic_config["min_vnf_cpu"], traffic_config["max_vnf_cpu"] + 1)) * traffic_config["vnf_cpu_scale"]
        ram = np.random.choice(np.arange(traffic_config["min_vnf_ram"], traffic_config["max_vnf_ram"] + 1)) * traffic_config["vnf_ram_scale"]

        vnf = VNF(i, cpu, ram)
        vnfs_list.append(vnf)

    return vnfs_list


def print_vnfs_list(vnfs_list):
    for vnf in vnfs_list:
        print("VNF: type = ", vnf.vnf_type, "CPU = ", vnf.cpu, ", RAM = ", vnf.ram)


def generate_sfcs(vnfs_list):
    sfcs_num = traffic_config["max_sfc_num"]
    sfcs_list = []

    for i in range(sfcs_num):
        vnfs_num = np.random.choice(np.arange(traffic_config["min_vnf_per_sfc"], traffic_config["max_vnf_per_sfc"] + 1))
            
        sfc_vnfs = []
        for j in range(vnfs_num):
            vnf = vnfs_list[np.random.choice(len(vnfs_list))]
            sfc_vnfs.append(vnf)
        
        bw = np.random.choice(np.arange(traffic_config["min_sfc_bw"], traffic_config["max_sfc_bw"] + 1)) * traffic_config["sfc_bw_scale"]
        sfc = SFC_e2e_bw(i, sfc_vnfs, bw)

        sfcs_list.append(sfc)

    return sfcs_list

def print_vlinks(vlinks):
    for vl in vlinks:
        print("\t (", vl.src.vnf_type, ", ", vl.dst.vnf_type, "): ", vl.bw)

def print_sfcs_list(sfcs_list):
    for sfc in sfcs_list:
        print("SFC: id = ", sfc.sfc_id, "bw = ", sfc.bw)
        print_vnfs_list(sfc.vnfs)
        print_vlinks(sfc.vlinks)
        print("-----------------------------")

def generate_src_dst_list(nodes_num, pairs_num):
    src_dst_list = []
    for i in range(pairs_num):
        src = 1 + np.random.choice(nodes_num)
        dst = src
        while src == dst:
            dst = 1 + np.random.choice(nodes_num)
        src_dst_list.append((src, dst))

    return src_dst_list
   

def generate_per_pair_requests(src, dst, pair_index, num, sfcs):
    lam = traffic_config["traffic_rates"][pair_index]["lambda"]
    mu  = traffic_config["traffic_rates"][pair_index]["mu"]

    reqs = []
    t = 0
    for i in range(num):
        t += np.random.exponential(1.0 / lam)
        life = np.random.exponential(1.0 / mu)
        sfc = sfcs[np.random.choice(len(sfcs))]
        req = Request(src, dst, sfc, t, t + life)
        reqs.append(req)
    
    return reqs


def generate_all_requests(src_dst_list, num, sfcs):
    
    all_requests = []
    index = 0
    for (src, dst) in src_dst_list:
        reqs = generate_per_pair_requests(src, dst, index, num, sfcs)
        index += 1

        all_requests += reqs


    all_requests.sort(key=lambda x: x.t_start)
    result = all_requests[:num]

    return result


def print_requests(all_requests):
    print("**********************")
    for req in all_requests:
        print("Request: src = ", req.src, ", dst = ", req.dst, ", sfc = ", req.sfc.sfc_id, ", t_start = ", req.t_start, ", t_end = ", req.t_end)


def generate_traffic_load_config(topology):
    vnfs_list = generate_vnfs()
    #print_vnfs_list(vnfs_list)

    sfcs_list = generate_sfcs(vnfs_list)
    #print_sfcs_list(sfcs_list)

    src_dst_list = generate_src_dst_list(len(topology.nodes), traffic_config["max_src_dst_pairs"])

    return src_dst_list, traffic_config["request_num"], sfcs_list


