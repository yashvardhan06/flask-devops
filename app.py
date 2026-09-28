import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")


@app.get("/")
def index():
    return (
        "<h1>DevOps Portfolio App</h1>"
        "<p>Containerized Full-Stack Application with CI/CD and Kubernetes.</p>"
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "portfolio-app"})


@app.get("/api/db-check")
def db_check():
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=3) as connection:
            connection.execute("SELECT 1")
    except psycopg.Error:
        return jsonify({"status": "error", "database": "unavailable"}), 503

    return jsonify({"status": "ok", "database": "connected"})


@app.get("/api/status")
def api_status():
    return jsonify({
        "status": "ok",
        "database": DATABASE_URL,
        "environment": os.getenv("APP_ENV", "development"),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
