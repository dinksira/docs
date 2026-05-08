---
title: High Fidelity Ui Components
sidebar_label: High Fidelity Ui Components
id: implementation/high-fidelity-ui-components
---

**High-Fidelity UI Components**  
Following the **Atomic Design** principles, we built the following components in the \`deltalabs-frontend\` library:  
  
**1, \`NativeTitleBar\` (Atom)**  
**\- Purpose:** Replaces the native OS frame with a design-system-compliant header.  
**\- Features:** Draggable region, custom window controls, and platform detection.  
**\- Branding**: Integrated the official \`delta-logo.svg\` (with PNG fallback for taskbar compatibility).  
  
**2\. \`SideRail\` (Organism)**  
**\- Purpose:** Persistent vertical navigation for desktop and large viewports.  
**\- States:** Supports expanded (256px) and collapsed (80px) modes.  
**\- Transitions:** Smooth CSS transitions using design system duration tokens.
