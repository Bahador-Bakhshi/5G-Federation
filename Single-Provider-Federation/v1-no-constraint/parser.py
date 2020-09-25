import json
import Environment
from Environment import NFV_NS, Local_Domain, Traffic_Load, Providers

def print_domain(domain):
    print("\n* * ** *** ***** Local Domain ***** *** ** * *")
    print("Total CPU: ", domain.total_cpu)
    print("Services:")
    for ns in domain.services:
        print("\t ID:", ns.nsid, " CPU:", ns.cpu, " Revenue:", ns.revenue)


def print_loads(loads):
    print("\n* * ** *** ***** Loads ***** *** ** * *")
    for load in loads:
        print("ID:", load.service.nsid, " lam:", load.lam, " mu:", load.mu)


def parse_config(config_file):
    config_file_handler = open(config_file)
    config = json.load(config_file_handler)
    config_file_handler.close()

    # Config local domain
    Environment.domain
    Environment.domain = Local_Domain(config["local"]["total_cpu"])
    for ns in config["local"]["ns_catalog"]:
        service = NFV_NS(ns["id"], ns["cpu"], ns["revenue"])
        Environment.domain.add_service(service)

    print_domain(Environment.domain)

    # Config providers

    # Config traffic loads
    Environment.traffic_loads = []
    for load in config["loads"]:
        Environment.traffic_loads.append(Traffic_Load(load["catalog_id"], load["lambda"], load["mu"]))

    Environment.total_classes = len(Environment.traffic_loads)
    print_loads(Environment.traffic_loads)



if __name__ == "__main__":
    parse_config("config.json")
