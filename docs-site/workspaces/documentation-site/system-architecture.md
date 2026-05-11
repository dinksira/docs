---
title: System Architecture
sidebar_label: System Architecture
id: system-architecture
---

# <span style="color: rgb(37, 99, 235);"><strong>Delta Labs Documentation System Architecture</strong></span>

**1, Overview**

The Delta Labs Documentation System is a robust, custom-built Headless Content Management System (CMS) designed specifically to manage and publish technical documentation via \*\*Docusaurus\*\*. It provides a "Portal" for administrators to manage content with a rich-text editor and advanced sidebar management, while leveraging GitHub as a version-controlled storage layer and Docusaurus for the static-site presentation.

**Key Capabilities**  
\- **Multi-Workspace Support**: Separate documentation environments (e.g., "Documentation", "API Reference", "Internal Guides").  
\- **Live Version Control**: Every change is committed to GitHub, providing a full audit trail and easy reverts.  
\- **Rich Text Editing**: Powered by TipTap, allowing seamless content creation with markdown support.  
\- **Drag-and-Drop Sidebar Management**: A visual interface for organizing the documentation structure.  
\- **Automated Deployment:** One-click rebuilds that trigger Vercel deployment hooks.

\---

**2\. Stack**

**Backend (API)**  
\- **Framework**: FastAPI (Python)  
\- **Database**: MongoDB (via Motor/AsyncIOMotorClient)  
\- **Authentication**: JWT-based with Google OAuth integration  
**\- Integrations:**  
\- **PyGithub:** For direct interaction with the documentation repository.  
\- **Resend/SendGrid:** For transactional emails.  
\- **Vercel API:** For triggering production rebuilds.

**Frontend (Portal)**  
\- **Framework**: Next.js (App Router)  
\- **Styling**: Tailwind CSS  
\- **Editor**: TipTap (Rich Text) with Markdown sync  
\- **State Management:** React Context & Hooks  
\- **Drag & Drop:** @dnd-kit (for sidebar organization)

**Documentation Site (Public Docs)**  
\- **Framework**: Docusaurus (TypeScript)  
\- **Sync Mechanism**: Custom TypeScript script to bridge MongoDB data with Docusaurus filesystem requirements.  
\- **Deployment**: Vercel

\---

**3\. Data Architecture & Flow**

Content Lifecycle  
**1\. Creation/Edit**: An admin edits a page in the \*\*Portal\*\*.  
2\. **Persistence**:  
\- **MongoDB**: Stores the current "live" version of the page and a change log.  
\- **GitHub**: The Backend immediately commits the changes as a \`.md\` file to the configured repository.  
3\. **Sync**:  
\- For the primary workspace (\`docs\`), files are written directly to \`docs-site/docs/\`.  
\- For custom workspaces, files are managed in \`docs-site/workspaces/\` during the build process.  
4\. **Publication**: A rebuild trigger fires a Vercel hook. During the Vercel build, the \`sync-docs.ts\` script fetches all workspace data from the Backend and populates the Docusaurus file structure before the static build begins.

## **Storage Layers**

<table style="min-width: 75px;"><colgroup><col style="min-width: 25px;"><col style="min-width: 25px;"><col style="min-width: 25px;"></colgroup><tbody><tr><th colspan="1" rowspan="1"><p>Layer</p></th><th colspan="1" rowspan="1"><p>Role</p></th><th colspan="1" rowspan="1"><p>Primary Data</p></th></tr><tr><td colspan="1" rowspan="1"><p><strong>MongoDB</strong></p></td><td colspan="1" rowspan="1"><p>Real-time state &amp; App Logic</p></td><td colspan="1" rowspan="1"><p>User accounts, Workspace metadata, Sidebar trees, Drafts.</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>GitHub</strong></p></td><td colspan="1" rowspan="1"><p>Version Control &amp; Source</p></td><td colspan="1" rowspan="1"><p>Markdown content (.md), Sidebar configurations (.json/.ts).</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Vercel</strong></p></td><td colspan="1" rowspan="1"><p>Edge Delivery</p></td><td colspan="1" rowspan="1"><p>Static HTML/JS/CSS assets for the public docs.</p></td></tr></tbody></table>

\---

```
4. Directory Structure
delta-labs-docs/
├── backend/ # FastAPI Application
│ ├── app/
│ │ ├── auth/ # JWT & Google OAuth logic
│ │ ├── routes/ # API Endpoints (Content, Workspaces, etc.)
│ │ ├── services/ # Business logic (GitHub Client, etc.)
│ │ └── models/ # MongoDB schemas
│ └── scripts/
├── portal/ # Next.js Administrator Dashboard
│ ├── src/app/ # Dashboard Pages (Login, Editor, Settings)
│ ├── src/components/ # Atomic Design UI Components
│ └── src/lib/ # API Clients and Utils
├── docs-site/ # Docusaurus Documentation Site
│ ├── docs/ # Static markdown files (Main Workspace)
│ ├── workspaces/ # Dynamic workspace folder (populated during build)
│ ├── scripts/ # Sync scripts (MongoDB -> Filesystem)
│ └── sidebars.ts # Main sidebar configuration
```

\*\*5. Deployment Orchestration  
\*\*The system uses a **Continuous Integration** approach for documentation:  
**1\. Trigger:** User clicks "Trigger Rebuild" in the Portal.  
**2\. API Call:** Backend sends a POST request to the Vercel Deploy Hook.  
**3\. Vercel Pipeline:**  
\- \`git clone\` the latest repo.  
\- \`npm install\`  
\- \`npm run prebuild:sync\` (Runs \`sync-docs.ts\` to pull latest content from MongoDB).  
\- \`npm run build\` (Docusaurus generates static site).  
\- \`deploy\` to edge.

**6\. Key Workflows**

**Creating a New Workspace**  
1\. Define Workspace in Portal.  
2\. Backend creates directory in GitHub (\`workspaces/{slug}\`).  
3\. Backend initializes \`sidebars-{slug}.json\`.  
4\. Backend seeds a "Welcome" page in MongoDB and GitHub.

**Reverting Content**  
1\. Portal fetches commit history from GitHub API via Backend.  
2\. User selects a previous commit.  
3\. Backend fetches raw content from GitHub at that SHA.  
4\. Backend overwrites current file in GitHub and updates MongoDB state.  
5\. Backend triggers a Vercel rebuild to reflect changes publicly.
