import numpy as np

import Environment
import debugger
from debugger import verbose 

valid_actions_cache = {}

def update_valid_actions_cache(state):
    valid_actions_cache[state] = []

    for action in range(len(Environment.all_actions)):
        deployment_domains = Environment.all_actions[action]
        feasible_deployment = True
        for domain in deployment_domains:
            domain_index = deployment_domains.index(domain)
            tmp_domain_resources = list(state.domains_resources[domain_index]).copy()
            for sns in domain:
                if Environment.all_domains[domain_index].costs[sns] < np.inf and Environment.check_feasible_deployment(Environment.all_simple_ns[sns], tmp_domain_resources):
                    Environment.update_capacities(Environment.all_simple_ns[sns], tmp_domain_resources, -1)

                    if debugger.check_points:
                        for x in tmp_domain_resources:
                            if x < 0:
                                print("tmp_domain_resources < 0")
                                sys.exit(-1)

                else:
                    feasible_deployment = False
                    break

            if feasible_deployment == False:
                break

        if feasible_deployment:
            valid_actions_cache[state].append(action)

    valid_actions_cache[state].append(Environment.reject_action)
    
    if verbose:
        print("valid actions for state", state," = ", valid_actions_cache[state])


def random_policy(state):

    if state in valid_actions_cache:
        if verbose:
            print("using action cache :-)")
    else:
        update_valid_actions_cache(state)

    return np.random.choice(valid_actions_cache[state])


def first_fit_policy(state):
    if state in valid_actions_cache:
        if verbose:
            print("using action cache :-)")
    else:
        update_valid_actions_cache(state)

    return valid_actions_cache[state][0]

def get_deployment_cost(state, action):
    if action == Environment.reject_action:
        return np.inf

    deployment_domains = Environment.all_actions[action]
    total_cost = 0
    for domain in deployment_domains:
        domain_index = deployment_domains.index(domain)
            
        for sns in domain:
            cost_scale = -1
                
            if Environment.should_overcharge(Environment.all_simple_ns[sns], state.domains_resources[domain_index], Environment.all_domains[domain_index].quotas, Environment.all_domains[domain_index].reject_thresholds):
                cost_scale = Environment.all_domains[domain_index].overcharges[sns]
            else:
                cost_scale = 1

            total_cost += Environment.all_domains[domain_index].costs[sns] * cost_scale

    return total_cost

def greedy_policy(state):
    if state in valid_actions_cache:
        if verbose:
            print("using action cache :-)")
    else:
        update_valid_actions_cache(state)
    
    best_action = Environment.reject_action
    best_action_cost = np.inf
    for action in valid_actions_cache[state]:
        this_action_cost = get_deployment_cost(state, action)
        if verbose:
            print("action = ", action, ", cost = ", this_action_cost)
        
        if this_action_cost < best_action_cost:
            best_action = action
            best_action_cost = this_action_cost 

    if verbose:
        print("best_action = ", best_action)
        print("best_action_cost = ", best_action_cost)

    return best_action


