---
title: The Local First Rule
sidebar_label: The Local First Rule
id: the-local-first-rule
---

# The Local-First Rule

The single most important development rule for the Delta Labs Docs platform is: **The UI must never wait for the network.**

## The Philosophy

In a modern documentation engine, structural changes (Move, Rename, Delete) should feel like you are working on a desktop application like VS Code. Any delay—even 100ms—breaks the user's flow.

## Implementation Guidelines

1.  **Optimistic Updates**: When a user renames a page, update the state in `DocsSidebar.tsx` immediately. Do not show a spinner.
    
2.  **The Draft Store**: Use the `draftStore.ts` to persist these changes in `localStorage`. This ensures that if the user refreshes the page, their structural changes are still there, even if they haven't "Published" yet.
    
3.  **Batching**: Defer expensive network operations (GitHub Commits, MongoDB Upserts) until the user explicitly clicks the "Publish" button.
    
4.  **Feedback**: Only show a loading state during the final "Zap" (Publishing phase).
    

## Why we do this

By moving logic from the server to the client's memory, we achieve **Zero-Latency structural editing**. The backend's job is simply to "Catch up" and synchronize the physical state with the user's local draft.

* * *

> \[!IMPORTANT\] If a feature requires a network request to update the UI, consider if it can be moved to the `Draft State` first.
