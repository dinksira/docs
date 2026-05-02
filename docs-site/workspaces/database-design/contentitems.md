---
title: Ws:Database Design:Contentitems
sidebar_label: Ws:Database Design:Contentitems
id: contentitems
---

```markdown
### `content_items`

Public feed and media-published items. Demo seed in `content/repository.py`; public projection in `content/schemas.py` (`FeedItemPublic`).

Typical fields: `_id`, `visibility`, `content_type`, `created_at`, `updated_at`, `video_src`, `media_tone`, `caption`, `hashtags`, `pdf_label`, optional denormalized counters such as `like_count`.
```
