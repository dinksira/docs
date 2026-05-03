---
title: Rbac Role
sidebar_label: Rbac Role
id: deltalabs--database/rbac-role-catalog/rbac-role
---

> Authorization is \*\*tenant-scoped\*\*: every decision is tied to an \`org\_id\`, an active \`org\_memberships\` row, and then roles and permissions resolved from Mongo (plus one relationship-based exception below).

```
### Storage model (three layers)

| Layer | Collection | Responsibility |
|-------|------------|------------------|
| Catalog | `role_definitions` | Defines each `role_key`: human `title`, optional `description`, `permissions[]`, and UI/ranking hints `membership_state`, `membership_rank` |
| Assignment | `role_bindings` | Grants a `role_key` to `subject_user_id` within `org_id` for a scope `(scope_type, scope_id)` |
| School membership | `school_memberships` | Per-user-per-school row with `role_keys[]` (e.g. `school_owner`) for school product flows; **not** the same document type as `role_bindings` |

`ScopeType` in code is `org` \| `school` \| `lab` \| `course` \| `global` (`authorization/schemas.py`). Bindings store whatever scope the app assigned when the binding was written.

### How `authorize()` uses the catalog

1. **Org membership gate** — `find_membership` requires `status: "active"`. No membership ⇒ deny with reason `missing_org_membership`.
2. **Scope chain** — `_scope_resolution_chain` builds scope pairs checked for bindings. For non-`org` scopes it queries both the requested scope (e.g. school id) and the parent org scope `(org, org_id)`, so org-wide roles still apply when checking school-scoped permissions.
3. **Effective permissions** — Union of all `permissions` arrays from every `role_definition` whose `role_key` appears in the user’s bindings for those scopes. Literal permission match **or** catalog entry containing `"*"` grants allow (`org_owner`).
4. **Relationship exception** — For permission `student:read_progress` with `resource_owner_user_id` set, allow if `relationships` contains `parent_of`, `guardian_of`, or `mentor_of` from the caller to that student (even when the parent role’s permissions alone would not cover the call).

`get_access_profile` uses the same definition merge to expose `role_keys`, flattened `permissions`, and a single `membership_state` chosen by highest `membership_rank` across bound roles (for feature gating and UI).

### Bootstrap and mutability

`AuthorizationService.bootstrap_defaults` ensures indexes, a default org (from settings), and **upserts** every row in `_DEFAULT_ROLES` in `authorization/service.py` into `role_definitions`. New environments get a full catalog without a separate migration file. Changing default permissions in code updates Mongo on next bootstrap; production should treat catalog edits as intentional releases.

### Default `role_key` values (seed)

`system_admin`, `org_owner`, `org_admin`, `finance_admin`, `school_admin`, `teacher`, `student`, `parent`, `lab_manager`, `lab_assistant`, `lab_member`. Exact permission strings live only in code and persisted documents — **always** read `_DEFAULT_ROLES` and `upsert_role_definition` for the authoritative list.

### School `role_keys` vs org RBAC

`school_owner` is written on `school_memberships` by the school domain; it is **not** part of `_DEFAULT_ROLES`. School APIs use membership + school logic; org-level `require_permission` / `authorize` use `role_bindings` + `role_definitions`. Product features that need one model to imply the other must bridge explicitly in application code.

### Related types

- `PermissionCheckRequest` — `org_id`, `permission`, `scope_type`, `scope_id`, optional `resource_owner_user_id`.
- `relationships` — social graph edges used for the student-progress exception, not for generic RBAC.
```
