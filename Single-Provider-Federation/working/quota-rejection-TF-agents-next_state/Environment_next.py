from enum import IntEnum
import numpy as np
import sys 
import heapq

import Environment

class State_next:
    local_domain = 0
    domains_alives_current = []
    domains_alives_after_accept = []
    domains_alives_after_federate = []
    domains_alives_after_reject = []
    arrivals_departures = ()
    state_fields_num = 0

    def __init__(self, tc_num):
        State_next.state_fields_num = 4 * 2 * Environment.total_classes + Environment.total_classes
        self.domains_alives_current = [None] * (1 + Environment.providers_num) #1 for the local domain
        self.domains_alives_after_accept = [None] * (1 + Environment.providers_num) #1 for the local domain
        self.domains_alives_after_federate = [None] * (1 + Environment.providers_num) #1 for the local domain
        self.domains_alives_after_reject = [None] * (1 + Environment.providers_num) #1 for the local domain
        
        for i in range(len(self.domains_alives_after_accept)):
            alives_tuple= (0,) * tc_num
            self.domains_alives_current[i] = alives_tuple
            self.domains_alives_after_accept[i] = alives_tuple
            self.domains_alives_after_federate[i] = alives_tuple
            self.domains_alives_after_reject[i] = alives_tuple
        
        arrivals_list = [0] * tc_num
        self.arrivals_departures = tuple(arrivals_list)
    
    def __str__(self):
        res = ""

        res += "["
        for i in range(len(self.domains_alives_current)):
            res += str(self.domains_alives_current[i])

        res += "],"
 
        res += "["
        for i in range(len(self.domains_alives_after_accept)):
            res += str(self.domains_alives_after_accept[i])

        res += "],"
 
        res += "["
        for i in range(len(self.domains_alives_after_federate)):
            res += str(self.domains_alives_after_federate[i])

        res += "],"
 
        res += "["
        for i in range(len(self.domains_alives_after_reject)):
            res += str(self.domains_alives_after_reject[i])

        res += "],"

        res += str(self.arrivals_departures)
        return res

    def __eq__(self, other):
        for i in range(len(self.domains_alives_current)):
            for j in range(len(self.domains_alives_current[i])):
                if self.domains_alives_current[i][j] != other.domains_alives_current[i][j]:
                    return False

        for i in range(len(self.domains_alives_after_accept)):
            for j in range(len(self.domains_alives_after_accept[i])):
                if self.domains_alives_after_accept[i][j] != other.domains_alives_after_accept[i][j]:
                    return False

        for i in range(len(self.domains_alives_after_federate)):
            for j in range(len(self.domains_alives_after_federate[i])):
                if self.domains_alives_after_federate[i][j] != other.domains_alives_after_federate[i][j]:
                    return False

        for i in range(len(self.domains_alives_after_reject)):
            for j in range(len(self.domains_alives_after_reject[i])):
                if self.domains_alives_after_reject[i][j] != other.domains_alives_after_reject[i][j]:
                    return False

        for i in range(len(self.arrivals_departures)):
            if self.arrivals_departures[i] != other.arrivals_departures[i]:
                return False
        
        return True

    def __hash__(self):
        res = 0
        for a in self.domains_alives_current:
            res += hash(a)
        for a in self.domains_alives_after_accept:
            res += hash(a)
        for a in self.domains_alives_after_federate:
            res += hash(a)
        for a in self.domains_alives_after_reject:
            res += hash(a)
        res += hash(self.arrivals_departures)
        return res


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

class Request:
    w   = 0
    st  = 0
    dt  = 0
    rev = 0
    class_id = 0
    deployed = -1 # adomain id

    def __init__(self, w, st, dt, rev, index):
        self.w  = w
        self.st = st
        self.dt = dt
        self.rev= rev
        self.class_id = index

    def __str__(self):
        return "w = "+ str(self.w) +" st = "+ str(self.st) +" dt = "+ str(self.dt) +" rev = "+ str(self.rev) +", index = "+ str(self.class_id) +", deployed = "+ str(self.deployed)


