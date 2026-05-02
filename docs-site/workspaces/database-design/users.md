---
title: Ws:Database Design:Users
sidebar_label: Ws:Database Design:Users
id: users
---

```markdown
### `users`

Canonical shape matches `UserRecord` in `app/domain/identity/schemas.py` and inserts in `identity/repository.py`.

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | User id (UUID) |
| `username` | string | Display / login |
| `username_normalized` | string | Lowercased; unique index |
| `email` | string \| null | |
| `email_normalized` | string \| null | Unique partial index when string |
| `phone_e164` | string \| null | Unique partial index when string |
| `is_active` | bool | Default true |
| `is_verified` | bool | Default false |
| `created_at`, `updated_at` | datetime | |
| `password_hash` | string | |
```
