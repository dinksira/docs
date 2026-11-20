---
title: Readmemd
sidebar_label: Readmemd
id: readmemd
---

# lib/features/features/presentation/

Hub UI, search, and Riverpod state.

## pages/

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Screen</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>features_hub_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Features grid</p></td><td colspan="1" rowspan="1"><p><code>ConsumerStatefulWidget</code>. <code>ReorderableWrap</code> of <code>FeatureCardTile</code> (long-press drag). FAB to restore hidden cards. Menu per card (hide, rename). Error UI via <code>FeaturesHubErrorView</code> (load vs save errors). Tap → <code>openFeatureWorkspace</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features_search_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Feature search</p></td><td colspan="1" rowspan="1"><p><code>HookConsumerWidget</code>. Search field filters hub cards; tap result → workspace navigation (same as hub).</p></td></tr></tbody></table>

## widgets/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>feature_card_tile.dart</code></p></td><td colspan="1" rowspan="1"><p>Card UI: icon/ colors from <code>FeatureVisuals</code>, title, disabled styling, menu anchor.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>feature_card_menu_popup.dart</code></p></td><td colspan="1" rowspan="1"><p>Anchored popup (not bottom sheet): hide card, rename label.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features_hub_error_view.dart</code></p></td><td colspan="1" rowspan="1"><p>Custom error panel with retry for failed catalog/layout load.</p></td></tr></tbody></table>

## constants/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>feature_visuals.dart</code></p></td><td colspan="1" rowspan="1"><p><code>FeatureVisuals.forKey(featureKey)</code> — icon + chip colors per known feature keys.</p></td></tr></tbody></table>

## models/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>feature_card_ui.dart</code></p></td><td colspan="1" rowspan="1"><p>View model merging <code>Feature</code> + layout title + <code>disabled</code> flag + index metadata for reorder.</p></td></tr></tbody></table>

## providers/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>features_repository_provider.dart</code></p></td><td colspan="1" rowspan="1"><p><code>Provider&lt;FeaturesRepository&gt;</code> from <code>ServiceLocator</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features_hub_provider.dart</code></p></td><td colspan="1" rowspan="1"><p><code>FeaturesHubNotifier</code> / <code>FeaturesHubState</code>: <code>load</code>, <code>saveLayout</code>, <code>hideCard</code>, <code>renameCard</code>, <code>addCard</code>, <code>visibleCards</code> getter (order + filter + search query), separate <code>loadError</code> / <code>saveError</code>.</p></td></tr></tbody></table>

## State table

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Field</p></th><th colspan="1" rowspan="1"><p>Meaning</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>catalog</code></p></td><td colspan="1" rowspan="1"><p>All features user can access</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>orderKeys</code> / <code>hiddenKeys</code> / <code>labels</code></p></td><td colspan="1" rowspan="1"><p>Layout from API or cache</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>query</code></p></td><td colspan="1" rowspan="1"><p>Inline filter (search page uses its own field too)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>isSaving</code></p></td><td colspan="1" rowspan="1"><p>Layout POST in flight</p></td></tr></tbody></table>
