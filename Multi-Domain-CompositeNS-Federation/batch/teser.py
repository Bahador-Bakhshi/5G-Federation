import Environment
import parser
import non_ml_polices
from debugger import verbose
    
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
   
    total_reward = Environment.compute_profit(accepteds)
    return total_reward

 
if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 2

    demands = Environment.generate_req_set(demands_num)
    evaluate_policy(non_ml_polices.one_step_predict_policy, demands)
    
    '''
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
    '''
