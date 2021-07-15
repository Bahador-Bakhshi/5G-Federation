import sys
import network
import graph
import environment
import requests
import tensorflow as tf

from graph import debug 

class WidestKpath:
    k = 5
    class Observation:
        def __init__(self, topology, request):
            self.topology = topology
            self.request  = request

    def observer(topology, request):
        return WidestKpath.Observation(topology, request), 0

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
    k = 30

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
            print("observer: request = ", request)

        all_kpaths_bw = {}
        all_kpaths_util = {}

        for (src, dst) in FixKpathAllPairs.all_pairs_kpaths.keys():
            kpaths = FixKpathAllPairs.all_pairs_kpaths[(src, dst)]
            
            if debug > 2:
                print("observer: (src, dst) = ", src, dst, " kpaths = ", kpaths)
            
            kpaths_bw = [0] * FixKpathAllPairs.k
            index = 0
            #kpaths_org_bw = [] it was tried to adjust gamma according to load!!!!!
            for path in kpaths:
                bw = graph.get_path_bw(topology, path)
                kpaths_bw[index] = bw
                index += 1

                #org_bw = graph.get_path_org_bw(topology, path)
                #kpaths_org_bw.append(org_bw)

            all_kpaths_bw[(src,dst)] = kpaths_bw.copy()

            '''
            util = 0.0
            for i in range(len(kpaths_bw)):
                util += (1.0 * kpaths_bw[i]) / kpaths_org_bw[i]
            util /= len(kpaths_bw)

            all_kpaths_util[(src, dst)] = util
            '''

        observation = FixKpathAllPairs.Observation(all_kpaths_bw, request)
        
        if debug > 2:
            print("observer: observation = ", observation)
        
        discount = 0
        '''
        for (src, dst) in all_kpaths_util.keys():
            discount += all_kpaths_util[(src,dst)]
        discount /= len(all_kpaths_util)
        
        discount = 1.0 - discount 
        print("observer: discount = ", discount)
        '''

        return observation, discount

    def policy(observation):
        pass



class FEkpath:
    k = 10

    obs_fields_num = 0

    all_pairs_kpaths = {}

    def find_all_pair_kpaths(topology, src_dst_list):
        for src_dst in src_dst_list:
            src = src_dst[0]
            dst = src_dst[1]

            dummy_sfc = requests.SFC_e2e_bw(0, [], 0)
            dummy_req = requests.Request(src, dst, 0, dummy_sfc, 0, 0)
        
            is_path, kpaths = graph.k_shortest_paths(topology, dummy_req, FEkpath.k, graph.bw_feasibility, graph.link_weight_one)
            FEkpath.all_pairs_kpaths[(src, dst)] = kpaths.copy()
        
        if debug > 2:
            print("find_all_pair_kpaths: ", FEkpath.all_pairs_kpaths)

        '''
        Structure of the observation:
        1) one_hot coding for src
        2) one_hot coding for dst
        3) one_hot coding for bw level
        4) k * per action net state:
            4-1) per src-dst pair:
                4-1-1) k path bw
        '''
        src_dst_one_hot = tf.one_hot(0, topology.number_of_nodes() + 1)
        bw_levels_one_hot = tf.one_hot(0, requests.traffic_config["max_sfc_bw"] + 1)
        FEkpath.obs_fields_num =  2 * len(src_dst_one_hot) + len(bw_levels_one_hot) + FEkpath.k * (len(src_dst_list) * FEkpath.k)

    class Observation:
        def __init__(self, all_kpaths_bw_after_action, request, topology):
            self.all_kpaths_bw_after_action = []
            for kpaths_bw in all_kpaths_bw_after_action:
                self.all_kpaths_bw_after_action.append(kpaths_bw.copy())

            self.request = request
            self.topology = topology

        def __str__(self):
            return "req = "+ str(self.request) +", all_kpaths_bw_after_action = "+ str(self.all_kpaths_bw_after_action)

    def observer(topology, request):
        
        if debug > 2:
            print("observer: request = ", request)

        all_kpaths_bw_after_action = []
        this_request_kpaths = FEkpath.all_pairs_kpaths[(request.src, request.dst)]

        for action in range(FEkpath.k):
            # apply the action
            is_feasible = False
            if action < len(this_request_kpaths):
                is_feasible = network.route_path(topology, this_request_kpaths[action], request.sfc)

            # get the k paths bw for all src-dst pairs
            all_pairs_kpaths_bw = {}
            for (src, dst) in FEkpath.all_pairs_kpaths.keys():
                kpaths = FEkpath.all_pairs_kpaths[(src, dst)]
            
                if debug > 2:
                    print("observer: (src, dst) = ", src, dst, " kpaths = ", kpaths)
            
                kpaths_bw = [0] * FEkpath.k
                index = 0
                for path in kpaths:
                    bw = graph.get_path_bw(topology, path)
                    kpaths_bw[index] = bw
                    index += 1

                all_pairs_kpaths_bw[(src,dst)] = kpaths_bw.copy()
            all_kpaths_bw_after_action.append(all_pairs_kpaths_bw.copy())
            
            # undo action
            if is_feasible:
                network.free_path(topology, this_request_kpaths[action], request.sfc)
            else:
                pass

        observation = FEkpath.Observation(all_kpaths_bw_after_action, request, topology)
        
        if debug > 2:
            print("observer: observation = ", observation)
        
        discount = 0
        return observation, discount

    def policy(observation):
        pass


