---
title: Ws:Database Design:Rolebindings
sidebar_label: Ws:Database Design:Rolebindings
id: rolebindings
---

```markdown
### `role_bindings`

| Field | Type | Notes |
|-------|------|--------|
| `org_id` | string | |
| `subject_user_id` | string | User receiving the role |
| `role_key` | string | |
| `scope_type` | string | e.g. `org`, school-scoped values from authz layer |
| `scope_id` | string | |
| `created_at`, `updated_at` | datetime | |
```
