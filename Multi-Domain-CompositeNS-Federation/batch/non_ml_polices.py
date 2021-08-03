import numpy as np

import Environment
import debugger
from debugger import verbose
from Environment import print_valid_actions_cache, get_cached_valid_action

def random_policy(state):
    valid_actions = get_cached_valid_action(state)
    return np.random.choice(valid_actions)


def first_fit_policy(state):
    valid_actions = get_cached_valid_action(state)
    return valid_actions[0]

def cost_estimation_based_policy(state, cost_estimator_function, n=0):
    valid_actions = get_cached_valid_action(state)
    if len(valid_actions) == 1:
        return list(valid_actions)[0]
    
    cns_index = state.arrivals_events.index(1)
    revenue = Environment.all_composite_ns[cns_index].usage_charge * (1.0 / Environment.all_traffic_loads[cns_index].mu)

    best_action = tuple() # the reject
    best_action_profit = 0
    for action in valid_actions:
        if verbose:
            print("checking profit of action", action, "in state", state)

        if action != None and action != tuple():
            this_action_cost = cost_estimator_function(state, action, n)
            if verbose:
                print("action = ", action, ", cost = ", this_action_cost)
            
            this_action_profit = revenue - this_action_cost
            if this_action_profit > best_action_profit:
                best_action = action
                best_action_profit = this_action_profit 

    if verbose:
        print("best_action = ", best_action)
        print("best_action_profit = ", best_action_profit)

    return best_action

def deployment_cost_no_prediction(state, action, dummy):
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

    return total_cost


def greedy_policy(state):
    return cost_estimation_based_policy(state, deployment_cost_no_prediction)


def get_transient_state(state, action):
    
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


def n_step_cost_prediction(state, action, n):

    if action == tuple():
        print("n_step_cost_prediction: reject")
        sys.exit()

    if n == 1:
        next_state_cost_estimator = deployment_cost_no_prediction
    else:
        n -= 1
        next_state_cost_estimator = n_step_cost_prediction

    current_traffic_class = state.arrivals_events.index(1)
    total_cost = 0

    '''
    Cost of deployment of this sns in this domain
    '''
    all_deployment_domains = action
    for domain_index in range(len(all_deployment_domains)):
        deployment_domain_sns = all_deployment_domains[domain_index]
        print("all_deployment_domains = ", all_deployment_domains)
        print("domain_index = ", domain_index)
        print("deployment_domain_sns = ", deployment_domain_sns)
        for sns in deployment_domain_sns:
            total_cost += Environment.all_domains[domain_index].usage_costs[sns] * (1.0 / Environment.all_traffic_loads[current_traffic_class].mu)

    if verbose:
        print("cost of deploying s = ", state,", in ", all_deployment_domains, " = ", total_cost)

    '''
    Effect of this deployment on the cost of subsequent requests
    '''
    for tc_index in range(len(Environment.all_traffic_loads)):

        transient_state = get_transient_state(state, action)
        tc = Environment.all_traffic_loads[tc_index]
        next_event = [0 for i in range(len(Environment.all_traffic_loads))]
        next_event[tc_index] = 1
        
        transient_state.arrivals_events = tuple(next_event) #This is the next state
        
        copy_state = state.copy_me()
        copy_state.arrivals_events = tuple(next_event)
        
        this_state_valid_actions = get_cached_valid_action(copy_state)
        next_state_valid_actions = get_cached_valid_action(transient_state)

        if verbose:
            print("tc.cns_id = ", tc.cns_id)
            print("\t this_state_valid_actions = ", this_state_valid_actions)
            print("\t next_state_valid_actions = ", next_state_valid_actions)

        reduced_actions = False
        for next_state_action in this_state_valid_actions:
            if not (next_state_action in next_state_valid_actions): 
                if verbose:
                    print("Removed action = ", next_state_action)
                        
                reduced_actions = True
                break

        if reduced_actions:
            old_actions_costs = {}
            for next_state_action in this_state_valid_actions:
                old_actions_costs[next_state_action] = next_state_cost_estimator(transient_state, next_state_action, n)

            print("this_state_valid_actions = ", this_state_valid_actions)
            print("next_state_valid_actions = ", next_state_valid_actions)
            new_actions_costs = {}
            for next_state_action in next_state_valid_actions:
                new_actions_costs[next_state_action] = old_actions_costs[next_state_action]
            
            del new_actions_costs[tuple()]
            del old_actions_costs[tuple()]

            if verbose:
                print("old_actions_costs = ", old_actions_costs)
                print("new_actions_costs = ", new_actions_costs)

            old_best = min(old_actions_costs.values())
            new_best = min(new_actions_costs.values())

            total_cost += (new_best - old_best) * (1.0 / Environment.all_traffic_loads[tc_index].mu) * (Environment.all_traffic_loads[tc_index].lam / Environment.all_traffic_loads[current_traffic_class].mu)
        
        else:
            if verbose: 
                print("No change in actions")

    if verbose:
        print("total_cost = ", total_cost)

    return total_cost


def one_step_predict_policy(state):
    return cost_estimation_based_policy(state, n_step_cost_prediction, 1)

