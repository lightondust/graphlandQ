from dimod.reference.samplers import ExactSolver
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import json


def get_samplers(sampler_name):
    import os
    print(os.getcwd())

    with open('./regist_info.json', 'r') as f:
        regist_info = json.load(f)

    if sampler_name == 'dwave':
        sampler = EmbeddingComposite(DWaveSampler(**regist_info))
    elif sampler_name == 'exact':
        sampler = ExactSolver()

    return sampler
