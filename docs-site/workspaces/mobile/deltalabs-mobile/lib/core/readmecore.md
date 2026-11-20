---
title: Readmecore
sidebar_label: Readmecore
id: readmecore
---

# lib/core/

Shared infrastructure used across all features. Contains no feature-specific business logic.

## Sub-folders

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Folder</p></th><th colspan="1" rowspan="1"><p>Purpose</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>config/</code></p></td><td colspan="1" rowspan="1"><p>Environment detection and base URL configuration</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>di/</code></p></td><td colspan="1" rowspan="1"><p>Dependency injection container (get_it)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>domain/</code></p></td><td colspan="1" rowspan="1"><p>Base abstract classes for entities, repositories, use cases</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>error/</code></p></td><td colspan="1" rowspan="1"><p>Typed failures, exceptions, and error mapping</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>localization/</code></p></td><td colspan="1" rowspan="1"><p>i18n / multi-language support setup</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>logging/</code></p></td><td colspan="1" rowspan="1"><p>Structured app logger</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>network/</code></p></td><td colspan="1" rowspan="1"><p>Dio HTTP client, interceptors, pagination models</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>realtime/</code></p></td><td colspan="1" rowspan="1"><p>WebSocket connection manager</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>routing/</code></p></td><td colspan="1" rowspan="1"><p>GoRouter definition, route constants, auth guard</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>storage/</code></p></td><td colspan="1" rowspan="1"><p>Secure token storage and local SQLite database</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>sync/</code></p></td><td colspan="1" rowspan="1"><p>Background offline sync engine</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>theme/</code></p></td><td colspan="1" rowspan="1"><p>Design tokens: colors, typography, spacing, theme</p></td></tr></tbody></table>
