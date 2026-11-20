---
title: Readmeconfig
sidebar_label: Readmeconfig
id: readmeconfig
---

# lib/core/config/

Runtime configuration and environment management.

## app\_config.dart

Singleton initialized in `bootstrap.dart` before `runApp`. Holds:

-   `apiBaseUrl` — backend base URL per environment
    
-   `wsBaseUrl` — WebSocket base URL
    
-   `cdnBaseUrl` — CDN base URL
    
-   Timeout values, retry counts, feature flags
    

```dart
// Access anywhere
AppConfig.instance.apiBaseUrl
```

## environment.dart

`Environment` enum: `development`, `staging`, `production`.

Detected via `--dart-define=ENVIRONMENT=production` at build time. Defaults to `development` if not set.

```bash
# Build for production
flutter build apk --dart-define=ENVIRONMENT=production
```
