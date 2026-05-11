---
title: Ws:Folder Structure:Utilsts
sidebar_label: Ws:Folder Structure:Utilsts
id: utilsts
---

```typescript
/** ################################ COMPONENT ############################# */
/** Main exported component logic for this file. */
/** Shared utility helpers for theme primitives. */
export function cx(...classes: Array<string | false | null | undefined>): string {
  return classes.filter(Boolean).join(" ");
}
/** ################################ /COMPONENT ############################# */
```
