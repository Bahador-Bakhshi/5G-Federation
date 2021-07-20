import Environment
import parser

if __name__ == "__main__":
    parser.parse_config("config.json")
    env = Environment.Env(10)
    env.start()
