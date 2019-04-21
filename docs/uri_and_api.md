# URI
- /  
redirect to main page(/files/main.html)

- /files/*   
static files

- /calculate  
calculate graphs

# JSON format

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