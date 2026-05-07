# Delta Labs Docs — Unified Coding Standards

This document defines the engineering standards, architectural patterns, and best practices for the Delta Labs Documentation System. All contributors must adhere to these standards to maintain codebase health, security, and scalability.

---

## 1. Core Principles
- **Pragmatic Simplicity**: Prefer straightforward, readable code over complex abstractions.
- **Explicit Context**: Be explicit about types (TypeScript) and schemas (Pydantic).
- **Graceful Failure**: Services should fail silently (logged), and routes should return user-friendly errors. Never leak stack traces.
- **Source of Truth**: 
    - **GitHub**: Source of truth for content (.md) and configuration (.ts/.json).
    - **MongoDB**: Source of truth for application state (users, drafts, logs).

---

## 2. Backend Standards (Python / FastAPI)

### 2.1 Architecture
- **Framework**: FastAPI (Async-first).
- **Database**: MongoDB via `motor` (Async driver).
- **Structure**:
    - `app/routes/`: One router per domain logic (auth, content, workspaces).
    - `app/services/`: Reusable business logic (Email, SMS, GitHub).
    - `app/schemas/`: Pydantic models for request validation and response shapes.
    - `app/models/`: Database document schemas.

### 2.2 Route Pattern
All routes should follow a standard dependency injection pattern:
```python
@router.post("/save")
async def save_content(
    request: ContentSaveRequest,
    db=Depends(get_db),
    current_user=Depends(admin_only)
):
    # Logic...
    return {"success": True}
```

### 2.3 Naming Conventions
- **Files/Functions/Variables**: `snake_case`.
- **Classes/Models**: `PascalCase`.
- **Constants**: `UPPER_SNAKE_CASE`.

### 2.4 Error Handling
- Use `HTTPException` for client-facing errors.
- Use `logging.getLogger(__name__)` for system logs. Avoid `print()`.

---

## 3. Frontend Standards (Next.js / React)

### 3.1 Architecture
- **Framework**: Next.js (App Router).
- **Language**: TypeScript (Strict mode preferred).
- **Styling**: Tailwind CSS + CSS Custom Properties for design tokens.
- **State**: React Context/Hooks for local state; `localStorage` for persistent drafts and tokens.

### 3.2 Component Design
- **Client Components**: Use `'use client'` for interactive pages.
- **Shared Components**: Located in `src/components/`, named using `PascalCase.tsx`.
- **Atomic Design**: Components should be reusable and focused on a single concern.

### 3.3 State Management Singleton Pattern
For complex cross-component state (like drafts), use a singleton store:
```typescript
class DraftStore {
  private static instance: DraftStore;
  // logic...
}
export const draftStore = DraftStore.getInstance();
```

### 3.4 API Communication
Always use the centralized `api` client (`src/lib/api.ts`) which handles:
- Authorization header attachment.
- Automatic 401 redirect to `/login`.
- Environment-based base URL selection.

---

## 4. Documentation & Content Standards

### 4.1 Slug Management
- **Format**: Lowercase, kebab-case (e.g., `getting-started`).
- **Hierarchy**: Use forward slashes for nesting (e.g., `api/auth/login`).
- **Sanitization**: Backend automatically strips numbered prefixes (e.g., `01-intro` -> `intro`).

### 4.2 Content Persistence
- **Markdown**: All documentation is stored as standard Markdown with frontmatter.
- **Frontmatter Fields**:
    - `title`: Display title.
    - `sidebar_label`: Label used in the navigation tree.
    - `id`: Unique identifier (sanitized slug).

---

## 5. Security Standards

- **Authentication**: JWT-based. Tokens expire in 24 hours.
- **2FA**: Mandatory SMS/Email OTP for all admin logins.
- **Authorization**: Role-based access control (RBAC).
    - `super_admin`: Full system access.
    - `admin`: Content and workspace management.
- **Data Protection**: 
    - Never commit `.env` files.
    - Validate all inputs using Pydantic (Backend) and TypeScript types (Frontend).

---

## 6. Git & Workflow

- **Branching**: `main` is the primary branch.
- **Commit Messages**: Use semantic prefixes:
    - `feat:`: New feature.
    - `fix:`: Bug fix.
    - `docs:`: Documentation update.
    - `chore:`: Maintenance.
- **Automated Sync**: Every content save triggers a GitHub commit and a Vercel rebuild.
