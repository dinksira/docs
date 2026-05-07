"""
Delta Labs — Post-Migration Verification Script
================================================
Run this AFTER switching to the new database to verify
that the backend can operate correctly.

Usage:
    python scripts/verify_migration.py

This script:
  1. Connects to the database using the CURRENT .env config
  2. Checks all collections exist and have data
  3. Verifies indexes
  4. Tests critical queries (the same ones the app uses)
  5. Checks user auth flow readiness
  6. Outputs a full health report
"""

import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load the CURRENT .env (should already point to the new DB)
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

EXPECTED_COLLECTIONS = [
    "users",
    "pages",
    "sidebar_tree",
    "portal_workspaces",
    "chat_messages",
    "admin_notes",
    "password_resets",
    "workspaces",
]


async def main():
    print("=" * 60)
    print("  Delta Labs — Post-Migration Health Check")
    print("=" * 60)
    print(f"\n  Database: {DATABASE_NAME}")
    print(f"  URI:      {MONGO_URI[:50]}...")
    print()

    # 1. Connect
    print("🔌 Connecting...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]

    try:
        await db.command("ping")
        print("    ✅ Connection successful")
    except Exception as e:
        print(f"    ❌ Connection FAILED: {e}")
        return

    passed = 0
    failed = 0
    warnings = 0

    # 2. Check all collections exist
    print("\n📦 Collection Check:")
    existing = await db.list_collection_names()
    for col in EXPECTED_COLLECTIONS:
        count = await db[col].count_documents({})
        if col in existing and count > 0:
            print(f"    ✅ {col}: {count} documents")
            passed += 1
        elif col in existing:
            print(f"    ⚠️  {col}: exists but EMPTY (0 documents)")
            warnings += 1
        else:
            print(f"    ❌ {col}: MISSING")
            failed += 1

    # 3. Check indexes
    print("\n📑 Index Check:")
    
    # portal_workspaces.slug unique
    ws_indexes = await db.portal_workspaces.index_information()
    slug_unique = any(
        idx.get("unique") and any(k[0] == "slug" for k in idx.get("key", []))
        for idx in ws_indexes.values()
    )
    if slug_unique:
        print("    ✅ portal_workspaces.slug (unique)")
        passed += 1
    else:
        print("    ⚠️  portal_workspaces.slug unique index MISSING")
        warnings += 1

    # 4. Critical query tests
    print("\n🔍 Critical Query Tests:")

    # Test: Default workspace exists
    docs_ws = await db.portal_workspaces.find_one({"slug": "docs"})
    if docs_ws:
        print(f"    ✅ Default 'Documentation' workspace found")
        passed += 1
    else:
        print(f"    ❌ Default 'Documentation' workspace MISSING — app startup will auto-create it")
        warnings += 1

    # Test: At least one super admin exists
    super_admin = await db.users.find_one({"role": "super_admin", "status": "approved"})
    if super_admin:
        print(f"    ✅ Super admin exists: {super_admin.get('name', 'N/A')} ({super_admin.get('email', 'N/A')})")
        passed += 1
    else:
        print(f"    ❌ No approved super admin found — NO ONE CAN LOG IN")
        failed += 1

    # Test: Main sidebar tree exists
    main_tree = await db.sidebar_tree.find_one({"_id": "main"})
    if main_tree:
        tree_nodes = len(main_tree.get("tree", []))
        print(f"    ✅ Main sidebar tree: {tree_nodes} root nodes")
        passed += 1
    else:
        print(f"    ⚠️  Main sidebar tree MISSING — sidebar will show empty")
        warnings += 1

    # Test: Pages exist for docs workspace
    docs_pages = await db.pages.count_documents({
        "$or": [{"workspace": {"$exists": False}}, {"workspace": "docs"}]
    })
    if docs_pages > 0:
        print(f"    ✅ Documentation pages: {docs_pages} pages")
        passed += 1
    else:
        print(f"    ⚠️  No documentation pages found")
        warnings += 1

    # Test: Workspace listing query works
    workspaces = await db.portal_workspaces.find().sort("order", 1).to_list(200)
    print(f"    ✅ Workspace listing: {len(workspaces)} workspaces")
    for ws in workspaces:
        # Check that each workspace has a sidebar tree
        tree_id = "main" if ws["slug"] == "docs" else f"ws_{ws['slug']}"
        tree = await db.sidebar_tree.find_one({"_id": tree_id})
        has_tree = "✅" if tree else "⚠️ no tree"
        ws_pages = await db.pages.count_documents({"workspace": ws["slug"]}) if ws["slug"] != "docs" else docs_pages
        print(f"        {ws['name']} (slug={ws['slug']}) — {ws_pages} pages, {has_tree}")
    passed += 1

    # Test: Users query
    total_users = await db.users.count_documents({})
    approved = await db.users.count_documents({"status": "approved"})
    pending = await db.users.count_documents({"status": "pending"})
    print(f"    ✅ Users: {total_users} total ({approved} approved, {pending} pending)")
    passed += 1

    # Test: Chat messages query
    chat_count = await db.chat_messages.count_documents({})
    if chat_count > 0:
        latest = await db.chat_messages.find().sort("createdAt", -1).limit(1).to_list(1)
        if latest:
            print(f"    ✅ Chat: {chat_count} messages (latest: {latest[0].get('createdAt', 'N/A')})")
    else:
        print(f"    ✅ Chat: 0 messages (collection ready)")
    passed += 1

    # 5. Final report
    print("\n" + "=" * 60)
    print("  HEALTH CHECK REPORT")
    print("=" * 60)
    print(f"    ✅ Passed:   {passed}")
    print(f"    ⚠️  Warnings: {warnings}")
    print(f"    ❌ Failed:   {failed}")
    print()

    if failed == 0 and warnings == 0:
        print("  🎉 PERFECT — Database is fully operational!")
    elif failed == 0:
        print("  ✅ GOOD — Database is functional with minor warnings.")
        print("     Warnings are non-blocking; the app will handle them.")
    else:
        print("  ❌ ISSUES DETECTED — Review failures above before going live.")

    print("=" * 60)
    client.close()


if __name__ == "__main__":
    asyncio.run(main())
