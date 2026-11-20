---
title: Readmedi
sidebar_label: Readmedi
id: readmedi
---

# lib/core/di/

Dependency injection using **get\_it**.

## service\_locator.dart

`ServiceLocator.initialize()` registers all singletons at startup:

-   `AppConfig` — configuration
    
-   `SecureStorage` — token storage
    
-   `AuthInterceptor` — attaches Bearer token to requests
    
-   `RetryInterceptor` — retries failed requests
    
-   `ApiClient` — the shared Dio HTTP client
    
-   `LocalDatabase` — Drift SQLite instance
    
-   `WebSocketManager` — realtime connection
    
-   `SyncEngine` — offline sync coordinator
    

Access registered instances anywhere:

```dart
sl<ApiClient>()       // get the HTTP client
sl<SecureStorage>()   // get secure storage
```

Note: Riverpod providers use `sl<>()` to access these singletons rather than creating new instances.
