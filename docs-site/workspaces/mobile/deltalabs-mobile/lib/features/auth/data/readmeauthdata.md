---
title: Readmeauthdata
sidebar_label: Readmeauthdata
id: deltalabs-mobile/lib/features/auth/data/readmeauthdata
---

# lib/features/auth/data/

Data layer for authentication.

## data\_sources/auth\_remote\_data\_source.dart

Calls the backend auth API:

-   `signIn(identity, password)` → `POST /auth/login` → returns `AuthSession`
    
-   `signOut(token)` → `POST /auth/logout`
    
-   `getSession(token)` → `GET /auth/session` → returns `AuthUser`
    

## data\_sources/register\_remote\_data\_source.dart

Calls the multi-step signup API:

-   `stepIdentity(username)` → `POST /auth/signup/step/identity`
    
-   `stepContact(flowId, email, phone)` → `POST /auth/signup/step/contact`
    
-   `sendVerification(channel, destination)` → `POST /auth/verification/send`
    
-   `verifyCode(verificationId, code)` → `POST /auth/verification/verify`
    
-   `stepVerification(flowId, verificationId)` → `POST /auth/signup/step/verification`
    
-   `stepDob(flowId, dateOfBirth)` → `POST /auth/signup/step/dob`
    
-   `complete(flowId, password)` → `POST /auth/signup/complete`
    

## models/user\_model.dart

`UserModel` — Freezed data class for JSON parsing. Has `toDomain()` to convert to the domain `User` entity.

## repositories/auth\_repository\_impl.dart

Implements `AuthRepository`:

-   Calls remote data source
    
-   Persists token to `SecureStorage` on login
    
-   Clears storage on logout
    
-   Emits auth state changes via `BehaviorSubject`
