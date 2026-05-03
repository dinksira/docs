---
title: Ws:Database Design:Overview
sidebar_label: Ws:Database Design:Overview
id: overview
---

```markdown
Delta Labs uses **two persistence layers**:

| Layer | Technology | Role |
|-------|------------|------|
| **Primary store** | MongoDB (`deltalabs`) | Long-lived documents: users, tenants, schools, marketplace, content, engagement, media pipeline, feature catalog |
| **Ephemeral / coordination** | Redis | Short-lived state (signup flows, OTP, recovery), idempotency keys, rate limits, feed worker streams and cursors |

**Tenancy:** Most business data is scoped by **`org_id`** (organization). Schools, marketplace, workspace, and many queries hang off an org. Users belong to orgs via **`org_memberships`**; school access is modeled separately in **`school_memberships`**.

**Identity and sessions:** **`users`** holds credentials and profile identifiers; **`user_sessions`** stores hashed API tokens with **`expires_at`** (Mongo TTL deletes expired rows).

**Authorization:** **`role_definitions`** is the RBAC catalog (role → permission strings). **`role_bindings`** assigns roles to users within an org and scope (`org`, `school`, etc.). **`relationships`** supports a small set of graph edges (e.g. parent → student) used beside RBAC. See [RBAC role catalog](#rbac-role-catalog).

**Product domains in Mongo:** **School** (`schools`, workspace, marketplace, offers, memberships), **Content** (`content_items` + engagement collections), **Media** (`media_assets` upload/transcode metadata), **Library** (`feature_catalog` for gated UI features).

**Indexes:** Created at app runtime via `ensure_indexes()` per domain repository — full inventory in [MongoDB indexes](#mongodb-indexes).

**Lifecycle:** Only **`user_sessions`** uses a Mongo TTL index; other retention (events volume, Redis TTLs, archival flags like `schools.archived`) is application- or ops-driven. See [Data lifecycle and retention](#data-lifecycle-and-retention).

**Where to read next:** Collection purposes in the table below; field-level tables in [Collection field reference](#collection-field-reference); Redis key patterns in [Redis usage](#redis-usage). **Drivers, env vars, and app startup** are in [Runtime connectivity and configuration](#runtime-connectivity-and-configuration).
```
