from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test Home API
def test_home():
    response = client.get("/")
    assert response.status_code == 200    # Status Code check
    assert response.json() == {"message":"Hello Tinks"}  # Response Data check

#  Test Add API
def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result":8}
