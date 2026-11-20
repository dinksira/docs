---
title: Database Architecture
sidebar_label: Database Architecture
id: database-architecture
---

# Database Architecture

Delta Labs Docs uses **MongoDB** as the primary metadata and content cache. We use the **Motor** asynchronous driver for high-performance FastAPI integration.

## Collections

### 1\. `pages`

The primary collection for documentation content.

-   **Fields**: `slug`, `title`, `content` (Markdown), `category`, `sidebar_position`, `sidebar_label`, `workspace`, `isDraft`, `updatedAt`.
    
-   **Indexing**: Unique index on `slug`.
    

### 2\. `portal_workspaces`

Defines the different documentation projects.

-   **Fields**: `name`, `slug`, `order`.
    
-   **Purpose**: Allows one portal instance to manage multiple distinct documentation sites.
    

### 3\. `users` & `admin_users`

Manages access control.

-   **Fields**: `email`, `hashed_password`, `name`, `role` (Admin/Viewer).
    

## Data Flow

1.  **Drafting**: Changes are initially saved to the `pages` collection in MongoDB.
    
2.  **Publishing**: Upon the final "Zap," the data is mirrored to the GitHub repository as physical `.md` files.
    
3.  **Syncing**: If a file is edited manually on GitHub, the backend fetches it and updates MongoDB to match.
    

* * *

> \[!TIP\] Always use `updatedAt` timestamps to resolve conflicts between local drafts and server state.
