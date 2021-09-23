import csv
import logging
import sys

from swagger_server.models.domain_actives import DomainActives
import swagger_server.core.init_ac as init_ac
import swagger_server.core.random_policy as random_policy

POLICY_FILE_NAME = "/usr/app/config/policy.csv"

policy = {}

def load_policy(policy_file_name=POLICY_FILE_NAME):
    global policy

    services_num = init_ac.ac_config.services_num
    logging.debug("Number of services = %d", services_num)
    
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
                policy[key] = row[6]

            line_count += 1
   
    logging.debug("policy = %s", policy)


def get_active_nums(activelist, output):
    for actives in activelist:
        output[init_ac.ac_config.service_id_mapping[actives.service_id]] = int(actives.num)


def get_request_key(request):
    services_num = init_ac.ac_config.services_num

    local = [0] * services_num
    provider = [0] * services_num
    arrivals = [0] * services_num

    for actives_info_dic in request.actives:
        actives_info = DomainActives.from_dict(actives_info_dic)
        logging.debug("actives_info = %s", actives_info)
        if actives_info.domainid.lower() == 'local':
            get_active_nums(actives_info.activelist, local)
        elif actives_info.domainid.lower() == 'provider1':
            get_active_nums(actives_info.activelist, provider)
        else:
            logging.error("Unknown domain")
            sys.exit(-1)

    arrivals[init_ac.ac_config.service_id_mapping[request.nsd.id]] = 1

    logging.debug("key = %s", tuple([local, provider, arrivals]))
    return tuple([tuple(local), tuple(provider), tuple(arrivals)])


def lookup(request):
    key = get_request_key(request)
    
    action = None
    logging.debug("key = %s, type = %s", key, type(key))
    if key in policy.keys():
        action = policy[key]
    
    if action == None:
        if init_ac.ac_config.error_on_unknown_state == True:
            logging.error("Unknown action")
            logging.error(request)
            sys.exit(-1)
        else:
            domain_action_map = {"null": "reject", "local": "accept", "provider1": "federate"}
            logging.warning("Unknown action")
            logging.warning(request)
            rand_valid_domain = ((random_policy.random_valid_action(request.nsd, request.available))["domainid"]).lower()
            action = domain_action_map[rand_valid_domain]

    revenue = 0
    federation_cost = 0

    if action != "reject":
        revenue = init_ac.ac_config.service_costs[request.nsd.id].revenue

    if action == "federate":
        federation_cost = init_ac.ac_config.service_costs[request.nsd.id].federation_cost

    logging.debug("request = %s", request)
    logging.critical("AC: request type = %s, request id = %s, decision = %s, revenue = %d, federation_cost = %s, profit = %s", request.nsd.id, request.nsd.name, action, revenue, federation_cost, revenue - federation_cost)

    return action

