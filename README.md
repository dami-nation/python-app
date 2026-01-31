# Simple Web Application (Flask + Docker)

A minimal Python Flask web application packaged as a Docker image and deployed to an EC2 instance using GitHub Actions.

---

## Application

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DockerHub - Dami's EC2 on Ubuntu 24.04!, What is going on?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

- Listens on port 80
- Binds to `0.0.0.0` so it is reachable outside the container

---

## Docker Image

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY app.py .

RUN pip install flask
EXPOSE 80

CMD ["python", "app.py"]
```

The Docker image contains:
- Python runtime
- Flask dependency
- Application code

The host system only requires Docker.

---

## CI/CD

A GitHub Actions workflow builds and deploys the application on every push to the `main` branch.

### Build
- Builds the Docker image using the Dockerfile
- Pushes the image to Docker Hub

### Deploy
- Connects to the EC2 instance over SSH
- Installs Docker if not present
- Pulls the latest image
- Replaces the running container

Secrets are stored in GitHub Actions secrets.

---

## Prerequisites

### Local / CI
- Docker

### EC2
- Ubuntu 24.04
- Inbound TCP port 80 allowed in the Security Group

---

## Run Locally

```bash
docker build -t python-app:local .
docker run --rm -p 8080:80 python-app:local
```

Test:

```bash
curl http://localhost:8080
```

---

## Deployment

Deployment is handled automatically by GitHub Actions.

On deploy, the EC2 instance runs:

```bash
docker pull <dockerhub-username>/python-app
docker run -d -p 80:80 <dockerhub-username>/python-app
```

---

## Notes

- Uses Flask's built-in development server
- No application dependencies are installed directly on the host

