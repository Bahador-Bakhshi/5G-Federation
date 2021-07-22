import numpy as np

import Environment
from debuger import verbose 

valid_actions_cache = {}

def policy(state):

    if state in valid_actions_cache:
        if verbose:
            print("using action cache :-)")
        return np.random.choice(valid_actions_cache[state])

    valid_actions_cache[state] = []
    valid_actions_cache[state].append(Environment.reject_action)

    for action in range(len(Environment.all_actions)):
        deployment_domains = Environment.all_actions[action]
        feasible_deployment = True
        for domain in deployment_domains:
            domain_index = deployment_domains.index(domain)
            for sns in domain:
                if Environment.all_domains[domain_index].costs[sns] < np.inf and Environment.check_feasible_deployment(Environment.all_simple_ns[sns], state.domains_resources[domain_index]):
                    pass
                else:
                    feasible_deployment = False
                    break

            if feasible_deployment == False:
                break

        if feasible_deployment:
            valid_actions_cache[state].append(action)

    if verbose:
        print("valid actions for state", state," = ", valid_actions_cache[state])

    return np.random.choice(valid_actions_cache[state])

