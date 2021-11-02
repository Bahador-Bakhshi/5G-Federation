import numpy as np
import sys
import math 

import Environment
import debugger
from debugger import verbose
from Environment import print_valid_actions_cache, get_cached_valid_action

#gamma = 1.0
profit_cache = {}
max_prediction_steps = 10


def random_policy(state):
    valid_actions = get_cached_valid_action(state)
    return np.random.choice(valid_actions)


def first_fit_policy(state):
    valid_actions = get_cached_valid_action(state)
    return valid_actions[0]

def profit_estimation_based_policy(state, profit_estimator_function, n=0):
    #verbose = True
    valid_actions = get_cached_valid_action(state)
    if len(valid_actions) == 1:
        return list(valid_actions)[0]
    
    best_action = tuple() # the reject
    best_action_profit = 0
    for action in valid_actions:
        if verbose:
            print("checking profit of action", action, "in state", state)

        if action != None:
            ongoing_estimations = {}
            this_action_profit = profit_estimator_function(state, action, n, ongoing_estimations)
            if verbose:
                print("action = ", action, ", profit = ", this_action_profit)
            
            if this_action_profit > best_action_profit:
                best_action = action
                best_action_profit = this_action_profit 

    if verbose:
        print("best_action = ", best_action)
        print("best_action_profit = ", best_action_profit)

    return best_action

'''
def deployment_profit_no_prediction(state, action, dummy):
    if action == tuple():
        return 0

    deployment_domains = action
    total_cost = 0
    for domain in deployment_domains:
        domain_index = deployment_domains.index(domain)
            
        for sns in domain:
            cost_scale = -1
                
            if Environment.should_overcharge(Environment.all_simple_ns[sns], state.domains_resources[domain_index], Environment.all_domains[domain_index].quotas, Environment.all_domains[domain_index].reject_thresholds):
                cost_scale = Environment.all_domains[domain_index].overcharges[sns]
            else:
                cost_scale = 1

            total_cost += Environment.all_domains[domain_index].usage_costs[sns] * cost_scale

    current_cns_index = state.arrivals_events.index(1)
    total_profit = (Environment.all_composite_ns[current_cns_index].usage_charge - total_cost) * (1.0 / Environment.all_traffic_loads[current_cns_index].mu)
    
    if verbose:
        print("deployment_profit_no_prediction:")
        print("\t state = ", state)
        print("\t action = ", action)
        print("\t total_profit = ", total_profit)

    return total_profit
'''

def deployment_profit_no_prediction_old(state, action, dummy_n=0, dummy_ongoing=None):
    if action == None or action == tuple():
        return 0

    deployment_domains = action
    total_cost = 0
    for domain in deployment_domains:
        domain_index = deployment_domains.index(domain)
            
        for sns in domain:
            cost_scale = -1
                
            if Environment.should_overcharge(Environment.all_simple_ns[sns], state.domains_resources[domain_index], Environment.all_domains[domain_index].quotas, Environment.all_domains[domain_index].reject_thresholds):
                cost_scale = Environment.all_domains[domain_index].overcharges[sns]
            else:
                cost_scale = 1

            total_cost += Environment.all_domains[domain_index].usage_costs[sns] * cost_scale

    current_cns_index = state.arrivals_events.index(1)
    total_profit = (Environment.all_composite_ns[current_cns_index].usage_charge - total_cost)
    
    if verbose:
        print("deployment_profit_no_prediction_old:")
        print("\t state = ", state)
        print("\t action = ", action)
        print("\t total_profit = ", total_profit)

    return total_profit


def greedy_policy(state):
    return profit_estimation_based_policy(state, deployment_profit_no_prediction_old)


