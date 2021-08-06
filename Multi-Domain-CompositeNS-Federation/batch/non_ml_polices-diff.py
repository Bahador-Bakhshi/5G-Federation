import numpy as np

import Environment
import debugger
from debugger import verbose
from Environment import print_valid_actions_cache, get_cached_valid_action

gamma = 0.9999

def random_policy(state):
    valid_actions = get_cached_valid_action(state)
    return np.random.choice(valid_actions)


def first_fit_policy(state):
    valid_actions = get_cached_valid_action(state)
    return valid_actions[0]

def profit_estimation_based_policy(state, profit_estimator_function, n=0):
    valid_actions = get_cached_valid_action(state)
    if len(valid_actions) == 1:
        return list(valid_actions)[0]
    
    best_action = tuple() # the reject
    best_action_profit = 0
    for action in valid_actions:
        if verbose:
            print("checking profit of action", action, "in state", state)

        if action != None:
            this_action_profit = profit_estimator_function(state, action, n)
            if verbose:
                print("action = ", action, ", profit = ", this_action_profit)
            
            if this_action_profit > best_action_profit:
                best_action = action
                best_action_profit = this_action_profit 

    if verbose:
        print("best_action = ", best_action)
        print("best_action_profit = ", best_action_profit)

    return best_action

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


def greedy_policy(state):
    return profit_estimation_based_policy(state, deployment_profit_no_prediction)


def get_transient_arrival_state(state, action):
    
    domains_deployed_simples = [list(x) for x in state.domains_deployed_simples].copy()
    domains_resources = [list(x) for x in state.domains_resources].copy()
    
    all_deployment_domains = action
    for domain_index in range(len(all_deployment_domains)):
        deployment_domain_sns = all_deployment_domains[domain_index]
        for sns in deployment_domain_sns:
            domains_deployed_simples[domain_index][sns] += 1
            Environment.update_capacities(Environment.all_simple_ns[sns], domains_resources[domain_index], -1)

    current_traffic_class = state.arrivals_events.index(1)
    
    alive_composites = list(state.alive_composites).copy()
    alive_composites[current_traffic_class] += 1

    alive_traffic_classes = list(state.alive_traffic_classes).copy()
    alive_traffic_classes[current_traffic_class] += 1

    events = [0 for i in range(len(state.arrivals_events))].copy()

    transient_state = Environment.State(domains_deployed_simples, domains_resources, alive_composites, alive_traffic_classes, events)

    if verbose:
        print("state = ", state)
        print("action = ", action)
        print("transient_state = ", transient_state)    
    
    return transient_state

def get_transient_departure_state(state, action, tc_index):
    
    if action != None:
        print("action must be none")
        sys.exit(1)

    domains_deployed_simples = [list(x) for x in state.domains_deployed_simples].copy()
    domains_resources = [list(x) for x in state.domains_resources].copy()
    
    for domain_index in range(len(all_deployment_domains)):
        deployment_domain_sns = all_deployment_domains[domain_index]
        for sns in deployment_domain_sns:
            domains_deployed_simples[domain_index][sns] += 1
            Environment.update_capacities(Environment.all_simple_ns[sns], domains_resources[domain_index], -1)

    current_traffic_class = state.arrivals_events.index(1)
    
    alive_composites = list(state.alive_composites).copy()
    alive_composites[current_traffic_class] += 1

    alive_traffic_classes = list(state.alive_traffic_classes).copy()
    alive_traffic_classes[current_traffic_class] += 1

    events = [0 for i in range(len(state.arrivals_events))].copy()

    transient_state = Environment.State(domains_deployed_simples, domains_resources, alive_composites, alive_traffic_classes, events)

    if verbose:
        print("state = ", state)
        print("action = ", action)
        print("transient_state = ", transient_state)    
    
    return transient_state



