---
title: Readmemd
sidebar_label: Readmemd
id: readmemd
---

# lib/features/feed/

TikTok-style **content feed** — vertical video on the **Video** tab, filtered feed on **Custom** tab, engagement (like, comment, save, share). Hosted inside `shell/`; not a standalone bottom-nav route.

**Status:** ✅ Implemented (video + custom tab + engagement). Audio / AI / Simulation tabs are shell placeholders.

## User flows

### Video tab (default)

`MainShellPage` → `FeedPage` → `feedProvider.loadInitial()` → `GET /feed?content_type=video` → `PageView` of `FeedVideoSlide`

-   Swipe up/down between clips; prefetches when near end (`loadMore`).
    
-   Tap video → pause + `FeedPlayPauseOverlay`.
    
-   Like / comment / save / share → `FeedNotifier` → repository → `POST /feed/{id}/…` (requires auth via `FeedAuthGateDialog`).
    

### Custom tab

`CustomFeedTabPage` → `customFeedTabProvider` → `GET /me/feed/custom-tab`

-   If not configured: setup UI → `CustomFeedFilterSheet` → `PUT /me/feed/custom-tab` → `customTabFeedProvider` → `GET /feed` with `FeedQueryFilters`.
    

### Demo fallback

If `GET /feed` fails or returns empty items, `feedProvider` loads `data/demo/demo_feed_items.dart` so UX can be tested offline.

## API summary

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Action</p></th><th colspan="1" rowspan="1"><p>Endpoint</p></th></tr><tr><td colspan="1" rowspan="1"><p>List feed</p></td><td colspan="1" rowspan="1"><p><code>GET /feed</code> (+ cursor, filters)</p></td></tr><tr><td colspan="1" rowspan="1"><p>Like / save / share</p></td><td colspan="1" rowspan="1"><p><code>POST /feed/{id}/like</code>, <code>save</code>, <code>share</code></p></td></tr><tr><td colspan="1" rowspan="1"><p>Comments</p></td><td colspan="1" rowspan="1"><p><code>GET/POST /feed/{id}/comments</code></p></td></tr><tr><td colspan="1" rowspan="1"><p>Custom tab</p></td><td colspan="1" rowspan="1"><p><code>GET/PUT /me/feed/custom-tab</code></p></td></tr></tbody></table>

## Layers

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Layer</p></th><th colspan="1" rowspan="1"><p>Doc</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>data/</code></p></td><td colspan="1" rowspan="1"><p><a target="_blank" rel="noopener noreferrer nofollow" href="./data/README.md">README</a></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>domain/</code></p></td><td colspan="1" rowspan="1"><p><a target="_blank" rel="noopener noreferrer nofollow" href="./domain/README.md">README</a></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>presentation/</code></p></td><td colspan="1" rowspan="1"><p><a target="_blank" rel="noopener noreferrer nofollow" href="./presentation/README.md">README</a></p></td></tr></tbody></table>

## Diagrams (Mermaid)

`deltalabs-mobile-docs/feed-page/` — system flow, backend, component hierarchy.
