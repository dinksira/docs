---
title: Auto Provisioning
sidebar_label: Auto Provisioning
id: auto-provisioning
---

# Auto-Provisioning Logic

Auto-Provisioning is the "Glue" that allows the Delta Labs Docs platform to be Local-First while maintaining physical file integrity on GitHub.

## Why it exists

In a local-first sidebar, a user can create 10 folders and 50 pages in seconds. Making 60 API calls to create 60 GitHub files would be slow and prone to failure. Instead, we defer file creation until the **"Publish"** action.

## How it works

1.  **Sidebar Tree Submission**: The portal sends the entire hierarchical tree (JSON) to the `/sidebar/save` endpoint.
    
2.  **Recursive Scan**: The backend function `ensure_pages_exist` recursively traverses every node in that tree.
    
3.  **Existence Check**: It checks if a page with that slug already exists in MongoDB and GitHub.
    
4.  **Creation**: If a page is new, the backend **auto-provisions** it by:
    
    -   Generating a default Markdown body.
        
    -   Writing it to GitHub with the correct hierarchy.
        
    -   Registering it in MongoDB.
        

## Benefits

-   **Zero Ghost Pages**: You will never have a link in the sidebar that leads to a 404 page.
    
-   **Massive Speed**: The user experience is instantaneous; the backend handles the "Heavy Lifting" of file creation in the background.
    

* * *

> \[!NOTE\] Auto-provisioning is triggered automatically every time a structural "Publish" (Zap) is initiated.
