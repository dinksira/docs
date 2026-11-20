---
title: Readmeshared
sidebar_label: Readmeshared
id: readmeshared
---

# lib/shared/

Reusable widgets used across multiple features. No business logic here — pure UI components.

## widgets/auth/

Auth-specific reusable widgets:

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>auth_scaffold.dart</code></p></td><td colspan="1" rowspan="1"><p>Shared layout for all auth screens: logo → title → content → button → OR → social → bottom link. Shows back button automatically when screen can be popped.</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>auth_text_field.dart</code></p></td><td colspan="1" rowspan="1"><p>Labeled text field with error display, password toggle, and all input options</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>primary_button.dart</code></p></td><td colspan="1" rowspan="1"><p>Full-width dark button with built-in loading spinner state</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>auth_bottom_text.dart</code></p></td><td colspan="1" rowspan="1"><p>"Already have account? Log in" style link row</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>delta_logo.dart</code></p></td><td colspan="1" rowspan="1"><p>App logo widget — renders <code>assets/icons/playstore.png</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>social_buttons_row.dart</code></p></td><td colspan="1" rowspan="1"><p>Row of 4 social login buttons: Google, Facebook, Apple, Fayda ID</p></td></tr></tbody></table>

## widgets/error/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>error_view.dart</code></p></td><td colspan="1" rowspan="1"><p>Full-screen error state with retry button</p></td></tr></tbody></table>

## widgets/loading/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>shimmer_loader.dart</code></p></td><td colspan="1" rowspan="1"><p>Shimmer skeleton loading placeholder for list items</p></td></tr></tbody></table>

## widgets/network\_image/

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>File</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>cached_image.dart</code></p></td><td colspan="1" rowspan="1"><p>Image widget with caching via <code>cached_network_image</code>, placeholder, and error fallback</p></td></tr></tbody></table>
