---
title: General Folder Structure Explanation
sidebar_label: General Folder Structure Explanation
id: deltalabsfrontend/general-folder-structure-explanation
---

## Routing

-   `src/app/(public)/` — Marketing and auth entry (`/`, `/login`, `/signup`, `/terms`, `/privacy`). Uses `PublicLayoutShell` + `TopNav`.
    
-   `src/app/(app)/` — Signed-in shell (`AppShell`): `/dashboard`, `/features`, `/features/school` (School workspace: screens in `modules/School/views/`, composites in `components/features/school/`), `/enrolled-courses`.
    
-   **Middleware** (`src/middleware.ts`) — Cookie-based redirects for protected vs auth pages.
    

Route files stay **thin**: they import a single view from `src/modules/<Module>/views/`.

## Modules (domain folders)

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Module</p></th><th colspan="1" rowspan="1"><p>Responsibility</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>Auth</code></p></td><td colspan="1" rowspan="1"><p>Login, signup, recovery views; mock <code>authApi</code>; auth mutations &amp; types.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>Marketing</code></p></td><td colspan="1" rowspan="1"><p>Legal / static marketing views (terms, privacy) only.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>Features</code></p></td><td colspan="1" rowspan="1"><p>Authenticated features hub (workspace grid + tabs).</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>Dashboard</code></p></td><td colspan="1" rowspan="1"><p>App dashboard placeholder until domain dashboards land.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>Feed</code></p></td><td colspan="1" rowspan="1"><p>Public <strong>explorer</strong> surface: video <code>LandingPageView</code>, module hub shells (<code>/audio</code>, <code>/ai</code>, <code>/simulation</code>, <code>/explore</code>) sharing <code>FeedExplorerShell</code> + <code>FeedSearchInput</code> / <code>FeedFilterPanel</code>; mock clip data; <code>useFeedClips</code> / <code>useFeedComments</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>School</code></p></td><td colspan="1" rowspan="1"><p>School workspace under <code>/features/school</code>: <code>views/</code> compose <code>components/features/school/</code> (rail, shell, cards, tables — same pattern as <code>feed/</code>); <code>modules/School/types/</code> for route query guards. Future domain <strong>features</strong> (e.g. enrollment, roster) stay in <code>modules/School/</code> as <code>api/</code>, <code>hooks/</code>, etc.</p></td></tr></tbody></table>

Other scaffold modules under `src/modules/*` (Course, …) follow the same layout as they are implemented.

## Cross-cutting UI

-   `src/components/theme/` — Design-system primitives (Button, Input, Typography, …).
    
-   `src/components/features/` — Shared composites (e.g. `feed/*`, `auth/*`, `school/*`) used by one or more modules.
    
-   `src/components/navigation/` — Shells, `TopNav`, `AppShell`.
    

## Responsiveness (mobile-first + layout tokens)

-   **Order:** tokens → theme → features → shells → module views (see `docs/frontend-responsiveness-standard.md`).
    
-   **Layout constants** (`--dl-layout-*`) live in `src/styles/design-tokens.css`; reuse them instead of copying pixel/rem values into multiple components.
    

## State

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Concern</p></th><th colspan="1" rowspan="1"><p>Tool</p></th></tr><tr><td colspan="1" rowspan="1"><p>Server / cached API</p></td><td colspan="1" rowspan="1"><p><strong>TanStack React Query</strong> (<code>QueryProvider</code> in <code>Root</code>). Prefer <code>useQuery</code> / <code>useMutation</code> in <code>modules/&lt;X&gt;/hooks</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Global client UI</p></td><td colspan="1" rowspan="1"><p><strong>Redux Toolkit</strong> (<code>src/store/</code>) — start with focused slices (e.g. <code>feedUi</code> for comment sidebar).</p></td></tr><tr><td colspan="1" rowspan="1"><p>Auth session</p></td><td colspan="1" rowspan="1"><p><code>AuthSessionProvider</code> (<code>src/contexts/AuthSession_Context.tsx</code>).</p></td></tr><tr><td colspan="1" rowspan="1"><p>Theme</p></td><td colspan="1" rowspan="1"><p><code>ThemeProvider</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Local / screen scope</p></td><td colspan="1" rowspan="1"><p><code>useState</code><strong> / </strong><code>useRef</code> in views and leaf components.</p></td></tr></tbody></table>

**Rule of thumb:** API data → Query. Cross-route or multi-component client rules → Redux slice. Everything else → local state.

## Redux store

-   `src/store/store.ts` — `configureStore`.
    
-   `src/store/*Slice.ts` — Feature slices (`createSlice`).
    
-   `src/store/selectors.ts` — Typed selectors using `RootState`.
    
-   `src/store/hooks.ts` — `useAppDispatch`, `useAppSelector`.
    
-   `Root` wraps the app with `<Provider store={store}>` (client).
    

## Feed data (until API exists)

-   Clips: `modules/Feed/data/mockVideoFeed.ts` + `useFeedClips`.
    
-   Comments: `modules/Feed/data/mockComments.ts` + `useFeedComments(clipId)`.
    
-   Demo presenter (creator row): `modules/Feed/data/landingFeedPresenter.ts`.
    

Swap `queryFn` implementations later; keep hook names stable so views change minimally.
