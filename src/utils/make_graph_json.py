import json

import networkx as nx
import os
from networkx.readwrite import json_graph

static_folder = '../view'

G = nx.barbell_graph(6, 3)

for n in G:
    G.nodes[n]['name'] = n

d = json_graph.node_link_data(G)  # node-link format to serialize

json.dump(d, open(os.path.join(static_folder, 'graph_example.json'), 'w'))
