---
title: Readmemd
sidebar_label: Readmemd
id: deltalabs-mobile/lib/features/features/data/readmemd
---

# lib/features/features/data/

Catalog + layout API and offline layout cache.

## data\_sources/features\_remote\_data\_source.dart

`FeaturesRemoteDataSource` / `FeaturesRemoteDataSourceImpl`

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Method</p></th><th colspan="1" rowspan="1"><p>HTTP</p></th><th colspan="1" rowspan="1"><p>Body</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>fetchFeatures</code></p></td><td colspan="1" rowspan="1"><p><code>GET /features</code></p></td><td colspan="1" rowspan="1"><p>—</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>fetchLayout</code></p></td><td colspan="1" rowspan="1"><p><code>GET /features/layout</code></p></td><td colspan="1" rowspan="1"><p>—</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>upsertLayout</code></p></td><td colspan="1" rowspan="1"><p><code>POST /features/layout</code></p></td><td colspan="1" rowspan="1"><p><code>order_keys</code>, <code>hidden_keys</code>, <code>labels</code></p></td></tr></tbody></table>

On **405** from POST, retries `PUT /features/layout` (older servers / proxies).

## data\_sources/features\_layout\_local\_store.dart

`FeaturesLayoutLocalStore` — persists layout in `LocalDatabase` (SQLite via Drift):

-   `save` — write order, hidden, labels after successful API or offline fallback.
    
-   `load` — read last cached layout when `GET /features/layout` fails.
    

Enables drag-and-drop to work when production API is not deployed yet.

## models/feature\_model.dart

`FeatureModel` — one catalog row from API:

-   `feature_key`, `title`, `description`, `route_path`, capability flags, `disabled`, etc.
    
-   `toEntity()` → domain `Feature`.
    

## models/features\_layout\_model.dart

`FeaturesLayoutModel` — `order_keys`, `hidden_keys`, `labels` map.

-   `toEntity()` → `FeaturesLayout`.
    

## repositories/features\_repository\_impl.dart

`FeaturesRepositoryImpl` implements `FeaturesRepository`:

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Method</p></th><th colspan="1" rowspan="1"><p>Behavior</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>fetchFeatures</code></p></td><td colspan="1" rowspan="1"><p>Remote only; maps to entities</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>fetchLayout</code></p></td><td colspan="1" rowspan="1"><p>Remote first, sync to local store; on failure uses cache or empty layout if 405/404/501</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>saveLayout</code></p></td><td colspan="1" rowspan="1"><p>Remote upsert; on 405/404/501 saves <strong>local only</strong> and returns that layout</p></td></tr></tbody></table>

Uses `ErrorHandler` for unexpected errors.
