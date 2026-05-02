---
title: Ws:Database Design:Contentlikes
sidebar_label: Ws:Database Design:Contentlikes
id: contentlikes
---

```markdown
### `content_likes` / `content_saves`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | UUID |
| `content_id`, `user_id` | string | Unique compound index |
```
