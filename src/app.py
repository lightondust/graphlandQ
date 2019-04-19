from flask import Flask, request, jsonify, redirect
from utils.model_utils import get_model
from config import static_folder, port
import argparse

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
    res = model(request_dict['graph'], sampler_name=request_dict['sampler'])
    resp = {
        'result': res
    }

    return jsonify(resp)


if args.debug:
    @app.route('/debug', methods=['POST', 'GET'])
    def display():

        if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
            return str(request.json)

        return str(request)


app.run(port=port)
