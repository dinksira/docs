---
title: Readmeauthpresentaion
sidebar_label: Readmeauthpresentaion
id: deltalabs-mobile/lib/features/auth/presentation/readmeauthpresentaion
---

# lib/features/auth/presentation/

UI and state management for authentication.

## pages/

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Screen</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>login_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Log in</p></td><td colspan="1" rowspan="1"><p>Identity + password, error banner, loading state</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>register_step1_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Register</p></td><td colspan="1" rowspan="1"><p>Username input</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>register_step2_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Register</p></td><td colspan="1" rowspan="1"><p>Email + phone, sends OTP</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>register_otp_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Verify</p></td><td colspan="1" rowspan="1"><p>OTP code input, countdown timer, resend</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>register_dob_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Register</p></td><td colspan="1" rowspan="1"><p>Date of birth dropdowns</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>register_password_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Register</p></td><td colspan="1" rowspan="1"><p>Password + confirm, completes signup</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>forgot_password_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Recover</p></td><td colspan="1" rowspan="1"><p>Identity input, requests recovery code</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>forgot_otp_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Verify</p></td><td colspan="1" rowspan="1"><p>Recovery code input</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>reset_password_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Recover</p></td><td colspan="1" rowspan="1"><p>New password + confirm</p></td></tr></tbody></table>

All pages are `HookConsumerWidget` — they use both `flutter_hooks` (for controllers/timers) and Riverpod (for state).

## providers/

### auth\_provider.dart

-   `authProvider` (keepAlive) — `AuthNotifier` holds `AsyncValue<AuthUser?>`
    
-   `loginProvider` — `LoginNotifier` holds `LoginState` (loading, errors, isSuccess)
    
-   `isAuthenticatedProvider` — derived bool from `authProvider`
    

### register\_provider.dart

-   `registerProvider` — `RegisterNotifier` holds `RegisterState`
    
-   Persists `flowId` and `verificationId` across all registration steps
    
-   Full client-side validation matching backend password policy
    

### recover\_provider.dart

-   `recoverProvider` — `RecoverNotifier` holds `RecoverState`
    
-   Persists `recoverId` and `resetToken` across recovery steps
