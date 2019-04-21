import json

import networkx as nx
import os
from networkx.readwrite import json_graph

output_folder = '../../graph_view/graphs/'

# G = nx.barbell_graph(6, 3)
G = nx.karate_club_graph()

for n in G:
    G.nodes[n]['name'] = n

d = json_graph.node_link_data(G)  # node-link format to serialize

json.dump(d, open(os.path.join(output_folder, 'karateclub.json'), 'w'))
