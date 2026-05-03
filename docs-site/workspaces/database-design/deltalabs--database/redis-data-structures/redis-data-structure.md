---
title: Redis Data Structure
sidebar_label: Redis Data Structure
id: deltalabs--database/redis-data-structures/redis-data-structure
---

> Redis is not a document store; keys depend on features

```markdown
| Area | Pattern / keys | Code reference |
|------|----------------|----------------|
| Signup multi-step flow | `signup:flow:{flow_id}` | `identity/signup_flow_service.py` |
| OTP verification | Verification id keys | `identity/verification_service.py` |
| Account recovery | Recover id keys | `identity/recover_service.py` |
| Idempotency | Configurable TTL | `core/idempotency.py`, `idempotency_ttl_seconds` in config |
| Feed worker | Streams (defaults `feed:engagement:events`, `feed:engagement:dead_letter`), pub/sub `feed:clip:*`, worker cursor keys | `core/config.py`, `jobs/workers.py`, `engagement/queue.py` |
| Rate limiting | Per-IP / feature keys | `core/rate_limit.py` and related |

Stream key names and TTLs are configurable via `deltalabs-backend/app/core/config.py`.
```
