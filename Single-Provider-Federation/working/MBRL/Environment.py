from enum import IntEnum
import numpy as np
import sys 
import heapq

verbose = False
debug = print if verbose else lambda *a, **k: None
warning = print 
error = print


providers_num = 0

class State:
    local_domain = 0
    def __init__(self, tc_num):
        self.domains_alives= list()
        self.arrivals_departures = tuple()
        self.req = None

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
            res += str(self.domains_alives[i])

        res += "],"
        res += str(self.arrivals_departures)
        return res

    def __eq__(self, other):
        if other is None:
            return False

        for i in range(len(self.domains_alives)):
            for j in range(len(self.domains_alives[i])):
                if self.domains_alives[i][j] != other.domains_alives[i][j]:
                    return False
        for i in range(len(self.arrivals_departures)):
            if self.arrivals_departures[i] != other.arrivals_departures[i]:
                return False
        
        return True

    def __hash__(self):
        res = 0
        for a in self.domains_alives:
            res += hash(a)
        res += hash(self.arrivals_departures)
        return res


class NFV_NS:
    def __init__(self, nsid, cpu, revenue):
        self.nsid = nsid
        self.cpu  = cpu
        self.revenue = revenue


class Local_Domain:
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
    def __init__(self, nsid, lam, mu):
        for service in domain.services:
            if service.nsid == nsid:
                self.service = service
        self.lam  = lam
        self.mu   = mu


class Providers:
    def __init__(self, pid):
        self.pid = pid
        self.federation_costs = dict()

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
    def __init__(self, w, st, dt, rev, index):
        self.w  = w
        self.st = st
        self.dt = dt
        self.rev= rev
        self.class_id = index
        self.deployed = -1
        self.known_action = None

    def __str__(self):
        return "w = "+ str(self.w) +" st = "+ str(format(self.st,"2.3f")) +" dt = "+ str(format(self.dt,"2.3f")) +" rev = "+ str(self.rev) +", index = "+ str(self.class_id) +", deployed = "+ str(self.deployed) +", action = "+ (str(self.known_action) if hasattr(self, 'known_action') else "None")


def print_reqs(reqs):
    for i in range(len(reqs)):
        if verbose:
            debug(reqs[i])
        pass


def generate_class_req_set(service, load, time, class_id):
    t = 0
    all_req = []
    time_slot_size = (1.0 * time) / len(load.lam)
    
    while t < time:
        slot_index = int (t / time_slot_size)
        if load.lam[slot_index] > 0:
            t += np.random.exponential(1.0 / load.lam[slot_index])
            life = np.random.exponential(1.0 / load.mu)
            
            #t += np.random.uniform(0, 2 * 1.0 / load.lam[slot_index])
            #life = np.random.uniform(0, 2 * 1.0 / load.mu)
            
            #t += max(0.01, np.random.normal(10.0 / load.lam[slot_index], pow(10.0 / load.lam[slot_index], 2)))
            #life = max(0.01, np.random.normal(1.0 / load.mu, pow(1.0 / load.mu, 2)))
            
            all_req.append(Request(service.cpu, t, t + life, service.revenue, class_id))
        else:
            t += time_slot_size + 0.001

    if verbose:
        print_reqs(all_req)
    
    return all_req

def generate_class_req_set_with_learned_params(service, params, num, class_index):
    t = 0
    all_req = []
    
    for i in range(num):
        t += np.random.exponential(params["iat"])
        life = np.random.exponential(params["ht"])
        all_req.append(Request(service.cpu, t, t + life, service.revenue, class_index))

    if verbose:
        print_reqs(all_req)
    
    return all_req



known_traffic_params = dict() #of (service, load)
sample_rate = 1.0
decay = 1.0
ema_rate = 0.05

def take_moving_average(current, new, num):
    if current == 0:
        current = new
    else:
        current += ema_rate * (new - current)

    return current

def take_sample_average(current, new, num):
    if current == 0:
        current = new
    else:
        current += (sample_rate / (1 + num * decay))* (new - current)

    return current

def print_model_param(params):
    for class_index in params:
        print("params = ", class_index, params[class_index])

def update_IAT(class_id, current_arrival, learned_traffic_params):
    if not(class_id in learned_traffic_params):
        learned_traffic_params[class_id] = {"iat_seen": 0, "iat": current_arrival, "cr_ar": current_arrival, "ht_seen": -1, "ht": 0}
    else:
        current_estimate = learned_traffic_params[class_id]
        current_estimate["iat_seen"] += 1
        current_estimate["iat"] = take_moving_average(current_estimate["iat"], current_arrival - current_estimate["cr_ar"], current_estimate["iat_seen"])
        current_estimate["cr_ar"] = current_arrival

    if verbose:
        print("IAT: class_id = ", class_id, "-->", learned_traffic_params[class_id])


