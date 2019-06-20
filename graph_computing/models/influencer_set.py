def influencer_set(graph, sampler, params=5.0):
    res = _influencer_set(graph, sampler, l=float(params))
    return list(res), 'node'


def _influencer_set(G, sampler=None, l=5.0, **sampler_args):
    """Returns a set of influencers which is an approximate maximum cut with
    loss term on number of nodes

    Defines an Ising problem with ground states corresponding to
    a maximum cut and uses the sampler to sample from it.

    Parameters
    ----------
    G : NetworkX graph
        The graph on which to find a maximum cut.

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
    >>> cut = influencer_set(G, samplerSA)

    Notes
    -----
    Samplers by their nature may not return the optimal solution. This
    function does not attempt to confirm the quality of the returned
    sample.
    """
    # In order to form the Ising problem, we want to increase the
    # energy by 1 for each edge between two nodes of the same color.
    # The linear biases can all be 0.
    h = {v: l for v in G}
    J = {(u, v): 1 for u, v in G.edges}

    # draw the lowest energy sample from the sampler
    response = sampler.sample_ising(h, J, **sampler_args)
    sample = next(iter(response))

    return set(v for v in G if sample[v] >= 0)
