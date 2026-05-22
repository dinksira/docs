---
title: Readmemd
sidebar_label: Readmemd
id: deltalabs-mobile/lib/features/feed/domain/readmemd
---

# lib/features/feed/domain/

Domain layer — feed entities and repository contract. No Flutter imports.

## entities/feed\_item.dart

`FeedItem` extends `Entity` — one clip in the vertical feed:

-   Identity: `id`, `title`, `type` (`FeedItemType`: video, etc.)
    
-   Creator: `authorId`, `authorName`, `authorAvatarUrl`
    
-   Media: `thumbnailUrl`, `mediaUrl`, `duration`
    
-   Social: `likeCount`, `commentCount`, `shareCount`, `viewCount`, `isLiked`, `isSaved`
    
-   Presentation: `description`, `soundLabel`, `hashtags`, `publishedAt`
    

UI mutates counts locally after engagement API success (via `FeedNotifier._updateItem`).

## entities/feed\_page.dart

`FeedPage` — one page of results: `items`, `nextCursor`, `hasMore`.

## entities/feed\_comment.dart

`FeedComment` — comment thread row for bottom sheet.

## entities/feed\_custom\_tab.dart

`FeedCustomTab` — persisted user tab: custom **label** + filter criteria used to build `FeedQueryFilters`.

## entities/feed\_query\_filters.dart

`FeedQueryFilters` — maps to `GET /feed` query parameters (`content_type`, `course_category`, `min_duration_s`, `max_duration_s`, etc.). `empty` constant for unfiltered video tab.

## entities/engagement\_result.dart

-   `EngagementResult` — after like/save toggle (updated counts + flags).
    
-   `ShareResult` — share recorded.
    
-   `CommentPostResult` — new comment id + updated comment count.
    

## repositories/feed\_repository.dart

`FeedRepository` (abstract):

-   `getFeed(CursorParams, {contentType, filters})` → `Either<Failure, FeedPage>`
    
-   `toggleLike`, `toggleSave`, `recordShare`, `fetchComments`, `postComment`
    

Implemented in `data/repositories/feed_repository_impl.dart`.
