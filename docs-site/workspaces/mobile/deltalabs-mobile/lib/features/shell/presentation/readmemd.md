---
title: Readmemd
sidebar_label: Readmemd
id: readmemd
---

# lib/features/shell/presentation/

Shell widgets and pages only.

## pages/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>main_shell_page.dart</code></p></td><td colspan="1" rowspan="1"><p><code>ConsumerStatefulWidget</code>. Owns <code>FeedTopTab _tab</code> and <code>ShellSurface _surface</code>. Builds <code>MainTopChrome</code>, <code>IndexedStack</code> (feed tabs) or <code>FeaturesHubPage</code>. Adjusts <code>SystemUiOverlayStyle</code> (light icons on video). Background black (feed) or white (features).</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>feed_tab_placeholder_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Static placeholder for Audio / AI / Simulation tabs (icon, title, subtitle).</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>profile_tab_page.dart</code></p></td><td colspan="1" rowspan="1"><p>Profile summary + logout (used when profile is reachable from nav experiments; main shell today uses top tabs without bottom profile).</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features_hub_page.dart</code></p></td><td colspan="1" rowspan="1"><p><strong>Barrel only</strong> — <code>export</code> of <code>features/features/presentation/pages/features_hub_page.dart</code>. No logic here.</p></td></tr></tbody></table>

## widgets/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>main_top_chrome.dart</code></p></td><td colspan="1" rowspan="1"><p>Top bar: horizontal <strong>tab strip</strong> (<code>FeedTopTab</code> labels, dynamic Custom label), <strong>search</strong> icon, <strong>features switch</strong> icon. <code>overlayOnVideo</code> controls transparent vs solid background.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>feed_top_tab.dart</code></p></td><td colspan="1" rowspan="1"><p>Enum <code>FeedTopTab</code>: video, audio, ai, simulation, custom. Extension <code>displayLabel(customTabLabel)</code> truncates long custom names.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>features_switch_icon.dart</code></p></td><td colspan="1" rowspan="1"><p>Custom painted icon for toggling Features hub; highlighted when <code>isFeaturesMode</code>.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>main_bottom_nav.dart</code></p></td><td colspan="1" rowspan="1"><p><strong>Legacy</strong> bottom navigation (<code>MainTab</code> enum). Superseded by top-tab shell for TikTok layout; file may remain for reference.</p></td></tr></tbody></table>
