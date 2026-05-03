---
title: Mongodb I
sidebar_label: Mongodb I
id: deltalabs--database/index-catalog/mongodb-i
---

> Indexes are ensured at runtime in each repository’s \`ensure\_indexes()\` method (not from checked-in SQL). Refer to these files for exact names and partial filters:

```markdown
- `app/domain/identity/repository.py` — `users`, `user_sessions`
- `app/domain/authorization/repository.py` — `orgs`, `org_memberships`, `role_definitions`, `role_bindings`, `relationships`
- `app/domain/school/repository.py` — `schools`, `school_marketplace`, `school_offers`, `school_memberships`, `school_workspace_items`
- `app/domain/content/repository.py` — `content_items`
- `app/domain/engagement/repository.py` — engagement collections + `content_events`
- `app/domain/media/repository.py` — `media_assets`
- `app/domain/library/repository.py` — `feature_catalog`
```
