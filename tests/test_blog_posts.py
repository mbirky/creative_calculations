"""
Test each of the blog posts can be loaded
"""

def test_hello_world_post(client):
    """
    GIVEN a Flask application
    WHEN the hello_world post is requested (GET)
    THEN check the response is 200 and contains "Hello World"
    """
    response = client.get('/hello_world')
    assert response.status_code == 200
    assert b"<title>Hello World</title>" in response.data
    assert b"<h1>Hello World</h1>" in response.data

def test_why_i_chose_python_post(client):
    """
    GIVEN a Flask application
    WHEN the why_i_chose_python post is requested (GET)
    THEN check the response is 200 and contains "Why I Chose Python"
    """
    response = client.get('/why_i_chose_python')
    assert response.status_code == 200
    assert b"<h1>Why I Chose Python</h1>" in response.data

def test_a_fun_data_parser_post(client):
    """
    GIVEN a Flask application
    WHEN the a_fun_data_parser post is requested (GET)
    THEN check the response is 200 and contains "A Fun Data Parser"
    """
    response = client.get('/a_fun_data_parser')
    assert response.status_code == 200
    assert b"<h1>A Fun Data Parser</h1>" in response.data
