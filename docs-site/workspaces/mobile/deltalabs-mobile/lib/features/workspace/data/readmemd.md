---
title: Readmemd
sidebar_label: Readmemd
id: deltalabs-mobile/lib/features/workspace/data/readmemd
---

# lib/features/workspace/data/

## models/my\_school\_model.dart

`MySchoolModel` — parses one row from `GET /me/schools` `items[]`:

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Field</p></th><th colspan="1" rowspan="1"><p>JSON keys</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>schoolId</code></p></td><td colspan="1" rowspan="1"><p><code>schoolId</code> or <code>school_id</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>name</code></p></td><td colspan="1" rowspan="1"><p><code>name</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>slug</code></p></td><td colspan="1" rowspan="1"><p><code>slug</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>schoolType</code></p></td><td colspan="1" rowspan="1"><p><code>schoolType</code> / <code>school_type</code></p></td></tr><tr><td colspan="1" rowspan="1"><p><code>archived</code></p></td><td colspan="1" rowspan="1"><p><code>archived</code> (filtered out in provider)</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>roleKeys</code></p></td><td colspan="1" rowspan="1"><p><code>roleKeys</code> / <code>role_keys</code> list</p></td></tr></tbody></table>

`fromJson` factory only — no separate remote data source class; `my_schools_provider` calls `ApiClient` inline.
