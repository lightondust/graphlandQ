# What's

This is a simple app to see the effect of quantum computer.

- select a graph, a solver, a algorithm:
![Screenshot from 2019-05-13 00-37-11](https://user-images.githubusercontent.com/30369038/57584528-835b3100-7517-11e9-9ab7-4c3b00281bf6.png)

- Click Run(this example finds nodes corresponds to a set of influencer):
![Screenshot from 2019-05-13 00-37-55](https://user-images.githubusercontent.com/30369038/57584530-85bd8b00-7517-11e9-8071-2c1a01c182ce.png)

# install and setup

### install

[make an env](https://docs.python.org/3.6/tutorial/venv.html) for this project, clone this repository and run.

`pip install -r requirements.txt`

- We use python3.6.7, ubuntu 18.04.2 LTS (Bionic Beaver)
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

### how to add new algorithm
1. implement a new class in `graph_computing/models/**.py` 
1. add the function to `model_map` in `graph_computing/utils/model_utils.py`

### how to add new graph
1. create a `{graph name}.json`(see `utils.make_graph_json.py`) to `graph_view/graphs/`
2. add the `{graph name}` in `graph_view/graphs/list.json`

# Develops
Welcome. 
See the issues for what we need help.
For other changes, please add an issue.
