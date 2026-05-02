---
title: Ws:Database Design:Orgmemberships
sidebar_label: Ws:Database Design:Orgmemberships
id: orgmemberships
---

```markdown
### `org_memberships`

| Field | Type | Notes |
|-------|------|--------|
| `org_id`, `user_id` | string | Composite uniqueness |
| `status` | string | e.g. `active` |
| `created_at`, `updated_at` | datetime | Upsert via `$setOnInsert` / `$set` |
```
