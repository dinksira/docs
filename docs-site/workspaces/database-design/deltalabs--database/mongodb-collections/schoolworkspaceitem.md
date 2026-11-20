---
title: Schoolworkspaceitem
sidebar_label: Schoolworkspaceitem
id: schoolworkspaceitem
---

```markdown
### `school_workspace_items`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Prefix `wsi_` |
| `org_id`, `school_id` | string | |
| `parent_id` | string \| null | |
| `type` | string | folder, department, class, course, etc. |
| `title` | string | |
| `description` | string \| null | |
| `metadata` | object | |
| `is_root` | bool | One root per school (partial unique index) |
| `created_at`, `updated_at` | datetime | |
```
