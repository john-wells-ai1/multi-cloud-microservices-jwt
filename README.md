
# Multi-Cloud Microservices Case Study (AWS Lambda + AKS)

## Overview
This project demonstrates a **secure, cloud-based distributed microservices architecture**
using:
- **AWS Lambda + API Gateway** (serverless edge)
- **Azure Kubernetes Service (AKS)** (containerized backend)
- **JWT Authentication** for zero-trust communication

## Architecture
1. Client authenticates and sends JWT in Authorization header
2. API Gateway validates JWT using Lambda authorizer
3. Lambda forwards request to AKS REST API
4. AKS validates JWT and processes request

## Security
- HMAC-based JWT (HS256)
- API Gateway Lambda Authorizer
- Stateless auth, cloud-agnostic

## Components
- AWS Lambda (Python)
- API Gateway (REST)
- AKS + FastAPI
- Docker + Kubernetes

## Request Flow
```
Client → API Gateway → Lambda → AKS Service → Response
```

## Deployment Steps
See individual folders for AWS and AKS deployment instructions.