def print_reqs(reqs):
    for i in range(len(reqs)):
        if Environment.verbose:
            Environment.debug(reqs[i])
        pass


def generate_class_req_set(service, load, num, class_id):
    t = 0
    all_req = []
    
    for i in range(num):
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        all_req.append(Request(service.cpu, t, t + life, service.revenue, class_id))

    if Environment.verbose:
        print_reqs(all_req)
    
    return all_req


def generate_req_set(num):
    all_class_reqs = []
    
    total_n = 0
    for service in Environment.domain.services:
        class_id = 0
        for load in Environment.traffic_loads:
            if service.nsid == load.service.nsid:
                req_list = generate_class_req_set(service, load, num, class_id)
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

    result = req_set[:num]

    return result


def generate_state_next(state):
    state_next = State_next(len(Environment.traffic_loads))
    state_next.domains_alives_current = state.domains_alives.copy()
    state_next.domains_alives_after_accept = state.domains_alives.copy()
    state_next.domains_alives_after_reject = state.domains_alives.copy()
    state_next.domains_alives_after_federate = state.domains_alives.copy()
    state_next.arrivals_departures = state.arrivals_departures

    valid_actions = get_valid_actions(state)

    if Actions.no_action in valid_actions:
        error("No State_next for no_action")
        sys.exit(-1)

    if Actions.reject in valid_actions:
        state_next.domains_alives_after_reject = state.domains_alives
    else:
        error("Cannot reject !!!!")
        sys.exit(-1)

    if Actions.accept in valid_actions:
        next_local_alives = [sum(x) for x in zip(state.domains_alives[0], state.arrivals_departures)]
        state_next.domains_alives_after_accept[0] = tuple(next_local_alives)
    else:
        state_next.domains_alives_after_accept[0] = (-1,) * len(state_next.domains_alives_after_accept)

    if Actions.federate in valid_actions:
        next_remote_alives = [sum(x) for x in zip(state.domains_alives[1], state.arrivals_departures)]
        state_next.domains_alives_after_federate[1] = tuple(next_remote_alives)
    else:
        state_next.domains_alives_after_federate[1] = (-1,) * len(state_next.domains_alives_after_federate)

    return state_next


