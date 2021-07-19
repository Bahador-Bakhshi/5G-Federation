import csv
import Environment

def load_policy(policy_file_name, services_num):
    policy = {}

    with open(policy_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            elif len(row) > 0:
                if len(row) != (3 * services_num + 1):
                    logging.error("len(row) != 3 * services_num")
                    sys.exit(-1)    

                local_actives = tuple([int(x) for x in row[0 : 1 * services_num]])
                provider_activs = tuple([int(x) for x in row[1 * services_num : 2 * services_num]])
                arrivals = tuple([int(x) for x in row[services_num * 2 : 3 * services_num]])
                key = tuple([local_actives, provider_activs, arrivals])

                action = None
                action_name = row[6]
                if action_name == "reject":
                    action = Environment.Actions.reject
                elif action_name == "accept":
                    action = Environment.Actions.accept
                elif action_name == "federate":
                    action = Environment.Actions.federate
                else:
                    print("Policy Load: Uknown action")
                    sys.exit(-1)

                state = Environment.State(Environment.total_classes)
                state.domains_alives = [local_actives, provider_activs]
                state.arrivals_departures = arrivals

                policy[state] = action

            line_count += 1
  
    return policy
