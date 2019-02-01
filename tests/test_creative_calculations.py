"""
Testing of the creative_calculation module
"""

def test_home_page(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Hello World</h1>" in response.data

def test_post_200(client):
    """
    GIVEN a Flask application
    WHEN the '/<post_name>' pages is requested (GET)
    THEN check the response is 200 and contains <post_name>
    """
    response = client.get('/hello_world')
    assert response.status_code == 200
    assert b"<h1>Hello World</h1>" in response.data

def test_404(client):
    """
    GIVEN a Flask application
    WHEN an invalid page is requested (GET)
    THEN check for a 404 error
    """
    response = client.get('/bad_post_12345')
    assert response.status_code == 404
    assert response.data == b"404: Not all who wander are lost, but you are."
