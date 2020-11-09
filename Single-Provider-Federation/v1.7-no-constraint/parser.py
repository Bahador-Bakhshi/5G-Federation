import json
import Environment
from Environment import debug, warning, error, verbose
from Environment import NFV_NS, Local_Domain, Traffic_Load, Providers

def print_domain(domain):

    if verbose:
        debug("\n* * ** *** ***** Local Domain ***** *** ** * *")
        debug("Total CPU: ", domain.total_cpu)
        debug("Services:")
    
    for ns in domain.services:
        if verbose:
            debug("\t ID:", ns.nsid, " CPU:", ns.cpu, " Revenue:", ns.revenue)
        else:
            pass


def print_loads(loads):
    if verbose:
        debug("\n* * ** *** ***** Loads ***** *** ** * *")
    
    for index in range(len(loads)):
        if verbose:
            debug("index = ", index)
        
        load = loads[index]
        
        if verbose:
            debug("Service ID:", load.service.nsid, ", cpu:", load.service.cpu, ", revenue:", load.service.revenue, ", lam:", load.lam, " mu:", load.mu)


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
    for p in config["providers"]:
        provider = Providers(p["provider_id"])
        for costs in p["federation_costs"]:
            provider.add_fed_cost(costs["nsid"], costs["cost"])
        Environment.providers.append(provider)

    # Config traffic loads
    Environment.traffic_loads = []
    for load in config["loads"]:
        Environment.traffic_loads.append(Traffic_Load(load["catalog_id"], load["lambda"], load["mu"]))

    Environment.total_classes = len(Environment.traffic_loads)
    if verbose:
        print_loads(Environment.traffic_loads)



if __name__ == "__main__":
    parse_config("config.json")
