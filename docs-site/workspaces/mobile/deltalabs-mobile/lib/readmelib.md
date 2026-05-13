---
title: Readmelib
sidebar_label: Readmelib
id: deltalabs-mobile/lib/readmelib
---

# lib/

Root of all Dart source code.

## Key files

-   **main.dart** — Entry point. Calls `bootstrap()` then runs `ProviderScope(child: DeltaLabsApp())`.
    
-   **bootstrap.dart** — Runs before `runApp`. Initializes orientation lock, edge-to-edge UI, `AppConfig`, `ServiceLocator`, and reads the local auth token to determine the initial route (no flash on startup).
    
-   **firebase\_options.dart** — Auto-generated Firebase config (currently unused, ready for when Firebase is enabled).
