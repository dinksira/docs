---
title: Readmemd
sidebar_label: Readmemd
id: deltalabs-mobile/lib/features/features/domain/readmemd
---

# lib/features/features/domain/

## entities/feature.dart

`Feature` — one entry in the system catalog:

-   `featureKey` — stable id (e.g. `school`, `course`); used in layout and routing, not display title.
    
-   `title`, `description` — default copy from server.
    
-   `routePath` — web path (e.g. `/features/school`) for placeholder + `WorkspaceRoutes` mapping.
    
-   Capability / access fields — whether card is shown or `disabled` for this user.
    

## entities/features\_layout.dart

`FeaturesLayout` — per-user hub personalization:

-   `orderKeys` — display order of cards.
    
-   `hiddenKeys` — cards removed from grid (can be re-added via FAB).
    
-   `labels` — optional rename map `feature_key → custom title`.
    

`FeaturesLayout.empty` — default when no server layout.

## repositories/features\_repository.dart

`FeaturesRepository` (abstract):

```dart
Future<List<Feature>> fetchFeatures();
Future<FeaturesLayout> fetchLayout();
Future<FeaturesLayout> saveLayout({orderKeys, hiddenKeys, labels});
```

Implemented in `features_repository_impl.dart`. Wired in UI via `featuresRepositoryProvider` (GetIt).
