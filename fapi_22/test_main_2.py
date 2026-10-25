from fastapi.testclient import TestClient
from main2 import app

client = TestClient(app)

def test_home():
    response = client.get("/home")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello Tinks"}

def test_add():
    response = client.get("/add?a=3&b=5")

    assert response.status_code == 200
    assert response.json() == {"result":8} 