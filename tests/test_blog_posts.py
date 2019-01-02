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
    assert b"<h1>Hello World\n</h1>" in response.data

def test_why_i_chose_python_post(client):
    """
    GIVEN a Flask application
    WHEN the why_i_chose_python post is requested (GET)
    THEN check the response is 200 and contains "Hello World"
    """
    response = client.get('/why_i_chose_python')
    assert b"<h1>Why I Chose Python\n</h1>" in response.data
    assert response.status_code == 200
    print(response.data)
