---
title: Readmemd
sidebar_label: Readmemd
id: readmemd
---

# lib/features/shell/

**Post-login landing host** — TikTok-style top chrome over full-screen feed, or column layout for the Features hub. No `data/` or `domain/` layer (presentation only).

**Status:** ✅ Implemented

## Route

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Path</p></th><th colspan="1" rowspan="1"><p>Widget</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>/feed</code></p></td><td colspan="1" rowspan="1"><p><code>MainShellPage</code></p></td></tr></tbody></table>

Set as default after login in `bootstrap.dart` / `app_router`.

## Surfaces

`ShellSurface` (enum on `main_shell_page.dart`):

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Surface</p></th><th colspan="1" rowspan="1"><p>UI</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>feed</code></p></td><td colspan="1" rowspan="1"><p><code>Stack</code>: full-screen <code>IndexedStack</code> of tab bodies + <code>MainTopChrome</code> positioned on top</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features</code></p></td><td colspan="1" rowspan="1"><p><code>Column</code>: <code>MainTopChrome</code> + expanded <code>FeaturesHubPage</code> (from <code>features/features/</code>)</p></td></tr></tbody></table>

## Top tabs (`FeedTopTab`)

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Tab</p></th><th colspan="1" rowspan="1"><p>Body widget</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>video</code></p></td><td colspan="1" rowspan="1"><p><code>feed/FeedPage</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>audio</code>, <code>ai</code>, <code>simulation</code></p></td><td colspan="1" rowspan="1"><p><code>FeedTabPlaceholderPage</code> (“coming soon”)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>custom</code></p></td><td colspan="1" rowspan="1"><p><code>feed/CustomFeedTabPage</code></p></td></tr></tbody></table>

Custom tab label in chrome comes from `customFeedTabLabelProvider` (feed feature).

## Chrome actions

-   **Tab change** — stays on feed surface, switches `IndexedStack` index.
    
-   **Search** — feed surface → `context.push(/search)`; features surface → `/features/search`.
    
-   **Features switch** — toggles `ShellSurface` feed ↔ features.
    

## presentation/

All shell UI: [presentation/README.md](./presentation/README.md)
