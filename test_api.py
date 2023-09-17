from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_courses():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'courses': ['frontend', 'backend', 'gamedev', 'fullstack']}
    pass

def test_login_route():

    payload = {
        "username":"joe",
        "password":"12345678"
    }
    response = client.post("/login", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "you've logged in"}
    pass


def test_registration_route():
    payload = {
        "username": "joe",
        "password": "12345678",
        "e-mail": "joe@doe.com"
}
    response = client.post("/registration", json=payload)

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
    response = client.post("/user/joe/courses/add", json=payload)
    assert response.status_code == 200
    assert response.json() == {'message': 'Courses should be provided as a list.'}
    pass

