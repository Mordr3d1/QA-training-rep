import requests
import pytest


ENDPOINT = "http://127.0.0.1:8000"

response = requests.get(ENDPOINT)

data = response.json()
print(data)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

def test_courses():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    assert response.json() == {'courses': ['frontend', 'backend', 'gamedev', 'fullstack']}
    pass

def test_login_route():
    payload = {
        "username":"joe",
        "password":"12345678"
    }
    response = requests.post(ENDPOINT + "/login", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "you've logged in"}
    pass

def test_registration_route():
    payload = {
        "username": "joe",
        "password": "12345678",
        "e-mail": "joe@doe.com"
}
    response = requests.get(ENDPOINT + "/registration", json=payload)

    assert response.status_code == 200
    assert response.json() == {
    "new user": {
        "username": "joe",
        "password": "12345678",
        "e-mail": "joe@doe.com"
    }
}
    pass

def test_courses_add():
    payload = {
        "courses": "gamedev"
}
    response = requests.post(ENDPOINT + "/user/joe/courses/add", json=payload)

    assert response.status_code == 200
    assert response.json() == {'message': 'Courses should be provided as a list.'}
    pass

