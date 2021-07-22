import Environment
import parser
import RandomPolicy

if __name__ == "__main__":
    parser.parse_config("config.json")
    demands_num = 10

    env = Environment.Env(demands_num)
    total_reward = 0
    s = env.start()
    done = False
    while not done:
        a = RandomPolicy.policy(s)
        s,r,d = env.step(s, a)
        total_reward += r
        if d == 1:
            done = True

    print("total_reward = ", total_reward)

