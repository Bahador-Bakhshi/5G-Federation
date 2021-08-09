import Environment
import parser
import non_ml_polices
from debugger import verbose
import export_import_requests
import offline_policy 

def evaluate_policy(policy_fn, demands):
    total_reward = 0
    total_accept = 0
    done = False
   
    accepteds = []
    env = Environment.Env(accepteds, demands = demands)
    s = env.start()
    
    while not done:
        a = policy_fn(s)

        if a != None and a != tuple():
            total_accept += 1

        #print("evaluate_policy: selected action = ", a)
        s,r,d = env.step(s, a)
        if d == 1:
            done = True
   
    total_reward = Environment.compute_profit(accepteds)
    return total_reward, total_accept

 
if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 5000
    iteration = 1

    greedy_reward = greedy_accept = 0
    predict_reward = predict_accept = 0
    mdp_reward = mdp_accept = 0

    for i in range(iteration):
        #demands = Environment.generate_req_set(demands_num)
        demands = export_import_requests.load_reqs(reqs_file_name = "./requests.csv")
        demands_num = len(demands)

        '''
        print("-------------------RAND--------------------")
        random_reward = evaluate_policy(non_ml_polices.random_policy, demands)    
        print("-------------------First--------------------")
        first_fit_reward = evaluate_policy(non_ml_polices.first_fit_policy, demands)   
        '''

        print("-------------------Greedy--------------------")
        reward, accept = evaluate_policy(non_ml_polices.greedy_policy, demands)    
        greedy_reward += reward
        greedy_accept = accept
 
        print("-------------------MDP--------------------")
        lookup = offline_policy.load_mdp_policy()
        reward, accept = evaluate_policy(lookup, demands)    
        mdp_reward += reward
        mdp_accept = accept
 
        print("-------------------Predict--------------------")
        reward, accept = evaluate_policy(non_ml_polices.one_step_predict_policy, demands)
        predict_reward += reward
        predict_accept = accept
        
        print("greedy_accept  = ", greedy_accept / demands_num)
        print("mdp_accept     = ", mdp_accept / demands_num)
        print("predict_accept = ", predict_accept / demands_num)

    '''
    print("random_reward    = ", random_reward)
    print("first_fit_reward = ", first_fit_reward)
    '''

    print("-----------------------------------")
    print("greedy_reward = ", 1.0 * greedy_reward / demands_num / iteration)
    print("mdp_reward    = ", 1.0 * mdp_reward / demands_num / iteration)
    print("predict_reward= ", 1.0 * predict_reward / demands_num / iteration)
