---
title: Design System
sidebar_label: Design System
id: design-system
---

# **Delta Labs Docs — Design System**

This document outlines the visual language, design tokens, and UI components that define the premium aesthetic of the Delta Labs Documentation System.

**1\. Visual Philosophy**  
The design system is built on three core pillars:  
**1\. High Fidelity & Premium Feel**: Use of multi-layered shadows and subtle gradients to create depth.  
**2\. Glassmorphism:** Leveraging backdrop blurs to create a modern, "frosted glass" interface that feels airy and light.  
**3\. Interactive Feedback:** Every user action (hover, click, transition) is reinforced with micro-animations and visual state changes.

**2\. Design Tokens**

**2.1 Color Palette**  
The system uses a refined palette centered around \*\*SaaS Blue\*\*.

<table style="min-width: 100px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Category</p></th><th colspan="1" rowspan="1"><p>Token</p></th><th colspan="1" rowspan="1"><p>Value</p></th><th colspan="1" rowspan="1"><p>Description</p></th></tr><tr><td colspan="1" rowspan="1"><p><strong>Primary</strong></p></td><td colspan="1" rowspan="1"><p>`--accent-primary`</p></td><td colspan="1" rowspan="1"><p>`#174A5F`</p></td><td colspan="1" rowspan="1"><p>The official Delta Labs brand color.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Gradients</strong></p></td><td colspan="1" rowspan="1"><p>`--accent-gradient`</p></td><td colspan="1" rowspan="1"><p>`linear-gradient(135deg, #174A5F 0%, #2a6a84 100%)`</p></td><td colspan="1" rowspan="1"><p>Used for primary actions and highlights.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Background</strong></p></td><td colspan="1" rowspan="1"><p>`--bg-primary`</p></td><td colspan="1" rowspan="1"><p>`#ffffff`</p></td><td colspan="1" rowspan="1"><p>Clean white for content areas.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Secondary</strong></p></td><td colspan="1" rowspan="1"><p>`--bg-secondary`</p></td><td colspan="1" rowspan="1"><p>`#f8fafc`</p></td><td colspan="1" rowspan="1"><p>Soft cool slate for sidebars and secondary panels.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Success</strong></p></td><td colspan="1" rowspan="1"><p>`--success`</p></td><td colspan="1" rowspan="1"><p>`#10b981`</p></td><td colspan="1" rowspan="1"><p>Emerald Green.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Error</strong></p></td><td colspan="1" rowspan="1"><p>`--error`</p></td><td colspan="1" rowspan="1"><p>`#ef4444`</p></td><td colspan="1" rowspan="1"><p>Rose Red.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Warning</strong></p></td><td colspan="1" rowspan="1"><p>`--warning`</p></td><td colspan="1" rowspan="1"><p>`#f59e0b`</p></td><td colspan="1" rowspan="1"><p>Amber Yellow.</p></td></tr></tbody></table>

**2.2 Typography**  
**\- Primary Sans-Serif:** \`Inter\` — Chosen for its high legibility and professional look.  
**\- Monospace:** \`JetBrains Mono\` — Used for code blocks, technical IDs, and developer-centric data.  
**\- Base Size:** \`14px\` (Optimized for technical documentation Density).

**2.3 Glassmorphism Settings**  
**\- Background:** \`rgba(255, 255, 255, 0.72)\`  
**\- Blur:** \`blur(12px)\`  
**\- Border:** \`rgba(255, 255, 255, 0.4)\`

**3\. UI Components & Classes**

**3.1 Premium Cards (\`.premium-card\`)**  
**\- Visuals:** Elevated white background with a subtle border and premium multi-shadow.  
**\- Behavior:** Translates up by \`-2px\` on hover with an expanded shadow to simulate physical lift.

**3.2 Action Buttons  
**The system features specialized buttons with unique identities:

<table style="min-width: 100px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Name</p></th><th colspan="1" rowspan="1"><p>Class</p></th><th colspan="1" rowspan="1"><p>Style</p></th><th colspan="1" rowspan="1"><p>Icon Behavior</p></th></tr><tr><td colspan="1" rowspan="1"><p><strong>History Trigger</strong></p></td><td colspan="1" rowspan="1"><p>`.history-trigger-btn`</p></td><td colspan="1" rowspan="1"><p>Emerald Gradient</p></td><td colspan="1" rowspan="1"><p>Icon rotates -180° on hover.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>View Live</strong></p></td><td colspan="1" rowspan="1"><p>`.view-live-btn`</p></td><td colspan="1" rowspan="1"><p>Electric Blue Gradient</p></td><td colspan="1" rowspan="1"><p>Icon slides diagonally (top-right).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Logout</strong></p></td><td colspan="1" rowspan="1"><p>`.logout-btn`</p></td><td colspan="1" rowspan="1"><p>Crimson Blaze Gradient</p></td><td colspan="1" rowspan="1"><p>Icon slides to the right.</p></td></tr></tbody></table>

**3.3 Inputs & Controls**  
**\- Focus States:** High-contrast border (\`--accent-primary\`) with a soft focus ring (\`rgba(23, 74, 95, 0.15)\`).  
**\- Smooth Interaction:** All inputs use a \`0.25s\` cubic-bezier transition.

**4\. Animations & Transitions**

**\- Entrance Animations:**  
\- \`.animate-fade-in\`: Standard opacity transition for new elements.  
\- \`.animate-slide-up\`: Combined translation and fade for page sections.  
\- \*\*Micro-Interactions\*\*:  
\- \*\*Button Pulsing\*\*: Subtle scaling for critical "active" elements.  
\- \*\*Shimmer Effect\*\*: A light-sweep animation (\`::before\`) on premium buttons during hover.

**5\. Implementation Guidance**  
**\- Tailwind Integration:** Most layout and spacing should be handled via Tailwind utility classes.  
**\- Token Usage:** Always use CSS variables (e.g., \`var(--accent-primary)\`) rather than hardcoding hex values. This ensures theme consistency and enables easier maintenance.  
**\- Dark Mode Support:** The system includes foundational tokens for dark mode (e.g., \`.attribution-badge\` adjustments), using \`\[data-theme='dark'\]\` as the selector.
