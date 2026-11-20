---
title: Github Integration Client
sidebar_label: Github Integration Client
id: github-integration-client
---

# GitHub Integration Client

The GitHub Client is the bridge between the Delta Labs Admin Portal and the live Docusaurus site. It ensures that every "Publish" action results in a real commit on GitHub.

## Core Configuration

The client is initialized using:

-   `GITHUB_TOKEN`: A Personal Access Token with repo permissions.
    
-   `GITHUB_REPO`: The target repository (e.g., `DeltaLabs/docs-site`).
    

## Key Operations

### `write_doc(slug, content, message)`

Writes a Markdown file to the `docs-site/docs/` directory.

-   **Frontmatter**: Automatically prepends Docusaurus-compatible frontmatter (ID, Title, Sidebar Position).
    
-   **Atomic Commits**: Every write is a discrete commit on the `main` branch.
    

### `get_contents(path)`

Fetches the raw content of a file from the repository.

-   **Fallback Logic**: Used when a page exists in the sidebar but its content hasn't been cached in MongoDB yet.
    

## Automation Logic

The client handles the complexity of the GitHub API, including:

-   Updating existing files (finding the `sha`).
    
-   Creating new files.
    
-   Handling branch synchronization.
    

* * *

> \[!CAUTION\] Never expose the `GITHUB_TOKEN` in frontend code. All GitHub operations must go through the FastAPI backend.
