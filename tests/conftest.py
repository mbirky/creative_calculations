"""
Flask fixture and configurations that are shared amongst all of the tests
"""

import pytest

import creative_calculations

@pytest.fixture
# pylint: disable=unused-argument,redefined-outer-name
def client(scope="module"):
    """
    Create a client fixture to run the tests with
    """
    creative_calculations.APP.config['TESTING'] = True
    client = creative_calculations.APP.test_client()

    yield client