def update_HT(class_id, current_ht, learned_traffic_params):
    current_estimate = learned_traffic_params[class_id]
    current_estimate["ht_seen"] += 1
    current_estimate["ht"]= take_sample_average(current_estimate["ht"], current_ht, current_estimate["ht_seen"])
    
    if verbose:
        print("HT : class_id = ", class_id, "-->", learned_traffic_params[class_id])


def generate_req_set(time):
    all_class_reqs = []
    
    total_n = 0
    class_id = 0
    for service in domain.services:
        for load in traffic_loads:
            if service.nsid == load.service.nsid:
                req_list = generate_class_req_set(service, load, time, class_id)
                total_n += len(req_list)
                all_class_reqs.append(req_list)
                
                known_traffic_params[class_id] = (service, load)
                class_id += 1

    j = 0
    req_set = [None] * total_n
    for i in range(len(all_class_reqs)):
        for k in range(len(all_class_reqs[i])):
            req_set[j] = all_class_reqs[i][k]
            j += 1

    req_set.sort(key=lambda x: x.st)

    result = req_set

    return result


def generate_req_set_with_learned_param(num, learned_traffic_params, window = 0):
    all_class_reqs = []
    
    total_n = 0
    for class_index in learned_traffic_params:
        params = dict()

        if learned_traffic_params[class_index]["iat_seen"] > window:
            params["iat"] = learned_traffic_params[class_index]["iat"]
        else:
            params["iat"] = np.random.uniform(0, 1)

        if learned_traffic_params[class_index]["ht_seen"] > window:
            params["ht"] = learned_traffic_params[class_index]["ht"]
        else:
            params["ht"] = np.random.uniform(0, 1)

        req_list = generate_class_req_set_with_learned_params(known_traffic_params[class_index][0], params, num, class_index)
        total_n += len(req_list)
        all_class_reqs.append(req_list)
                
    j = 0
    req_set = [None] * total_n
    for i in range(len(all_class_reqs)):
        for k in range(len(all_class_reqs[i])):
            req_set[j] = all_class_reqs[i][k]
            j += 1

    req_set.sort(key=lambda x: x.st)

    result = req_set[:num]

    return result



