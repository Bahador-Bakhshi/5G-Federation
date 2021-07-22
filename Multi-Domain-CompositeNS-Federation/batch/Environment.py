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
all_actions = []
reject_action = 0

class State:
    domains_deployed_simples = []
    domains_resources = []
    alive_composites = ()
    alive_traffic_classes = ()
    arrivals_departures = ()

    def __init__(self, deployed_simples, capacities, alive_composites, alive_traffic_classes, events):
       
        if verbose:
            print("deployed_simples = ", deployed_simples)
            print("capacities = ", capacities)
            print("alive_composites = ", alive_composites)
            print("alive_traffic_classes = ", alive_traffic_classes)
            print("events = ", events)

        self.domains_deployed_simples = [None] * len(all_domains)
        for i in range(len(self.domains_deployed_simples)):
            this_deployed_simples = deployed_simples[i].copy()
            deployed_simples_tuple = tuple(this_deployed_simples)
            self.domains_deployed_simples[i] = deployed_simples_tuple

        self.domains_resources = [None] * len(all_domains)
        for i in range(len(self.domains_resources)):
            free_resources = capacities[i].copy()
            resources_tuple = tuple(free_resources)
            self.domains_resources[i] = resources_tuple

        composite_alive_list = alive_composites.copy()
        self.alive_composites = tuple(composite_alive_list)
        
        traffic_classes_alive_list = alive_traffic_classes.copy()
        self.alive_traffic_classes = tuple(traffic_classes_alive_list)

        arrivals_departure_list = events.copy()
        self.arrivals_departures = tuple(arrivals_departure_list)

    def __str__(self):
        res = ""
        res += "["
        for i in range(len(self.domains_deployed_simples)):
            res += str(self.domains_deployed_simples[i])

        res += "], ["
        
        for i in range(len(self.domains_resources)):
            res += str(self.domains_resources[i])

        res += "],"
   
        res += str(self.alive_composites)
        res += str(self.alive_traffic_classes)
        res += str(self.arrivals_departures)

        return res

    def __eq__(self, other):
        return ((self.domains_deployed_simples == other.domains_deployed_simples) and (self.arrivals_departures == other.arrivals_departures)) and (self.alive_traffic_classes == other.alive_traffic_classes)

    def __hash__(self):
        return hash((tuple(self.domains_deployed_simples), tuple(self.alive_traffic_classes), tuple(self.arrivals_departures)))

'''
class Actions(IntEnum):
    # [0, ..., len(all_domains) - 1] for deployment
    reject    = len(all_domains)
    no_action = len(all_domains) + 1
'''

class Request:
    st  = 0
    dt  = 0
    class_id = 0
    cns_id = 0
    deployed = {}

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

def rec_enum_one_action(current_sns_index, max_sns_index, current_placement, all_placements):
    if current_sns_index == max_sns_index:
        for domain in range(len(current_placement)):
            current_placement[domain].append(all_simple_ns[current_sns_index].sns_id)
            placement_tuple = tuple(tuple(x) for x in current_placement)
            all_placements.append(placement_tuple)
            current_placement[domain].remove(all_simple_ns[current_sns_index].sns_id)
        return

    for domain in range(len(current_placement)):
        current_placement[domain].append(all_simple_ns[current_sns_index].sns_id)
        rec_enum_one_action(current_sns_index + 1, max_sns_index, current_placement, all_placements)
        current_placement[domain].remove(all_simple_ns[current_sns_index].sns_id)


def enumerate_all_actions():
    current_placement = [[] for x in range(len(all_domains))]
    all_placements = []
    rec_enum_one_action(0, len(all_simple_ns) - 1, current_placement, all_placements)

    return all_placements


