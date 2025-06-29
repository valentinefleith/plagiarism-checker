from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello app!"}


def test_predict_class():
    text = {"body": "Coucou"}
    response = client.post("/prediction/", json=text)

    assert response.status_code == 200

    data = response.json()
    print(data)

    assert data["text"] == text["body"]
    assert data["prediction"] in ["human", "llm"]
    assert 0 <= data["probability"] <= 100
