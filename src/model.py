from dwave.system.samplers import DWaveSampler
from dimod.reference.samplers import ExactSolver
import dwave_networkx as dnx
import networkx as nx

samplers = {
    'dwave': DWaveSampler,
    'exact': ExactSolver
}


def model_min_vertex_cover(graph, sampler_name='exact'):
    res = dnx.min_vertex_cover(nx.node_link_graph(graph), samplers[sampler_name]())
    return res