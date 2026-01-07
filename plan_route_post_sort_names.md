
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
#   names=Sarah,Kathleen,Mitch,Tariq,Will
"""
Kathleen,Mitch,Sarah,Tariq,Will
"""
```

## 3. Test-drive the Route

```python
"""
POST /sort_names
    Parameters:
        names: Sarah,Kathleen,Mitch,Tariq,Will
    Expected response (200 OK):
        "Kathleen,Mitch,Sarah,Tariq,Will"
"""
def test_post_sort_names_with_list_of_names(web_client):
    response = web_client.post("/sort-names", data={"names": "Kathleen,Mitch,Sarah,Tariq,Will"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Kathleen,Mitch,Sarah,Tariq,Will"

"""
POST /sort_names
    Parameters:
        names: aaab,aaaz,aaac
    Expected response (200 OK):
        "aaab,aaac,aaac"
"""

def test_post_sort_names_only_differing_last_letter(web_client):
    response = web_client.post("/sort-names")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "aaab,aaaz,aaac"

"""
POST /sort_names
    Parameters:
        names: ""
    Expected response (400 BAD REQUEST):
        "No names submitted"
"""

def test_post_sort_names_no_names_provided(web_client):
    response = web_client.post("/sort-names")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "No names submitted"
```

