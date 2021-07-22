
class Simple_NFV_NS:
    sns_id = 0
    resources = None

    def __init__(self, sns_id):
        self.sns_id = sns_id
        self.resources = []
    
    def add_resource(self, r):
        self.resources.append(r)

class Composite_NFV_NS:
    cns_id = 0
    revenue = 0
    nested_ns = None

    def __init__(self, cns_id, revenue):
        self.cns_id = cns_id
        self.revenue = revenue
        self.nested_ns = []
    
    def add_nested_ns(self, nested_ns):
        self.nested_ns.append(nested_ns)


class Traffic_Load:
    cns_id = None
    lam  = 0
    mu   = 0

    def __init__(self, cns_id, lam, mu):
        self.cns_id = cns_id
        self.lam  = lam
        self.mu   = mu


