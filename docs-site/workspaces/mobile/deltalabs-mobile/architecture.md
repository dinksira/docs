---
title: Architecture
sidebar_label: Architecture
id: architecture
---

# DeltaLabs Mobile — Architecture Overview

## Tech Stack

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Layer</p></th><th colspan="1" rowspan="1"><p>Tool</p></th><th colspan="1" rowspan="1"><p>Version</p></th></tr><tr><td colspan="1" rowspan="1"><p>Language</p></td><td colspan="1" rowspan="1"><p>Dart</p></td><td colspan="1" rowspan="1"><p>≥3.8</p></td></tr><tr><td colspan="1" rowspan="1"><p>Framework</p></td><td colspan="1" rowspan="1"><p>Flutter</p></td><td colspan="1" rowspan="1"><p>≥3.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>State Management</p></td><td colspan="1" rowspan="1"><p>Riverpod (riverpod_generator)</p></td><td colspan="1" rowspan="1"><p>^3.0</p></td></tr><tr><td colspan="1" rowspan="1"><p>Routing</p></td><td colspan="1" rowspan="1"><p>go_router</p></td><td colspan="1" rowspan="1"><p>^14.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>HTTP Client</p></td><td colspan="1" rowspan="1"><p>Dio</p></td><td colspan="1" rowspan="1"><p>^5.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>Local DB</p></td><td colspan="1" rowspan="1"><p>Drift (SQLite)</p></td><td colspan="1" rowspan="1"><p>^2.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>Secure Storage</p></td><td colspan="1" rowspan="1"><p>flutter_secure_storage</p></td><td colspan="1" rowspan="1"><p>^9.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>Code Generation</p></td><td colspan="1" rowspan="1"><p>build_runner + freezed + riverpod_generator</p></td><td colspan="1" rowspan="1"><p>latest</p></td></tr><tr><td colspan="1" rowspan="1"><p>DI Container</p></td><td colspan="1" rowspan="1"><p>get_it</p></td><td colspan="1" rowspan="1"><p>^8.x</p></td></tr><tr><td colspan="1" rowspan="1"><p>Realtime</p></td><td colspan="1" rowspan="1"><p>WebSocket (socket_io_client)</p></td><td colspan="1" rowspan="1"><p>^2.x</p></td></tr></tbody></table>

* * *

## Architecture Pattern — Clean Architecture

The app follows **Clean Architecture** with three layers per feature:

```
Presentation  →  Domain  →  Data
(UI + State)     (Logic)    (API + Storage)
```

### Layer Responsibilities

**Presentation**

-   Flutter widgets (pages, components)
    
-   Riverpod notifiers (state management)
    
-   No business logic — only UI and state
    

**Domain**

-   Entities (pure Dart classes, no Flutter)
    
-   Repository interfaces (abstract contracts)
    
-   Use cases (single-responsibility business operations)
    
-   No dependencies on Flutter or external packages
    

**Data**

-   Repository implementations
    
-   Remote data sources (Dio API calls)
    
-   Local data sources (Drift, SecureStorage)
    
-   Data models (JSON parsing, DB mapping)
    

* * *

## State Management — Riverpod 3.x

We use **Riverpod with code generation** (`@riverpod` annotation).

### Pattern used

```dart
// 1. Define a notifier with @riverpod
@riverpod
class LoginNotifier extends _$LoginNotifier {
  @override
  LoginState build() => const LoginState();

  Future<void> signIn({...}) async { ... }
}

// 2. Watch in widget
final state = ref.watch(loginProvider);
final notifier = ref.read(loginProvider.notifier);
```

### Provider types used

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Type</p></th><th colspan="1" rowspan="1"><p>When used</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>@riverpod</code> (autoDispose)</p></td><td colspan="1" rowspan="1"><p>Screen-scoped state (login form, register flow)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>@Riverpod(keepAlive: true)</code></p></td><td colspan="1" rowspan="1"><p>Global state (auth session)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>@riverpod</code> functional</p></td><td colspan="1" rowspan="1"><p>Simple derived values (isAuthenticated)</p></td></tr></tbody></table>

### Key providers

-   `authProvider` — global session state (keepAlive)
    
-   `loginProvider` — login form state
    
-   `registerProvider` — multi-step registration flow state
    
-   `recoverProvider` — password recovery flow state
    
-   `appRouterProvider` — GoRouter instance (watches authProvider)
    

* * *

## Routing — go\_router

