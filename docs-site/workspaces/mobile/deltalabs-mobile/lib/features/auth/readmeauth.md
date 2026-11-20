---
title: Readmeauth
sidebar_label: Readmeauth
id: readmeauth
---

# lib/features/auth/

Authentication feature — fully implemented end-to-end.

## Flows

### Login

`login_page.dart` → `LoginNotifier` → `SignInUseCase` → `AuthRepositoryImpl` → `POST /auth/login`

### Registration (multi-step)

```
register_step1_page  →  POST /auth/signup/step/identity   (username)
register_step2_page  →  POST /auth/signup/step/contact    (email + phone)
                     →  POST /auth/verification/send      (sends OTP email)
register_otp_page    →  POST /auth/verification/verify    (verify code)
                     →  POST /auth/signup/step/verification
register_dob_page    →  POST /auth/signup/step/dob        (date of birth)
register_password    →  POST /auth/signup/complete        (set password → get token)
```

The `flow_id` is persisted in `RegisterState` across all steps.

### Password Recovery

```
forgot_password_page →  POST /auth/recover/request   (sends code to email)
forgot_otp_page      →  POST /auth/recover/verify    (verify code → get reset_token)
reset_password_page  →  POST /auth/recover/reset     (set new password)
```

## State Management

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Provider</p></th><th colspan="1" rowspan="1"><p>Purpose</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>authProvider</code> (keepAlive)</p></td><td colspan="1" rowspan="1"><p>Global session — user object or null</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>loginProvider</code></p></td><td colspan="1" rowspan="1"><p>Login form state, loading, errors</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>registerProvider</code></p></td><td colspan="1" rowspan="1"><p>Multi-step registration state, flow_id</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>recoverProvider</code></p></td><td colspan="1" rowspan="1"><p>Password recovery state, recover_id, reset_token</p></td></tr></tbody></table>
