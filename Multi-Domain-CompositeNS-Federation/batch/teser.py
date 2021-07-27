import Environment
import parser
import non_ml_polices

def evaluate_policy(policy_fn, demands):
    total_reward = 0
    done = False
    
    env = Environment.Env(demands = demands)
    s = env.start()
    
    while not done:
        a = policy_fn(s)
        s,r,d = env.step(s, a)
        total_reward += r
        if d == 1:
            done = True
    
    return total_reward

 
if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 2000

    for i in range(20):
        demands = Environment.generate_req_set(demands_num)
        random_reward = evaluate_policy(non_ml_polices.random_policy, demands)    
        first_fit_reward = evaluate_policy(non_ml_polices.first_fit_policy, demands)    
        greedy_reward = evaluate_policy(non_ml_polices.greedy_policy, demands)    


        print("random_reward    = ", random_reward)
        print("first_fit_reward = ", first_fit_reward)
        print("greedy_reward    = ", greedy_reward)
