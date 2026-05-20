---
title: Backend Design Flow
sidebar_label: Backend Design Flow
id: backend/backend-design-flow
---

# System Architecture & Design Flow

This document provides a high-level overview of the architectural design, directory structure, and request flow for the **Delta Labs Backend** (FastAPI + MongoDB + Redis).

* * *

## 1\. High-Level Architecture

The backend implements a **Domain-Driven Design (DDD)** combined with a **Clean Architecture** pattern. This separates concerns into clear layers, ensuring business logic is isolated from external frameworks like HTTP routing or database drivers.

-   **Framework**: FastAPI (Python 3.11+)
    
-   **Database**: MongoDB (async via `Motor`)
    
-   **Cache & Rate Limiting**: Redis (async via `redis-py` with `hiredis`)
    
-   **Email Delivery**: Resend SDK
    
-   **Object Storage**: AWS S3 (via `boto3`) for Media Signing
    

* * *

## 2\. Directory Structure

The `app/` directory is logically partitioned into functional boundaries:

```text
app/
├── api/          # Presentation Layer (Routers & Endpoints)
├── core/         # Cross-Cutting Concerns (Settings, Security, Middlewares)
├── domain/       # Business Logic & Core Models (Bounded Contexts)
├── infra/        # External Systems (DB, Redis, AWS, Email)
├── jobs/         # Background Tasks & Workers
└── main.py       # Application Factory & Lifespan Bootstrap
```

### Layer Responsibilities:

1.  `api/` **(Presentation)**: Defines HTTP routes (e.g., `auth.py`, `schools.py`). It parses incoming JSON into Pydantic models and passes them to the Domain layer.
    
2.  `domain/` **(Business Logic)**: Contains multiple _Bounded Contexts_ (e.g., `identity`, `course`, `school`). Each context has its own `schemas.py` (Pydantic), `repository.py` (MongoDB logic), and `service.py` (Business rules).
    
3.  `infra/` **(Infrastructure)**: Houses connections to third-party services. Examples include `database.py` (MongoDB), `redis_client.py` (Redis), and `media_signer.py` (AWS S3 Presigned URLs).
    
4.  `core/` **(Core)**: Handles application configuration (`BaseSettings`), exceptions, request metrics, and middlewares.
    

* * *

## 3\. The Request Lifecycle Flow

When an HTTP request hits the backend, it passes through the following lifecycle:

### Step 1: Middlewares (`core/`)

The request first traverses a strict middleware chain defined in `main.py`:

-   **Request ID Middleware**: Assigns a unique `X-Request-Id` UUID to every request for tracing.
    
-   **CORS Middleware**: Validates the `Origin` header against allowed clients (e.g., the Next.js web app and the Desktop Electron app).
    
-   **Idempotency Middleware**: Captures idempotency keys to prevent duplicate POST actions (like duplicate payments or signups).
    
-   **Rate Limiting Middleware**: Connects to Redis to throttle excessive requests (e.g., protecting authentication endpoints).
    
-   **Logging Middleware**: Records the start and end times to track performance metrics.
    

### Step 2: Routing (`api/`)

The request reaches an endpoint in `api/v1/`. Here, FastAPI automatically validates the request body, path parameters, and query strings using Pydantic models.

-   Dependency injection (e.g., `deps_authz.py`) extracts the JWT token, validates it, and injects the authenticated `User` object into the endpoint function.
    

### Step 3: Business Logic (`domain/`)

The endpoint calls a specific Service (e.g., `SignupFlowService.execute()`).

-   The Service strictly handles business rules.
    
-   It does **not** write raw SQL or MongoDB queries. Instead, it delegates data access to a `Repository`.
    

### Step 4: Data Persistence (`domain/*/repository.py` & `infra/`)

The `Repository` executes the `Motor` async queries against MongoDB.

-   If emails need to be sent, it calls the `email_client.py` in `infra/`.
    
-   If data needs to be cached, it interacts with `redis_client.py`.
    

### Step 5: Global Exception Handler

If a business rule fails (e.g., `ConflictError`, `NotFoundError`), the Service raises a domain-specific exception. The global exception handlers in `main.py` intercept this and format it into a standardized JSON error response with the correct HTTP status code (409, 404, 400).

* * *

## 4\. Bootstrapping & Lifespan (`main.py`)

FastAPI uses an `@asynccontextmanager` called `lifespan` to handle startup and shutdown sequences efficiently:

1.  **Connect Database**: Opens async connection pools to MongoDB and Redis.
    
2.  **Ensure Indexes**: The repositories automatically check and create necessary MongoDB indexes (e.g., unique email constraints) once at startup.
    
3.  **Application Runs**: Begins accepting HTTP requests.
    
4.  **Shutdown**: Gracefully drains connections to prevent memory leaks when the server is stopped.
