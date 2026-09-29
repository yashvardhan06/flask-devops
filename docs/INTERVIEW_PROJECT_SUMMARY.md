# DevOps Portfolio Project - Interview Summary
This project was built as a practical, local-first DevOps portfolio to demonstrate the complete lifecycle of a simple Python web application using free and commonly available tools. The goal was to show how an application moves from development to containerization, automated testing, source control, CI/CD, and deployment preparation without relying on paid cloud services.

## Overview

The project includes a Flask application, PostgreSQL integration, Docker configuration, automated tests, GitHub Actions workflow, and Kubernetes/Helm deployment files. Even though the application itself is small, the infrastructure around it reflects a realistic DevOps setup used in real environments.

## What I built

The application includes:
- a landing page at `/`
- a basic health endpoint at `/health`
- a real database connectivity check at `/api/db-check`
- an environment/status endpoint at `/api/status`

The main idea was to prove that the service is not just running, but also that it can reach and use its dependencies correctly. This distinction is important in real-world deployment because an app can be "up" while still failing its database connection.

## Technologies used

- Python with Flask
- PostgreSQL
- Docker and Docker Compose
- GitHub and GitHub Actions
- Trivy for image security scanning
- Kubernetes manifests and Helm chart

This stack was chosen to represent a realistic delivery pipeline while keeping the project manageable and easy to explain.

## How I implemented it

1. Built the Flask app and created basic routes.
2. Added a database connectivity check using `psycopg`.
3. Wrote test cases for health and database behavior.
4. Containerized the app with a Dockerfile.
5. Added a Docker Compose stack with the app and PostgreSQL.
6. Used health checks so the app waits for PostgreSQL to be ready.
7. Pushed the project to GitHub.
8. Created a GitHub Actions workflow to run tests, compile checks, build the Docker image, and scan it.
9. Published the image to GitHub Container Registry.
10. Prepared Kubernetes and Helm files to show how the app could be deployed to a cluster environment.

## What I achieved

The project successfully demonstrates:
- application development with Python and Flask
- real database integration
- local container orchestration with Docker Compose
- automated testing
- security scanning using Trivy
- CI/CD with GitHub Actions
- Docker image publishing to GHCR
- Kubernetes and Helm deployment preparation

This is valuable because it shows a working end-to-end DevOps lifecycle rather than a single script or simple app.

## Challenges faced and how I resolved them

### 1. Docker name and port conflicts
The first issue was a Docker container conflict because a previous container with the same name already existed. I fixed this by removing the fixed naming issue and using Compose-managed names so the environment could restart cleanly.

### 2. Database was not ready when app started
The app and PostgreSQL were started together, but the app could begin before PostgreSQL was ready. I added a PostgreSQL health check and used `depends_on: condition: service_healthy` so the app waits until the database is actually ready.

### 3. Health endpoint was not enough
The root health endpoint only proved that Flask was running, not that the database was reachable. I added `/api/db-check`, which performs a real database query and returns a failure if the database is unavailable.

### 4. Windows PowerShell curl issue
In PowerShell, `curl` often behaves like `Invoke-WebRequest`, which caused confusion during validation. I used `curl.exe` or `Invoke-RestMethod` to make correct HTTP requests and verify the endpoints properly.

### 5. Test execution inside Docker
Running the raw `pytest` command in the container failed due to import path issues. The fix was to use `python -m pytest -q`, which reliably runs the project tests in that environment.

### 6. Trivy scan blocking the workflow
The first CI scan was too strict for a learning pipeline. I adjusted the security gate to align with a practical approach: fail only on fixable critical issues, which kept the workflow usable while still enforcing security checks.

### 7. GitHub-hosted runners and local Kubernetes
A GitHub-hosted runner cannot directly access a local Minikube cluster running on a developer machine. This meant the final live cluster deployment step needed a self-hosted runner or an externally reachable cluster. The Kubernetes/Helm files were included as a strong foundation, but the actual cluster deployment step requires the right environment.

## Why this project matters

This project demonstrates foundational DevOps skills that are very relevant in interviews and real engineering work:
- understanding application dependencies
- packaging with Docker
- writing reliable health checks
- automating with CI/CD
- validating security in container images
- preparing for cloud-native deployment with Kubernetes and Helm

## Final statement

This project shows that I can build a simple app, package it correctly, validate it with automated tests, integrate it with infrastructure tools, and prepare it for deployment in a modern DevOps workflow. It is a strong example of practical DevOps knowledge and hands-on implementation.
