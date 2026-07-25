# Deployment

## Deployment Workflow

Every push to the `main` branch automatically starts the deployment pipeline.

### Steps

1. Push source code to GitHub
2. GitHub Actions starts
3. Docker image is built
4. Image is pushed to Azure Container Registry
5. Azure Container App updates to the new image

## Azure Resources

| Resource | Name |
|-----------|------|
| Subscription | mo-abo |
| Resource Group | my-cloud-rg |
| Container Registry | mocloudacr |
| Container App | my-cloud-app |

## Authentication

Azure Container Apps uses a **System Assigned Managed Identity** with the **AcrPull** role to pull images securely from Azure Container Registry.
