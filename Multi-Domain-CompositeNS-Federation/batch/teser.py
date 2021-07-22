import Environment
import parser
import non_ml_polices

if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 10

    env = Environment.Env(demands_num)
    total_reward = 0
    s = env.start()
    done = False
    while not done:
        #a = non_ml_polices.random_policy(s)
        #a = non_ml_polices.first_fit(s)
        a = non_ml_polices.greedy(s)
        s,r,d = env.step(s, a)
        total_reward += r
        if d == 1:
            done = True

    print("total_reward = ", total_reward)

