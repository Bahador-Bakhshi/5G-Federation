from enum import IntEnum
import numpy as np
import sys 
import heapq


# Classes
class NFV_NS:
    nsid = 0
    cpu = 0
    revenue = 0

    def __init__(self, nsid, cpu, revenue):
        self.nsid = nsid
        self.cpu  = cpu
        self.revenue = revenue


class Local_Domain:
    total_cpu = 0
    services = None

    def __init__(self, cpu):
        self.total_cpu = cpu
        self.services = []

    def add_service(self, service):
        self.services.append(service)


class Traffic_Load:
    service = None
    lam  = 0
    mu   = 0

    def __init__(self, nsid, lam, mu):
        for service in domain.services:
            if service.nsid == nsid:
                self.service = service
        self.lam  = lam
        self.mu   = mu


class Providers:
    pid = 0
    federation_costs = None

    def __init__(self, pid):
        self.pid = pid

    def add_fed_cost(nsid, cost):
        for service in domain.services:
            if service.nsid == nsid:
                self.federation_costs[service] = cost


class Actions(IntEnum):
    no_action = 0
    reject = 1
    accept = 2

# Global Variables

domain = None
traffic_loads = None
providers = None 
total_actions = len(Actions)
total_classes = 0

class Request:
    w   = 0
    st  = 0
    dt  = 0
    rev = 0
    class_id = 0

    def __init__(self, w, st, dt, rev, index):
        self.w  = w
        self.st = st
        self.dt = dt
        self.rev= rev
        self.class_id = index

    def __str__(self):
        return "w = "+ str(self.w) +" st = "+ str(self.st) +" dt = "+ str(self.dt) +" rev = "+ str(self.rev) +", index = "+ str(self.class_id)


def print_reqs(reqs):
    for i in range(len(reqs)):
        print(reqs[i])


def generate_class_req_set(service, load, time):
    t = 0
    all_req = []
    
    while t <= time:
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        all_req.append(Request(service.cpu, t, t + life, service.revenue, service.nsid))

    #print_reqs(all_req)
    return all_req


def generate_req_set(time):
    all_class_reqs = []
    
    total_n = 0
    for service in domain.services:
        for load in traffic_loads:
            if service.nsid == load.service.nsid:
                req_list = generate_class_req_set(service, load, time)
                total_n += len(req_list)
                all_class_reqs.append(req_list)

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

    return req_set[:cut_num]

class Env:
    action_space = None
    server_size = 0
    episode_len = 0
    capacity = 0
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, size, eplen):
        self.action_space = Actions
        self.server_size  = size
        self.episode_len = eplen
        self.events = []

    def start(self):
        print("env start")
        self.capacity = self.server_size
        self.alives = [0 for i in range(total_classes)]
        
        self.demands = generate_req_set(self.episode_len)
        print_reqs(self.demands)

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        #print_events(self.events)
        event = heapq.heappop(self.events)
        #print_events(self.events)

        self.active_reqs = [0 for i in range(total_classes)]
        print("event.req.class_id = ", event.req.class_id)
        self.active_reqs[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = (tuple(self.alives), tuple(self.active_reqs))

        return state

    def stop(self):
        print("env stop")
        return

    def reset(self):
        print("env reset")
        self.stop()
        return self.start()
    
    def step(self, state, action):
        reward = 0
        print("===========  env step ==================")
        print("s = ", state, ", a = ", action)
        current_alives = state[0]
        current_requests = state[1]
        current_capacity = compute_capacity(current_alives)
        
        '''
        #check state correctness
        if current_capacity != self.capacity:
            print("Error in capacity")
            sys.exit()
        for i in range(len(current_alives)):
            if current_alives[i] != self.alives[i]:
                print("Error in alives")
                sys.exit()
        for i in range(len(current_requests)):
            if current_requests[i] != self.requests[i]:
                print("Error in requests")
                sys.exit()
        '''
        if action == Actions.no_action:
            print("no action")
            reward = 0

        elif action == Actions.reject: #reject
            print("reject")
            reward = 0

        elif action == Actions.accept: #accept
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] != 0:
                    count += 1
            
            if count > 1:
                print("Error in requests = ", current_requests)
                sys.exit()

            if count == 0: #there is no requst to accept
                print("Invalid action")
                sys.exit()
            else:
                req = self.arriaved_demand
                self.arriaved_demand = None

                print("Try to accept: req = ", req)

                if self.capacity < req.w:
                    #cannot accept
                    print("\t cannot accept")
                    reward = -1 * np.inf
                else:
                    print("\t accepted")
                    reward = req.rev
                    self.capacity -= req.w
                    self.alives[req.class_id] += 1
                    event = Event(0, req.dt, req) #add the departure event
                    heapq.heappush(self.events, event)
        else:
            print("Unknown action")
            sys.exit()

        #print_events(self.events)
        if len(self.events) == 0:
            return None, 0, 1

        #generate the next state
        event = heapq.heappop(self.events)
        print("event: type = ", event.event_type ,", req = ", event.req)

        if event.event_type == 0: #departure, update the nework
            self.capacity += event.req.w
            self.alives[event.req.class_id] -= 1
                
            requests = [0 for i in range(total_classes)]
            state = (tuple(self.alives), tuple(requests))
                
            if len(self.events) == 0:
                done = 1
            else:
                done = 0
        
        else: #new arrival
            requests = [0 for i in range(total_classes)]
            requests[event.req.class_id] = 1
            self.arriaved_demand = event.req

            state = (tuple(self.alives), tuple(requests))
            done = 0

        
        print("************  env step *************")
        return state, reward, done


def get_valid_actions(state):
    alives = state[0]
    requests = state[1]
    actions = []

    arrived = 0
    for i in range(len(requests)):
        arrived += requests[i]

    if arrived > 1:
        print("get_valid_actions: Error in state")
        print("state = ", state)
        sys.exit()

    if arrived == 0:
        #agent cannot do anything
        actions.append(Actions.no_action)

    if arrived == 1:
        actions.append(Actions.accept)
        actions.append(Actions.reject)
  
    print("Valid actions = ", actions)
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
    print("----------------------------")
    for i in range(len(events)):
        e = events[i]
        print("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(alives):
    capacity = domain.total_cpu
    for i in range(total_classes):
        capacity -= alives[i] * domain.services[i].cpu

    return capacity


