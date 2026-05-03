---
title: Rbac Role
sidebar_label: Rbac Role
id: deltalabs--database/rbac-role-catalog/rbac-role
---

> Role-based access control is split between a \*\*catalog\*\* (what roles exist and which permissions they carry) and \*\*bindings\*\* (who has which role in what scope).

```markdown
| Concept | Storage | Notes |
|--------|---------|--------|
| Role catalog | `role_definitions` | One document per `role_key`; `permissions` is the allow-list; `title`, `description`, `membership_state`, `membership_rank` support UI and ordering |
| Scoped assignment | `role_bindings` | `subject_user_id` + `role_key` under `org_id`, with `scope_type` / `scope_id` (e.g. org-wide vs school-scoped values from the authz layer) |
| School-local roles | `school_memberships` | `role_keys[]` on the membership row; complements org-level catalog roles for school-specific duties |

Evaluating access in application code combines catalog definitions, bindings, and school membership role keys as appropriate to the route or resource.
```
