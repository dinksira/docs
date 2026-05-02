---
title: Ws:Database Design:Featurecatalog
sidebar_label: Ws:Database Design:Featurecatalog
id: featurecatalog
---

```markdown
### `feature_catalog`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | `feat_{feature_key}` |
| `feature_key` | string | Unique |
| `title`, `description` | string | |
| `enabled`, `beta` | bool | |
| `sort_order` | int | |
| `route_path` | string | |
| `capability_requirements` | object | Serialized capability model |
| `created_at`, `updated_at` | datetime | |
```
