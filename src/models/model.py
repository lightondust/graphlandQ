from utils.sampler_utils import get_samplers
import dwave_networkx as dnx
import networkx as nx


def min_vertex_cover(graph, sampler_name):
    print('called: min vertex cover')
    sampler = get_samplers(sampler_name)
    res = dnx.min_vertex_cover(nx.node_link_graph(graph), sampler)
    return res