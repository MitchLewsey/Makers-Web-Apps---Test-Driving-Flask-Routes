
# Post Sort Names Route Design Recipe

## 1. Design the Route Signature

```
# Sort names route
POST /sort-names
    names: string

# Add names route
GET /add-name
    names: string
    added_name: string

```

## 2. Create Examples as Tests

```python
# POST /sort-names
# Parameters:
#   names=Sarah,Kathleen,Mitch,Tariq,Will
# Expected response (200 OK):
"""
Kathleen,Mitch,Sarah,Tariq,Will
"""

# POST /sort_names
# Parameters:
#   names=aaab,aaaz,aaac
# Expected response (200 OK):
"""
aaab,aaac,aaaz
"""

#POST /sort_names
# Parameters:
#   names=
# Expected response (400 BAD REQUEST):
"""
No names submitted
"""

# GET /add-name
# Parameters:
#     names=Sarah,Kathleen,Mitch,Tariq,Will
#     added_name=Charlotte
# Expected response (200 OK):
"""
Charlotte,Kathleen,Mitch,Sarah,Tariq,Will
"""

# GET /add-name
# Parameters:
#     names=Sarah,Kathleen,Mitch,Tariq,Will
#     added_name=
# Expected response (400 BAD REQUEST):
"""
No names to add
"""

# GET /add-name
# Parameters:
#     names=Sarah,Kathleen,Mitch,Tariq,Will
#     added_name=Charlotte,Paul
# Expected response (200 OK):
"""
Charlotte,Kathleen,Mitch,Paul,Sarah,Tariq,Will
"""

```

## 3. Test-drive the Route

```python
"""
POST /sort-names
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
POST /sort-names
    Parameters:
        names: aaab,aaaz,aaac
    Expected response (200 OK):
        "aaab,aaac,aaaz"
"""

def test_post_sort_names_only_differing_last_letter(web_client):
    response = web_client.post("/sort-names", data={"names": "aaab,aaaz,aaac"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "aaab,aaac,aaaz"

"""
POST /sort-names
    Parameters:
        names: ""
    Expected response (400 BAD REQUEST):
        "No names submitted"
"""

def test_post_sort_names_no_names_provided(web_client):
    response = web_client.post("/sort-names")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "No names submitted"

"""
POST /add-names
    Parameters: 
        names: Sarah,Kathleen,Mitch,Tariq,Will
        added_name: Charlotte
    Expected response (200 OK):
    "Charlotte, Kathleen, Mitch, Sarah, Tariq, Will"
"""
def test_get_add_name_given_name(web_client):
    response = web_client.get("/add-name?names=Sarah,Kathleen,Mitch,Tariq,Will&added_name=Charlotte")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Charlotte, Kathleen, Mitch, Sarah, Tariq, Will"

"""
POST /add-names
    Parameters: 
        names: Sarah,Kathleen,Mitch,Tariq,Will
    Expected response (400 BAD REQUEST):
    "No names to add"
"""

def test_get_add_name_no_given_name(web_client):
    response = web_client.get("/add-name", data={"names": "Sarah,Kathleen,Mitch,Tariq,Will"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "No names to add"

"""
POST /add-names
    Parameters: 
        names: Sarah,Kathleen,Mitch,Tariq,Will
        added_name: Charlotte,Paul
    Expected response (200 OK):
    "Charlotte, Kathleen, Mitch, Paul, Sarah, Tariq, Will"
"""
def test_get_add_name_given_name(web_client):
    response = web_client.get("/add-name?names=Sarah,Kathleen,Mitch,Tariq,Will&added_name=Charlotte,Paul")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Charlotte, Kathleen, Mitch, Paul, Sarah, Tariq, Will"
```

