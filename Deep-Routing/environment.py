
import numpy as np
import sys
import heapq
from enum import IntEnum

import requests
import network

debug = True

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

    def __init__(self, topology, observation_maker, episode_len = 0, test_requests = None):
        self.topology = topology
        self.observer = observation_maker
        self.episode_len = episode_len
        self.events = []
        self.in_test_mode = False
        if test_requests != None:
            self.all_requests = test_requests
            self.in_test_mode = True

    def stop(self):
        print("Environment stop")
        return

    def reset(self):
        print("Environment reset")
        self.stop()
        return self.start()

    def start(self):
        print("Environment start: begin ---------------->>>>>")

        if self.in_test_mode == False:
            src_dst_list, req_num, sfcs_list = requests.generate_traffic_load_config(self.topology)

            self.all_requests = requests.generate_all_requests(src_dst_list, req_num, sfcs_list)

        for req in self.all_requests:
            self.events.append(Event(1, req.t_start, req))
        
        heapq.heapify(self.events)
        if debug:
            print_events(self.events)

        self.current_event = heapq.heappop(self.events)
        
        observation = self.observer(self.topology, self.current_event.req)

        print("Environment start: <<<<-----------------  end")

        return observation

    
    def step(self, action):
        print("Environment step: *************** >>>>>")
        print("action = ", action)
        
        reward = 0
        done   = 0
        
        if action == Actions.reject:
            #no thing to do
            pass
        elif action == Actions.accept:
            network.deploy_request(self.topology, self.current_event.req)
            reward = 1

            event = Event(0, self.current_event.req.t_end, self.current_event.req)
            heapq.heappush(self.events, event)


        else:
            print("Unknown action")
            sys.exit(-1)


        if len(self.events) > 0:
            self.current_event = heapq.heappop(self.events)
            while self.current_event.event_type == 0:
                network.free(self.topology, self.current_event.req)
                if len(self.events) > 0:
                    self.current_event = heapq.heappop(self.events)
                else:
                    break

        if len(self.events) == 0:
            if network.is_empty(self.topology) == False:
                print("At the end, network is NOT empty")
                sys.exit(-1)
            done = 1

        
        observation = self.observer(self.topology, self.current_event.req)
        
        print("Environment step: <<<<************** end")
        
        return observation, reward, done

