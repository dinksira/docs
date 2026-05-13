---
title: Readmeauthdomain
sidebar_label: Readmeauthdomain
id: deltalabs-mobile/lib/features/auth/domain/readmeauthdomain
---

# lib/features/auth/domain/

Domain layer — pure business logic, no Flutter or external dependencies.

## entities/

### auth\_repository.dart (AuthSession, AuthUser)

-   `AuthSession` — issued on login: `accessToken`, `sessionId`, `userId`, `expiresAt`, `user`
    
-   `AuthUser` — public user data: `userId`, `username`, `email`, `phoneE164`, `isVerified`
    
-   `AuthState` — sealed class: `AuthAuthenticated`, `AuthUnauthenticated`, `AuthLoading`
    

## repositories/auth\_repository.dart

Abstract contract:

```dart
abstract class AuthRepository {
  Future<Either<Failure, AuthSession>> signIn({...});
  Future<Either<Failure, void>> signOut();
  Future<Either<Failure, AuthUser?>> getCurrentUser();
  Future<bool> isAuthenticated();
  Stream<AuthState> get authStateStream;
}
```

## use\_cases/sign\_in\_use\_case.dart

`SignInUseCase` — takes `SignInParams(identity, password)`, delegates to `AuthRepository.signIn()`.

Returns `Either<Failure, AuthSession>` — left is a typed failure, right is success.
