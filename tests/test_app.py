# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post("/count_vowels", data={"text": "eee"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "There are 3 vowels in 'eee'"

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post("/count_vowels", data={"text": "eunoia"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "There are 5 vowels in 'eunoia'"

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post("/count_vowels", data={"text": "mercurial"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "There are 4 vowels in 'mercurial'"

"""
POST /sort_names
    Parameters:
        names: Sarah,Kathleen,Mitch,Tariq,Will
    Expected response (200 OK):
        "Kathleen,Mitch,Sarah,Tariq,Will"
"""
def test_post_sort_names_with_list_of_names(web_client):
    response = web_client.post("/sort-names", data={"names": "Sarah,Kathleen,Mitch,Tariq,Will"})
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
    response = web_client.post("/sort-names", data={"names": "aaab,aaaz,aaac"})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "aaab,aaac,aaaz"

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
    response = web_client.get("/add-name?names=Sarah,Kathleen,Mitch,Tariq,Will")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "No names to add"

def test_get_add_name_given_multiple_names(web_client):
    response = web_client.get("/add-name?names=Sarah,Kathleen,Mitch,Tariq,Will&added_name=Charlotte,Paul")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Charlotte, Kathleen, Mitch, Paul, Sarah, Tariq, Will"

# === End Example Code ===
