---
title: Ws:Database Design:Schooloffers
sidebar_label: Ws:Database Design:Schooloffers
id: schooloffers
---

```markdown
### `school_offers`

| Field | Type | Notes |
|-------|------|--------|
| `_id` | string | Prefix `offer_` |
| `org_id`, `school_id`, `school_name` | string | |
| `status` | string | requested, approved, amendment, rejected, … |
| `negotiation_turn` | string | e.g. `sender`, `recipient` |
| `requested_at`, `updated_at` | datetime | |
| `sender_user_id`, `sender_email` | string \| null | |
| `recipient_email` | string \| null | |
| `party_full_name`, `party_email` | string \| null | |
| `ownership_percentage` | number \| null | |
| `share_accesses` | array \| null | |
| `listing_id` | string \| null | Marketplace link |
| `offered_price`, `offered_currency` | number / string \| null | |
| `note` | string \| null | |
| `offer_kind` | string \| null | e.g. `marketplace_transfer` |
| `amendment_rounds` | int | Set for marketplace transfer |
| `expires_at` | datetime \| null | |
| `shortlisted` | bool | Marketplace shortlist |
| `amendment_data` | object \| null | |
```
