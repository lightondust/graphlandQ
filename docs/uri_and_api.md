# URI

### main page and static files

- uri: `/`  
redirect to main page html (`/files/main.html`)

- uri: `/files/*`   
static files

### calculate

calculation on graphs

- uri: `/calculate`  

- request json  
```
{
    'algorithm': algorithm to use,
    'sampler': sampler to use,
    'graph': graph json
}
```

- response json  
```
{
    'type' : result type,
    'result': result nodes
}
```

`type` values: 'node', 'edge', 'alert'

### model infos

get model list

- uri: `/model`  

- request: GET

- response

```
['model i', 'model ro', 'model ha', ...]
```

