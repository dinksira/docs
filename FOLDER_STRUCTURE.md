# Delta Labs Docs — Project Folder Structure

This document provides a detailed breakdown of the project's directory hierarchy, explaining the purpose of each major module and file.

---****

## 1. Root Directory Structure
The project is organized as a monorepo containing the backend API, the admin portal, and the public documentation site.

```text
delta-labs-docs/
├── backend/               # FastAPI (Python) Backend Service
├── portal/                # Next.js (TypeScript) Admin Dashboard
├── docs-site/             # Docusaurus (TypeScript) Documentation Site
├── SYSTEM_ARCHITECTURE.md # High-level technical overview
├── CODING_STANDARDS.md    # Engineering best practices
├── DESIGN_SYSTEM.md       # Visual design tokens and UI guide
└── FOLDER_STRUCTURE.md    # This file
```

---

## 2. Backend Service (`/backend`)
The backend follows a standard FastAPI structure optimized for cloud deployment.

```text
backend/
├── app/
│   ├── auth/              # JWT, hashing, and OAuth logic
│   ├── middleware/        # Request logging and auth guards
│   ├── models/            # MongoDB document schemas (Pydantic)
│   ├── routes/            # API endpoints (auth, content, workspaces, etc.)
│   ├── schemas/           # Request/Response data shapes
│   ├── services/          # Business logic (GitHub, Email, SMS)
│   ├── config.py          # Environment settings loader
│   ├── database.py        # MongoDB connection management
│   └── main.py            # Application entry point
├── scripts/               # Maintenance, migration, and seed scripts
├── .env                   # Local environment variables
├── requirements.txt       # Python dependencies
└── render.yaml            # Render.com deployment configuration
```

---

## 3. Admin Portal (`/portal`)
A Next.js 16.1.6 application using the App Router for the administrative CMS.

```text
portal/
├── src/
│   ├── app/               # Next.js Pages and Layouts
│   │   ├── admin/         # Super-admin management pages
│   │   ├── chat/          # Team collaboration page
│   │   ├── docs/          # Main documentation editor (Dynamic)
│   │   ├── login/         # Authentication and password reset
│   │   ├── notes/         # Personal workspace notes
│   │   └── signup/        # New admin request form
│   ├── components/        # Reusable UI components
│   │   ├── RichEditor/    # TipTap editor wrapper and extensions
│   │   ├── HistoryModal/  # GitHub commit history viewer
│   │   └── ...            # Navbars, Sidebars, Modals, Buttons
│   ├── lib/               # Shared logic and utilities
│   │   ├── api.ts         # Centralized Fetch/API client
│   │   ├── draftStore.ts  # LocalStorage draft management
│   │   └── utils.ts       # Formatting and color helpers
│   └── styles/            # CSS tokens and design system
└── tailwind.config.ts     # Tailwind styling configuration
```

---

## 4. Documentation Site (`/docs-site`)
A Docusaurus 3.9.2 static-site generator that serves the final content.

```text
docs-site/
├── docs/                  # Markdown files for the main workspace
├── workspaces/            # Auto-generated folders for custom workspaces
├── scripts/               # Sync script (MongoDB -> Filesystem)
│   └── sync-docs.ts       # Core logic for content synchronization
├── src/                   # Custom React components and theme overrides
│   ├── components/        # Login guards and UI features
│   ├── css/               # Global CSS and theme variables
│   └── theme/             # Docusaurus theme extensions
├── sidebars.ts            # Main sidebar configuration (Auto-generated)
├── static/                # Static assets (images, fonts, favicons)
├── docusaurus.config.ts   # Core Docusaurus configuration
└── package.json           # Docusaurus and sync script dependencies
```

---

## 5. Summary of Key Files

| File | Location | Purpose |
| :--- | :--- | :--- |
| `main.py` | `backend/app/` | Initializes the FastAPI app and mounts all routers. |
| `github_client.py` | `backend/app/` | Handles all communication with the GitHub API. |
| `sync-docs.ts` | `docs-site/scripts/` | Bridges the dynamic database content into the static site. |
| `draftStore.ts` | `portal/src/lib/` | Prevents data loss by saving un-published edits locally. |
| `design-system.css` | `portal/src/styles/` | The "Source of Truth" for all visual styles and tokens. |
