---
title: Component Hierarchy
sidebar_label: Component Hierarchy
id: frontend/component-hierarchy
---

# Component Hierarchy & Atomic Design

This document provides a comprehensive map of the frontend component architecture used in the Delta Labs platform. The UI strictly adheres to **Atomic Design** principles, ensuring all interfaces are constructed systematically from reusable, isolated components.

* * *

## 1\. Architectural Philosophy

The UI library separates components based on their structural complexity, avoiding monolithic files and promoting immense reusability across features and modules.

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Level</p></th><th colspan="1" rowspan="1"><p>Definition</p></th><th colspan="1" rowspan="1"><p>Rules</p></th></tr><tr><td colspan="1" rowspan="1"><p><strong>Atoms</strong></p></td><td colspan="1" rowspan="1"><p>Basic HTML elements with base styling.</p></td><td colspan="1" rowspan="1"><p>Cannot contain other components (except icons/wrappers).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Molecules</strong></p></td><td colspan="1" rowspan="1"><p>Simple UI groups built from multiple Atoms.</p></td><td colspan="1" rowspan="1"><p>Cannot contain Organisms.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Organisms</strong></p></td><td colspan="1" rowspan="1"><p>Complex, standalone UI sections.</p></td><td colspan="1" rowspan="1"><p>Formed by Molecules and Atoms.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Templates</strong></p></td><td colspan="1" rowspan="1"><p>Page-level layout scaffolds.</p></td><td colspan="1" rowspan="1"><p>Does not inject data (props only).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Pages / Views</strong></p></td><td colspan="1" rowspan="1"><p>Route-level wrappers.</p></td><td colspan="1" rowspan="1"><p>Injects data into Templates and Organisms.</p></td></tr></tbody></table>

* * *

## 2\. Component Directory Map

All components reside in `src/components/`, strictly organized by their atomic level or specific cross-cutting domain (e.g., `navigation`, `system`).

### 🟡 Atoms (`src/components/theme` & `src/components/atoms`)

The fundamental building blocks. The `theme` folder acts as the core UI kit containing headless or base-styled primitives.

-   **Typography & Layout**: `Typography`, `Card`
    
-   **Inputs & Forms**: `Button`, `ButtonLink`, `Input`, `SearchInput`, `Checkbox`, `RadioGroup`, `Select`, `Textarea`, `Field`, `Switch`
    
-   **Indicators**: `Badge`, `ProgressBar`, `Rating`, `StatusBanner`
    
-   **System/App Boundaries**: `NativeTitleBar`, `FAB` (Floating Action Button)
    

### 🟢 Molecules (`src/components/molecules`)

Simple, single-purpose groups of atoms that form cohesive functional units.

-   **Cards**: `MyResourceCard`, `OrderCard`, `RentCard`, `ResourceCard`, `RoadmapCard`, `RoadmapSummaryCard`
    
-   **List Items**: `CartItem`, `ChatMessage`, `CommunityContactItem`, `NotificationItem`
    
-   **Widgets**: `FileUploader`, `SearchPill`
    

### 🔵 Organisms (`src/components/organisms`)

Complex, highly interactive, and standalone sections of an interface.

-   **Modals & Overlays**: `MessageModal`, `PostModal`, `CustomParametersModal`, `RoadmapSelectionModal`, `TimeSelectionModal`, `TutorSelectionModal`, `SuccessModal`, `AiAssistantModal`
    
-   **Sidebars & Navigation**: `ResourceSidebar`, `RoadmapSidebar`, `SideRail`
    
-   **Data Layouts**: `OrderGrid`, `ResourceGrid`, `CartSummary`, `RoadmapTimeline`, `CourseWorkspaceHeader`
    
-   **System Overlays**: `SplashScreen`
    

### 🟣 Templates (`src/components/templates`)

Scaffolding wrappers that define where organisms and molecules should be placed on a screen.

-   **Dashboards**: `ResourceManagementLayout`
    

### 🔴 Navigation & System (`src/components/navigation`, `src/components/system`)

High-level structural components that wrap the entire application or manage deep integrations.

-   **Navigation**: `AppShell`, `PublicLayoutShell`
    
-   **System**: `GlobalAuthPendingBar`, `DesktopSplashGate`
    

* * *

## 3\. Implementation Rules

When creating or modifying components in the Delta Labs repository, the following compliance rules are enforced:

1.  **Folder Isolation**: Every component MUST live in its own named folder (e.g., `components/atoms/Button/Button.tsx`). _Note: The_ `theme` _directory currently holds some flat files, which is an exception for primitive core elements, though strict compliance recommends migrating them._
    
2.  **Barrel Exports**: Every component folder must have an `index.ts` file that re-exports the component and its types.
    
3.  **Strict Prop Typing**: All component properties must be defined in an exported interface (e.g., `ComponentNameProps`).
    
4.  **No Direct Data Fetching**: Atoms, Molecules, Organisms, and Templates must **never** make direct API calls (no `useQuery` or `fetch`). Data fetching is strictly reserved for the `modules/*/views/` level (Pages) which then pass data down as props.
    
5.  **Design Tokens Only**: Components cannot use hardcoded colors or sizes (e.g., `bg-[#123456]`). They must strictly utilize the Tailwind v4 design tokens defined in `index.css`.
