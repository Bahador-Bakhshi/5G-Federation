from enum import IntEnum
import numpy as np
import sys 
import heapq

from debuger import verbose, debug, warning, error

# Global Variables
all_domains = []
all_simple_ns = []
all_composite_ns = []
all_traffic_loads = []

class State:
    domains_alives = []
    domains_resources = []
    arrivals_departures = ()

    def __init__(self, alives, capacities, events):
        
        print("alives = ", alives)
        print("capacities = ", capacities)
        print("events = ", events)

        self.domains_alives = [None] * len(all_domains)
        for i in range(len(self.domains_alives)):
            this_alives = alives[i].copy()
            alives_tuple = tuple(this_alives)
            self.domains_alives[i] = alives_tuple

        self.domains_resources = [None] * len(all_domains)
        for i in range(len(self.domains_resources)):
            free_resources = capacities[i].copy()
            resources_tuple = tuple(free_resources)
            self.domains_resources[i] = resources_tuple

        arrivals_departure_list = events.copy()
        self.arrivals_departures = tuple(arrivals_departure_list)

    def __str__(self):
        res = ""
        res += "["
        for i in range(len(self.domains_alives)):
            res += str(self.domains_alives[i])

        res += "], ["
        
        for i in range(len(self.domains_alives)):
            res += str(self.domains_resources[i])

        res += "],"
   
        res += str(self.arrivals_departures)
        return res

    def __eq__(self, other):
        '''
        for i in range(len(self.domains_alives)):
            for j in range(len(self.domains_alives[i])):
                if self.domains_alives[i][j] != other.domains_alives[i][j]:
                    return False
        for i in range(len(self.arrivals_departures)):
            if self.arrivals_departures[i] != other.arrivals_departures[i]:
                return False
        
        return True
        '''
        return ((self.domains_alives == other.domains_alives) and (self.arrivals_departures == other.arrivals_departures))

    def __hash__(self):
        t = tuple(self.domains_alives)
        return hash((t, self.arrivals_departures))

    '''
        res = 0
        for a in self.domains_alives:
            res += hash(a)
        res += hash(self.arrivals_departures)
        return res
    '''

class Actions(IntEnum):
    # [0, ..., len(all_domains) - 1] for deployment
    reject    = len(all_domains)
    no_action = len(all_domains) + 1

class Request:
    st  = 0
    dt  = 0
    class_id = 0
    cns_id = 0
    deployed = -1 # ID of the domain where the demand is deployed

    def __init__(self, st, dt, index, cns_id):
        self.st = st
        self.dt = dt
        self.class_id = index
        self.cns_id = cns_id

    def __str__(self):
        return " st = "+ str(self.st) +" dt = "+ str(self.dt) +", index = "+ str(self.class_id)+", cns_id = "+ str(self.cns_id) +", deployed = "+ str(self.deployed)


def print_reqs(reqs):
    for i in range(len(reqs)):
        if verbose:
            debug(reqs[i])
        pass


def deploy_service(instance_num, service, domain_capacities):
    for index in range(len(service.resources)):
        domain_capacities[index] -= instance_num * service.resources[index]

def depart_demand(service, domain_capacities):
    for index in range(len(service.resources)):
        domain_capacities[index] += service.resources[index]

def generate_class_req_set(service, load, num, class_id, cns_id):
    
    t = 0
    all_req = []
   
    for i in range(num):
        t += np.random.exponential(1.0 / load.lam)
        life = np.random.exponential(1.0 / load.mu)
        req = Request(t, t + life, class_id, cns_id)
        all_req.append(req)

    return all_req

def generate_req_set(num):
    all_class_reqs = []
    
    total_n = 0
    for service in all_composite_ns:
        class_id = 0
        for load in all_traffic_loads:
            if service.cns_id == load.cns_id:
                req_list = generate_class_req_set(service, load, num, class_id, service.cns_id)
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

