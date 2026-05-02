---
title: Ws:Database Design:Schoolmarketplace
sidebar_label: Ws:Database Design:Schoolmarketplace
id: schoolmarketplace
---

```markdown
### `school_marketplace`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Prefix `mkt_` |
| `org_id`, `school_id`, `school_name`, `school_type` | string | |
| `owner_user_id`, `bidder_user_id` | string \| null | |
| `status` | string | e.g. `active`, `under_offer`, `sold`, `withdrawn` |
| `title`, `description` | string | |
| `price` | number | |
| `currency` | string | Uppercased |
| `created_at` | datetime | `updated_at` on updates |
```
