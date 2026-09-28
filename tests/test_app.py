from app import app


def test_root_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert "DevOps Portfolio App" in response.get_data(as_text=True)


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
