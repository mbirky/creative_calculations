"""
Testing of the creative_calculation module
"""

import pytest

import creative_calculations

# pylint:disable=redefined-outer-name

@pytest.fixture
def client():
    """
    Create a client fixture to run the tests with
    """
    creative_calculations.app.config['TESTING'] = True
    client = creative_calculations.app.test_client()

    yield client

def test_home_page(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World" in response.data

def test_post_200(client):
    """
    GIVEN a Flask application
    WHEN the '/<post_name>' pages is requested (GET)
    THEN check the response is 200 and contains <post_name>
    """
    response = client.get('/helloworld')
    assert response.status_code == 200
    assert b"Hello World" in response.data

def test_post_404(client):
    """
    GIVEN a Flask application
    WHEN the '/<post_name>' pages is requested (GET)
    THEN check the response is 200 and contains <post_name>
    """
    response = client.get('/bad_post_12345')
    assert response.status_code == 404
    assert response.data == b"404: Not all who wander are lost, but you are."

def test_404(client):
    """
    GIVEN a Flask application
    WHEN an invalid page is requested (GET)
    THEN check for a 404 error
    """
    response = client.get('/error/404')
    assert response.status_code == 404
    assert response.data == b"404: Not all who wander are lost, but you are."
