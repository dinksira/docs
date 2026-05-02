---
title: Ws:Database Design:Schools
sidebar_label: Ws:Database Design:Schools
id: schools
---

```markdown
### `schools`

Written by `SchoolRepository.create_school` (`school/repository.py`).

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Prefix `school_` + hex |
| `org_id` | string | |
| `name`, `slug`, `school_type` | string | |
| `email` | string \| null | Normalized lower |
| `logo_url` | string \| null | |
| `custom_fields` | `{ key, value }[]` | |
| `onboarding_status` | string | e.g. `active`, `pending_partner_acceptance` |
| `partners`, `documents` | array | Structured per API / schema |
| `created_by_user_id` | string | |
| `archived` | bool | |
| `created_at`, `updated_at` | datetime | |
```
