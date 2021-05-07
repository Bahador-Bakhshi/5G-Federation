
import network
import graph
import environment
import requests

from graph import debug 

class WidestKpath:
    k = 5
    class Observation:
        def __init__(self, topology, request):
            self.topology = topology
            self.request  = request

    def observer(topology, request):
        return WidestKpath.Observation(topology, request)

    def policy(observation):
        topology = observation.topology
        request  = observation.request

        is_path, kpaths = graph.k_shortest_paths(topology, request, WidestKpath.k, graph.bw_feasibility, graph.link_weight_one)
        
        if is_path:
            max_bw = 0
            widest_path = None
            for path in kpaths:
                bw = graph.get_path_bw(topology, path)
                if bw > max_bw:
                    widest_path = path
                    max_bw = bw

            request.path = widest_path
            return environment.Actions.accept
        else:
            return environment.Actions.reject


class FixKpathSinglePair:
    k = 10

    obs_fields_num = k + 2 + 1  # kpath_bw src dst sfc_id

    all_pairs_kpaths = {}

    def find_all_pair_kpaths(topology, src_dst_list):
        for src_dst in src_dst_list:
            src = src_dst[0]
            dst = src_dst[1]

            dummy_sfc = requests.SFC_e2e_bw(0, [], 0)
            dummy_req = requests.Request(src, dst, 0, dummy_sfc, 0, 0)
        
            is_path, kpaths = graph.k_shortest_paths(topology, dummy_req, FixKpathSinglePair.k, graph.bw_feasibility, graph.link_weight_one)
            FixKpathSinglePair.all_pairs_kpaths[(src, dst)] = kpaths.copy()
        
        if debug > 2:
            print("find_all_pair_kpaths: ", FixKpathSinglePair.all_pairs_kpaths)  

    class Observation:

        def __init__(self, kpaths_bw, request):
            self.kpaths_bw = kpaths_bw.copy()
            self.request   = request

        def __str__(self):
            return "req = "+ str(self.request) +", kpaths_bw = "+ str(self.kpaths_bw)

    def observer(topology, request):
        if debug > 2:
            print("observer: request = ", request)
        
        kpaths = FixKpathSinglePair.all_pairs_kpaths[(request.src, request.dst)]
        
        if debug > 2:
            print("observer: kpaths = ", kpaths)
        
        kpaths_bw = []
        for path in kpaths:
            bw = graph.get_path_bw(topology, path)
            kpaths_bw.append(bw)

        return FixKpathSinglePair.Observation(kpaths_bw, request)

    def policy(observation):
        pass


class FixKpathAllPairs:
    k = 10

    obs_fields_num = 0

    all_pairs_kpaths = {}

    def find_all_pair_kpaths(topology, src_dst_list):
        for src_dst in src_dst_list:
            src = src_dst[0]
            dst = src_dst[1]

            dummy_sfc = requests.SFC_e2e_bw(0, [], 0)
            dummy_req = requests.Request(src, dst, 0, dummy_sfc, 0, 0)
        
            is_path, kpaths = graph.k_shortest_paths(topology, dummy_req, FixKpathAllPairs.k, graph.bw_feasibility, graph.link_weight_one)
            FixKpathAllPairs.all_pairs_kpaths[(src, dst)] = kpaths.copy()
        
        if debug > 2:
            print("find_all_pair_kpaths: ", FixKpathAllPairs.all_pairs_kpaths)  

        FixKpathAllPairs.obs_fields_num = len(src_dst_list) * FixKpathAllPairs.k + 2 + 1  # kpath_bw for all pairs + src + dst + sfc_id

    class Observation:

        def __init__(self, kpaths_bw, request):
            self.kpaths_bw = kpaths_bw.copy()
            self.request   = request

        def __str__(self):
            return "req = "+ str(self.request) +", kpaths_bw = "+ str(self.kpaths_bw)

    def observer(topology, request):
        
        if debug > 2:
            print("observer:  request = ", request)

        all_kpaths_bw = {}
        for (src, dst) in FixKpathAllPairs.all_pairs_kpaths.keys():
            kpaths = FixKpathAllPairs.all_pairs_kpaths[(src, dst)]
            
            if debug > 2:
                print("observer: (src, dst) = ", src, dst, " kpaths = ", kpaths)
            
            kpaths_bw = []
            for path in kpaths:
                bw = graph.get_path_bw(topology, path)
                kpaths_bw.append(bw)

            all_kpaths_bw[(src,dst)] = kpaths_bw.copy()

        observation = FixKpathAllPairs.Observation(all_kpaths_bw, request)
        
        if debug > 2:
            print("observer: observation = ", observation)
        
        return observation

    def policy(observation):
        pass


