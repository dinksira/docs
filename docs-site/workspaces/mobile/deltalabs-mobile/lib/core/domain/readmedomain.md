---
title: Readmedomain
sidebar_label: Readmedomain
id: deltalabs-mobile/lib/core/domain/readmedomain
---

# lib/core/domain/

Base abstract classes that define the Clean Architecture contracts.

## entity.dart

`Entity` — base interface for all domain entities. Requires an `id` field.

## repository.dart

`Repository<T>` — base interface for all repositories. Defines the contract that data layer implementations must fulfill.

## use\_case.dart

`UseCase<Type, Params>` — base class for all use cases.

```dart
// Every use case follows this pattern:
class SignInUseCase extends UseCase<AuthSession, SignInParams> {
  @override
  Future<Either<Failure, AuthSession>> call(SignInParams params) {
    return repository.signIn(...);
  }
}
```

Use cases enforce single responsibility — one use case = one operation. They return `Either<Failure, T>` from the `dartz` package for functional error handling.
