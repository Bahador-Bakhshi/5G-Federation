from enum import IntEnum
import numpy as np
import sys 
import heapq
import Environment

def print_reqs(reqs):
    for i in range(len(reqs)):
        if Environment.verbose:
            Environment.debug(reqs[i])


def generate_class_req_set(service, load, time, class_id):
    t = 0
    all_req = []
    
    while t <= time:
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        all_req.append(Environment.Request(service.cpu, t, t + life, service.revenue, class_id))

    #print_reqs(all_req)
    return all_req


def generate_req_set(time):
    all_class_reqs = []
    
    total_n = 0
    for service in Environment.domain.services:
        class_id = 0
        for load in Environment.traffic_loads:
            if service.nsid == load.service.nsid:
                req_list = generate_class_req_set(service, load, time, class_id)
                total_n += len(req_list)
                all_class_reqs.append(req_list)
            class_id += 1

    j = 0
    req_set = [None] * total_n
    for i in range(len(all_class_reqs)):
        for k in range(len(all_class_reqs[i])):
            req_set[j] = all_class_reqs[i][k]
            j += 1

    req_set.sort(key=lambda x: x.st)
    cut_num = 0
    for i in range(len(req_set)):
        if req_set[i].st <= time:
            cut_num += 1
        else:
            break

    result = req_set[:cut_num]

    for cid in range(2):
        life = 0
        cnt = 0
        delay = 0
        last_st = 0
        for r in result:
            if r.class_id == cid:
                cnt += 1
                life += r.dt - r.st
                delay += r.st - last_st
                last_st = r.st

        #print("cid = ", cid,", cnt = ", cnt,", life = ", life / cnt, ", delay = ", delay / cnt)

    return result


class Env:
    action_space = None
    server_size = 0
    episode_len = 0
    capacity = 0
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, size, eplen):
        self.action_space = Environment.Actions
        self.server_size  = size
        self.episode_len = eplen
        self.events = []

    def start(self):
        if Environment.verbose:
            Environment.debug("env start")
        self.capacity = self.server_size
        self.alives = [0 for i in range(Environment.total_classes)]
        
        self.demands = generate_req_set(self.episode_len)
        #print_reqs(self.demands)

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        #print_events(self.events)
        event = heapq.heappop(self.events)
        #print_events(self.events)

        self.active_reqs = [0 for i in range(Environment.total_classes)]
        self.active_reqs[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = (tuple(self.alives), tuple(self.active_reqs))

        return state

    def stop(self):
        if Environment.verbose:
            Environment.debug("env stop")
        return

    def reset(self):
        if Environment.verbose:
            Environment.debug("env reset")
        self.stop()
        return self.start()
    
    def step(self, state, action):
        reward = 0
        if Environment.verbose:
            Environment.debug("===========  env step ==================")
            Environment.debug("s = ", state, ", a = ", action)
        current_alives = state[0]
        current_requests = state[1]
        current_capacity = compute_capacity(current_alives)
        
        if action == Environment.Actions.no_action:
            if Environment.verbose:
                Environment.debug("no action")
            reward = 0

        elif action == Environment.Actions.reject: #reject
            if Environment.verbose:
                Environment.debug("reject")
            reward = 0

        elif action == Environment.Actions.accept: #accept
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] != 0:
                    count += 1
            
            if count > 1:
                error("Error in requests = ", current_requests)
                sys.exit()

            if count == 0: #there is no requst to accept
                error("Invalid action")
                sys.exit()
            else:
                req = self.arriaved_demand
                self.arriaved_demand = None
                    
                if Environment.verbose:
                    Environment.debug("Try to accept: req = ", req)

                if self.capacity < req.w:
                    #cannot accept
                    if Environment.verbose:
                        Environment.debug("\t cannot accept")
                    reward = -1 * np.inf
                else:
                    if Environment.verbose:
                        Environment.debug("\t accepted")
                    reward = req.rev
                    self.capacity -= req.w
                    self.alives[req.class_id] += 1
                    event = Event(0, req.dt, req) #add the departure event
                    heapq.heappush(self.events, event)
        
        elif action == Environment.Actions.federate: #federate
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] != 0:
                    count += 1
            
            if count > 1:
                error("Error in requests = ", current_requests)
                sys.exit()

            if count == 0: #there is no requst to accept
                error("Invalid action")
                sys.exit()
            else:
                req = self.arriaved_demand
                self.arriaved_demand = None
                
                if Environment.verbose:
                    Environment.debug("Try to federate: req = ", req)

                provider_domain = Environment.providers[0] # in this version, there is only one provider
                if Environment.verbose:
                    Environment.debug("\t federated")

                reward = req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
                #FIXME: update iner-domain link usage
                #FIXME: update number of federated requests

        else:
            error("Unknown action")
            sys.exit()

        next_state = None
        #print_events(self.events)
        if len(self.events) == 0:
            for i in range(len(self.alives)):
                if self.alives[i] != 0:
                    error("bug in the last state")
                    sys.exit()
            
            next_state = (tuple([0 for i in range(Environment.total_classes)]), tuple([0 for i in range(Environment.total_classes)]))
            return next_state, reward, 1

        #generate the next state
        event = heapq.heappop(self.events)
        if Environment.verbose:
            Environment.debug("event: type = ", event.event_type ,", req = ", event.req)

        if event.event_type == 0: #departure, update the nework
            self.capacity += event.req.w
            self.alives[event.req.class_id] -= 1
                
            requests = [0 for i in range(Environment.total_classes)]
            next_state = (tuple(self.alives), tuple(requests))
                
            if len(self.events) == 0:
                if Environment.verbose:
                    Environment.debug("done = 1, next_state = ", next_state)
                done = 1
            else:
                done = 0
        
        else: #new arrival
            requests = [0 for i in range(Environment.total_classes)]
            requests[event.req.class_id] = 1
            self.arriaved_demand = event.req

            next_state = (tuple(self.alives), tuple(requests))
            done = 0
        
        if Environment.verbose:
            Environment.debug("************  env step *************")
        return next_state, reward, done


def get_valid_actions(state):
    alives = state[0]
    requests = state[1]
    actions = []

    arrived = 0
    for i in range(len(requests)):
        arrived += requests[i]

    if arrived > 1:
        error("get_valid_actions: Error in state")
        error("state = ", state)
        sys.exit()

    if arrived == 0:
        #agent cannot do anything
        actions.append(Environment.Actions.no_action)

    if arrived == 1:
        actions.append(Environment.Actions.reject)
        actions.append(Environment.Actions.federate)
        tmp_alives = [0] * len(alives)
        for i in range(len(tmp_alives)):
            tmp_alives[i] = alives[i] + requests[i]
        
        if compute_capacity(tmp_alives) >= 0:
            actions.append(Environment.Actions.accept)
  
    if Environment.verbose:
        Environment.debug("Valid actions = ", actions)
    return actions

class Event:
    event_type = 0 # 0 for departure 1 for arrival
    time = 0
    req = None

    def __init__(self, ty, ti, rq):
        self.event_type = ty
        self.time = ti
        self.req = rq

    def __lt__(self, other):
        return self.time <= other.time

def print_events(events):
    debug("----------------------------")
    for i in range(len(events)):
        e = events[i]
        debug("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(alives):
    capacity = Environment.domain.total_cpu
    for i in range(Environment.total_classes):
        capacity -= alives[i] * Environment.traffic_loads[i].service.cpu

    return capacity


