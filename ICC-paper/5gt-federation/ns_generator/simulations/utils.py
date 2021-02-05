import json
import random

def createRandMultiDomain(domains, fatDegrees, meshBw, meshDelay, fatBw,
        fatDelay, sMem, sCpu, sDisk, foreigns, pods, meshProps, outF):
    """Generates randomly a JSON file ready to read for the
    MultiDomainConfReader

    :domains: number of domains
    :fatDegrees: list of allowed fat-tree degrees
    :meshBw: {'min':_, 'max':_} mesh bw resources
    :meshDelay: {'min':_, 'max':_} mesh delay resources
    :fatBw: {'min':_, 'max':_} fat-tree bw resources
    :fatDelay: {'min':_, 'max':_} fat-tree delay resources
    :sMem: {'min':_, 'max':_} fat-tree servers memory resources
    :sCpu: {'min':_, 'max':_} fat-tree servers cpu resources
    :sDisk: {'min':_, 'max':_} fat-tree servers disk resources
    :foreigns: number of foreign domains available for a domain
    :pods: {'min':_, 'max':_} number of pods available in foreign domains
    :meshProps: list with mesh resources sharing proportions
    :outF: absolute path where the JSON will be written
    :returns: Nothing

    """
    mdDict = {
        "name": "tabuPerfection",
        "description": "multiDomain to test the optimal tabu parameters",
        "domains": domains,
        "meshDegree": 1,
        "meshProps": meshProps,
        "meshLnkRes": { "bw": meshBw, "delay": meshDelay },
        "fatLnkRes": { "bw": fatBw, "delay": fatDelay },
        "servRes": {
            "memory": sMem,
            "cpu": sCpu,
            "disk": sDisk
        }
    }

    # Set fat-tree degrees
    fatDegs = [fatDegrees[random.randint(0, len(fatDegrees) - 1)] for _ in
            range(domains)]
    mdDict["fatTreeDegrees"] = fatDegs

    # Generate foreign used domains
    foreignFriends = dict()
    for domain in range(domains):
        friends = range(domains)
        del friends[domain]
        while len(friends) > foreigns:
            idx = random.randint(0, len(friends) - 1)
            del friends[idx]

        foreignFriends[domain] = friends


    # Initialize proportions arrays
    foreignPods = []
    fatLnkProps = [[0 if other != domain else 1 for other in range(domains)]
            for domain in range(domains)]
    fatSrvProps = [list(domProps) for domProps in fatLnkProps]

    for domain in range(domains):
        sharedPods = {}

        for friend in foreignFriends[domain]:
            fatLnkProps[friend][domain] = 1
            fatSrvProps[friend][domain] = 1
            targetPods = range(1, fatDegs[domain] + 1)
            numPods = random.randint(pods['min'], pods['max'])
            while len(targetPods) > numPods:
                idx = random.randint(0, len(targetPods) - 1)
                del targetPods[idx]
            sharedPods[str(friend)] = targetPods

        foreignPods.append(sharedPods)
    mdDict["fatLnkProps"] = fatLnkProps
    mdDict["fatSrvProps"] = fatSrvProps
    mdDict["foreignPods"] = foreignPods

    with open(outF, 'w') as f:
        json.dump(mdDict, f)