class Env:
    original_domains_capacities = None
    current_domains_capacities = None 
    domains_deployed_simples = None
    alive_composites = None
    alive_traffic_classes = None
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

        self.domains_deployed_simples = [[0 for i in range(len(all_simple_ns))] for j in range(len(all_domains))]
        self.alive_composites = [0 for i in range(len(all_composite_ns))]
        self.alive_traffic_classes = [0 for i in range(len(all_traffic_loads))]
        
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

        state = State(self.domains_deployed_simples, self.current_domains_capacities, self.alive_composites, self.alive_traffic_classes, requests)
        
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
        return self.start()
    
    def step(self, state, action):
        reward = 0
        if verbose:
            debug("============= env step: start  ================")
            debug("s = ", state, ", a = ", action)
        
        req = self.arriaved_demand
        current_requests = state.arrivals_departures
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

        if action == reject_action:
            if verbose:
                debug("reject")
            reward = 0
        
        else: # action = a batch deployment
            
            if verbose:
                debug("Try to deploy: req = ", req,", in domains = ", all_actions[action])
            
            deployment_domains = all_actions[action]

            deployed_sns = {}
            total_cost = 0
            feasible_deployment = True
            for domain in deployment_domains:
                domain_index = deployment_domains.index(domain)
                for sns in domain:
                    print("try to deploy", sns, "in domain", domain_index)
                    cost_scale = -1
            
                    if all_domains[domain_index].costs[sns] < np.inf and check_feasible_deployment(all_simple_ns[sns], self.current_domains_capacities[domain_index]):
                        if should_overcharge(all_simple_ns[sns], self.current_domains_capacities[domain_index], all_domains[domain_index].quotas, all_domains[domain_index].reject_thresholds):
                            cost_scale = all_domains[domain_index].overcharges[sns]
                        else:
                            cost_scale = 1
                    else:
                        error("invalid deployment domain")
                        print("sns.resources = ", all_simple_ns[sns].resources)
                        print("domain = ", domain_index)
                        print("capacity = ", self.current_domains_capacities[domain_index])

                        for sns in deployed_sns.keys():
                            tmp_domain_index = deployed_sns[sns]
                            update_capacities(all_simple_ns[sns], self.current_domains_capacities[tmp_domain_index], 1)
                            self.domains_deployed_simples[tmp_domain_index][sns] -= 1
 
                        feasible_deployment = False
                        break

                    total_cost += all_domains[domain_index].costs[sns] * cost_scale
                    if verbose:
                        debug("cost_scale = ", cost_scale)
                        debug("total_cost = ", total_cost)

                    update_capacities(all_simple_ns[sns], self.current_domains_capacities[domain_index], -1)

                    self.domains_deployed_simples[domain_index][sns] += 1
                    deployed_sns[sns] = domain_index
                
                if feasible_deployment == False:
                    break

            if feasible_deployment:
                print("self.alive_composites: ", self.alive_composites)
                print("req.cns_id: ", req.cns_id)
                self.alive_composites[req.cns_id] += 1
                self.alive_traffic_classes[req.class_id] += 1
                req.deployed = deployed_sns
                reward = all_composite_ns[req.cns_id].revenue - total_cost
                event = Event(0, req.dt, req) #add the departure event
                heapq.heappush(self.events, event)

        if len(self.events) == 0:
            done = 1
            return None, reward, done 

        event = heapq.heappop(self.events)
        
        if verbose:
            debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
            debug("self.domains_deployed_simples = ", self.domains_deployed_simples)

        while event.event_type == 0: #departure, update the nework
            req = event.req
            if verbose:
                debug("Departure event")
           
            for sns in req.deployed.keys():
                domain_index = req.deployed[sns]
                update_capacities(all_simple_ns[sns], self.current_domains_capacities[domain_index], 1)
                self.domains_deployed_simples[domain_index][sns] -= 1

            self.alive_composites[req.cns_id] -= 1
            self.alive_traffic_classes[req.class_id] -= 1

            if verbose:
                debug("self.domains_deployed_simples = ", self.domains_deployed_simples)
                debug("self.domain_capacities = ", self.current_domains_capacities)
                debug("self.alive_composites = ", self.alive_composites)
                debug("self.alive_traffic_classes = ", self.alive_traffic_classes)

            if len(self.events) == 0:
                for i in range(len(self.domains_deployed_simples)):
                    for j in range(len(self.domains_deployed_simples[i])):
                        if self.domains_deployed_simples[i][j] != 0:
                            error("bug in the last state: ", self.domains_deployed_simples)
                            sys.exit()
            
                done = 1
                return None, reward, done 

            event = heapq.heappop(self.events)
            
            if verbose:
                debug("event: time = ", event.time, ", type = ", event.event_type ,", req = ", event.req)
                debug("self.domains_deployed_simples = ", self.domains_deployed_simples)
                debug("self.domain_capacities = ", self.current_domains_capacities)
                debug("self.alive_composites = ", self.alive_composites)
                debug("self.alive_traffic_classes = ", self.alive_traffic_classes)

  
        self.arriaved_demand = None
        next_state = None
        done = 0

        requests = [0 for i in range(len(all_traffic_loads))]
        requests[event.req.class_id] = 1
        self.arriaved_demand = event.req

        next_state = State(self.domains_deployed_simples, self.current_domains_capacities, self.alive_composites, self.alive_traffic_classes, requests)

        if verbose:
            debug("next_state = ", next_state)
            debug("************  env step: end *************")

        return next_state, reward, done



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


def check_feasible_deployment(simple_ns, capacities):
    for i in range(len(simple_ns.resources)):
        if simple_ns.resources[i] > capacities[i]:
            return False

    return True


def update_capacities(simple_ns, capacities, inc_dec):
    for i in range(len(simple_ns.resources)):
        capacities[i] += inc_dec * simple_ns.resources[i]

def should_overcharge(simple_ns, current_capacities, quotas, reject_threshold):
    for i in range(len(simple_ns.resources)):
        if (current_capacities[i] - simple_ns.resources[i]) < ((reject_threshold[i] - 1) * quotas[i]):
            return True

    return False


if __name__ == "__main__":
    s1 = State(4)
    print(s1)


