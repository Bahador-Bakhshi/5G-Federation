import Environment
import parser

if __name__ == "__main__":
    parser.parse_config("config.json")
    env = Environment.Env(3)
    total_reward = 0
    s = env.start()
    s,r,d = env.step(s, 1)
    total_reward += r
    s,r,d = env.step(s, 0)
    total_reward += r
    s,r,d = env.step(s, 10)
    total_reward += r


    print("total_reward = ", total_reward)

