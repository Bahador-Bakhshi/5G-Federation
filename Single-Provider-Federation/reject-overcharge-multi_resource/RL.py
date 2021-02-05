#!/usr/bin/python3

from TD import *

def rLearning(env, num_episodes, dynamic, alpha0, epsilon0, beta0):
    
    Q = defaultdict(lambda: np.random.uniform(0, 1, len(env.action_space)))

    # Create an epsilon greedy policy function
    # appropriately for environment action space
    policy = createEpsilonGreedyPolicy(Q, env)
    seen_states = set()

    rho = 1.0
    decay = 0.025

    # For every episode
    for ith_episode in range(num_episodes):

        if(dynamic == 1):
            '''
            alpha = alpha * 0.97
            epsilon = epsilon * 0.97
            beta = beta * 0.97
            '''
            alpha = alpha0 / (1.0 + ith_episode * decay)
            epsilon = epsilon0 / (1.0 + ith_episode * decay)
            beta = beta0 / (1.0 + ith_episode * decay)

        if verbose:
            debug("alpha = ", alpha, "epsilon = ", epsilon)
        
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():
            
            # get probabilities of all actions from current state
            action_probabilities = policy(state, epsilon, seen_states)
            
            action_index = np.random.choice(np.arange(len(action_probabilities)), p = action_probabilities)
            action = Environment.Actions(action_index)
            
            if verbose:
                debug("selected action =", action)

            # take action and get reward, transit to next state
            next_state, reward, done = env.step(state, action)

            if verbose:
                debug("next_state =", next_state, "reward =", reward, ", done =", done)
            
            # done is True if episode terminated
            if done:
                break


            best_next_action = np.argmax(Q[next_state])
                
            if verbose:
                debug("best_next_action = ", best_next_action)
                debug("reward = ", reward, ", rho = ", rho, " Q = ", Q[next_state][best_next_action])
                
            td_target = reward - rho + Q[next_state][best_next_action]

            if verbose:
                debug("td_target = ", td_target)
                
            td_delta = td_target - Q[state][action]
                
            if verbose:
                debug("td_delta = ", td_delta)

            Q[state][action] += alpha * td_delta

            current_best_action = np.argmax(Q[state])

            if Q[state][action] == Q[state][current_best_action]:
                rho += beta * (reward - rho + Q[next_state][best_next_action] - Q[state][current_best_action])
                
            if verbose:
                debug("rho = ", rho)
            
            seen_states.add(state)
            state = next_state
    
    final_policy = {}
    for i in Q:
        final_policy[i] = Environment.Actions(np.argmax(Q[i]))

    return final_policy


if __name__ == "__main__":

    demand_num = 20

    parser.parse_config("config.json")
    
    pi_policy = policy_iteration(0.995)
    print("********* DP Policy ***********")
    print_policy(pi_policy)

    env = Environment.Env(Environment.domain.capacities.copy(), Environment.providers[1].quotas.copy(), demand_num)
    rl_policy = rLearning(env, 1, 1, 0.9, 0.9, 0.9)

    print("********* RL Policy ***********")
    print_policy(rl_policy)


