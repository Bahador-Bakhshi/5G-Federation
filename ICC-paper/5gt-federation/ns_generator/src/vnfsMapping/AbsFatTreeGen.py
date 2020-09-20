import networkx as nx
import random
import math

class AbsFatTreeGen(object):

    """Generates fat-tree graphs attending to different abstractions.
    The idea is to provide different level of details according to CTTC's Inaki
    Pascual idea"""

    def __init__(self):
        """"""

    def __genSerId(self, serverNum, switchNum, podNum):
        """Generates an ID for a fat-tree server

        :serverNum: number of the server inside the switch
        :switchNum: number of the switch inside the pod
        :podNum: pod number
        :returns: string with the server ID

        """
        return 'server_' + str(serverNum) + '_switch_' + str(switchNum) +\
            '_pod_' + str(podNum)


    def __createAbsLinksNET(self, k, hostsGraph, linkProps):
        """Creates the abstraction links of the NET view inside
        the hosts graph.

        :k: fat-tree degree
        :hostsGraph: networkX graphs with unconnected fat-tree hosts
        :linkProps: fat-tree link properties (it must contain 'delay' and 'capacity')
        :returns: the passed networkX graph

        """
        linkProps_ = dict(linkProps)
        links_bw = linkProps['capacity'] / (math.pow(k, 3) / 4)
        linkProps_['capacity'] = links_bw

        for pod in range(k):
            for switch in range(int(k / 2)):
                for server in range(int(k / 2)):
                    server_id = self.__genSerId(server, switch, pod)

                    # Link with servers inside the switch
                    same_sw_props = dict(linkProps_)
                    same_sw_props['delay'] = linkProps_['delay'] * 2
                    for server2 in range(int(k / 2)):
                        server2_id = self.__genSerId(server2, switch, pod)
                        if server2_id == server_id:
                            continue
                        hostsGraph.add_edge(server_id, server2_id,
                            **same_sw_props)

                    # Link with servers in same pod and different switch
                    same_pod_props = dict(linkProps_)
                    same_pod_props['delay'] = linkProps_['delay'] * 4
                    for switch2 in range(int(k / 2)):
                        if switch2 == switch:
                            continue
                        for server2 in range(int(k / 2)):
                            server2_id = self.__genSerId(
                                server2, switch2, pod)
                            hostsGraph.add_edge(server_id, server2_id,
                                **same_pod_props)

                    # Link with servers in other pod and other switch
                    different_pod_props = dict(linkProps_)
                    different_pod_props['delay'] = linkProps_['delay'] * 6
                    for pod2 in range(k):
                        if pod2 == pod:
                            continue
                        for switch2 in range(int(k / 2)):
                            for server2 in range(int(k / 2)):
                                server2_id = self.__genSerId(
                                    server2, switch2, pod2)
                                hostsGraph.add_edge(server_id,
                                    server2_id, **different_pod_props)

        return hostsGraph


    def yieldFatTree(self, k, linkProps, serverProps, abstraction='NET'):
        """Generates a fat-tree netwotkx graph attending to the specified
        abstraction level.

        :k: fat-tree degree. Note it has to be a power of 2
        :linkProps: links properties (it must contain 'delay' and 'capacity')
        :serverProps: server properties
        :abstraction: level of abstraction for the generated graph:
            ['NET', 'ZERO', 'VIM', 'FULL']
        :returns: networkX representation of the fat-tree

        """
        if abstraction != 'NET':
            raise Exception('Currently only NET abstraction is supported')

        fat_tree = nx.Graph()

        # Create the nodes
        for pod in range(k):
            for switch in range(int(k / 2)):
                for server in range(int(k / 2)):
                    properties = dict(serverProps)
                    properties['pod'] = pod
                    properties['server'] = server
                    properties['switch'] = switch
                    fat_tree.add_node(
                        self.__genSerId(server, switch, pod),
                        **properties)

        if abstraction == 'NET':
            return self.__createAbsLinksNET(k, fat_tree, linkProps)
        else:
            return None


    @staticmethod
    def PimrcGenCosts(scenario, support_th, cost_th):
        """Creates the costs of assignment in the PIMRC18 model.
        Both hosts and services must be generated in the scenario.

        :pimrc: PIMRC18 JSON to add the information with services inside
        :support_th: {'min': ,'max' } percentage of #vnfs to support
        :cost_th: {'min': , 'max': } placement costs
        :returns: the JSON scenario with costs added

        """
        num_vnfs = len(scenario['vnfs'])
        vnf_names = [v['vnf_name'] for v in scenario['vnfs']]
        if 'costs' not in scenario:
            scenario['costs'] = []

        for host in scenario['hosts']:
            random.shuffle(vnf_names)
            support = int(math.floor(random.uniform(support_th['min'],
                support_th['max']) * num_vnfs))
            for i in range(support):
                scenario['costs'].append({
                    'vnf': vnf_names[i],
                    'host': host['host_name'],
                    'cost': random.uniform(cost_th['min'], cost_th['max'])
                })

        return scenario



    @staticmethod
    def NETtoPimrc(fatTree, linkProps, serverProps, pimrc=None):
        """Translates the generated fatTree with NET abstraction
        to a PIMRC18 JSON

        :fatTree: networkX fat-tree instance
        :linkProps: links properties (just the keys)
        :serverProps: server properties (just the keys)
        :pimrc: PIMRC18 JSON to add the information
        :returns: PIMRC18 JSON

        """
        if not pimrc:
            pimrc = {
                'hosts': [],
                'host_edges': []
            }

        # Insert the hosts
        hostsProps = {}
        for hostProp in serverProps:
            for host in fatTree.nodes():
                if host not in hostsProps:
                    hostsProps[host] = {}
                    hostsProps[host]['host_name'] = host
                hostsProps[host][hostProp] =\
                    nx.get_node_attributes(fatTree, hostProp)[host]
        for host in hostsProps:
            pimrc['hosts'].append(hostsProps[host])

        # Insert the host edges
        for edge in fatTree.edges(data=True):
            host_edge = dict(edge[2])
            host_edge['source'] = edge[0]
            host_edge['target'] = edge[1]
            pimrc['host_edges'].append(host_edge)

        return pimrc