class Env:
    action_space = None
    local_domain_capacity = 0
    provider_domain_capacity = 0
    episode_len = 0
    current_local_capacity = 0
    current_provider_capacity = 0
    local_alives = None
    provider_alives = None
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, local_capacity, provider_capacity, eplen):
        self.action_space = Actions
        self.local_domain_capacity  = local_capacity
        self.provider_domain_capacity = provider_capacity
        self.episode_len = eplen
        self.events = []
        
        state_next = State_next(len(Environment.traffic_loads)) #to initialize tghe state_fields_num

    def start(self, requests = None):
        if Environment.verbose:
            Environment.debug("------------- env start ---------------")
        
        self.current_local_capacity = self.local_domain_capacity
        self.current_provider_capacity = self.provider_domain_capacity

        self.local_alives = [0 for i in range(Environment.total_classes)]
        self.provider_alives = [0 for i in range(Environment.total_classes)]
        
        if requests == None:
            print("Generating new demands ....")
            self.demands = generate_req_set(self.episode_len)
        else:
            print("Using the old demands ....")
            self.demands = requests

        if Environment.verbose:
            print_reqs(self.demands)

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        if Environment.verbose:
            print_events(self.events)
        
        # The first event
        event = heapq.heappop(self.events)
        
        if Environment.verbose:
            print_events(self.events)

        requests = [0 for i in range(Environment.total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = Environment.State(len(Environment.traffic_loads))
        state.domains_alives = [tuple(self.local_alives), tuple(self.provider_alives)]
        state.arrivals_departures = tuple(requests)
            
        state_next = generate_state_next(state)

        if Environment.verbose:
            print("The first state = ", state_next)

        return state_next

    def stop(self):
        if Environment.verbose:
            Environment.debug("env stop")
        return

    def reset(self, requests):
        if Environment.verbose:
            Environment.debug("env reset")
        
        self.stop()
        return self.start(requests)
    
    def step(self, state_next, action):
        reward = 0
        state = Environment.State(len(Environment.traffic_loads))
        state.domains_alives = state_next.domains_alives_current.copy()
        state.arrivals_departures = state_next.arrivals_departures

        if Environment.verbose:
            Environment.debug("============= env step: start  ================")
            Environment.debug("s = ", state, ", a = ", action)
        
        current_local_alives = state.domains_alives[0]
        current_provider_alives = state.domains_alives[1]
        current_requests = state.arrivals_departures

        self.current_local_capacity = compute_capacity(0, state.domains_alives)
        self.current_provider_capacity = compute_capacity(1, state.domains_alives)
        
        if action == Actions.no_action:
            error("no_action")
            sys.exit()

        req = self.arriaved_demand
        count = 0
        for i in range(len(current_requests)):
            if current_requests[i] == -1:
                error("Invalid state, departure event!!!")
                sys.exit()

            if current_requests[i] == 1:
                count += 1
            
        if count > 1:
            error("Error in requests = ", current_requests)
            sys.exit()

        if count == 0: #there is no requst to accept
            error("Invalid state, no event!!!")
            sys.exit()


        if action == Actions.reject: #reject
            if Environment.verbose:
                Environment.debug("reject")
            reward = 0
        
        elif action == Actions.federate: #federate
            if Environment.verbose:
                Environment.debug("Try to federate: req = ", req)
            
            if self.current_provider_capacity < req.w:
                if Environment.verbose:
                    Environment.debug("\t cannot federate: just reject")
                
                #error("Error in valid actions, cannot federate")
                #sys.exit()
                reward = 0
            
            else:
                if Environment.verbose:
                    Environment.debug("\t federated")
 
                provider_domain = Environment.providers[1] # in this version, there is only one provider
                reward = req.rev - provider_domain.federation_costs[Environment.traffic_loads[req.class_id].service]
                self.current_provider_capacity -= req.w
                self.provider_alives[req.class_id] += 1
                req.deployed = 1
                event = Event(0, req.dt, req) #add the departure event
                heapq.heappush(self.events, event)

        elif action == Actions.accept: #accept
            if Environment.verbose:
                Environment.debug("Try to accept: req = ", req)
            
            if self.current_local_capacity < req.w:
                
                if Environment.verbose:
                    Environment.debug("\t cannot accept, just reject")
                
                #error("Error in valid actions, cannot accept")
                #sys.exit()
                reward = 0
            
            else:
                if Environment.verbose:
                    Environment.debug("\t accepted")
                
                reward = req.rev
                self.current_local_capacity -= req.w
                self.local_alives[req.class_id] += 1
                req.deployed = 0
                event = Event(0, req.dt, req) #add the departure event
                heapq.heappush(self.events, event)
        
        else:
            error("Unknown action")
            sys.exit()
        
        if len(self.events) == 0:
            for i in range(len(self.local_alives)):
                if self.local_alives[i] != 0:
                    error("bug in the last state for local domain")
                    sys.exit()
            
            for i in range(len(self.provider_alives)):
                if self.provider_alives[i] != 0:
                    error("bug in the last state for provider domain")
                    sys.exit()

            done = 1
            return None, reward, done 


        event = heapq.heappop(self.events)
        
        if Environment.verbose:
            Environment.debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
            Environment.debug("self.local_alives = ", self.local_alives)
            Environment.debug("self.provider_alives = ", self.provider_alives)
            Environment.debug("event.req.class_id = ", event.req.class_id)

        while event.event_type == 0: #departure, update the nework
            if Environment.verbose:
                Environment.debug("Departure event")
           
            if event.req.deployed == 0:
                self.current_local_capacity += event.req.w
                self.local_alives[event.req.class_id] -= 1
            elif event.req.deployed == 1:
                self.current_provider_capacity += event.req.w
                self.provider_alives[event.req.class_id] -= 1
            else:
                error("Wrong deployment")
                sys.exit()

            if Environment.verbose:
                Environment.debug("self.local_alives = ", self.local_alives)
                Environment.debug("self.provider_alives = ", self.provider_alives)

            if len(self.events) == 0:
                for i in range(len(self.local_alives)):
                    if self.local_alives[i] != 0 or self.provider_alives[i]:
                        error("bug in the last state")
                        sys.exit()
            
                done = 1
                return None, reward, done 

            event = heapq.heappop(self.events)
            
            if Environment.verbose:
                Environment.debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
                Environment.debug("self.local_alives = ", self.local_alives)
                Environment.debug("self.provider_alives = ", self.provider_alives)
                Environment.debug("event.req.class_id = ", event.req.class_id)

  
        if compute_capacity(0, [self.local_alives]) != self.current_local_capacity or compute_capacity(1, [0,self.provider_alives]) != self.current_provider_capacity:
            error("capacity error")
            error("compute local = ", compute_capacity(0, [self.local_alives]), ", self.local = ", self.current_local_capacity, ", compute provider = ", compute_capacity(1, [0,self.provider_alives]), ", self.provider = ", self.current_provider_capacity)
            sys.exit()

        self.arriaved_demand = None
        next_state = None
        done = 0

        requests = [0 for i in range(Environment.total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        next_state = Environment.State(len(Environment.traffic_loads))
        next_state.domains_alives = [tuple(self.local_alives), tuple(self.provider_alives)]
        next_state.arrivals_departures = tuple(requests)

        next_state_next = generate_state_next(next_state)

        if Environment.verbose:
            Environment.debug("next_state = ", next_state_next)
            Environment.debug("************  env step: end *************")
        
        return next_state_next, reward, done


def is_active_state(state):
    events = state.arrivals_departures

    return True if (1 in events) else False


def get_valid_actions(state):
    all_domains_alives = state.domains_alives.copy()
    events = state.arrivals_departures 
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
        
        local_alives = [0] * len(all_domains_alives[Environment.State.local_domain])
        for i in range(len(local_alives)):
            local_alives[i] = all_domains_alives[Environment.State.local_domain][i] + events[i]
        all_domains_alives[Environment.State.local_domain] = tuple(local_alives)
       
        if compute_capacity(Environment.State.local_domain, all_domains_alives) >= 0:
            actions.append(Actions.accept)

        provider_alives = [0] * len(all_domains_alives[1]) #There is only one provider domain
        for i in range(len(provider_alives)):
            provider_alives[i] = all_domains_alives[1][i] + events[i]
        all_domains_alives[1] = tuple(provider_alives)
         
        if compute_capacity(1, all_domains_alives) >= 0:
            actions.append(Actions.federate)

    if Environment.verbose:
        Environment.debug("get_valid_actions: state =", state, ", Valid actions = ", actions)
    
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
    if Environment.verbose:
        Environment.debug("----------------------------")
    
    for i in range(len(events)):
        e = events[i]
        if Environment.verbose:
            Environment.debug("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(domain_index, all_domains_alives):
    if domain_index == Environment.State.local_domain:
        capacity = Environment.domain.total_cpu
    else:
        capacity = Environment.providers[domain_index].quota

    alives = all_domains_alives[domain_index]
    
    for i in range(Environment.total_classes):
        capacity -= alives[i] * Environment.traffic_loads[i].service.cpu

    return capacity


if __name__ == "__main__":
    s1 = State(4)
    print(s1)
