---
title: Atomic Design Methodology
sidebar_label: Atomic Design Methodology
id: frontend/atomic-design-methodology
---

# Atomic Design Methodology

Delta Labs Docs follows a strict **Atomic Design** pattern. This ensures that the UI is modular, reusable, and easy to maintain as the documentation portal grows.

## 1\. Atoms (The Building Blocks)

The smallest functional units. They cannot be broken down further without losing their purpose.

-   **Icons**: Using `lucide-react`.
    
-   **Inputs**: Styled text fields for search and renaming.
    
-   **Badges**: The Language Badges in code blocks.
    
-   **Buttons**: Basic interactive elements.
    

## 2\. Molecules (Component Combinations)

Groups of atoms bonded together.

-   **ToolBtn**: A specialized button used in the `FloatingToolbar` with icons and hover tooltips.
    
-   **PageItem**: A single row in the sidebar containing a page title and its action icons.
    
-   **SearchField**: An input paired with a magnifying glass icon.
    

## 3\. Organisms (Functional Sections)

Complex components that form a distinct part of the interface.

-   **DocsSidebar**: Manages the entire tree structure, drag-and-drop logic, and node CRUD.
    
-   **FloatingToolbar**: The interactive editor control center that follows the user's focus.
    
-   **RichEditor**: The core content engine powered by Tiptap.
    

## 4\. Templates (The Layout)

Generic layouts that define how organisms are arranged on a page.

-   **WorkspaceLayout**: Defines the relationship between the Sidebar (Left) and the Editor (Right).
    

## 5\. Pages (The Final View)

Specific instances where the layout is populated with real data.

-   **EditorPage**: The main dashboard where a specific page slug is loaded and rendered.
    

* * *

> \[!TIP\] When building new features, always start at the **Atom** level and work your way up. Never hardcode styles into a Page component; move them into a Molecule or Organism.
