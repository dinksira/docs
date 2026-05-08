---
title: Platform Integration
sidebar_label: Platform Integration
id: implementation/platform-integration
---

**Platform Integration**  
Updated the **\`AppShell\`** (Template) to handle platform-specific layout logic.  
  
**\- Auto-Detection:** The shell now detects the Electron environment and automatically injects the \`NativeTitleBar\` and \`SideRail\`.  
**\- Responsive Breakpoints:** Established rules for Tablet (md), Desktop (lg), and Ultra-Wide (xl) viewports.  
  
**Build & Deployment**  
**\- Local Dev:** \`npm run dev\` handles TypeScript compilation and starts the Electron shell pointing to \`http://localhost:4000\`.  
**\- Production Dist:** \`npm run dist\` packages the app into a native installer (\`.exe\` / \`.dmg\`).  
  
  
**Standards Compliance**  
**\- Naming:** Followed PascalCase for components and kebab-case for folders.  
**\- Typing:** 100% Type-safe IPC and Props interfaces.  
**\- Documentation:** Added headers and section separators to all new files.  
**\- Library First:** All UI components were built in the frontend library before use.
