#!/usr/bin/python3

import numpy as np
import math
from collections import defaultdict
import sys
import plotting
import QL
import heapq
import itertools 
import matplotlib 
import matplotlib.style 

matplotlib.style.use('ggplot') 

server_size = 20
total_classes = 2
total_actions = 2

lams = [0] * total_classes
mus  = [0] * total_classes
ws   = [0] * total_classes
rs   = [0] * total_classes

lams[0] = 5.0
mus[0] = 2.0
ws[0] = 1.0
rs[0] = 20.0

lams[1] = 5.0
mus[1] = 0.1
ws[1]= 10.0
rs[1] = 1.0

reject = 0
accept = 1
no_request = 0
with_request = 1

gamma = 0.9 #TODO  FIXME !!!!!!!!!!!!!!!!!!!!!!!!!!!

class Actions:
    n = 0
    count = 0
    def __init__(self, n):
        self.n = n

    def move(self, action):
        if action == 0: # 1 left
            return -1
        elif action == 1: # no move
            return 0
        elif action == 2: # 1 right
            return 1
        elif action == 3: # 2 right
            return 2
        else:
            print("Unknown Action")


def arrival_after_reject(cs, arrival_index, total_rates):
    alives = cs[0]
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = lams[arrival_index] / total_rates
    return {ns: p}


