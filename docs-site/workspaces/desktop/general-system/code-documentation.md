---
title: Code Documentation
sidebar_label: Code Documentation
id: code-documentation
---

# Code Documentation Standards

This document outlines the strict documentation and commenting standards that **all engineers** must follow when contributing to any Delta Labs repository (Frontend, Backend, Desktop, or Admin).

Consistency in documentation ensures that code remains easily readable, maintainable, and self-explanatory for current and future developers.

* * *

## 1\. Core Philosophy

-   **Explain WHY, not WHAT**: The code itself tells us _what_ it is doing. Comments should be reserved for explaining _why_ a specific approach was taken, documenting business logic, detailing edge cases, or explaining complex architectural decisions.
    
-   **Documentation is Code**: Documentation is treated as a first-class citizen. A Pull Request with perfectly working code but missing documentation will fail code review and CI checks.
    
-   **Zero Console Logs**: `console.log` statements are strictly forbidden in committed code. Use the standard logger utilities provided in the core modules instead.
    

* * *

## 2\. File-Level Documentation (JSDoc)

**Every single file** in the codebase MUST begin with a JSDoc block at the very top. This provides immediate context to any developer opening the file.

### Required Fields:

-   **Component / Module Name**: The exact name of the primary export.
    
-   **Description**: A 1-2 sentence summary of what the file does and its atomic level (if applicable).
    
-   **@example**: A minimal, usable code snippet demonstrating how to import and use the component/utility.
    

### Example File Header:

```tsx
/**
 * PrimaryButton
 * Atomic Level: Atom
 * 
 * A reusable, highly accessible button component utilizing Delta Labs design tokens.
 * Handles loading states, disabled states, and dynamic icon rendering.
 *
 * @example
 * ```tsx
 * <PrimaryButton 
 *   variant="solid" 
 *   isLoading={false} 
 *   onClick={handleClick}
 * >
 *   Save Changes
 * </PrimaryButton>
 * ```
 */
```

* * *

## 3\. Function & Hook Documentation

Every exported function, custom hook, or context provider MUST include a JSDoc block immediately preceding its declaration.

### Required Fields:

-   **Description**: Brief explanation of the function's purpose.
    
-   **@param**: Description and type for every parameter.
    
-   **@returns**: Description of the expected output or state shape.
    

### Example Function Header:

```ts
/**
 * Fetches the paginated list of enrolled courses for the active user.
 * 
 * @param {string} userId - The unique UUID of the authenticated user.
 * @param {number} [page=1] - The page number for pagination.
 * @returns {Promise<CourseState>} A promise resolving to the user's course list.
 */
export const fetchUserCourses = async (userId: string, page: number = 1) => {
   // Implementation...
}
```

* * *

## 4\. Section Separators (Mandatory)

To prevent files from becoming unreadable walls of text, all files (especially React components and Context files) MUST be partitioned using exact section separators.

### The Separator Format:

```tsx
// ============================================================================
// SECTION NAME IN ALL CAPS
// ============================================================================
```

### Standard Sections:

A standard React component file should utilize the following sections in this exact order:

1.  `// IMPORTS` (Usually omitted if the file header makes it obvious, but imports must still follow the 8-group strict order)
    
2.  `// TYPES & INTERFACES`
    
3.  `// CONSTANTS` (e.g., variant mappings, animation variants)
    
4.  `// COMPONENT` (or `// HOOK` / `// CONTEXT`)
    
5.  `// HELPER FUNCTIONS` (Internal scoped functions)
    
6.  `// EXPORTS`
    

* * *

## 5\. Component Catalog Integration

Documentation doesn't end in the source code. Every new UI component merged into the `src/components/` library MUST be registered in the Delta Labs Design System catalog.

1.  **Create Markdown File**: A documentation file must be created at `docs/design-system/components/<component-name>.md`.
    
2.  **Define Props**: The markdown file must contain a table of all props, default values, and accepted types.
    
3.  **Update Index**: The component must be added as a new row in the Component Catalog index table, explicitly noting its Atomic Level (Atom, Molecule, Organism, Template).
    

* * *

## 6\. Pre-Commit Checklist

Before opening a PR, ensure your documentation is compliant:

-   Does the file start with a JSDoc header and `@example`?
    
-   Are all exported functions and hooks documented with `@param` and `@returns`?
    
-   Are all `console.log` statements removed?
    
-   Are section separators used to divide Types, Constants, and Components?
    
-   Do inline comments explain _why_ instead of _what_?
    
-   Is the new component registered in the `docs/design-system/` catalog?