def get_transient_state(state, action):
   
    domains_deployed_simples = [list(x) for x in state.domains_deployed_simples].copy()
    domains_resources = [list(x) for x in state.domains_resources].copy()
    alive_composites = list(state.alive_composites).copy()
    alive_traffic_classes = list(state.alive_traffic_classes).copy()
    arrival_requests = [0 for i in range(len(state.arrivals_events))].copy()
    departure_events = [[0 for i in range(len(state.departure_events_perdomain[0]))] for j in range(len(state.departure_events_perdomain))]
    
    if action == None:
        #find the departing demand from the domain
        departing_tc = 0
        departing_domain = 0
        
        for domain in range(len(state.departure_events_perdomain)):
            for tc in range(len(state.departure_events_perdomain[domain])):
                if state.departure_events_perdomain[domain][tc] == 1:
                    departing_tc = tc
                    departing_domain = domain
        
        domains_deployed_simples[departing_domain][departing_tc] -= 1
        Environment.update_capacities(Environment.all_simple_ns[departing_tc], domains_resources[departing_domain], +1)

        alive_composites[departing_tc] -= 1
        alive_traffic_classes[departing_tc] -= 1

    elif action == tuple():
        pass

    else:
        all_deployment_domains = action
        for domain_index in range(len(all_deployment_domains)):
            deployment_domain_sns = all_deployment_domains[domain_index]
            for sns in deployment_domain_sns:
                domains_deployed_simples[domain_index][sns] += 1
                Environment.update_capacities(Environment.all_simple_ns[sns], domains_resources[domain_index], -1)

        current_traffic_class = state.arrivals_events.index(1)
    
        alive_composites[current_traffic_class] += 1
        alive_traffic_classes[current_traffic_class] += 1

    transient_state = Environment.State(domains_deployed_simples, domains_resources, alive_composites, alive_traffic_classes, arrival_requests, departure_events)

    if verbose:
        print("state = ", state)
        print("action = ", action)
        print("transient_state = ", transient_state)    
   
    Environment.check_state_validity(transient_state)

    return transient_state


def estimate_next_state_value(this_event_rate, total_arrival_rates, total_departure_rates, state_if_action_applied, next_state_profit_estimator, n, ongoing_estimations):

    if state_if_action_applied in ongoing_estimations:
        if verbose:
            print("found in ongoing_estimations, state = ", state_if_action_applied,", action = ", ongoing_estimations[state_if_action_applied])
        ongoing_action = ongoing_estimations[state_if_action_applied]
        next_event_valids_if_action_applied = (ongoing_action, )
    else:
        next_event_valids_if_action_applied = get_cached_valid_action(state_if_action_applied)

    if verbose:
        print("ongoing_estimations = ", ongoing_estimations)
        print("next_event_valids_if_action_applied = ", next_event_valids_if_action_applied)
        
    profits_if_action_applied = {}
    for a in next_event_valids_if_action_applied:
        profits_if_action_applied[a] = next_state_profit_estimator(state_if_action_applied, a, n, ongoing_estimations.copy())
        
        if verbose:
            print("profits_if_action_applied = ", profits_if_action_applied)

    max_profit_if_action_applied = max(profits_if_action_applied.values())

    this_next_profit = (max_profit_if_action_applied) * (this_event_rate / (total_arrival_rates + total_departure_rates))

    if verbose:
        print("this_next_profit = ", this_next_profit)

    return this_next_profit
 

