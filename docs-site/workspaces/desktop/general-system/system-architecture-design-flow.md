---
title: System Architecture Design Flow
sidebar_label: System Architecture Design Flow
id: general-system/system-architecture-design-flow
---

# System Architecture Design Flow

This document provides a high-level overview of the architectural design, build pipeline, and routing flow for the **Delta Labs Desktop Application**.

* * *

## 1\. High-Level Architecture Overview

The application follows a **two-process architecture** standard to Electron, dividing responsibilities between system-level operations and the user interface.

-   **Main Process (Node.js/Electron)**: Handles OS-level integrations, window management, custom protocol registration, and network interception. It is strictly compiled via `tsc` (TypeScript Compiler).
    
-   **Renderer Process (React/Vite)**: Handles the user interface, state management, and client-side routing. It is built as a highly optimized Single Page Application (SPA) using Vite and esbuild.
    
-   **Context Bridge (Preload)**: A secure IPC (Inter-Process Communication) layer that connects the Main and Renderer processes without exposing Node.js directly to the frontend.
    

* * *

## 2\. Boot & Initialization Flow

When a user launches the `Delta Labs Setup 1.0.0.exe`, the application bootstraps through the following sequence:

1.  **Electron Lifecycle (**`main.ts`**)**: The Node environment spins up and registers a custom `app://` protocol.
    
2.  **CORS Interceptor**: To allow the desktop app to securely fetch data from the remote production backend (`delta-labs.onrender.com`), the Main process intercepts outgoing API requests and injects an authorized `Origin` header (`https://delta-labs-pi.vercel.app`), bypassing strict browser CORS policies.
    
3.  **Window Creation**: A frameless, chromeless Chromium window is spawned (`width: 1280`, `height: 800`).
    
4.  **Vite Asset Loading**: The window loads `app://./index.html`, which imports the compiled Vite React bundle.
    

* * *

## 3\. UI & Component Mounting (`App.tsx`)

Once the React application mounts, it cascades through a series of foundational context providers and layout shells.

### 3.1. The Provider Stack

The root component wraps the application in a strict hierarchical order:

1.  `<QueryProvider>`: Initializes TanStack React Query for caching API responses.
    
2.  `<LocaleProvider>`: Injects multi-language i18n dictionaries.
    
3.  `<AuthSessionProvider>`: Hydrates the active user session from local storage.
    
4.  `<ThemeProvider>`: Mounts design tokens (Dark/Light mode).
    
5.  `Redux <Provider>`: Connects the global UI state (e.g., feed exploration data).
    

### 3.2. Title Bar & Window Controls

Because the window is natively frameless, a custom `<NativeTitleBar />` is mounted at the very top of the DOM.

-   It exposes a draggable `-webkit-app-region: drag` area.
    
-   It utilizes the isolated `window.electron` preload bridge to trigger OS-level minimize, maximize, and close events.
    

* * *

## 4\. Client-Side Hash Routing Engine

The web version of Delta Labs utilizes Next.js Server-Side Routing. Because the desktop app operates entirely locally offline, it uses a **Custom Hash-Based Routing Engine** to simulate Next.js behavior.

### 4.1. Navigation Shims

The desktop environment maps Next.js native modules to custom shims (`vite.config.mts` aliases):

-   `next/navigation` ➔ Shimmed to track `window.location.hash` changes. React state hooks (`usePathname`, `useRouter`, `useParams`) listen to `hashchange` events and force the UI to re-render instantly without reloading the HTML document.
    
-   `next/image` ➔ Shimmed to return standard responsive `<img>` tags, bypassing Next.js server optimization requirements.
    

### 4.2. Layout Resolution

Based on the active hash path (e.g., `#/explore` or `#/dashboard`), `App.tsx` dynamically resolves the viewport:

-   **Public Routes**: Wrapped in `<PublicLayoutShell>` (e.g., Landing, Login, Signup).
    
-   **Private/App Routes**: Wrapped in `<AppShell>` containing sidebars and authenticated user controls (e.g., Dashboard, School Workspaces).
    

* * *

## 5\. Build & Deployment Pipeline

The compilation process is managed by `package.json` scripts, specifically `npm run dist`, which triggers three distinct phases:

1.  **Main Build (**`build:main`**)**: Compiles `main.ts` and `preload.ts` into CommonJS using `tsc`.
    
2.  **Renderer Build (**`build:renderer`**)**: Vite analyzes the React tree, strips TypeScript types, bundles the Tailwind v4 CSS tokens, and heavily minifies the JS chunks into a `dist/out` directory. _Vite explicitly replaces environment variables (like_ `NEXT_PUBLIC_API_BASE_URL`_) with hardcoded strings at compile time._
    
3.  **NSIS Packaging (**`electron-builder`**)**: Compresses the Chromium binary, Node modules, and the compiled `dist/` folder into a single, self-extracting Windows `.exe` installer.
    

* * *

## 6\. Directory Structure Mapping

The workspace heavily enforces the Delta Labs atomic design and strict folder conventions:

```text
deltalabs-desktop/
├── scripts/                 # Custom build/dev runners
├── src/
│   ├── components/          # Reusable UI (Atoms, Molecules, Organisms)
│   │   └── atoms/NativeTitleBar/ # Desktop-specific window controls
│   ├── contexts/            # Global React Contexts
│   ├── lib/                 # Shared utilities and configurations
│   ├── modules/             # Feature-based view boundaries (Auth, Feed, School)
│   ├── shims/               # Compatibility layers for Next.js imports
│   ├── store/               # Redux Toolkit configuration
│   ├── App.tsx              # Main routing and layout wrapper
│   ├── index.css            # Tailwind v4 entry and design tokens
│   ├── main.ts              # Electron Main Process entry
│   ├── main.tsx             # React Application entry
│   └── preload.ts           # IPC Context Bridge
├── package.json             # Build scripts and dependency map
└── vite.config.mts          # Bundler and alias configurations
```
