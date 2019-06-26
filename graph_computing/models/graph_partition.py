from config import GRAPH_PARTITION_SCALE


def graph_partition(graph, sampler, params=5.0):
    res = _graph_partition(graph, sampler, l=float(params)/GRAPH_PARTITION_SCALE)
    return list(res), 'node'


def _graph_partition(G, sampler=None, l=5.0, **sampler_args):
    """
    Ising model corresponds to
    l (/sum_{nodes} q_i)^2 - /sum_{edges} q_i q_j

    Parameters
    ----------
    G : NetworkX graph

    sampler
        A binary quadratic model sampler. A sampler is a process that
        samples from low energy states in models defined by an Ising
        equation or a Quadratic Unconstrained Binary Optimization
        Problem (QUBO). A sampler is expected to have a 'sample_qubo'
        and 'sample_ising' method. A sampler is expected to return an
        iterable of samples, in order of increasing energy. If no
        sampler is provided, one must be provided using the
        `set_default_sampler` function.

    sampler_args
        Additional keyword parameters are passed to the sampler.

    Returns
    -------
    S : set
        A set of inluencers G.javascript:void(0)

    Example
    -------
    This example uses a sampler from
    `dimod <https://github.com/dwavesystems/dimod>`_
    for a graph of a Chimera unit cell created using the `chimera_graph()`
    function.

    >>> import dimod
    >>> samplerSA = dimod.SimulatedAnnealingSampler()
    >>> G = dnx.chimera_graph(1, 1, 4)
    >>> cut = graph_partition(G, samplerSA)

    Notes
    -----
    Samplers by their nature may not return the optimal solution. This
    function does not attempt to confirm the quality of the returned
    sample.
    """
    nodes = [v for v in G]
    h = {v: 2*l for v in nodes}
    J = {}
    for idx, v in enumerate(nodes):
        for u in nodes[:idx]:
            J[(v, u)] = l

    for u, v in G.edges:
        J[(u, v)] = -1+l

    # draw the lowest energy sample from the sampler
    response = sampler.sample_ising(h, J, **sampler_args)
    sample = next(iter(response))

    return set(v for v in G if sample[v] >= 0)