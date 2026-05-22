---
title: Readmemd
sidebar_label: Readmemd
id: deltalabs-mobile/lib/features/feed/data/readmemd
---

# lib/features/feed/data/

Data layer — HTTP calls, JSON models, repository implementation, demo clips.

## data\_sources/feed\_remote\_data\_source.dart

`FeedRemoteDataSource` (abstract) / `FeedRemoteDataSourceImpl`

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Method</p></th><th colspan="1" rowspan="1"><p>HTTP</p></th><th colspan="1" rowspan="1"><p>Notes</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>fetchFeed</code></p></td><td colspan="1" rowspan="1"><p><code>GET /feed</code></p></td><td colspan="1" rowspan="1"><p>Query: <code>limit</code>, <code>cursor</code>, <code>content_type</code>, plus filter params from <code>FeedQueryFilters</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>toggleLike</code></p></td><td colspan="1" rowspan="1"><p><code>POST /feed/{id}/like</code></p></td><td colspan="1" rowspan="1"><p>Sends <code>Idempotency-Key</code> header</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>toggleSave</code></p></td><td colspan="1" rowspan="1"><p><code>POST /feed/{id}/save</code></p></td><td colspan="1" rowspan="1"><p>Idempotency header</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>recordShare</code></p></td><td colspan="1" rowspan="1"><p><code>POST /feed/{id}/share</code></p></td><td colspan="1" rowspan="1"><p>Returns share result payload</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>fetchComments</code></p></td><td colspan="1" rowspan="1"><p><code>GET /feed/{id}/comments</code></p></td><td colspan="1" rowspan="1"><p><code>limit</code> query param</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>postComment</code></p></td><td colspan="1" rowspan="1"><p><code>POST /feed/{id}/comment</code></p></td><td colspan="1" rowspan="1"><p>Body: comment text</p></td></tr></tbody></table>

Uses shared `ApiClient` (Dio, base `/v1`).

## data\_sources/feed\_custom\_tab\_remote\_data\_source.dart

`FeedCustomTabRemoteDataSource`

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Method</p></th><th colspan="1" rowspan="1"><p>HTTP</p></th></tr><tr><td colspan="1" rowspan="1"><p>Load saved tab</p></td><td colspan="1" rowspan="1"><p><code>GET /me/feed/custom-tab</code></p></td></tr><tr><td colspan="1" rowspan="1"><p>Save label + filters</p></td><td colspan="1" rowspan="1"><p><code>PUT /me/feed/custom-tab</code></p></td></tr></tbody></table>

Maps JSON to `FeedCustomTabModel`.

## models/feed\_page\_model.dart

`FeedPageModel` — parses paginated feed response: list of items + `next_cursor` / has-more flags. Converts to domain `FeedPage`.

## models/feed\_item\_model.dart

`FeedItemModel` — single clip/document from API: ids, title, media URLs, counts, author fields, content type. `toEntity()` → `FeedItem`.

## models/feed\_comment\_model.dart

`FeedCommentModel` — comment row (id, body, author, created\_at). `toEntity()` → `FeedComment`.

## models/engagement\_response\_model.dart

`EngagementResponseModel` — like/save toggle response (updated counts, `is_liked` / `is_saved`). Maps to `EngagementResult`.

## models/feed\_custom\_tab\_model.dart

`FeedCustomTabModel` — user’s custom tab: display label, filter fields (content type, course category, duration range, etc.). `toEntity()` → `FeedCustomTab`.

## repositories/feed\_repository\_impl.dart

`FeedRepositoryImpl` implements `FeedRepository`:

-   Delegates to `FeedRemoteDataSource`.
    
-   Wraps errors with `ErrorHandler.fromObject` → `Failure`.
    
-   Returns `Either<Failure, T>` for feed page and engagement operations (domain contract).
    

## demo/demo\_feed\_items.dart

`demoFeedItems` — hard-coded `FeedItem` list used when the network returns nothing or errors. Keeps Video tab usable without backend data.

## utils/feed\_media\_url.dart

Helpers to resolve playable **video URL** from API fields (absolute URL vs path joined to CDN/base). Used by `FeedVideoSlide` when initializing the player.