class Env:
    def __init__(self, local_capacity, provider_capacity, eplen = 0, given_demands = None):
        self.action_space = Actions
        self.local_domain_capacity  = local_capacity
        self.provider_domain_capacity = provider_capacity
        self.episode_len = eplen
        if given_demands is not None:
            self.demands = given_demands.copy()
        self.events = []
        self.learned_traffic_params = dict()

    def set_requests(self, demands):
        self.demands = demands

    def start(self):
        if verbose:
            debug("------------- env start ---------------")
        
        self.current_local_capacity = self.local_domain_capacity
        self.current_provider_capacity = self.provider_domain_capacity

        self.local_alives = [0 for i in range(total_classes)]
        self.provider_alives = [0 for i in range(total_classes)]
       
        if self.episode_len > 0:
            self.demands = generate_req_set(self.episode_len)
        
        if verbose:
            print("env.demands...")
            print_reqs(self.demands)

        if len(self.demands) == 0:
            return None

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        if verbose:
            print_events(self.events)
        
        # The first event
        event = heapq.heappop(self.events)
        
        if verbose:
            print_events(self.events)

        requests = [0 for i in range(total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = State(len(traffic_loads))
        state.domains_alives = [tuple(self.local_alives), tuple(self.provider_alives)]
        state.arrivals_departures = tuple(requests)
        state.req = event.req
        
        if verbose:
            print("The first state = ", state)

        return state

    def stop(self):
        if verbose:
            debug("env stop")
        return

    def reset(self):
        if verbose:
            debug("env reset")
        
        self.stop()
        self.learned_traffic_params.clear()
        return self.start()
    
    def step(self, state, action):
        update_IAT(state.req.class_id, state.req.st, self.learned_traffic_params)
        reward = 0
        if verbose:
            debug("============= env step: start  ================")
            debug("s = ", state, ", a = ", action)
        
        current_local_alives = state.domains_alives[0]
        current_provider_alives = state.domains_alives[1]
        current_requests = state.arrivals_departures

        self.current_local_capacity = compute_capacity(0, state.domains_alives)
        self.current_provider_capacity = compute_capacity(1, state.domains_alives)
        
        if action == Actions.no_action:
            error("no_action")
            raise Exception("no_action")
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
            if verbose:
                debug("reject")
            reward = 0
        
        elif action == Actions.federate: #federate
            if verbose:
                debug("Try to federate: req = ", req)
            
            if self.current_provider_capacity < req.w:
                if verbose:
                    debug("\t cannot accept")
                
                error("Erro in valid actions, cannot accept")
                sys.exit()
            
            else:
                if verbose:
                    debug("\t federated")
 
                provider_domain = providers[1] # in this version, there is only one provider
                reward = req.rev - provider_domain.federation_costs[traffic_loads[req.class_id].service]
                self.current_provider_capacity -= req.w
                self.provider_alives[req.class_id] += 1
                req.deployed = 1
                event = Event(0, req.dt, req) #add the departure event
                heapq.heappush(self.events, event)

        elif action == Actions.accept: #accept
            if verbose:
                debug("Try to accept: req = ", req)
            
            if self.current_local_capacity < req.w:
                #cannot accept
                
                if verbose:
                    debug("\t cannot accept")
                
                error("Erro in valid actions, cannot accept")
                sys.exit()
            
            else:
                if verbose:
                    debug("\t accepted")
                
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
        
        if verbose:
            debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
            debug("self.local_alives = ", self.local_alives)
            debug("self.provider_alives = ", self.provider_alives)
            debug("event.req.class_id = ", event.req.class_id)

        while event.event_type == 0: #departure, update the nework
            update_HT(event.req.class_id, event.req.dt - event.req.st, self.learned_traffic_params)
            if verbose:
                debug("Departure event")
           
            if event.req.deployed == 0:
                self.current_local_capacity += event.req.w
                self.local_alives[event.req.class_id] -= 1
            elif event.req.deployed == 1:
                self.current_provider_capacity += event.req.w
                self.provider_alives[event.req.class_id] -= 1
            else:
                error("Wrong deployment")
                sys.exit()

            if verbose:
                debug("self.local_alives = ", self.local_alives)
                debug("self.provider_alives = ", self.provider_alives)

            if len(self.events) == 0:
                for i in range(len(self.local_alives)):
                    if self.local_alives[i] != 0 or self.provider_alives[i]:
                        error("bug in the last state")
                        sys.exit()
            
                done = 1
                return None, reward, done 

            event = heapq.heappop(self.events)
            
            if verbose:
                debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
                debug("self.local_alives = ", self.local_alives)
                debug("self.provider_alives = ", self.provider_alives)
                debug("event.req.class_id = ", event.req.class_id)

  
        if compute_capacity(0, [self.local_alives]) != self.current_local_capacity or compute_capacity(1, [0,self.provider_alives]) != self.current_provider_capacity:
            error("capacity error")
            error("compute local = ", compute_capacity(0, [self.local_alives]), ", self.local = ", self.current_local_capacity, ", compute provider = ", compute_capacity(1, [0,self.provider_alives]), ", self.provider = ", self.current_provider_capacity)
            sys.exit()

        self.arriaved_demand = None
        next_state = None
        done = 0

        requests = [0 for i in range(total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        next_state = State(len(traffic_loads))
        next_state.domains_alives = [tuple(self.local_alives), tuple(self.provider_alives)]
        next_state.arrivals_departures = tuple(requests)
        next_state.req = event.req

        if verbose:
            debug("next_state = ", next_state)
            debug("************  env step: end *************")
        
        return next_state, reward, done


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
        
        local_alives = [0] * len(all_domains_alives[State.local_domain])
        for i in range(len(local_alives)):
            local_alives[i] = all_domains_alives[State.local_domain][i] + events[i]
        all_domains_alives[State.local_domain] = tuple(local_alives)
       
        if compute_capacity(State.local_domain, all_domains_alives) >= 0:
            actions.append(Actions.accept)

        provider_alives = [0] * len(all_domains_alives[1]) #There is only one provider domain
        for i in range(len(provider_alives)):
            provider_alives[i] = all_domains_alives[1][i] + events[i]
        all_domains_alives[1] = tuple(provider_alives)
         
        if compute_capacity(1, all_domains_alives) >= 0:
            actions.append(Actions.federate)
        
        if True:
        #if len(actions) == 0:
            actions.append(Actions.reject)

    if verbose:
        debug("get_valid_actions: state =", state, ", Valid actions = ", actions)
    
    return actions

class Event:
    def __init__(self, ty, ti, rq):
        self.event_type = ty
        self.time = ti
        self.req = rq

    def __lt__(self, other):
        return (self.time < other.time) or (self.time == other.time and self.req.known_action != None)

def print_events(events):
    if verbose:
        debug("----------------------------")
    
    for i in range(len(events)):
        e = events[i]
        if verbose:
            debug("type = ", e.event_type ,", req = ", e.req)

def compute_capacity(domain_index, all_domains_alives):
    if domain_index == State.local_domain:
        capacity = domain.total_cpu
    else:
        capacity = providers[domain_index].quota

    alives = all_domains_alives[domain_index]
    
    for i in range(total_classes):
        capacity -= alives[i] * traffic_loads[i].service.cpu

    return capacity


if __name__ == "__main__":
    parser.parse_config("config.json")

