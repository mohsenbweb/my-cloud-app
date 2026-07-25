# Troubleshooting

## GitHub Push returns HTTP 403

### Problem

```
Permission denied
```

### Solution

Created a new GitHub Personal Access Token with the required `repo` permission.

---

## Azure Login failed

### Problem

```
No subscriptions found
```

### Solution

Generated new `AZURE_CREDENTIALS` using a Service Principal and updated the GitHub secret.

---

## Azure Container Registry authentication failed

### Problem

```
UNAUTHORIZED: authentication required
```

### Solution

- Created Azure Container Registry
- Enabled Managed Identity
- Assigned the AcrPull role
- Connected the Container App to the registry

---

## Application URL returned Connection Refused

### Problem

```
Connection refused
```

### Solution

The application listened on port **8000**, while Azure Container Apps was configured for **5000**. Updated the target port to **8000**.
