import dwave_networkx as dnx


def min_vertex_cover(graph, sampler):
    res = dnx.min_vertex_cover(graph, sampler)
    return res, 'node'