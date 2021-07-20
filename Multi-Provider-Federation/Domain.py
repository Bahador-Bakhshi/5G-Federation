import numpy as np

class Domain:
    def __init__(self, name, domain_id, all_simple_ns):
        self.domain_name = name
        self.domain_id = domain_id
        self.quotas = []
        self.reject_thresholds = []
        self.costs = {}
        self.overcharges = {}
        for ns in all_simple_ns:
            self.costs[ns.sns_id] = np.inf

    def add_quota_threshold(self, q, t):
        self.quotas.append(q)
        self.reject_thresholds.append(t)