class Env:
    original_domains_capacities = None
    current_domains_capacities = None 
    domains_alives = None
    episode_len = 0
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, eplen):
        self.original_domains_capacities = [[x for x in y.quotas] for y in all_domains]
        self.episode_len = eplen
        self.events = []

    def start(self):
        if verbose:
            debug("------------- env start ---------------")
   
        self.current_domains_capacities = [[0 for i in range(len(all_domains[0].quotas))] for j in range(len(all_domains))]
        for i in range(len(all_domains)):
            for j in range(len(all_domains[0].quotas)):
                self.current_domains_capacities[i][j] = self.original_domains_capacities[i][j] * all_domains[i].reject_thresholds[j]

        self.domains_alives = [[0 for i in range(len(all_traffic_loads))] for j in range(len(all_domains))]

        
        self.demands = generate_req_set(self.episode_len)
        
        if verbose:
            print_reqs(self.demands)

        for i in range(len(self.demands)):
            self.events.append(Event(1, self.demands[i].st, self.demands[i]))

        heapq.heapify(self.events)
    
        if verbose:
            print_events(self.events)
        
        # The first event
        event = heapq.heappop(self.events)
        

        requests = [0 for i in range(len(all_traffic_loads))]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        state = State(self.domains_alives, self.current_domains_capacities, requests)
        
        if verbose:
            print("The first state = ", state)

        return state
    
    '''
    def stop(self):
        if verbose:
            debug("env stop")
        return

    def reset(self):
        if verbose:
            debug("env reset")
        
        global seen_state_valid_actions
        seen_state_valid_actions = {}

        self.stop()
        return self.start()
    
    def step(self, state, action):
        reward = 0
        if verbose:
            debug("============= env step: start  ================")
            debug("s = ", state, ", a = ", action)
            debug("local_capacities = ", self.current_local_capacities)
            debug("provider_capacities = ", self.current_provider_capacities)
        
        current_local_alives = state.domains_alives[0]
        current_provider_alives = state.domains_alives[1]
        current_requests = state.arrivals_departures

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
            if verbose:
                debug("reject")
            reward = 0
        
        elif action == Actions.federate: #federate
            
            if verbose:
                debug("Try to federate: req = ", req)
            
            provider_domain = providers[1] # in this version, there is only one provider
            federation_cost_scale = -1
            
            if check_feasible_deployment(req, self.current_provider_capacities):
                if should_overcharge(req, self.current_provider_capacities, provider_domain.quotas, provider_domain.reject_threshold):
                    federation_cost_scale = provider_domain.overcharge
                else:
                    federation_cost_scale = 1
            else:
                error("invalid federation")
                sys.exit(-1)

            if verbose:
                debug("federation_cost_scale = ", federation_cost_scale)

            reward = req.rev - provider_domain.federation_costs[traffic_loads[req.class_id].service] * federation_cost_scale
            update_capacities(req, self.current_provider_capacities, -1)
            self.provider_alives[req.class_id] += 1
            req.deployed = 1
            event = Event(0, req.dt, req) #add the departure event
            heapq.heappush(self.events, event)

        elif action == Actions.accept: #accept
            if verbose:
                debug("Try to accept: req = ", req)
            
            if not check_feasible_deployment(req, self.current_local_capacities):
                #cannot accept
                
                if verbose:
                    debug("\t cannot accept")
                
                error("Error in valid actions, cannot accept")
                error("req = ", req)
                error("current_local_capacities = ", self.current_local_capacities)
                error("state = ", state)
                error("valid actions = ", get_valid_actions(state))

                sys.exit()
            
            else:
                if verbose:
                    debug("\t accepted")
                
                reward = req.rev
                update_capacities(req, self.current_local_capacities, -1)
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
            if verbose:
                debug("Departure event")
           
            if event.req.deployed == 0:
                update_capacities(event.req, self.current_local_capacities, 1)
                self.local_alives[event.req.class_id] -= 1
            elif event.req.deployed == 1:
                update_capacities(event.req, self.current_provider_capacities, 1)
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

  
        self.arriaved_demand = None
        next_state = None
        done = 0

        requests = [0 for i in range(total_classes)]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        next_state = State(len(traffic_loads))
        next_state.domains_alives = [tuple(self.local_alives), tuple(self.provider_alives)]
        next_state.arrivals_departures = tuple(requests)

        if verbose:
            debug("next_state = ", next_state)
            debug("local_capacities = ", self.current_local_capacities)
            debug("provider_capacities = ", self.current_provider_capacities)
            debug("************  env step: end *************")

        return next_state, reward, done
        '''

def is_active_state(state):
    events = state.arrivals_departures

    return True if (1 in events) else False


seen_state_valid_actions = {}

def get_valid_actions(state):

    if state in seen_state_valid_actions:
        return seen_state_valid_actions[state]

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
        
        req_index = np.argmax(events)
       
        if can_be_deployed(1, req_index, State.local_domain, 1, all_domains_alives):
            actions.append(Actions.accept)

        domain_index = 1
        if can_be_deployed(1, req_index, domain_index, providers[domain_index].reject_threshold, all_domains_alives):
            actions.append(Actions.federate)

    if verbose:
        debug("get_valid_actions: state =", state, ", Valid actions = ", actions)
    
    seen_state_valid_actions[state] = actions
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


def can_be_deployed(instance_num, req_index, domain_index, scale, all_domains_alives):
    if domain_index == State.local_domain:
        capacities = domain.capacities.copy()
    else:
        capacities = providers[domain_index].quotas.copy()
  
    capacities = [x * scale for x in capacities]

    for index in range(len(all_domains_alives[domain_index])):
        required_resources = traffic_loads[index].service.resources
        for res_index in range(len(required_resources)):
            capacities[res_index] -= required_resources[res_index] * all_domains_alives[domain_index][index]

    required_resources = traffic_loads[req_index].service.resources
    for res_index in range(len(required_resources)):
        capacities[res_index] -= required_resources[res_index] * instance_num

    for res_index in range(len(capacities)):
        if capacities[res_index] < 0:
            return False

    return True


def check_feasible_deployment(req, capacities):
    for i in range(len(req.cap)):
        if req.cap[i] > capacities[i]:
            return False

    return True


def update_capacities(req, capacities, inc_dec):
    for i in range(len(req.cap)):
        capacities[i] += inc_dec * req.cap[i]

def should_overcharge(req, current_capacities, quotas, reject_threshold):
    for i in range(len(req.cap)):
        if (current_capacities[i] - req.cap[i]) < ((reject_threshold - 1) * quotas[i]):
            return True

    return False


if __name__ == "__main__":
    s1 = State(4)
    print(s1)

