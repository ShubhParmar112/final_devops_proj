
import pytest
from app import app, model


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_model_loaded():
    assert model is not None


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


def test_flower_info_api(client):
    response = client.get("/api/flower-info")

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()

    assert "setosa" in data
    assert "versicolor" in data
    assert "virginica" in data


def test_prediction(client):
    response = client.post(
        "/predict",
        data={
            "sepal_length": "5.1",
            "sepal_width": "3.5",
            "petal_length": "1.4",
            "petal_width": "0.2"
        }
    )

    assert response.status_code == 200
