---
title: Rich Editor
sidebar_label: Rich Editor
id: frontend/rich-editor
---

# Rich Editor Architecture

The Delta Labs Rich Editor is a customized implementation of **Tiptap**, designed specifically for high-performance documentation management.

## Core Features

1.  **Dual Mode Operation**:
    
    -   **Read Mode**: Default view. optimized for reading. Internal links are clickable for wiki-style navigation.
        
    -   **Edit Mode**: Triggered by **Double-Click**. Enables the floating toolbar and content modification.
        
2.  **Floating Toolbar**:
    
    -   A draggable, context-aware control center.
        
    -   Includes a sophisticated **Internal Page Search** that is workspace-aware.
        

## Custom Extensions

The editor uses several "High-End" custom extensions:

### 1\. Interactive Code Blocks (`CodeBlockComponent.tsx`)

-   **Lowlight Integration**: Real-time syntax highlighting for 50+ languages.
    
-   **Language Selector**: Ability to specify the programming language via the toolbar.
    
-   **Copy to Clipboard**: A floating button with visual checkmark feedback.
    
-   **Language Badges**: Auto-rendered labels (e.g., "PYTHON") in the corner of code blocks.
    

### 2\. Smart Link Interceptor

-   Overrides the standard anchor behavior.
    
-   **Internal Links**: Detects links starting with `/` or containing workspace parameters and uses the **Next.js Router** for instant portal navigation.
    
-   **External Links**: Open in new tabs as standard.
    

### 3\. Resizable Media

-   **Images & Video**: Custom node views that allow for real-time resizing and aspect-ratio preservation.
    

## Content Workflow

1.  **Input**: The editor accepts Markdown-formatted strings.
    
2.  **Processing**: Content is parsed into Tiptap's JSON structure for editing.
    
3.  **Output**: Upon saving, content is converted back to **Clean Markdown** (via `turndown`) for GitHub compatibility.
    

* * *

> \[!IMPORTANT\] The editor is **Local-First**. Every keystroke is saved to the `Draft State` (local storage) before being published to the backend.
