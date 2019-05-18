from dimod.reference.samplers import ExactSolver
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import json
from config import MAX_NODES_NUMBER, DWAVE_ALLOWED
from config import TOO_MANY_NODES, DWAVE_NOT_ALLOWED


def check_graph(graph):
    """
    check if the graph is suitable to calculate
    :param graph:
    :return:
    """
    if graph.number_of_nodes() > MAX_NODES_NUMBER:
        return False

    return True


def get_sampler(sampler_name, graph):
    from config import REGIST_INFO_PATH

    with open(REGIST_INFO_PATH, 'r') as f:
        regist_info = json.load(f)

    if sampler_name == 'exact':
        if check_graph(graph):
            sampler = ExactSolver()
        else:
            return TOO_MANY_NODES

    elif sampler_name == 'dwave':
        if DWAVE_ALLOWED:
            sampler = EmbeddingComposite(DWaveSampler(**regist_info))
        else:
            return DWAVE_NOT_ALLOWED

    return sampler
