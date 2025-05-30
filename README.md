🌦 Weather App – DevOps Enabled Deployment
A full-stack Python-based weather forecasting app deployed using Docker, Kubernetes, CI/CD (GitHub Actions), and Argo CD. Built to demonstrate production-ready DevOps practices and seamless cloud deployment.

📁 Project Structure

.
├── .github/workflows/ci-cd.yml     # CI/CD workflow with GitHub Actions
├── .dockerignore                   # Files ignored by Docker
├── .env.txt                        # Sample environment variables
├── .gitignore                      # Git ignored files
├── Dockerfile                      # Docker build configuration
├── README.md                       # Project documentation
├── app.py                          # Main Python application
├── requirements.txt                # Python dependencies
├── kubectl/                        # Kubernetes manifests (YAML files)
├── static/                         # Static files (CSS, JS, images)
└── templates/                      # HTML templates (Jinja2)
🚀 Features
🛰 Live Weather Data: Fetches real-time weather information

🐳 Dockerized: Runs inside a container for consistency across environments

☸️ Kubernetes Deployment: Deployed to K8s cluster using manifests

🔄 CI/CD Integration: GitHub Actions pipeline for build, test, and deploy

📦 Argo CD: GitOps-based continuous deployment

📁 Clean File Structure: Easy to navigate and extend

🛠 Tech Stack
Frontend: HTML, CSS (in templates/ and static/)

Backend: Python (Flask-based)

Containerization: Docker

Orchestration: Kubernetes

CI/CD: GitHub Actions, Argo CD


