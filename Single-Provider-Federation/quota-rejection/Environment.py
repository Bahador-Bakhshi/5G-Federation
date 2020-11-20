from enum import IntEnum
import numpy as np
import sys 
import heapq

verbose = True
debug = print if verbose else lambda *a, **k: None
warning = print 
error = print


providers_num = 0

class State:
    local_domain = 0
    domains_alives= []
    arrivals_departures = ()

    def __init__(self, tc_num):
        self.domains_alives = [None] * (1 + providers_num) #1 for the local domain
        for i in range(len(self.domains_alives)):
            alives_tuple= (0,) * tc_num
            self.domains_alives[i]=alives_tuple
        
        arrivals_list = [0] * tc_num
        self.arrivals_departures = tuple(arrivals_list)

    def __str__(self):
        res = ""
        res += "["
        for i in range(len(self.domains_alives)):
            res += "("
            res += str(self.domains_alives[i])
            res += ")"

        res += "],"
        res += str(self.arrivals_departures)
        return res

    def __eq__(self, other):
        for i in range(len(self.domains_alives)):
            for j in range(len(self.domains_alives[i])):
                if self.domains_alives[i][j] != other.domains_alives[i][j]:
                    return False
        for i in range(len(self.arrivals_departures)):
            if self.arrivals_departures[i] != other.arrivals_departures[i]:
                return False
        
        return True


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
    quota = 0
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
        if verbose:
            debug(reqs[i])
        pass


def generate_class_req_set(service, load, time, class_id):
    t = 0
    all_req = []
    
    while t <= time:
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        all_req.append(Request(service.cpu, t, t + life, service.revenue, class_id))

    if verbose:
        print_reqs(all_req)
    
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

    '''
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

        print("cid = ", cid,", cnt = ", cnt,", life = ", life / cnt, ", delay = ", delay / cnt)
    '''

    return result


class Env:
    action_space = None
    local_domain_capacity = 0
    provider_domain_capacity = 0
    episode_len = 0
    capacity = 0
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, local_capacity, eplen):
        self.action_space = Actions
        self.local_domain_capacity  = local_capacity
        self.episode_len = eplen
        self.events = []

    def start(self):
        if verbose:
            debug("------------- env start ---------------")
        
        self.capacity = self.local_domain_capacity
        self.alives = [0 for i in range(total_classes)]
        
        self.demands = generate_req_set(self.episode_len)
        
        if verbose:
            print_reqs(self.demands)

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        if verbose:
            print_events(self.events)
        
        event = heapq.heappop(self.events)
        
        if verbose:
            print_events(self.events)

        self.active_reqs = [0 for i in range(total_classes)]
        self.active_reqs[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = (tuple(self.alives), tuple(self.active_reqs))

        return state

    def stop(self):
        if verbose:
            debug("env stop")
        return

    def reset(self):
        if verbose:
            debug("env reset")
        
        self.stop()
        return self.start()
    
    def step(self, state, action):
        reward = 0
        if verbose:
            debug("===========  env step ==================")
            debug("s = ", state, ", a = ", action)
        
        current_alives = state[0]
        current_requests = state[1]
        current_capacity = compute_capacity(current_alives)
        
        if action == Actions.no_action:
            error("no_action")
            sys.exit()

        req = self.arriaved_demand
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

        if action == Actions.reject: #reject
            if verbose:
                debug("reject")
            reward = 0
        
        elif action == Actions.federate: #federate
            if verbose:
                debug("Try to federate: req = ", req)
            
            provider_domain = providers[0] # in this version, there is only one provider
            
            if verbose:
                debug("\t federated")

            reward = req.rev - provider_domain.federation_costs[traffic_loads[req.class_id].service]

        elif action == Actions.accept: #accept
            if verbose:
                debug("Try to accept: req = ", req)
            
            if self.capacity < req.w:
                #cannot accept
                
                if verbose:
                    debug("\t cannot accept")
                
                error("Erro in valid actions, cannot accept")
                sys.exit()
            
            else:
                if verbose:
                    debug("\t accepted")
                
                reward = req.rev
                self.capacity -= req.w
                self.alives[req.class_id] += 1
                event = Event(0, req.dt, req) #add the departure event
                heapq.heappush(self.events, event)
        
        else:
            error("Unknown action")
            sys.exit()

        
        if len(self.events) == 0:
            for i in range(len(self.alives)):
                if self.alives[i] != 0:
                    error("bug in the last state")
                    sys.exit()
            
                if verbose:
                    next_state = (tuple([0 for i in range(total_classes)]), tuple([0 for i in range(total_classes)]))
            
            done = 1
            return None, reward, done 

        event = heapq.heappop(self.events)
        
        if verbose:
            debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
            debug("self.alives = ", self.alives)
            debug("event.req.class_id = ", event.req.class_id)

        while event.event_type == 0: #departure, update the nework
            if verbose:
                debug("Departure event")
            
            self.capacity += event.req.w
            self.alives[event.req.class_id] -= 1
            
            if verbose:
                debug("self.alives = ", self.alives)

            if len(self.events) == 0:
                for i in range(len(self.alives)):
                    if self.alives[i] != 0:
                        error("bug in the last state")
                        sys.exit()
            
                if verbose:
                    next_state = (tuple([0 for i in range(total_classes)]), tuple([0 for i in range(total_classes)]))
                
                done = 1
                return None, reward, done 

            event = heapq.heappop(self.events)
            
            if verbose:
                debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
                debug("self.alives = ", self.alives)
                debug("event.req.class_id = ", event.req.class_id)

        if compute_capacity(self.alives) != self.capacity:
            error("capacity error")
            sys.exit()

        self.arriaved_demand = None
        next_state = None
        done = 0

        requests = [0 for i in range(total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        next_state = (tuple(self.alives), tuple(requests))
        
        if verbose:
            debug("************  env step *************")
        
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
  
    if verbose:
        debug("state =", state, ", Valid actions = ", actions)
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
        return self.time < other.time


def print_events(events):
    if verbose:
        debug("----------------------------")
    
    for i in range(len(events)):
        e = events[i]
        if verbose:
            debug("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(alives):
    capacity = domain.total_cpu
    for i in range(total_classes):
        capacity -= alives[i] * traffic_loads[i].service.cpu

    return capacity


if __name__ == "__main__":
    s1 = State(4)
    print(s1)
