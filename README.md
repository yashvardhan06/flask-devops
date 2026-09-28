# DevOps Portfolio Project

This project demonstrates a production-style DevOps setup for a simple Python Flask application using local tooling and GitHub Actions.

## What this project includes

- Flask application with `/`, `/health`, and `/api/status`
- Dockerfile and docker-compose for local application + PostgreSQL
- GitHub Actions CI/CD pipeline
- Trivy image security scanning
- Kubernetes manifests for dev and prod
- Helm chart for environment-specific deployment
- Basic testing setup with pytest

## Local development

### 1. Install requirements

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the app locally

```bash
python app.py
```

Then open:

- http://localhost:5000/
- http://localhost:5000/health
- http://localhost:5000/api/status

### 3. Run tests

```bash
pytest -q
```

### 4. Run with Docker Compose

```bash
docker compose up --build
```

This starts the Flask app and a PostgreSQL container.

> Note: this is suitable for local development and learning, not for production-grade persistent storage.

## CI/CD pipeline

The workflow in `.github/workflows/ci.yml` covers the pipeline stages described in the project brief:

1. checkout code
2. install Python dependencies
3. run lint and compile checks
4. run unit tests
5. build the Flask app
6. build a Docker image
7. scan the image with Trivy
8. push to GHCR
9. deploy with Helm to dev and prod namespaces
10. verify rollout and smoke-test the app

### Required GitHub secrets

Add the following secrets in the GitHub repository settings:

- `KUBE_CONFIG` — base64-encoded kubeconfig for your Kubernetes cluster
- `GITHUB_TOKEN` — provided automatically by GitHub Actions for ghcr.io pushes

### Example deploy command

```bash
helm upgrade --install portfolio-dev ./helm/portfolio-app \
  -f ./helm/portfolio-app/values-dev.yaml \
  --namespace dev \
  --create-namespace \
  --set image.repository=ghcr.io/<your-user>/portfolio-app \
  --set image.tag=latest

helm upgrade --install portfolio-prod ./helm/portfolio-app \
  -f ./helm/portfolio-app/values-prod.yaml \
  --namespace prod \
  --create-namespace \
  --set image.repository=ghcr.io/<your-user>/portfolio-app \
  --set image.tag=latest
```

## Kubernetes

Kubernetes manifests are placed under `k8s/` for namespaces, deployment, service, ingress, secrets, configmaps, and HPA.

### Deploy with Helm

```bash
helm install dev-release ./helm/portfolio-app -f ./helm/portfolio-app/values-dev.yaml
helm install prod-release ./helm/portfolio-app -f ./helm/portfolio-app/values-prod.yaml
```

## Security note

- Trivy is used to scan container images for vulnerabilities.
- In a real production project, you would also add SAST, dependency scanning, secret scanning, and policy enforcement.

## Why this project is a good DevOps portfolio piece

- It shows application packaging with Docker
- It demonstrates automated testing and CI
- It includes container security scanning
- It uses Kubernetes and Helm for deployment
- It separates environments with dev and prod values
- It is simple enough to understand but realistic in structure
