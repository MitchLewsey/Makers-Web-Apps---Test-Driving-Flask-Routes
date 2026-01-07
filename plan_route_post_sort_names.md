
# Post Sort Names Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Sort names route
POST /sort-names
    names: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /sort_names
# Parameters:
#   names_list=Sarah,Kathleen,Mitch,Tariq,Will
"""
Kathleen,Mitch,Sarah,Tariq,Will
"""
```

## 3. Test-drive the Route

```python
"""
POST /sort_names
    Parameters:
        names_list: Sarah,Kathleen,Mitch,Tariq,Will
    Expected response (200 OK):
        "Kathleen,Mitch,Sarah,Tariq,Will"
"""
def sort_names(web_client):
    response = web_client.get('/sort-names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Kathleen,Mitch,Sarah,Tariq,Will'
```

