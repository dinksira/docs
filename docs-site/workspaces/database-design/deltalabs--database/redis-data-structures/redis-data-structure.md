---
title: Redis Data Structure
sidebar_label: Redis Data Structure
id: redis-data-structure
---

> Redis is not a document store; keys depend on features

```markdown
### Redis

| Item | Detail |
|------|--------|
| **Engine** | Redis (in-memory with optional persistence, depending on server config) |
| **Python client** | **`redis.asyncio`** — `redis.from_url()` (`deltalabs-backend/app/infra/redis_client.py`) |
| **Decoding** | `encoding="utf-8"`, `decode_responses=True` — command results that are Redis strings become Python `str` |
| **Startup / shutdown** | `connect_redis()` on startup; `disconnect_redis()` (`aclose`) runs **before** Mongo disconnect on app shutdown |

**Environment variables (Redis):**

| Variable | Default | Purpose |
|----------|---------|---------|
| `REDIS_URL` | `redis://localhost:6379/0` | URL including host, port, optional password (`redis://:pass@host:6379/0`), and **DB index** (`/0`) |
| `REDIS_MAX_CONNECTIONS` | `50` | Async connection pool size |

### Other settings that touch “data” paths (Redis-backed)

Configured on the same `Settings` object; full list in `config.py`. Examples:

| Variable | Role |
|----------|------|
| `IDEMPOTENCY_HEADER_NAME`, `IDEMPOTENCY_TTL_SECONDS` | Header for idempotency keys and Redis record lifetime |
| `FEED_ENGAGEMENT_STREAM_KEY`, `FEED_ENGAGEMENT_STREAM_MAXLEN` | Primary Redis Stream for feed worker input |
| `FEED_ENGAGEMENT_DEAD_LETTER_STREAM_KEY`, `…_MAXLEN` | Failed events stream |
| `FEED_ENGAGEMENT_PUBSUB_CHANNEL_PREFIX` | Pub/Sub prefix for clip channels |
| `RATE_LIMIT_*`, `TRUST_X_FORWARDED_FOR` | Rate limit storage uses Redis where implemented |

See [Redis usage](#redis-usage) for key naming by feature, not for connection strings.

```
