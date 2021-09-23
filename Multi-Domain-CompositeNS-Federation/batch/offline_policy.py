import csv
import Environment
import parser

def load_policy(policy_file_name = "./mdp-policy.csv"):

    policy = {}

    with open(policy_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            elif len(row) > 0:
                l1 = int(row[0])
                l2 = int(row[1])
                l3 = int(row[2])
                f1 = int(row[3])
                f2 = int(row[4])
                f3 = int(row[5])
                d1 = int(row[6])
                d2 = int(row[7])
                d3 = int(row[8])
                action = row[9]
                
                deployed_simples = [None, None]
                deployed_simples[0] = [l1, l2, l3]
                deployed_simples[1] = [f1, f2, f3]
                
                capacities = [None, None]
                capacities[0] = [0, 0, 0]
                capacities[1] = [0, 0, 0]

                alive_composites = [0, 0, 0]
                alive_traffic_classes = [l1 + f1, l2 + f2, l3 + f3]
                events = [d1, d2, d3]

                state = Environment.State(deployed_simples, capacities, alive_composites, alive_traffic_classes, events)

                deployment = ()
                if action == "accept":
                    if d1 == 1:
                        deployment = ((0,), ())
                    elif d2 == 1:
                        deployment = ((1,), ())
                    elif d3 == 1:
                        deployment = ((2,), ())
                elif action == "federate":
                    if d1 == 1:
                        deployment = ((), (0,))
                    elif d2 == 1:
                        deployment = ((), (1,))
                    elif d3 == 1:
                        deployment = ((), (2,))
                elif action == "reject":
                    deployment = ()
                elif action == "no_action":
                    deployment = None
                
                policy[state] = deployment
                #print("state = ", state, ", action = ", action,", deployment = ", deployment)

            line_count += 1

    return policy

def print_policy(policy):
    for p in policy:
        print(p,"-->",policy[p])

global_policy = None
def lookup(s):
    return global_policy[s]

def load_mdp_policy():
    global global_policy
    global_policy = load_policy(policy_file_name = "./mdp-policy.csv")
    return lookup

if __name__ == "__main__":

    parser.parse_config("config.json")
    policy = load_policy(policy_file_name = "./mdp-policy.csv")
    print_policy(policy)


