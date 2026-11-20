---
title: Draft State
sidebar_label: Draft State
id: draft-state
---

# Draft State & Local-First Sync ☁️

Delta Labs Docs is built with a **"Local-First"** philosophy. The goal is to eliminate UI latency by performing all structural and content changes in the browser's memory first.

## The Problem we Solved

Standard documentation platforms wait for a "Success" response from a server (or GitHub) before updating the UI. This leads to slow, "laggy" experiences during sidebar reorganization.

## The Solution: `draftStore.ts`

The system uses a centralized local store (`localStorage`) that acts as the single source of truth during an editing session.

### 1\. The Persistence Cycle

-   **Keystroke**: When you type in the editor, the content is instantly saved to `localStorage` under the page slug.
    
-   **Structural Change**: When you rename, delete, or move a page, the **Sidebar Tree** is updated locally.
    
-   **Draft Indicator**: The system tracks which pages have unsaved changes.
    

### 2\. The "Zap" (Publish) Workflow

When the user clicks the **"Publish"** (Lightning Bolt) button:

1.  The portal sends the **entire Sidebar Tree** to the backend.
    
2.  The portal sends all **Unsaved Page Content** to the backend.
    
3.  The backend (`sidebar.py`) performs a "Batch Update" to MongoDB.
    

### 3\. Self-Healing Auto-Provisioning

A critical feature of our backend is **Auto-Provisioning**:

-   The backend scans the tree for any pages that don't have a corresponding physical `.md` file on GitHub.
    
-   It automatically creates these files with the correct frontmatter (ID, Slug, Position).
    
-   This ensures that the Draft State is eventually consistent with the live GitHub repository.
    

* * *

> \[!NOTE\] This architecture allows for **Sub-millisecond Sidebar Actions**, as there are no blocking network requests during page creation or deletion.
