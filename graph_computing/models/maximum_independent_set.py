import dwave_networkx as dnx


def maximum_independent_set(graph, sampler):
    res = dnx.maximum_independent_set(graph, sampler)
    return res, 'node'
