import requests


def test_home_sends_200_response():
    """Test the homepage returns a 200 status code."""
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200


def test_home_200_body():
    """Test body of successful GET request."""
    response = requests.get('http://127.0.0.1:3000')
    assert response.text == '<a href="/cowsay">Cowsay</a>'


def test_home_headers():
    """Test headers exist on homepage GET."""
    response = requests.get('http://127.0.0.1:3000')
    assert response.headers


def test_server_sends_404_response():
    """Test the server can return a 404 error."""
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404


def test_server_404_body():
    """Test response body on a 404."""
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.text == 'This doesn\'t exist in GET!'


def test_cowsay_sends_200_response():
    """Test the cowsay route returns a 200 status code."""
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200


def test_cowsay_headers():
    """Test headers on cowsay GET."""
    response = requests.get('http://127.0.0.1:3000')
    assert response.headers


def test_server_query_string_code():
    """Test that the GET route handles a query string."""
    response = requests.get('http://127.0.0.1:3000/cow?msg=test')
    assert response.status_code == 200


def test_server_query_string_headers():
    """Test that headers exist."""
    response = requests.get('http://127.0.0.1:3000/cow?msg=test')
    assert response.headers


def test_server_post_sends_200_response():
    """Test that a valid POST returns a 200 status code."""
    response = requests.post('http://127.0.0.1:3000/cow?msg=test')
    assert response.status_code == 200


def test_server_post_sends_404_response():
    """Test POST request since 404 status code."""
    response = requests.post('http://127.0.0.1:3000/test')
    assert response.status_code == 404


def test_server_post_404_body():
    """Test server POST 404 response body."""
    response = requests.post('http://127.0.0.1:3000/test')
    assert response.text == 'This doesn\'t exist in POST!'
