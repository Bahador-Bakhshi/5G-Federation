import json
import Environment
from debuger import verbose, debug, warning, error
from Domain import Domain
from NS import Simple_NFV_NS, Composite_NFV_NS, Traffic_Load

def print_ns(simples, composites):
    debug("\n* * ** *** ***** NS Catalog ***** *** ** * *")
    
    print("Simple NS ...:")
    for ns in simples:
        print("id = ", ns.sns_id)
        print("\t resources: ", ns.resources)

    print("Composite NS ...:")
    for ns in composites:
        print("id = ", ns.cns_id)
        print("\t revenue = ", ns.revenue)
        print("\t nested_ns  = ", ns.nested_ns)

def print_loads(loads):
    debug("\n* * ** *** ***** Loads ***** *** ** * *")
    for index in range(len(loads)):
        debug("index:", index)
        load = loads[index]
        debug("\t Service ID:", load.cns_id, ", lam:", load.lam, " mu:", load.mu)

def print_domains(domains):
    debug("\n* * ** *** ***** Domains ***** *** ** * *")
    for d in domains:
        if d == None:
            continue

        debug("Name:", d.domain_name)
        debug("ID:", d.domain_id)
        debug("Quotas:", d.quotas)
        debug("reject_thresholds: ", d.reject_thresholds)
        debug("Costs: ", d.costs)
        debug("Overcharges: ", d.overcharges)
        debug("-------------")
    

def parse_config(config_file):
    config_file_handler = open(config_file)
    config = json.load(config_file_handler)
    config_file_handler.close()

    # Config NS
    simple_ns = config["ns_catalog"]["simple_ns"]
    for ns in simple_ns:
        service = Simple_NFV_NS(ns["sns_id"])
        for w in ns["resources"]:
            service.add_resource(w)

        Environment.all_simple_ns.append(service)

    composite_ns = config["ns_catalog"]["composite_ns"]
    for ns in composite_ns:
        service = Composite_NFV_NS(ns["cns_id"], ns["revenue"])
        for nns in ns["nested_ns"]:
            service.add_nested_ns(nns)

        Environment.all_composite_ns.append(service)

    if verbose:
        print_ns(Environment.all_simple_ns, Environment.all_composite_ns)
    
    # Config providers
    for d in config["domains"]:
        domain = Domain(d["name"], d["domain_id"], Environment.all_simple_ns)
        
        for q in d["quotas"]:
            domain.add_quota_threshold(q["capcity"], q["reject_threshold"])

        for c in d["costs"]:
            domain.costs[c["sns_id"]] = c["cost"]
            domain.overcharges[c["sns_id"]] = c["overcharge"]
        
        Environment.all_domains.append(domain)

    print_domains(Environment.all_domains)

    # Config traffic loads
    for load in config["loads"]:
        Environment.all_traffic_loads.append(Traffic_Load(load["cns_id"], load["lambda"], load["mu"]))

    if verbose:
        print_loads(Environment.all_traffic_loads)


if __name__ == "__main__":
    parse_config("config.json")
