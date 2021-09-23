
import numpy as np

def get_service_aggregated_requirements(request):
    vnfs = request.vn_fs #the name is converted to vn_fs by swagger codegen !!!
    cpu = 0
    ram = 0

    for vnf in vnfs:
        cpu += vnf.requirements.cpu
        ram += vnf.requirements.ram

    return {"cpu": cpu, "ram": ram}


def get_valid_domains(request, available_resources):
    service_requirements = get_service_aggregated_requirements(request)

    valid_domains = []
    valid_domains.append({"domainid": "null"}) #rejection is always a valid action

    for domain_resources in available_resources:
        enough_resource = True
        for resource_name in service_requirements.keys():
            if service_requirements[resource_name] > domain_resources[resource_name]:
                enough_resource = False
                break

        if enough_resource:
            valid_domains.append({"domainid": domain_resources["domainid"]})

    return valid_domains

def random_valid_action(nsd, available_resources):
    valid_domains = get_valid_domains(nsd, available_resources)
    
    return valid_domains[np.random.choice(len(valid_domains))]

