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

```markdown
## Runtime connectivity and configuration

Low-level view: **which databases**, **which Python clients**, **which environment variables**, and **when connections are opened**.

### Where settings live

| Piece | Location |
|-------|----------|
| All tunables | `deltalabs-backend/app/core/config.py` — class `Settings` (Pydantic `BaseSettings`) |
| Cached accessor | `get_settings()` — `@lru_cache` process singleton |
| Env file | `.env` in the backend working directory (see `SettingsConfigDict` `env_file=".env"`) |
| Example copy | `deltalabs-backend/.env.example` |

Environment variable names are **case-insensitive** to pydantic-settings. Underscores in env map to the `snake_case` fields (e.g. `MONGODB_URI` → `mongodb_uri`).

### MongoDB

| Item | Detail |
|------|--------|
| **Engine** | MongoDB (document database); no SQL migrations in-repo |
| **Python driver stack** | **Motor** — `AsyncIOMotorClient` / `AsyncIOMotorDatabase` (`motor.motor_asyncio`) wrapping PyMongo, async-first |
| **Connection module** | `deltalabs-backend/app/infra/database.py` |
| **Startup / shutdown** | `app/main.py` FastAPI `lifespan`: `connect_mongodb()` on startup; `disconnect_mongodb()` on shutdown (after Redis is closed) |
| **Client shape** | One **global** Motor client per process; `get_database()` indexes it with `[settings.mongodb_db_name]` so all repositories share one pool |

**Environment variables (Mongo):**

| Variable | Default | Purpose |
|----------|---------|---------|
| `MONGODB_URI` | `mongodb://localhost:27017` | Full connection string (Atlas, replica set, TLS query params all go here) |
| `MONGODB_DB_NAME` | `deltalabs` | Logical database name within the cluster |
| `MONGODB_MAX_POOL_SIZE` | `100` | `maxPoolSize` on the client |
| `MONGODB_MIN_POOL_SIZE` | `0` | `minPoolSize` |
| `MONGODB_SERVER_SELECTION_TIMEOUT_MS` | `5000` | How long to wait when picking a server before error |

Repositories receive the database handle from FastAPI dependencies (`get_db` yields `get_database()`).
```
