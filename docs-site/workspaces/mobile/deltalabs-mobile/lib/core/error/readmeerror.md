---
title: Readmeerror
sidebar_label: Readmeerror
id: readmeerror
---

# lib/core/error/

Typed error handling across all layers.

## failures.dart

Sealed `Failure` classes returned from repositories via `Either<Failure, T>`:

<table style="min-width: 50px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Class</p></th><th colspan="1" rowspan="1"><p>When</p></th></tr><tr><td colspan="1" rowspan="1"><p><code>NetworkFailure</code></p></td><td colspan="1" rowspan="1"><p>Generic network error</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>TimeoutFailure</code></p></td><td colspan="1" rowspan="1"><p>Request timed out</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>NoInternetFailure</code></p></td><td colspan="1" rowspan="1"><p>No connectivity</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>ServerFailure</code></p></td><td colspan="1" rowspan="1"><p>5xx response</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>UnauthorizedFailure</code></p></td><td colspan="1" rowspan="1"><p>401 — session expired</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>ValidationFailure</code></p></td><td colspan="1" rowspan="1"><p>400 — bad input</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>AuthFailure</code></p></td><td colspan="1" rowspan="1"><p>Auth-specific errors</p></td></tr><tr><td colspan="1" rowspan="1"><p><code>ConflictFailure</code></p></td><td colspan="1" rowspan="1"><p>409 — duplicate resource</p></td></tr></tbody></table>

## exceptions.dart

Raw exceptions thrown by data sources before being mapped to Failures.

## error\_handler.dart

`ErrorHandler.fromObject(e, stackTrace)` — converts any exception into a typed `Failure`.

Handles: `DioException`, `AppException`, `SocketException`, and unknown errors. Maps HTTP status codes to the correct `Failure` subclass.
