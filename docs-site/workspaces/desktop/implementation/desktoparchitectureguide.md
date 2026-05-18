---
title: Desktoparchitectureguide
sidebar_label: Desktoparchitectureguide
id: implementation/desktoparchitectureguide
---

# Delta Labs Desktop — Complete Technical & Runtime Architecture Guide

* * *

This document outlines the high-performance architectural systems, security layers, and offline/online routing mechanisms powering the **Delta Labs Desktop Application**.

* * *

## 1\. Core Architecture (Hybrid Shell Pattern)

The desktop application operates on a **hybrid architectural model**, combining a compiled **Next.js Single-Page Application (SPA) static export** with a native **Electron C++ runtime wrapper**.

### Process Separation:

-   **The Main Process (**`main.ts`**)**: Runs in a full Node.js environment. It manages native operating system tasks, window lifecycle, system event registrations, protocol routing, and security policies.
    
-   **The Renderer Process (Chromium)**: Runs inside a sandboxed web-view. It compiles the CSS, renders React components, and executes client-side page animations.
    
-   **The Preload Bridge (**`preload.ts`**)**: Acts as a secure, selective gatekeeper. Using Electron's `contextBridge` and `ipcRenderer`, it exposes specific native functions (like minimize, maximize, close) to the web-view safely, without exposing dangerous raw Node.js APIs.
    

* * *

## 2\. Offline vs. Online Runtime Operations

The application is engineered to operate seamlessly in both fully disconnected **Offline Mode** and connected **Online Mode**.

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Feature / System</p></th><th colspan="1" rowspan="1"><p>🚫 Offline Mode (Disconnected)</p></th><th colspan="1" rowspan="1"><p>🌐 Online Mode (Connected)</p></th></tr><tr><td colspan="1" rowspan="1"><p><strong>UI Rendering</strong></p></td><td colspan="1" rowspan="1"><p>Loaded 100% locally from SSD. Sub-millisecond start.</p></td><td colspan="1" rowspan="1"><p>Loaded 100% locally from SSD. Zero server dependencies.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Routing / Navigation</strong></p></td><td colspan="1" rowspan="1"><p>Static router falls back to local <code>.html</code> pages.</p></td><td colspan="1" rowspan="1"><p>Static router falls back to local <code>.html</code> pages.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Fonts &amp; Icons</strong></p></td><td colspan="1" rowspan="1"><p>Local bundled <strong>Syne</strong> &amp; Geist fonts.</p></td><td colspan="1" rowspan="1"><p>Local bundled <strong>Syne</strong> &amp; Geist fonts (no Google Font calls).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Authentication</strong></p></td><td colspan="1" rowspan="1"><p>Restricts actions, serves cached profile (read-only).</p></td><td colspan="1" rowspan="1"><p>Connects to Render API via bypassed HTTPS CORS calls.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Interactive Features</strong></p></td><td colspan="1" rowspan="1"><p>Renders elegant offline states and retry bars.</p></td><td colspan="1" rowspan="1"><p>Syncs data, submits comments, saves user profiles.</p></td></tr></tbody></table>

### How Offline Works:

1.  **Custom** `app://` **Protocol**: Electron registers a custom scheme `app://./`. When Chromium requests a route like `/settings`, the custom handler intercepts it, checks for the presence of a local `/settings.html` on the SSD, and serves it directly. This bypasses the need for an active web server or internet connection.
    
2.  **Local Static Bundling**: All fonts, SVGs, Next.js chunks, and image assets are baked directly into the installation package. The app never queries external CDNs to resolve styling.
    

### How Online Works (CORS & Security Bypass):

When the desktop application communicates with the production backend (`https://delta-labs.onrender.com`), standard web browsers block these calls due to **Cross-Origin Resource Sharing (CORS)** (since requests originate from the custom protocol `app://` instead of `https://`).  
To enable seamless remote work, we implemented a custom header bypass in the Main Process (`main.ts`):

This forces Chromium to treat requests originating from the desktop shell as authenticated, allowing secure login and data synchronizations.

* * *

## 3\. Cinematic Splash Screen & Lifecycle Control

We implemented a beautiful, lightweight **5-phase CSS-accelerated animation** sequence inside `SplashScreen.tsx` powered by `framer-motion`:

1.  **The Spark Phase**: Cyan glow radial pulse expands.
    
2.  **Facet Assembly Phase**: The 3D crystal logo facets assemble from 3 distinct clip-paths (`top-left`, `top-right`, `bottom-right`) using an exponential ease-out curve (`[0.16, 1, 0.3, 1]`) and sub-pixel blur filters.
    
3.  **Depth Breath Phase**: A physical scale heartbeat animation simulates breathing.
    
4.  **Wordmark Rise Phase**: The letter spacing of **Syne** wordmark contracts elegantly (`0.3em` to `0.12em`).
    
5.  **Exit Phase**: Container fades out, shifting visibility seamlessly to the dashboard.
    

### Session Storage Safeguard (No Repeated Plays):

To prevent the animation from playing on every minor click or internal route navigation:

-   The `DesktopSplashGate` checks `sessionStorage` at mount.
    
-   If `sessionStorage.getItem("dl.splash_played")` is `"true"`, it immediately renders the page, completely skipping the splash screen.
    
-   The flag is set once the opening animation finishes and persists for the entire lifetime of the desktop app session (cleared only when the app is fully closed).
    

* * *

## 4\. Custom Window Frame & IPC Bridge

To create a gorgeous frameless experience, the standard operating system window border is hidden (`frame: false`, `titleBarStyle: "hidden"`). We replace it with a custom React NativeTitleBar:

### IPC Bridge Communications:

When a user clicks on the custom close, minimize, or maximize buttons, the requests cross the Electron context bridge to execute native OS calls:

This enables native-like OS interactions while letting us style the control buttons with custom, high-fidelity SVG graphics!
