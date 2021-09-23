
import numpy as np
import sys
import heapq
from enum import IntEnum

import requests
import network
from graph import debug

class Actions(IntEnum):
    reject    = 0
    accept    = 1

class Event:
    event_type = 0 # 0 for departure 1 for arrival
    time = 0
    req = None

    def __init__(self, ty, ti, rq):
        self.event_type = ty
        self.time = ti
        self.req = rq

    def __lt__(self, other):
        return self.time < other.time


def print_events(events):
    for e in events:
        print("type = ", e.event_type ,", req = ", e.req)


class Environment:

    def __init__(self, topology, observation_maker, src_dst_list = None, req_num = 0, sfcs_list = 0, number_of_paths = 0):
        self.topology = topology
        self.observer = observation_maker
        self.episode_len = req_num
        self.events = []
        self.in_test_mode = False
        self.src_dst_list = src_dst_list
        self.req_num = req_num
        self.sfcs_list = sfcs_list

        self.global_pairs_paths_actives = {}
        if number_of_paths > 0:
            for (src, dst) in src_dst_list:
                paths_actives = []
                for k in range(number_of_paths):
                    this_path_actives = [0] * len(sfcs_list)
                    paths_actives.append(this_path_actives.copy())
                self.global_pairs_paths_actives[(src,dst)] = paths_actives.copy()
    
    def set_test_requests(self, test_requests):
        self.all_requests = test_requests
        self.in_test_mode = True

    def stop(self):
        self.events.clear()
        network.reset_topology(self.topology)
        if debug > 2:
            print("Environment stop")
        return

    def reset(self):
        if debug > -1:
            print("Environment reset")
        print("RESET !!!!")
        self.stop()
        return self.start()

    def start(self):
        self.events.clear()
        if debug > 1:
            print("Environment start: begin ---------------->>>>>")
            print("in_test_mode = ", self.in_test_mode)
            print("req_num = ", self.req_num)
        
        if self.in_test_mode == False:
            self.all_requests = requests.generate_all_requests(self.src_dst_list, self.req_num, self.sfcs_list)

        for req in self.all_requests:
            self.events.append(Event(1, req.t_start, req))
        
        heapq.heapify(self.events)
        if debug > 2:
            print_events(self.events)

        self.current_event = heapq.heappop(self.events)
        
        observation, discount = self.observer(self.topology, self.src_dst_list, self.current_event.req)
        
        if debug > 1:
            print("Environment start: <<<<-----------------  end")

        return observation, discount

    
    def step(self, action):
        if debug > 1:
            print("Environment step: start **************>>>>")
            print("action = ", action)
        
        reward = 0
        done   = 0
        
        if action == Actions.reject:
            #no thing to do
            pass
        elif action == Actions.accept:
            feasible = network.deploy_request(self.topology, self.current_event.req)
            if feasible:
                self.global_pairs_paths_actives[(self.current_event.req.src, self.current_event.req.dst)][self.current_event.req.path_id][self.current_event.req.sfc.sfc_id] += 1
                reward = self.current_event.req.sfc.bw
                #reward = 1.0
                event = Event(0, self.current_event.req.t_end, self.current_event.req)
                heapq.heappush(self.events, event)

        else:
            print("Unknown action")
            sys.exit(-1)

        if len(self.events) > 0:
            self.current_event = heapq.heappop(self.events)
            if debug > 2:
                print_events([self.current_event])
            
            while self.current_event.event_type == 0:
                self.global_pairs_paths_actives[(self.current_event.req.src, self.current_event.req.dst)][self.current_event.req.path_id][self.current_event.req.sfc.sfc_id] -= 1
                network.free(self.topology, self.current_event.req)
                if len(self.events) > 0:
                    self.current_event = heapq.heappop(self.events)
                    if debug > 2:
                        print_events([self.current_event])
                else:
                    break

        if len(self.events) == 0:
            if network.is_empty(self.topology) == False:
                print("At the end, network is NOT empty")
                sys.exit(-1)
            done = 1

        
        observation, discount = self.observer(self.topology, self.current_event.req)
        
        if debug > 1:
            print("Environment step: <<<<************** end")
        
        return observation, 1 * reward, done, discount

