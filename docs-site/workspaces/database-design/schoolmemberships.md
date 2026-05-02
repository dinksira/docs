---
title: Ws:Database Design:Schoolmemberships
sidebar_label: Ws:Database Design:Schoolmemberships
id: schoolmemberships
---

```markdown
### `school_memberships`

Upserted by `user_id` + `school_id` (`upsert_school_membership`).

| Field | Type | Notes |
|-------|------|--------|
| `user_id`, `school_id` | string | Logical key |
| `org_id` | string | |
| `role_keys` | string[] | e.g. `school_owner` |
| `status` | string | `active`, `inactive` |
| `created_at`, `updated_at` | datetime | |
```
