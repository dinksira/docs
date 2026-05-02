---
title: Ws:Database Design:Mediaassets
sidebar_label: Ws:Database Design:Mediaassets
id: mediaassets
---

```markdown
### `media_assets`

Created on upload intent in `media/service.py`.

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Media id |
| `org_id`, `owner_user_id` | string | |
| `source_filename`, `source_content_type` | string | |
| `file_size_bytes` | int | |
| `caption` | string | |
| `hashtags` | string[] | |
| `visibility` | string | |
| `publish_to_feed` | bool | |
| `status` | string | e.g. `upload_pending`, … |
| `upload_object_key`, `upload_url_fallback` | string | |
| `hls_url`, `poster_url` | string \| null | |
| `duration_seconds` | number \| null | |
| `renditions` | array | |
| `created_at`, `updated_at` | datetime | |
```