def departure_after_reject(cs, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = mus[dep_index] / total_rates
    return {ns: p}


def arrival_after_accept(cs, accept_index, arrival_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    requests[arrival_index] = 1
    ns = (alives, tuple(requests))
    p = lams[arrival_index] / total_rates
    return {ns: p}


def departure_after_accept(cs, accept_index, dep_index, total_rates):
    alives = cs[0]
    alives_list = list(alives)
    alives_list[accept_index] += 1
    alives_list[dep_index] -= 1
    alives = tuple(alives_list)
    requests = [0] * len(cs[1])
    ns = (alives, tuple(requests))
    p = mus[dep_index] / total_rates
    return {ns: p}


def get_total_rates(total_classes, state):
    alives = state[0]
    requests = state[1]
    capacity = compute_capacity(alives)
 
    total_rates = 0
    for j in range(total_classes):
        total_rates += lams[j]
        if alives[j] > 0:
            total_rates += mus[j]
    
    return total_rates


def compute_capacity(alives):
    capacity = server_size
    for i in range(total_classes):
        capacity -= alives[i] * ws[i]

    return capacity


def pr(state, action):
    prob = {}
    alives = state[0]
    requests = state[1]
    capacity = compute_capacity(alives)

    total_rates = get_total_rates(total_classes, state)
    
    print("State = ", state, ", action = ", action)

    active = 0
    for i in range(len(requests)):
        if requests[i] > 0:
            active += 1
    if active > 1:
        print("Error in requests: ", requests)
        sys.exit()
        
    if action == reject:
        print("Reject")
        reward = 0
        
        for j in range(total_classes):
            prob.update(arrival_after_reject(state, j, total_rates))
            
        for j in range(total_classes):
            if alives[j] > 0:
                prob.update(departure_after_reject(state, j, total_rates))
            
    elif action == accept:
        active = 0
        for i in range(len(requests)):
            if requests[i] > 0:
                active += 1

        if active == 0:
            print("Accept for no demand!!!")
            # cannot be accepted, it is like reject but -inf for reward
            reward = -1 * np.inf

            for j in range(total_classes):
                prob.update(arrival_after_reject(state, j, total_rates))
            
            for j in range(total_classes):
                if alives[j] > 0:
                    prob.update(departure_after_reject(state, j, total_rates))
 
        else:
            req_index = np.argmax(requests)
            
            print("alives = ", requests)
            print("req_index = ", req_index, "capacity = ", capacity, "ws[req_index] = ", ws[req_index])

            if capacity < ws[req_index]:
                print("Try to accept but no resource")
                #cannot be accepted, it is like reject but -inf for reward

                reward = -1 * np.inf

                for j in range(total_classes):
                    prob.update(arrival_after_reject(state, j, total_rates))
            
                for j in range(total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_reject(state, j, total_rates))
            else:
                print("Accepting")
                reward = rs[req_index]

                for j in range(total_classes):
                    prob.update(arrival_after_accept(state, req_index, j, total_rates))

                for j in range(total_classes):
                    if alives[j] > 0:
                        prob.update(departure_after_accept(state, req_index, j, total_rates))

    else:
        print("Error")
        sys.exit()

    tp = 0
    for i in prob.keys():
        tp += prob[i]
    if abs(tp - 1.0) > 0.0001:
        print("Error in p: ", prob)
        sys.exit()

    print("State = ", state, ", action = ", action)
    print("\t Prob: ", prob)
    print("\t Reward: ", reward)

    return prob, reward


def generate_all_states(c, w):
    res = []
    for i in range (int(c / w[0]) + 1):
        for j in range(int(c / w[1]) + 1):
            if i * w[0] + j * w[1] <= c:
                capacity = c - (i * w[0] + j * w[1])
                alives = (i , j)
                
                requests = (0, 0)
                s = (alives, requests)
                res.append(s)
                
                requests = (0, 1)
                s = (alives, requests)
                res.append(s)
                
                requests = (1, 0)
                s = (alives, requests)
                res.append(s)
                

    print("All States:", res)

    return res


def print_V(V, all_s):
    print("**************************")
    for s in all_s:
        if V[s] != 0:
            print("V[{}] = {}".format(s,V[s]))
    print("==========================")

    
def DP():
    V = defaultdict(lambda: np.random.uniform(-100,-90))
    policy = {}
    all_possible_state = generate_all_states(server_size, ws)
   
    loop = True
    while loop:
        max_diff = 0

        for s in all_possible_state:
            #print_V(V, all_possible_state)
            improve = np.zeros(total_actions)
            for a in range(total_actions):
                p, r = pr(s, a)
                for ns in p.keys():
                    print("a  = ", a)
                    print("ns = ", ns)
                    print("p[ns] = ", p[ns])
                    print("r = ", r)
                    print("V[ns] = ", V[ns])
                    improve[a] += (p[ns] * (r + gamma * V[ns]))
                    print("improve[a] = ", improve[a])
            
            new_val = max(improve)
            policy.update({s: np.argmax(improve)})
            
            diff = abs(V[s] - new_val)
            if diff > max_diff:
                max_diff = diff

            V[s] = new_val
            print("Updated V[s] = ", V[s])

        if max_diff < 0.0001:
            loop = False


    print("Optimal Policy: ", policy)
    return policy

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


def generate_class_req_set(class_id, time):
    t = 0
    all_req = []
    
    while t <= time:
        t += np.random.exponential(1.0 / lams[class_id])
        life = np.random.exponential(1.0 / mus[class_id])
        all_req.append(Request(ws[class_id], t, t + life, rs[class_id], class_id))

    #print_reqs(all_req)
    return all_req


def generate_req_set(total_classes, time):
    all_class_reqs = []
    
    total_n = 0
    for i in range(total_classes):
        req_list = generate_class_req_set(i, time)
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

def test_greedy_policy(demands):
    profit = 0
    accepted = []
    capacity = server_size
    for i in range(len(demands)):
        req = demands[i]
        print("current: ", req, ", capacity = ", capacity)
        t = req.st
       
        j = 0
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                print("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                j += 1

        if req.w <= capacity:
            print("accept")
            profit += req.rev
            accepted.append(req)
            capacity -= req.w
        else:
            print("reject")

        if capacity > server_size:
            print("Error in capacity: ", capacity, ", server_size = ", server_size)

    return profit

def test_policy(demands, policy):
    profit = 0
    accepted = []
    capacity = server_size
    for i in range(len(demands)):
        req = demands[i]
        print("current: ", req, ", capacity = ", capacity)
        t = req.st

        j = 0
        alives_list = [0] * total_classes
        while j < len(accepted):
            tmp_req = accepted[j]
            if tmp_req.dt <= t:
                print("remove: ", tmp_req)
                capacity += tmp_req.w
                accepted.remove(tmp_req)
            else:
                alives_list[tmp_req.class_id] += 1
                j += 1
            
        req_index = req.class_id
        arrival_list = [0] * total_classes
        arrival_list[req_index] = 1
        
        state = (tuple(alives_list), tuple(arrival_list))
        print("State = ", state)
        random_action = False
        if state in policy:
            action = policy[state]
        else:
            print("Unknown state")
            action = int(np.random.uniform(0,1.9999))
            random_action = True
        print("Action = ", action)

        if action == 1:
            if req.w > capacity:
                if random_action == False:
                    print("Error: w = ", req.w, "capacity = ", capacity)
                    sys.exit()
                else:
                    print("Invalid random action")
            else:
                print("accept")
                profit += req.rev
                accepted.append(req)
                capacity -= req.w
        else:
            print("reject")
        
        if capacity > server_size:
            print("Error in capacity: ", capacity, ", server_size = ", server_size)

    return profit


class Actions:
    n = 0
    
    def __init__(self, n):
        self.n = n

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


class Environment:
    action_space = None
    server_size = 0
    episode_len = 0
    capacity = 0
    demands = None
    events  = None
    arriaved_demand = None

    def __init__(self, size, eplen):
        self.action_space = Actions(2)
        self.server_size  = size
        self.episode_len = eplen
        self.events = []

    def start(self):
        print("env start")
        self.capacity = self.server_size
        self.alives = [0 for i in range(total_classes)]
        
        self.demands = generate_req_set(total_classes, self.episode_len)
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
        if action == 0: #reject
            print("reject")
            reward = 0

        elif action == 1: #accept
            count = 0
            for i in range(len(current_requests)):
                if current_requests[i] != 0:
                    count += 1
            
            if count > 1:
                print("Error in requests = ", current_requests)
                sys.exit()

            if count == 0: #there is no requst to accept
                print("accepting no demand !!!!")
                reward = -1 * np.inf
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


if __name__ == "__main__":
    sim_time = 100

    init_size = 5
    step = 5
    scale = 50

    for i in range(scale):
        episode_no = init_size + i * step

        dp_policy = DP()
        env = Environment(server_size, sim_time)
        ql_policy = QL.qLearning(env, episode_no)

        greedy_profit = 0
        dp_profit = 0
        ql_profit = 0
 
        for j in range(100):

            demands = generate_req_set(total_classes, sim_time)
            #print_reqs(demands)
            greedy_profit += test_greedy_policy(demands)

            dp_profit += test_policy(demands, dp_policy)
    
            ql_profit += test_policy(demands, ql_policy)

        
        print("Profits for episode_no = ", episode_no)
        print("Greedy Profit = ", greedy_profit / 100)
        print("QL Profit = ", ql_profit / 100)
        print("DP Profit = ", dp_profit / 100)