def n_step_profit_prediction(state, action, n, ongoing_estimations):
    #verbose = False
    #if n == max_prediction_steps:
    #    verbose = True

    if verbose:
        print("\n\nn_step: state = ", state, ", action = ", action)

    #gamma = 1.0 / ((max_prediction_steps - n) / max_prediction_steps + 1.0)
    #gamma = (1.0 * n) / max_prediction_steps
    #gamma = 1 - math.exp(-2 * (1 - ((max_prediction_steps - n) / (1.0 * max_prediction_steps))))
    gamma = 0.999
    ongoing_estimations[state] = action

    if n != max_prediction_steps:
        for i in range(max_prediction_steps, -1, -1):
        #for i in range(max_prediction_steps, n-1, -1):
        #for i in range(n, n - 1, -1):
            key = (state, action, i)
            if key in profit_cache:
                #print("using profit_cache...")
                return profit_cache[key]
        
        if n == 0:
            return deployment_profit_no_prediction_old(state, action)
    '''
    n -= 1
    if n == 0:
        next_state_profit_estimator = deployment_profit_no_prediction_old
    else:
        next_state_profit_estimator = n_step_profit_prediction
    '''
    n -= 1
    next_state_profit_estimator = n_step_profit_prediction

    this_action_profit = 0
    this_action_cost  = 0
    current_traffic_class = -1
    if action == None:
        this_action_profit = 0
        this_action_cost = 0
    elif action == tuple():
        current_traffic_class = state.arrivals_events.index(1)
        this_action_profit = 0
        this_action_cost = 0
    else:
        '''
        profit of deployment of this sns in this domain
        '''
        current_traffic_class = state.arrivals_events.index(1)
        this_action_profit = deployment_profit_no_prediction_old(state, action)

        if verbose:
            print("\t this_action_profit = ", this_action_profit)
        
    '''
    transient state
    '''
    transient_state = get_transient_state(state, action)
    
    if verbose:
        print("\t transient_state = ", transient_state)

    '''
    profit of subsequent requests
    '''
    total_next_profit = 0
    total_arrival_rates = 0
    total_departure_rates = 0

    for tc_index in range(len(Environment.all_traffic_loads)):
        #if action == tuple() and tc_index == current_traffic_class:
        #    pass
        #else:
        total_arrival_rates += Environment.all_traffic_loads[tc_index].lam

    for tc_index in range(len(Environment.all_traffic_loads)):
        for domain_index in range(len(Environment.all_domains)):
            tc = Environment.all_traffic_loads[tc_index]
            num = transient_state.domains_deployed_simples[domain_index][tc_index]
        total_departure_rates += tc.mu * num

    '''
    arrival events
    '''
    for tc_index in range(len(Environment.all_traffic_loads)):
        #if action == tuple() and tc_index == current_traffic_class:
        #    continue 

        state_if_action_applied = transient_state.copy_me()
        tc = Environment.all_traffic_loads[tc_index]
        next_event = [0 for i in range(len(Environment.all_traffic_loads))]
        next_event[tc_index] = 1
        state_if_action_applied.arrivals_events = tuple(next_event)
        
        this_next_profit = gamma * estimate_next_state_value(Environment.all_traffic_loads[tc_index].lam, total_arrival_rates, total_departure_rates, state_if_action_applied, next_state_profit_estimator, n, ongoing_estimations.copy())

        if verbose:
            print("\t state_if_action_applied = ", state_if_action_applied, ", this_next_profit = ", this_next_profit)

        total_next_profit += this_next_profit

    '''
    departure events
    '''
    for tc_index in range(len(Environment.all_traffic_loads)):
        for domain_index in range(len(Environment.all_domains)):
            if transient_state.domains_deployed_simples[domain_index][tc_index] > 0:
                state_if_action_applied = transient_state.copy_me()
                tc = Environment.all_traffic_loads[tc_index]
                next_event = [[0 for i in range(len(Environment.all_traffic_loads))] for j in range(len(Environment.all_domains))]
                next_event[domain_index][tc_index] = 1
                state_if_action_applied.departure_events_perdomain = tuple([tuple(x) for x in next_event])
 
                this_next_profit = gamma * estimate_next_state_value(Environment.all_traffic_loads[tc_index].mu * transient_state.domains_deployed_simples[domain_index][tc_index], total_arrival_rates, total_departure_rates, state_if_action_applied, next_state_profit_estimator, n, ongoing_estimations.copy())

                if verbose:
                    print("\t state_if_action_applied = ", state_if_action_applied, ", this_next_profit = ", this_next_profit)
                
                total_next_profit += this_next_profit
           
    total_profit = this_action_profit + total_next_profit

    if verbose:
        print("final total_profit = ", total_profit)

    key = (state, action, n+1)
    profit_cache[key] = total_profit

    ongoing_estimations.pop(state)
    
    return (total_profit)

average_reward = 0
'''
processed_demands_cnt = 0
total_accum_reward = 0
'''
time_step = 0
def one_step_predict_policy(state):
    global time_step, max_prediction_steps
    time_step += 1
    #max_prediction_steps = int(time_step / 2000) + 1
    profit = profit_estimation_based_policy(state, n_step_profit_prediction, max_prediction_steps)
    '''
    global total_accum_reward, processed_demands_cnt, average_reward
    total_accum_reward += profit
    processed_demands_cnt += 1
    average_reward = (1.0 * total_accum_reward) / processed_demands_cnt
    if processed_demands_cnt % 100 == 0:
        print("cnt = ", processed_demands_cnt, " avg = ", average_reward)
    '''
    return profit

