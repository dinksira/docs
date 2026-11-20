---
title: Mongodb I
sidebar_label: Mongodb I
id: mongodb-i
---

> Indexes are created at runtime by each domain repository’s \`ensure\_indexes()\` (there is no checked-in migration script). Application startup or tests call these methods so indexes converge to the definitions below. \*\*Unique\*\* indexes enforce identity and prevent duplicate bindings; \*\*compound\*\* indexes match the sort fields used in list queries; \*\*partial\*\* indexes apply only when a filter matches; \*\*TTL\*\* indexes ask the server to delete documents after a datetime threshold.

```markdown
### How to read this section

- **Keys** list field order and sort direction (`1` = ascending, `-1` = descending).
- **Source file** is the single place to verify names if code and this doc drift.

### Identity — `deltalabs-backend/app/domain/identity/repository.py`

| Collection | Index name (or Mongo default) | Keys | Unique | TTL / partial | Role |
|------------|------------------------------|------|--------|---------------|------|
| `users` | `username_normalized_1` | `username_normalized` ↑ | yes | — | Fast login lookup; one account per normalized username |
| `users` | `email_normalized_1` | `email_normalized` ↑ | yes | only if value is BSON string | Optional emails remain sparse; avoids duplicate addresses |
| `users` | `phone_e164_1` | `phone_e164` ↑ | yes | only if value is BSON string | Same pattern for optional phone |
| `user_sessions` | (default) | `token_hash` ↑ | yes | — | Resolve session by presented token hash |
| `user_sessions` | (default) | `expires_at` ↑ | no | **TTL** `expireAfterSeconds=0` | Mongo removes the document when `expires_at` is in the past |

### Authorization — `app/domain/authorization/repository.py`

| Collection | Index name | Keys | Unique | Notes |
|------------|------------|------|--------|--------|
| `orgs` | (default) | `slug` ↑ | yes | Org slug is the tenant-facing identifier |
| `org_memberships` | `uq_org_membership` | `org_id`, `user_id` | yes | One membership row per user per org |
| `org_memberships` | `ix_org_membership_status` | `org_id`, `status` | no | Filters like “all active members in org” |
| `role_definitions` | `uq_role_definition` | `role_key` | yes | Catalog row is keyed by stable `role_key` |
| `role_bindings` | `uq_role_binding` | `org_id`, `subject_user_id`, `scope_type`, `scope_id`, `role_key` | yes | Same role cannot be bound twice for the same scope |
| `role_bindings` | `ix_role_binding_lookup` | `org_id`, `subject_user_id`, `scope_type`, `scope_id` | no | Loads all roles for a user in a scope (used with `$or` across resolved scopes) |
| `relationships` | `uq_relationship` | `org_id`, `relation`, `from_user_id`, `to_user_id` | yes | One edge per tuple (parent/mentor/guardian links) |

### School — `app/domain/school/repository.py`

| Collection | Index name | Keys | Unique | Partial | Notes |
|------------|------------|------|--------|---------|--------|
| `schools` | `ix_schools_org_archived_name` | `org_id`, `archived`, `name` | no | — | Listing schools within an org by archive bucket and name |
| `schools` | `uq_schools_org_slug` | `org_id`, `slug` | yes | — | Slug unique per org, not globally |
| `school_marketplace` | `ix_school_marketplace_org_created` | `org_id`, `created_at` | no | — | Time-ordered marketplace queries per tenant |
| `school_offers` | `ix_school_offers_org_status_updated` | `org_id`, `status`, `updated_at` | no | — | Inbox / pipeline views by status and recency |
| `school_memberships` | `uq_school_memberships_user_school` | `user_id`, `school_id` | yes | — | One membership document per user per school |
| `school_memberships` | `ix_school_memberships_school` | `school_id` | no | — | Enumerate members of a school |
| `school_workspace_items` | `ix_school_workspace_items_org_school_type_created` | `org_id`, `school_id`, `type`, `created_at` | no | — | Tree / listing queries scoped to a school |
| `school_workspace_items` | `uq_school_workspace_items_single_root` | `org_id`, `school_id`, `is_root` | yes | `is_root: true` | At most one root folder item per school |

### Content — `app/domain/content/repository.py`

| Collection | Index name | Keys | Notes |
|------------|------------|------|--------|
| `content_items` | `ix_content_items_visibility_created_id` | `visibility` ↑, `created_at` ↓, `_id` ↓ | Matches public feed pagination (cursor uses `created_at` + `_id`) |
| `content_items` | `ix_content_items_type_created` | `content_type` ↑, `created_at` ↓ | Filtered feeds by content type |

### Engagement — `app/domain/engagement/repository.py`

| Collection | Index name | Keys | Unique | Notes |
|------------|------------|------|--------|--------|
| `content_likes` | `uq_content_likes_content_user` | `content_id`, `user_id` | yes | One like row per user per item |
| `content_saves` | `uq_content_saves_content_user` | `content_id`, `user_id` | yes | Same for saves |
| `content_comments` | `ix_content_comments_content_created` | `content_id`, `created_at` | no | Thread comments in posting order |
| `content_shares` | `ix_content_shares_content_created` | `content_id`, `created_at` | no | Share history per item |
| `content_events` | `ix_content_events_user_created` | `user_id`, `created_at` | no | Per-user telemetry timelines |
| `content_events` | `ix_content_events_content_event_created` | `content_id`, `event`, `created_at` | no | Analytics grouped by item and event type |

### Media — `app/domain/media/repository.py`

| Collection | Index name | Keys | Notes |
|------------|------------|------|--------|
| `media_assets` | `ix_media_assets_org_created` | `org_id`, `created_at` ↓ | Tenant media library ordering |
| `media_assets` | `ix_media_assets_owner_created` | `owner_user_id`, `created_at` ↓ | User-owned assets |
| `media_assets` | `ix_media_assets_status_updated` | `status`, `updated_at` ↓ | Pipeline / ops dashboards by processing state |

### Library — `app/domain/library/repository.py`

| Collection | Index name | Keys | Unique | Notes |
|------------|------------|------|--------|--------|
| `feature_catalog` | `uq_feature_catalog_feature_key` | `feature_key` | yes | Stable feature id |
| `feature_catalog` | `ix_feature_catalog_enabled_sort` | `enabled`, `sort_order` | no | Matches `list_enabled_features` sort |

```
