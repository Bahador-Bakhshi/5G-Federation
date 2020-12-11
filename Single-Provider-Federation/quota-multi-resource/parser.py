import json
import Environment
from Environment import verbose, debug, warning, error
from Environment import NFV_NS, Local_Domain, Traffic_Load, Providers

def print_domain(domain):
    debug("\n* * ** *** ***** Local Domain ***** *** ** * *")
    debug("Capacities: ", domain.capacities)
    debug("Services:")
    for ns in domain.services:
        debug("\t ID:", ns.nsid)
        for w in ns.resources:
            debug("\t\t Resources:", w)
        debug("\t Revenue:", ns.revenue)


def print_loads(loads):
    debug("\n* * ** *** ***** Loads ***** *** ** * *")
    for index in range(len(loads)):
        debug("index:", index)
        load = loads[index]
        debug("\t Service ID:", load.service.nsid, ", lam:", load.lam, " mu:", load.mu)


def print_providers(providers):
    debug("\n* * ** *** ***** Providers ***** *** ** * *")
    for p in providers:
        if p == None:
            continue

        debug("ID:", p.pid)
        debug("Quotas:", p.quotas)
        debug("Overcharge: ", p.overcharge)
        debug("Costs: ")
        for c in p.federation_costs.keys():
            debug("\t service = ", c.nsid, ", cost = ", p.federation_costs[c]), 


def parse_config(config_file):
    config_file_handler = open(config_file)
    config = json.load(config_file_handler)
    config_file_handler.close()

    # Config local domain
    Environment.domain = Local_Domain()
    for c in config["local"]["capacities"]:
        Environment.domain.add_capacity(c)

    for ns in config["local"]["ns_catalog"]:
        service = NFV_NS(ns["id"], ns["revenue"])
        for w in ns["resources"]:
            service.add_resource(w)

        Environment.domain.add_service(service)

    if verbose:
        print_domain(Environment.domain)

    # Config providers
    Environment.providers = []
    Environment.providers.append(None) #this is the placeholder for the local/consumer domain
    for p in config["providers"]:
        provider = Providers(p["provider_id"])
        provider.overcharge = p["overcharge"]
        
        for q in p["quotas"]:
            provider.add_quota(q)

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
    print_loads(Environment.traffic_loads)



if __name__ == "__main__":
    parse_config("config.json")