def n_step_profit_prediction(state, action, n):

    if n == 1:
        next_state_profit_estimator = deployment_profit_no_prediction
    else:
        if action != None:
            n -= 1
        next_state_profit_estimator = n_step_profit_prediction

    current_traffic_class = state.arrivals_events.index(1)
    total_profit = 0

    '''
    profit of deployment of this sns in this domain
    '''
    total_cost = 0
    all_deployment_domains = action
    for domain_index in range(len(all_deployment_domains)):
        deployment_domain_sns = all_deployment_domains[domain_index]
        for sns in deployment_domain_sns:
            total_cost += Environment.all_domains[domain_index].usage_costs[sns] * (1.0 / Environment.all_traffic_loads[current_traffic_class].mu)

    if action != tuple():
        total_revenue = Environment.all_composite_ns[current_traffic_class].usage_charge *  (1.0 / Environment.all_traffic_loads[current_traffic_class].mu)
    else:
        total_revenue = 0

    total_profit = total_revenue - total_cost
    if verbose:
        print("profit of deploying s = ", state,", in ", all_deployment_domains, " = ", total_profit)

    '''
    effect of this deployment on the profit of subsequent requests
    '''
    total_profit_reduction = 0
    total_arrival_rates = 0
    total_departure_rates = 0

    for tc_index in range(len(Environment.all_traffic_loads)):
        total_arrival_rates += Environment.all_traffic_loads[tc_index].lam

    tmp_state = get_transient_state(state, action)
    for tc_index in range(len(Environment.all_traffic_loads)):
        tc = Environment.all_traffic_loads[tc_index]
        total_departure_rates += tc.mu * (tmp_state.alive_composites[tc.cns_id])

    for tc_index in range(len(Environment.all_traffic_loads)):
        if tc_index == current_traffic_class:
            continue 

        state_if_action_applied = get_transient_state(state, action)
        tc = Environment.all_traffic_loads[tc_index]
        next_event = [0 for i in range(len(Environment.all_traffic_loads))]
        next_event[tc_index] = 1
        
        state_if_action_applied.arrivals_events = tuple(next_event)
        
        state_without_applying_action = state.copy_me()
        state_without_applying_action.arrivals_events = tuple(next_event)
        
        next_event_valids_if_action_applied = get_cached_valid_action(state_if_action_applied)
        next_event_valids_without_applying_action = get_cached_valid_action(state_without_applying_action)

        if verbose:
            print("ARRIVAL: tc.cns_id = ", tc.cns_id)
            print("\t next_event_valids_without_applying_action = ", next_event_valids_without_applying_action)
            print("\t next_event_valids_if_action_applied = ", next_event_valids_if_action_applied)
        
        '''
        reduced_actions = False
        for next_state_action in this_state_valid_actions:
            if not (next_state_action in next_state_valid_actions): 
                if verbose:
                    print("Removed action = ", next_state_action)
                        
                reduced_actions = True
                break

        if reduced_actions:
        '''
        if True:
            profits_if_action_applied = {}
            for a in next_event_valids_if_action_applied:
                profits_if_action_applied[a] = next_state_profit_estimator(state_if_action_applied, a, n)
        
            '''
            if verbose:
                print("this_state_valid_actions = ", this_state_valid_actions)
                print("next_state_valid_actions = ", next_state_valid_actions)
            
            new_actions_profit = {}
            for next_state_action in next_state_valid_actions:
                new_actions_profit[next_state_action] = old_actions_profit[next_state_action]
            
            #del new_actions_costs[tuple()]
            #del old_actions_costs[tuple()]
            '''
            
            profits_without_applying_action = {}
            for a in next_event_valids_without_applying_action:
                profits_without_applying_action[a] = next_state_profit_estimator(state_without_applying_action, a, n)
 
            if verbose:
                print("profits_if_action_applied = ", profits_if_action_applied)
                print("profits_without_applying_action = ", profits_without_applying_action)

            max_profit_if_action_applied  = max(profits_if_action_applied.values())
            max_profit_without_applying_action  = max(profits_without_applying_action.values())

            this_profit_reduction = (max_profit_if_action_applied - max_profit_without_applying_action) * (Environment.all_traffic_loads[tc_index].lam / (total_arrival_rates + total_departure_rates))
            #* (Environment.all_traffic_loads[tc_index].lam / Environment.all_traffic_loads[current_traffic_class].mu)

            if verbose:
                print("this_profit_reduction = ", this_profit_reduction)
            
            total_profit_reduction += this_profit_reduction
            
        else:
            if verbose: 
                print("No change in actions")


    tmp_state = get_transient_state(state, action)
    for tc_index in range(len(Environment.all_traffic_loads)):
        if tmp_state.alive_composites[Environment.all_traffic_loads[tc_index].cns_id] <= 0:
            continue

        state_if_action_applied = get_transient_state(state, action)
        tc = Environment.all_traffic_loads[tc_index]
        next_event = [0 for i in range(len(Environment.all_traffic_loads))]
        next_event[tc_index] = 1
        state_if_action_applied.departure_events = tuple(next_event)
        
        state_without_applying_action = state.copy_me()
        state_without_applying_action.departure_events = tuple(next_event)
        
        next_event_valids_if_action_applied = get_cached_valid_action(state_if_action_applied)
        next_event_valids_without_applying_action = get_cached_valid_action(state_without_applying_action)

        if verbose:
            print("DEPARTURE: tc.cns_id = ", tc.cns_id)
            print("\t state  = ", state)
            print("\t action = ", action)
            print("\t next_event_valids_without_applying_action = ", next_event_valids_without_applying_action)
            print("\t next_event_valids_if_action_applied = ", next_event_valids_if_action_applied)
        
        if True:
            profits_if_action_applied = {}
            profits_if_action_applied[None] = next_state_profit_estimator(state_if_action_applied, None, n)
        
            profits_without_applying_action = {}
            profits_without_applying_action[None] = next_state_profit_estimator(state_without_applying_action, None, n)
 
            if verbose:
                print("profits_if_action_applied = ", profits_if_action_applied)
                print("profits_without_applying_action = ", profits_without_applying_action)

            max_profit_if_action_applied  = max(profits_if_action_applied.values())
            max_profit_without_applying_action  = max(profits_without_applying_action.values())

            this_profit_reduction = (max_profit_if_action_applied - max_profit_without_applying_action) * ((Environment.all_traffic_loads[tc_index].mu * tmp_state.alive_composites[Environment.all_traffic_loads[tc_index].cns_id])/ (total_arrival_rates + total_departure_rates))

            if verbose:
                print("this_profit_reduction = ", this_profit_reduction)
            
            total_profit_reduction += this_profit_reduction
        


    total_profit = total_profit + gamma * total_profit_reduction

    if verbose:
        print("final total_profit = ", total_profit)

    return total_profit


def one_step_predict_policy(state):
    return profit_estimation_based_policy(state, n_step_profit_prediction, 3)

