---
title: Readmenetwork
sidebar_label: Readmenetwork
id: deltalabs-mobile/lib/core/network/readmenetwork
---

# lib/core/network/

HTTP networking layer built on **Dio**.

## api\_client.dart

`ApiClient` — the single shared Dio instance used by all data sources.

-   Configured with `baseUrl`, timeouts, and JSON headers
    
-   Has `get`, `post`, `put`, `patch`, `delete`, `uploadFile` methods
    
-   Interceptors added: `AuthInterceptor`, `RetryInterceptor`, `PrettyDioLogger` (debug only)
    

## interceptors/auth\_interceptor.dart

Runs on every request:

-   **onRequest** — reads token from `SecureStorage`, adds `Authorization: Bearer <token>` header
    
-   **onError** — if 401 received, clears local token (session expired)
    

## interceptors/retry\_interceptor.dart

Automatically retries failed requests:

-   Up to 3 attempts
    
-   1 second delay between retries
    
-   Only retries on connection errors and timeouts (not 4xx responses)
    

## pagination/paginated\_response.dart

Generic `PaginatedResponse<T>` model for list endpoints. Contains `items`, `total`, `page`, `pageSize`, `hasMore`.
