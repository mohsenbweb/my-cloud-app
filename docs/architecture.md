# Architecture

## Overview

The application is deployed automatically to Azure Container Apps using GitHub Actions.

## Architecture Diagram

```text
Developer
     │
     ▼
Git Push
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ├── Build Docker Image
     ├── Push Image to Azure Container Registry
     └── Deploy Azure Container App
              │
              ▼
Azure Container Registry
              │
              ▼
Azure Container Apps
              │
              ▼
Flask Application
```

## Components

| Component | Purpose |
|-----------|---------|
| GitHub | Source code management |
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |
| Azure Container Registry | Stores Docker images |
| Azure Container Apps | Runs the application |
| Managed Identity | Secure authentication to ACR |
