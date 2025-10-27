# access-openai-ptu-using-jwt-token

This project demonstrates how to **securely access Azure OpenAI Provisioned Throughput Units (PTUs)** using **JWT-based authentication** implemented in **Azure API Management (APIM)**.  
It ensures controlled access, token validation, and rate-limiting for OpenAI APIs within enterprise-grade environments.

---

## Table of Contents

- Overview
- Key Components
- JWT Authentication Flow
- Security Highlights

---

## Overview

Azure OpenAI PTUs (Provisioned Throughput Units) provide **dedicated and predictable capacity** for OpenAI workloads like Chat Completions and Embeddings.

This implementation uses **Azure API Management (APIM)** as a **security gateway** to:
- Validate incoming **JWT tokens**
- Control and monitor API usage
- Route authenticated traffic to **Azure OpenAI endpoints**

---

## Key Components

| **Azure API Management (APIM)** | Acts as the API gateway for authentication, security, and routing |
| **JWT Token** | Used for client authentication and access validation |
| **Azure OpenAI PTUs** | Dedicated capacity for consistent OpenAI performance |
| **Azure Key Vault** *(optional)* | Stores JWT signing keys or secrets |
| **Terraform / ARM Templates** | Automate resource deployment and configuration |

---

## JWT Authentication Flow

1. **Client** requests a JWT token from a trusted identity provider (e.g., Azure AD, Auth0).  
2. **Client** calls the APIM endpoint with the token in the `Authorization` header.  
3. **APIM** validates the token using its public key or JWKS URI.  
4. On success, APIM forwards the request to the **Azure OpenAI PTU endpoint**.  
5. Invalid or expired tokens are rejected with `401 Unauthorized`.

---

## Security Highlights

1. JWT-based authentication for token validation
2. Supports Azure AD / external IdPs for token issuance
3. Enforced expiration, audience, and issuer claims
4. Optional rate-limiting and quota policies
5. Optional Azure Key Vault integration for secret management

---