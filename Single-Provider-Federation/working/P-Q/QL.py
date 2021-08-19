#!/usr/bin/python3

from TD import *


def qLearning(env, num_episodes, dynamic, alpha0, epsilon0, gamma0, prefix):

    Q = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))
    
    # Create an epsilon greedy policy function
    # appropriately for environment action space
    seen_states = set()
    policy = createEpsilonGreedyPolicy(Q, env)

    discount_factor = 0.0
    decay = 0.025

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            #alpha = alpha * 0.97
            #epsilon = epsilon * 0.97
            alpha = alpha0 / (1.0 + ith_episode * decay)
            epsilon = epsilon0 / (1.0 + ith_episode * decay)
        if verbose:
            debug("alpha = ", alpha, "epsilon = ", epsilon, "gamma = ", gamma0)
        
        state = env.reset()

        for t in itertools.count():
            if verbose:
                debug("\nt =", t, "sate =", state)
                print_Q(Q)

            action_probabilities = policy(state, epsilon, seen_states)
            if verbose:
                debug("action_probabilities = ", action_probabilities)

            # choose action according to the probability distribution
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)

            if verbose:
                debug("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
            if done:
                break

            if Environment.is_active_state(state):
                discount_factor = gamma0
            else:
                discount_factor = 1.0

            best_next_action = np.argmax(Q[next_state])
                
            if verbose:
                debug("best_next_action = ", best_next_action)

            #if state == next_state:
            #        pass #FIXME!!!!!!!!!!!!!!!!!

            td_target = reward + discount_factor * Q[next_state][best_next_action]

            if verbose:
                debug("td_target = ", td_target)
                
            td_delta = td_target - Q[state][action]
                    
            if verbose:
                debug("td_delta = ", td_delta)

            Q[state][action] += alpha * td_delta
 
            seen_states.add(state)
            
            if verbose:
                debug("seen_states = ", seen_states)
           
            state = next_state
    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    if verbose:
        print(final_policy)
    
    print(prefix, " ", num_episodes, get_q_values_stat(Q))
    return final_policy


if __name__ == "__main__":

    demand_num = 200

    parser.parse_config("config.json")
    
    #pi_policy = policy_iteration(0.995)
    #print("********* DP Policy ***********")
    #print_policy(pi_policy)

    for i in range(1,5):
        env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), demand_num)
        ql_policy = qLearning(env, i * 100, 1, 0.9, 0.9, 0.9, "XYX")

    #print("********* QL Policy ***********")
    #print_policy(ql_policy)


