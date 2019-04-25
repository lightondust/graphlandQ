# install and setup

### install

clone this repository and run.

`pip install -r requirments.txt`

- We use python3.6.7
- Use Flask and dwave-ocean-sdk

### use dwave(optional)
Regist an account at [D-Wave Leap](https://cloud.dwavesys.com/leap/) and set your `token`, `endpoint`, `solver` in `graph_computing/regist_info.json` 

Please keep your token secret. 
To prevent an accident, you can make a new file `regist_info_.json` and change the value of `regist_info_path` to `regist_info_.json` in `config.py`. 
The new file will be ignored by git due to `.gitignore`.

# start apps

```cd graph_computing```

```python app.py```

access to [localhost:8009](http://localhost:8009)

# develop

### how to add new algorithm
1. implement a new class in `graph_computing/models/**.py` 
1. add the function to `model_map` in `graph_computing/utils/model_utils.py`

### how to add new graph
1. create a `{graph name}.json`(see `utils.make_graph_json.py`) to `graph_view/graphs/`
2. add the `{graph name}` in `graph_view/graphs/list.json`

## TODO
1. display links as results
1. add a maximum value to the exact solver, so a request would not crush the server