Declarative routing with **auth guards via redirect**.

```
/ (login)
/auth/login
/auth/register/step1
/auth/register/step2
/auth/register/otp
/auth/register/dob
/auth/register/password
/auth/forgot-password
/auth/forgot-otp
/auth/reset-password
/home
```

### Auth Guard Strategy

The router watches `authProvider`. On every navigation:

-   If `isLoading` → no redirect (initial route already set correctly)
    
-   If logged in + on auth screen → redirect to `/home`
    
-   If not logged in + on protected screen → redirect to `/auth/login`
    

### Initial Route (no flash)

Before `runApp`, `bootstrap.dart` reads the local token from `SecureStorage` and sets `initialAppRoute`. The router starts at the correct screen with zero redirect flash.

* * *

## Folder Structure

```
lib/
├── main.dart              # Entry point
├── bootstrap.dart         # App initialization (token check, DI, system UI)
├── app/
│   └── app.dart           # MaterialApp.router setup
├── core/                  # Shared infrastructure (no feature logic)
│   ├── config/            # Environment config, base URLs
│   ├── di/                # Dependency injection (get_it)
│   ├── domain/            # Base classes (Entity, UseCase, Repository)
│   ├── error/             # Failures, exceptions, error handler
│   ├── localization/      # i18n setup
│   ├── logging/           # App logger
│   ├── network/           # Dio client, interceptors, pagination
│   ├── realtime/          # WebSocket manager
│   ├── routing/           # GoRouter, route constants, guards
│   ├── storage/           # SecureStorage, Drift local DB
│   ├── sync/              # Offline sync engine
│   └── theme/             # Colors, typography, spacing, theme
├── features/              # Feature modules (self-contained)
│   ├── auth/              # Login, register, recover password
│   ├── feed/              # Content feed (FYP)
│   ├── classes/           # Live and recorded classes
│   ├── exams/             # Exam management
│   ├── library/           # Content library
│   ├── chat/              # Messaging
│   ├── tutoring/          # 1-on-1 tutoring sessions
│   ├── notifications/     # Push notifications
│   ├── erp/               # HR + Finance modules
│   └── home/              # Home screen
└── shared/                # Reusable widgets across features
    └── widgets/
        ├── auth/          # Auth-specific widgets (scaffold, fields, buttons)
        ├── error/         # Error display widgets
        ├── loading/       # Shimmer loaders
        └── network_image/ # Cached image widget
```

* * *

## Network Layer

-   **Dio** as the HTTP client
    
-   **AuthInterceptor** — attaches `Bearer` token to every request; clears session on 401
    
-   **RetryInterceptor** — retries failed requests up to 3 times with exponential backoff
    
-   **PrettyDioLogger** — logs requests/responses in debug mode only
    
-   Base URL configured per environment (dev/staging/production) in `AppConfig`
    

* * *

## Data Flow Example (Login)

```
LoginPage (widget)
  → ref.read(loginProvider.notifier).signIn(identity, password)
    → LoginNotifier validates fields
    → SignInUseCase.call(params)
      → AuthRepository.signIn(identity, password)
        → AuthRemoteDataSource.signIn() [Dio POST /auth/login]
        → SecureStorage.saveAccessToken(token)
    → state = LoginState(isSuccess: true)
  → ref.listen detects isSuccess
  → context.go('/home')
  → authProvider.onLoginSuccess() [background session verify]
```

* * *

## Offline-First Strategy

-   **Drift** (SQLite) for local data persistence
    
-   **SyncEngine** coordinates background sync between local DB and server
    
-   Auth tokens stored in **flutter\_secure\_storage** (AES on Android, Keychain on iOS)
    

* * *

## Code Generation

Run after any model/provider change:

```bash
dart run build_runner build
```

Generated files (`.g.dart`, `.freezed.dart`) are committed to the repo.

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Generator</p></th><th colspan="1" rowspan="1"><p>Purpose</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>riverpod_generator</code></p></td><td colspan="1" rowspan="1"><p>Provider boilerplate from <code>@riverpod</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>freezed</code></p></td><td colspan="1" rowspan="1"><p>Immutable data classes with copyWith</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>json_serializable</code></p></td><td colspan="1" rowspan="1"><p>JSON parsing</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>drift_dev</code></p></td><td colspan="1" rowspan="1"><p>Database schema + queries</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>retrofit_generator</code></p></td><td colspan="1" rowspan="1"><p>Type-safe API client</p></td></tr></tbody></table>
