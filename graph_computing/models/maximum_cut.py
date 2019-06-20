import dwave_networkx as dnx


def maximum_cut(graph, sampler, params=None):
    res = dnx.maximum_cut(graph, sampler)
    return list(res), 'node'
