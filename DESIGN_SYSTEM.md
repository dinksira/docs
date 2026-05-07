# Delta Labs Docs — Design System 2.0 (Premium)

This document outlines the visual language, design tokens, and UI components that define the premium aesthetic of the Delta Labs Documentation System.

---

## 1. Visual Philosophy
The design system is built on three core pillars:
1.  **High Fidelity & Premium Feel**: Use of multi-layered shadows and subtle gradients to create depth.
2.  **Glassmorphism**: Leveraging backdrop blurs to create a modern, "frosted glass" interface that feels airy and light.
3.  **Interactive Feedback**: Every user action (hover, click, transition) is reinforced with micro-animations and visual state changes.

---

## 2. Design Tokens

### 2.1 Color Palette
The system uses a refined palette centered around **SaaS Blue**.

| Category | Token | Value | Description |
| :--- | :--- | :--- | :--- |
| **Primary** | `--accent-primary` | `#174A5F` | The official Delta Labs brand color. |
| **Gradients** | `--accent-gradient` | `linear-gradient(135deg, #174A5F 0%, #2a6a84 100%)` | Used for primary actions and highlights. |
| **Background** | `--bg-primary` | `#ffffff` | Clean white for content areas. |
| **Secondary** | `--bg-secondary` | `#f8fafc` | Soft cool slate for sidebars and secondary panels. |
| **Success** | `--success` | `#10b981` | Emerald Green. |
| **Error** | `--error` | `#ef4444` | Rose Red. |
| **Warning** | `--warning` | `#f59e0b` | Amber Yellow. |

### 2.2 Typography
- **Primary Sans-Serif**: `Inter` — Chosen for its high legibility and professional look.
- **Monospace**: `JetBrains Mono` — Used for code blocks, technical IDs, and developer-centric data.
- **Base Size**: `14px` (Optimized for technical documentation Density).

### 2.3 Glassmorphism Settings
- **Background**: `rgba(255, 255, 255, 0.72)`
- **Blur**: `blur(12px)`
- **Border**: `rgba(255, 255, 255, 0.4)`

---

## 3. UI Components & Classes

### 3.1 Premium Cards (`.premium-card`)
- **Visuals**: Elevated white background with a subtle border and premium multi-shadow.
- **Behavior**: Translates up by `-2px` on hover with an expanded shadow to simulate physical lift.

### 3.2 Action Buttons
The system features specialized buttons with unique identities:

| Name | Class | Style | Icon Behavior |
| :--- | :--- | :--- | :--- |
| **History Trigger** | `.history-trigger-btn` | Emerald Gradient | Icon rotates -180° on hover. |
| **View Live** | `.view-live-btn` | Electric Blue Gradient | Icon slides diagonally (top-right). |
| **Logout** | `.logout-btn` | Crimson Blaze Gradient | Icon slides to the right. |

### 3.3 Inputs & Controls
- **Focus States**: High-contrast border (`--accent-primary`) with a soft focus ring (`rgba(23, 74, 95, 0.15)`).
- **Smooth Interaction**: All inputs use a `0.25s` cubic-bezier transition.

---

## 4. Animations & Transitions

- **Entrance Animations**:
    - `.animate-fade-in`: Standard opacity transition for new elements.
    - `.animate-slide-up`: Combined translation and fade for page sections.
- **Micro-Interactions**:
    - **Button Pulsing**: Subtle scaling for critical "active" elements.
    - **Shimmer Effect**: A light-sweep animation (`::before`) on premium buttons during hover.

---

## 5. Implementation Guidance
- **Tailwind Integration**: Most layout and spacing should be handled via Tailwind utility classes.
- **Token Usage**: Always use CSS variables (e.g., `var(--accent-primary)`) rather than hardcoding hex values. This ensures theme consistency and enables easier maintenance.
- **Dark Mode Support**: The system includes foundational tokens for dark mode (e.g., `.attribution-badge` adjustments), using `[data-theme='dark']` as the selector.
