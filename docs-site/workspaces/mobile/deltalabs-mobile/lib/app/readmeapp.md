---
title: Readmeapp
sidebar_label: Readmeapp
id: deltalabs-mobile/lib/app/readmeapp
---

# lib/app/

App-level widget setup.

## app.dart

`DeltaLabsApp` — the root `ConsumerWidget`. Sets up:

-   `MaterialApp.router` with the GoRouter instance from `appRouterProvider`
    
-   Light theme from `AppTheme.light`
    
-   Localization delegates
    
-   Debug banner disabled
    

This is the only place `MaterialApp` is created.
