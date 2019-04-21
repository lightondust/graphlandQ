from flask import Flask, request, jsonify, redirect
from utils.model_utils import get_model, model_map
from utils.sampler_utils import get_sampler
from config import static_folder, port
import argparse
import networkx as nx

parser = argparse.ArgumentParser(description='Graphland with quantum computer')
parser.add_argument('-d', '--debug', type=str, default='',
                    help='enable debug url')

args = parser.parse_args()
print(args)

app = Flask(__name__, static_folder=static_folder)

@app.route('/')
def index():
    return redirect('/file/main.html')


# return static files
@app.route('/file/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


# run algorithms
@app.route('/calculate', methods=['POST'])
def calculate():
    request_dict = request.json
    model = get_model(request_dict['algorithm'])
    sampler = get_sampler(request_dict['sampler'])
    graph = nx.node_link_graph(request_dict['graph'])
    res, type = model(graph, sampler=sampler)

    resp = {
        'type': type,
        'result': res
    }

    return jsonify(resp)


# return model list
@app.route('/models', methods=['GET'])
def models():
    model_list = list(model_map.keys())
    return jsonify(model_list)


if args.debug:
    @app.route('/debug', methods=['POST', 'GET'])
    def display():

        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            return str(request.json)

        return str(request)


app.run(port=port)
