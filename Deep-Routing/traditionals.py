
import network
import graph
import environment

class MinHopCount:
    class Observation:
        def __init__(self, topology, request):
            self.topology = topology
            self.request  = request

    def observer(topology, request):
        return MinHopCount.Observation(topology, request), 0

    def policy(observation):
        topology = observation.topology
        request  = observation.request

        is_path, path = graph.shortest_path(topology, request, graph.bw_feasibility, graph.link_weight_one)

        if is_path:
            request.path = path
            return environment.Actions.accept
        else:
            return environment.Actions.reject
