import json
import Environment
from Environment import verbose, debug, warning, error
from Environment import NFV_NS, Local_Domain, Traffic_Load, Providers

def print_domain(domain):
    debug("\n* * ** *** ***** Local Domain ***** *** ** * *")
    debug("Total CPU: ", domain.total_cpu)
    debug("Services:")
    for ns in domain.services:
        debug("\t ID:", ns.nsid, " CPU:", ns.cpu, " Revenue:", ns.revenue)


def print_loads(loads):
    debug("\n* * ** *** ***** Loads ***** *** ** * *")
    for index in range(len(loads)):
        debug("index = ", index)
        load = loads[index]
        debug("\t Service ID:", load.service.nsid, ", cpu:", load.service.cpu, ", revenue:", load.service.revenue, ", lam:", load.lam, " mu:", load.mu)


def print_providers(providers):
    debug("\n* * ** *** ***** Providers ***** *** ** * *")
    for p in providers:
        if p == None:
            continue

        debug("ID = ", p.pid)
        debug("Quota = ", p.quota)
        debug("Costs = ")
        for c in p.federation_costs.keys():
            debug("\t service = ", c.nsid, ", cost = ", p.federation_costs[c]), 

def parse_config(config_file):
    config_file_handler = open(config_file)
    config = json.load(config_file_handler)
    config_file_handler.close()

    # Config local domain
    Environment.domain = Local_Domain(config["local"]["total_cpu"])
    for ns in config["local"]["ns_catalog"]:
        service = NFV_NS(ns["id"], ns["cpu"], ns["revenue"])
        Environment.domain.add_service(service)

    if verbose:
        print_domain(Environment.domain)

    # Config providers
    Environment.providers = []
    Environment.providers.append(None) #this is the placeholder for the local/consumer domain
    for p in config["providers"]:
        provider = Providers(p["provider_id"])
        provider.quota = p["quota"]
        for costs in p["federation_costs"]:
            provider.add_fed_cost(costs["nsid"], costs["cost"])
        Environment.providers.append(provider)

    Environment.providers_num = len(Environment.providers) - 1
    print_providers(Environment.providers)

    # Config traffic loads
    Environment.traffic_loads = []
    for load in config["loads"]:
        Environment.traffic_loads.append(Traffic_Load(load["catalog_id"], load["lambda"], load["mu"]))

    Environment.total_classes = len(Environment.traffic_loads)
    Environment.State.state_fields_num = 3 * Environment.total_classes
    print_loads(Environment.traffic_loads)



if __name__ == "__main__":
    parse_config("config.json")
