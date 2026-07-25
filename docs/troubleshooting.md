# Troubleshooting

This document summarizes common issues encountered during the development and deployment of this project and how they were resolved.

---

# GitHub Push - HTTP 403

## Problem

Git push failed with:

```text
remote: Permission denied
fatal: HTTP 403
```

## Cause

The GitHub Personal Access Token (PAT) did not have sufficient permissions.

## Solution

- Created a new Personal Access Token
- Enabled the **repo** permission
- Updated the Git credentials

---

# Azure Login

## Problem

GitHub Actions failed with:

```text
No subscriptions found
```

## Cause

The Service Principal used by GitHub Actions was not associated with the Azure subscription.

## Solution

- Created a new Service Principal
- Generated a new `AZURE_CREDENTIALS`
- Updated the GitHub Secret

---

# Azure Container Registry Authentication

## Problem

Deployment failed with:

```text
UNAUTHORIZED: authentication required
```

## Cause

Azure Container Apps was not authorized to pull images from Azure Container Registry.

## Solution

- Created Azure Container Registry
- Enabled System Assigned Managed Identity
- Assigned the **AcrPull** role
- Connected the Container App to Azure Container Registry

---

# Managed Identity

## Problem

The Managed Identity could not be selected in the Azure Portal.

## Cause

No identity had been assigned to the Container App.

## Solution

Assigned a System Assigned Managed Identity using Azure CLI.

---

# Registry Configuration

## Problem

The Container App was not linked to Azure Container Registry.

## Solution

Configured the registry using Azure CLI.

---

# Connection Refused

## Problem

The application returned:

```text
Connection refused
```

## Cause

Azure Container Apps forwarded requests to port **5000**, while Gunicorn listened on port **8000**.

## Solution

Updated the Container App target port to **8000**.

---

# Lessons Learned

During this project I learned how to:

- Configure Docker for Azure Container Apps
- Build an automated CI/CD pipeline with GitHub Actions
- Use Azure Container Registry
- Configure Managed Identity
- Assign Azure RBAC roles
- Troubleshoot deployment issues
- Diagnose container startup problems
- Read Azure logs and deployment errors
