---
title: Ws:Database Design:Usersessions
sidebar_label: Ws:Database Design:Usersessions
id: usersessions
---

```markdown
### `user_sessions`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Session id |
| `user_id` | string | |
| `token_hash` | string | Unique index |
| `created_at`, `expires_at` | datetime | TTL index on `expires_at` (expire after 0) |
| `revoked_at` | datetime \| null | |
```
