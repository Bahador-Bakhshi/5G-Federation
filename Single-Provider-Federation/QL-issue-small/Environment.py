from enum import IntEnum
import numpy as np
import sys 
import heapq

verbose = True
debug = print if verbose else lambda *a, **k: None
warning = print 
error = print


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

    def get_service(self, nsid):
        for s in self.services:
            if s.nsid == nsid:
                return s

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
        self.federation_costs = {}

    def add_fed_cost(self, nsid, cost):
        for service in domain.services:
            if service.nsid == nsid:
                self.federation_costs[service] = cost


class Actions(IntEnum):
    no_action = 0
    reject    = 1
    accept    = 2
    federate  = 3

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
        #debug(reqs[i])
        pass


def generate_class_req_set(service, load, time, class_id):
    t = 0
    all_req = []
    
    while t <= time:
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        all_req.append(Request(service.cpu, t, t + life, service.revenue, class_id))

    #print_reqs(all_req)
    return all_req


def generate_req_set(time):
    all_class_reqs = []
    
    total_n = 0
    for service in domain.services:
        class_id = 0
        for load in traffic_loads:
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
        self.action_space = Actions
        self.server_size  = size
        self.episode_len = eplen
        self.events = []

    def start(self):
        #debug("env start")
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
        self.active_reqs[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = (tuple(self.alives), tuple(self.active_reqs))

        return state

    def stop(self):
        #debug("env stop")
        return

    def reset(self):
        #debug("env reset")
        self.stop()
        return self.start()
    
    def step(self, state, action):
        reward = 0
        #debug("===========  env step ==================")
        #debug("s = ", state, ", a = ", action)
        current_alives = state[0]
        current_requests = state[1]
        current_capacity = compute_capacity(current_alives)
        
        if action == Actions.no_action:
            #debug("no action, in fact it is departure")
            index = -1
            for i in range(len(current_requests)):
                if current_requests[i] == -1:
                    if index != -1:
                        Error("Multiple departure")
                        sys.exit()
                    
                    index = i

            self.alives[index] -= 1
            self.capacity += traffic_loads[index].service.cpu
            reward = 0

        elif action == Actions.reject: #reject
            #debug("reject")
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] == -1:
                    error("Invalid state, both arrival and departure")
                    sys.exit()

                if current_requests[i] == 1:
                    count += 1
            
            if count > 1:
                error("Error in requests = ", current_requests)
                sys.exit()

            if count == 0: #there is no requst to accept
                error("Invalid action")
                sys.exit()

            req = self.arriaved_demand
            self.arriaved_demand = None
            reward = 0

        elif action == Actions.accept: #accept
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] == -1:
                    error("Invalid state, both arrival and departure")
                    sys.exit()

                if current_requests[i] == 1:
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

                #debug("Try to accept: req = ", req)

                if self.capacity < req.w:
                    #cannot accept
                    #debug("\t cannot accept")a
                    error("Erro in valid actions, cannot accept")
                    sys.exit()
                    reward = -1 * np.inf
                else:
                    #debug("\t accepted")
                    reward = req.rev
                    self.capacity -= req.w
                    self.alives[req.class_id] += 1
                    event = Event(0, req.dt, req) #add the departure event
                    heapq.heappush(self.events, event)
        
        elif action == Actions.federate: #federate
            
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] == -1:
                    error("Invalid state, both arrival and departure")
                    sys.exit()

                if current_requests[i] == 1:
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

                #debug("Try to federate: req = ", req)

                provider_domain = providers[0] # in this version, there is only one provider
                #debug("\t federated")

                reward = req.rev - provider_domain.federation_costs[traffic_loads[req.class_id].service]
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
            
            #next_state = (tuple([0 for i in range(total_classes)]), tuple([0 for i in range(total_classes)]))
            done = 1
            return next_state, reward, done 

        #generate the next state
        event = heapq.heappop(self.events)
        done = 0
        #debug("event: type = ", event.event_type ,", req = ", event.req)

        if event.event_type == 0: #departure, update the nework
            requests = [0 for i in range(total_classes)]
            requests[event.req.class_id] = -1
            next_state = (tuple(self.alives), tuple(requests))
                
        else: #new arrival
            requests = [0 for i in range(total_classes)]
            requests[event.req.class_id] = 1
            self.arriaved_demand = event.req

            next_state = (tuple(self.alives), tuple(requests))
        
        #debug("************  env step *************")
        return next_state, reward, done


def is_active_state(state):
    alives = state[0]
    events = state[1]

    return True if (1 in events) else False


def get_valid_actions(state):
    alives = state[0]
    events = state[1]
    actions = []

    actives = 0
    for i in range(len(events)):
        actives += abs(events[i])

    if actives != 1:
        error("get_valid_actions: Error in state")
        error("state = ", state)
        sys.exit()

    if -1 in events:
        #agent cannot do anything
        actions.append(Actions.no_action)

    else:
        actions.append(Actions.reject)
        actions.append(Actions.federate)
        tmp_alives = [0] * len(alives)
        for i in range(len(tmp_alives)):
            tmp_alives[i] = alives[i] + events[i]
        
        if compute_capacity(tmp_alives) >= 0:
            actions.append(Actions.accept)
  
    #debug("state =", state, ", Valid actions = ", actions)
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
    #debug("----------------------------")
    for i in range(len(events)):
        e = events[i]
        #debug("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(alives):
    capacity = domain.total_cpu
    for i in range(total_classes):
        capacity -= alives[i] * traffic_loads[i].service.cpu

    return capacity


