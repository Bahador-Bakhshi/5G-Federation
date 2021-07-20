import numpy as np

class Domain:
    domain_name = ""
    domain_id = 0
    quotas = None
    overcharge = 0
    reject_threshold = 0
    costs = None

    def __init__(self, name, domain_id, all_simple_ns):
        self.domain_name = name
        self.domain_id = domain_id
        self.quotas = []
        self.costs = {}
        for ns in all_simple_ns:
            self.costs[ns.sns_id] = np.inf

    def add_quota(self, q):
        self.quotas.append(q)


