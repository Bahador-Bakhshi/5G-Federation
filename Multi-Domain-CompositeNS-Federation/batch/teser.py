import Environment
import parser
import non_ml_polices
from debugger import verbose

def compute_profit(accepteds):
    revenue = 0
    cost = 0

    for req in accepteds:
        if verbose:
            print("compute_profit = ")
            print("\t req: ", req)
            print("\t setup_charge = ", Environment.all_composite_ns[req.cns_id].setup_charge)
            print("\t usage_charge = ", Environment.all_composite_ns[req.cns_id].usage_charge * (req.dt - req.st))

        revenue += Environment.all_composite_ns[req.cns_id].setup_charge
        revenue += Environment.all_composite_ns[req.cns_id].usage_charge * (req.dt - req.st)

        for sns in req.deployed:
            domain_index = req.deployed[sns][0]
            cost_scale = req.deployed[sns][1]
            
            if verbose:
                print("\t domain usage_costs = ", Environment.all_domains[domain_index].usage_costs[sns])
                print("\t cost_scale  = ", cost_scale)
                print("\t cost = ", Environment.all_domains[domain_index].usage_costs[sns] * cost_scale * (req.dt - req.st))
            
            cost += Environment.all_domains[domain_index].usage_costs[sns] * cost_scale * (req.dt - req.st)

    return revenue - cost
    
def evaluate_policy(policy_fn, demands):
    total_reward = 0
    done = False
   
    accepteds = []
    env = Environment.Env(accepteds, demands = demands)
    s = env.start()
    
    while not done:
        '''
        arrival_count = 0
        for e in s.arrivals_events:
            if e == 1:
                arrival_count += 1

        if arrival_count == 0:
            a = Environment.depart_action
        else:
        '''

        a = policy_fn(s)
        
        s,r,d = env.step(s, a)
        if d == 1:
            done = True
   
    total_reward = compute_profit(accepteds)
    return total_reward

 
if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 2000
    for i in range(1):
        demands = Environment.generate_req_set(demands_num)
        print("-------------------RAND--------------------")
        random_reward = evaluate_policy(non_ml_polices.random_policy, demands)    
        print("-------------------First--------------------")
        first_fit_reward = evaluate_policy(non_ml_polices.first_fit_policy, demands)    
        print("-------------------Greedy--------------------")
        greedy_reward = evaluate_policy(non_ml_polices.greedy_policy, demands)    


        print("random_reward    = ", random_reward)
        print("first_fit_reward = ", first_fit_reward)
        print("greedy_reward    = ", greedy_reward)
