# install and set

If you want to use dwave solver, regist an account at [D-Wave Leap](https://cloud.dwavesys.com/leap/) and set your `token`, `endpoint`, `solver` in `graph_computing/regist_info.json` (beware to keep these information secret)


# start apps

```cd graph_computing```

```python app.py```

access to `localhost:8009`

# develop

## how to add a new algorithm
1. implement a new class in `graph_computing/models/**.py` 
1. add the function in `graph_computing/utils/model_utils.py`
1. add an option tab in `graph_view/main.html`

## TODO

use Vue.js

### add graphs

structure graph json list

- list.json
- ***.json

### add algorithms

get drop down list from server