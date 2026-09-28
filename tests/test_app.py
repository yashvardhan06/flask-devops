import psycopg

import app as app_module
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


def test_db_check_endpoint(monkeypatch):
    class FakeConnection:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

        def execute(self, query):
            assert query == "SELECT 1"

    monkeypatch.setattr(
        app_module.psycopg,
        "connect",
        lambda *args, **kwargs: FakeConnection(),
    )

    response = app.test_client().get("/api/db-check")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "database": "connected"}


def test_db_check_returns_503_when_database_is_unavailable(monkeypatch):
    def raise_connection_error(*args, **kwargs):
        raise psycopg.OperationalError("database unavailable")

    monkeypatch.setattr(app_module.psycopg, "connect", raise_connection_error)

    response = app.test_client().get("/api/db-check")

    assert response.status_code == 503
    assert response.get_json() == {"status": "error", "database": "unavailable"}
