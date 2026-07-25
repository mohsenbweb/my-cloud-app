# Deployment

## CI/CD Pipeline

The deployment process is fully automated using GitHub Actions.

Every push to the **main** branch starts the following workflow:

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
    ├── Checkout Repository
    ├── Azure Login
    ├── Login to Azure Container Registry
    ├── Build Docker Image
    ├── Push Docker Image
    └── Deploy Azure Container App
            │
            ▼
Azure Container Apps
```

---

## Deployment Steps

1. Push changes to the `main` branch.
2. GitHub Actions automatically starts.
3. A Docker image is built.
4. The image is pushed to Azure Container Registry.
5. Azure Container Apps creates a new revision.
6. The latest revision becomes active.

---

## Azure Resources

| Resource           | Name         |
| ------------------ | ------------ |
| Subscription       | mo-abo       |
| Resource Group     | my-cloud-rg  |
| Container Registry | mocloudacr   |
| Container App      | my-cloud-app |

---

## Authentication

Azure Container Apps authenticates to Azure Container Registry using a **System Assigned Managed Identity** with the **AcrPull** role.
