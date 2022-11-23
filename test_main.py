from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_():
  response = client.get("/blog/all")
  assert response.status_code == 200

def test_auth_error():
  response = client.post("/token",
  data={"username": "","password:": ""}
  )
  access_token = response.json().get("access_token")
  assert access_token == None
  message = response.json().get("detail")[0].get("msg")
  assert message == "field required"

def test_auth_success():
  pass