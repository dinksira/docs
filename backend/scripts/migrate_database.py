"""
Delta Labs — Safe MongoDB Migration Script
===========================================
Copies ALL data from the source database to the target database.
Preserves all documents, indexes, and collection structures.

Usage:
    python scripts/migrate_database.py

The script will:
  1. Connect to both source and target databases
  2. Show a summary of what will be migrated
  3. Ask for confirmation before proceeding
  4. Copy all collections with progress tracking
  5. Recreate indexes
  6. Verify document counts match
  7. Generate a verification report

IMPORTANT: This script READS from source and WRITES to target.
           It does NOT modify or delete anything in the source database.
"""

import asyncio
import sys
import os
from datetime import datetime, timezone

# Add parent directory to path so we can import app modules if needed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.motor_asyncio import AsyncIOMotorClient

# ============================================================
# CONFIGURATION — Update these before running
# ============================================================

# Source: Your OLD database
SOURCE_URI = os.getenv("SOURCE_MONGO_URI", "")
SOURCE_DB_NAME = os.getenv("SOURCE_DATABASE_NAME", "deltalabs")

# Target: Your NEW database
TARGET_URI = os.getenv("MONGO_URI", "")
TARGET_DB_NAME = os.getenv("DATABASE_NAME", "")

# All collections used by Delta Labs
COLLECTIONS = [
    "users",
    "pages",
    "sidebar_tree",
    "portal_workspaces",
    "chat_messages",
    "admin_notes",
    "password_resets",
    "workspaces",       # Notes personal folders
]

# Indexes to recreate on the target
# Format: (collection, field, options)
INDEXES = [
    ("portal_workspaces", "slug", {"unique": True}),
    ("users", "email", {"unique": True}),
    ("pages", "slug", {}),
    ("pages", "workspace", {}),
    ("chat_messages", "createdAt", {}),
    ("admin_notes", "adminId", {}),
    ("password_resets", "email", {}),
]


async def get_collection_stats(db, collection_name: str) -> dict:
    """Get document count and sample doc for a collection."""
    count = await db[collection_name].count_documents({})
    sample = None
    if count > 0:
        sample = await db[collection_name].find_one()
        if sample:
            # Show field names only (not values) for privacy
            sample = list(sample.keys())
    return {"count": count, "fields": sample}


async def migrate_collection(source_db, target_db, collection_name: str) -> dict:
    """
    Copy all documents from source collection to target collection.
    Returns migration stats.
    """
    source_col = source_db[collection_name]
    target_col = target_db[collection_name]

    # Count source documents
    source_count = await source_col.count_documents({})
    if source_count == 0:
        return {"collection": collection_name, "source": 0, "migrated": 0, "status": "SKIPPED (empty)"}

    # Check if target already has data (safety check)
    target_count = await target_col.count_documents({})
    if target_count > 0:
        return {
            "collection": collection_name,
            "source": source_count,
            "migrated": 0,
            "status": f"SKIPPED (target already has {target_count} docs — use --force to overwrite)"
        }

    # Fetch all documents from source
    documents = await source_col.find({}).to_list(length=None)

    # Insert into target in batches of 500
    batch_size = 500
    total_inserted = 0

    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        result = await target_col.insert_many(batch)
        total_inserted += len(result.inserted_ids)
        print(f"    [{collection_name}] Inserted {total_inserted}/{source_count} documents...")

    # Verify count
    final_count = await target_col.count_documents({})
    match = "✅ MATCH" if final_count == source_count else f"❌ MISMATCH (expected {source_count}, got {final_count})"

    return {
        "collection": collection_name,
        "source": source_count,
        "migrated": final_count,
        "status": match
    }


async def create_indexes(target_db):
    """Recreate all indexes on the target database."""
    print("\n📑 Creating indexes...")
    for collection_name, field, options in INDEXES:
        try:
            kwargs = {}
            if options.get("unique"):
                kwargs["unique"] = True
            await target_db[collection_name].create_index(field, **kwargs)
            print(f"    ✅ {collection_name}.{field} (unique={options.get('unique', False)})")
        except Exception as e:
            print(f"    ⚠️  {collection_name}.{field} — {e}")


async def verify_migration(source_db, target_db) -> bool:
    """Verify that all collections have matching document counts."""
    print("\n🔍 Verification — Comparing source vs target...")
    all_match = True

    for col_name in COLLECTIONS:
        source_count = await source_db[col_name].count_documents({})
        target_count = await target_db[col_name].count_documents({})

        if source_count == target_count:
            print(f"    ✅ {col_name}: {source_count} docs (match)")
        else:
            print(f"    ❌ {col_name}: source={source_count}, target={target_count} (MISMATCH)")
            all_match = False

    # Deep verification: spot-check specific documents
    print("\n🔎 Deep verification — Spot-checking critical records...")

    # Check that default workspace exists
    ws = await target_db.portal_workspaces.find_one({"slug": "docs"})
    if ws:
        print(f"    ✅ Default 'Documentation' workspace found (slug='docs')")
    else:
        print(f"    ⚠️  Default 'Documentation' workspace NOT found")

    # Check sidebar tree
    sidebar = await target_db.sidebar_tree.find_one({"_id": "main"})
    if sidebar:
        tree_len = len(sidebar.get("tree", []))
        print(f"    ✅ Main sidebar tree found ({tree_len} root nodes)")
    else:
        print(f"    ⚠️  Main sidebar tree NOT found")

    # Check super admin exists
    super_admin = await target_db.users.find_one({"role": "super_admin", "status": "approved"})
    if super_admin:
        print(f"    ✅ Super admin found: {super_admin.get('email', 'N/A')}")
    else:
        print(f"    ⚠️  No approved super admin found")

    return all_match


async def main():
    # ── Validate configuration ──
    if not TARGET_URI or not TARGET_DB_NAME:
        print("=" * 60)
        print("❌ ERROR: You must configure TARGET_URI and TARGET_DB_NAME")
        print("   Open this script and fill in lines 47-48")
        print("=" * 60)
        return

    if TARGET_URI == SOURCE_URI and TARGET_DB_NAME == SOURCE_DB_NAME:
        print("❌ ERROR: Source and target are the same database!")
        return

    force = "--force" in sys.argv

    print("=" * 60)
    print("  Delta Labs — MongoDB Migration Tool")
    print("=" * 60)
    print(f"\n  Source: {SOURCE_DB_NAME} @ {SOURCE_URI[:50]}...")
    print(f"  Target: {TARGET_DB_NAME} @ {TARGET_URI[:50]}...")
    print(f"  Mode:   {'FORCE (will overwrite existing data)' if force else 'SAFE (skip non-empty collections)'}")
    print()

    # ── Connect to both databases ──
    print("🔌 Connecting to source database...")
    source_client = AsyncIOMotorClient(SOURCE_URI)
    source_db = source_client[SOURCE_DB_NAME]

    # Test source connection
    try:
        await source_db.command("ping")
        print("    ✅ Source connected")
    except Exception as e:
        print(f"    ❌ Source connection failed: {e}")
        return

    print("🔌 Connecting to target database...")
    target_client = AsyncIOMotorClient(TARGET_URI)
    target_db = target_client[TARGET_DB_NAME]

    # Test target connection
    try:
        await target_db.command("ping")
        print("    ✅ Target connected")
    except Exception as e:
        print(f"    ❌ Target connection failed: {e}")
        return

    # ── Pre-migration summary ──
    print("\n📊 Pre-Migration Summary:")
    print("-" * 50)

    total_docs = 0
    for col_name in COLLECTIONS:
        stats = await get_collection_stats(source_db, col_name)
        total_docs += stats["count"]
        fields_str = f" — fields: {stats['fields']}" if stats["fields"] else ""
        print(f"    {col_name}: {stats['count']} documents{fields_str}")

    print(f"\n    TOTAL: {total_docs} documents across {len(COLLECTIONS)} collections")
    print("-" * 50)

    # ── If --force, clear target collections ──
    if force:
        target_has_data = False
        for col_name in COLLECTIONS:
            count = await target_db[col_name].count_documents({})
            if count > 0:
                target_has_data = True
                break

        if target_has_data:
            print("\n⚠️  --force mode: Target database has existing data.")
            confirm = input("    Type 'DELETE' to clear target collections before migration: ").strip()
            if confirm != "DELETE":
                print("    Aborted.")
                return
            for col_name in COLLECTIONS:
                await target_db[col_name].delete_many({})
                print(f"    🗑️  Cleared {col_name}")

    # ── Confirm migration ──
    print(f"\n⚡ Ready to migrate {total_docs} documents to the new database.")
    confirm = input("    Type 'YES' to proceed: ").strip()
    if confirm != "YES":
        print("    Migration cancelled.")
        return

    # ── Run migration ──
    print("\n🚀 Starting migration...\n")
    start_time = datetime.now(timezone.utc)
    results = []

    for col_name in COLLECTIONS:
        result = await migrate_collection(source_db, target_db, col_name)
        results.append(result)
        print(f"    {result['status']}")

    # ── Create indexes ──
    await create_indexes(target_db)

    # ── Verify ──
    all_match = await verify_migration(source_db, target_db)

    # ── Final report ──
    elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()
    print("\n" + "=" * 60)
    print("  MIGRATION REPORT")
    print("=" * 60)
    print(f"  Duration: {elapsed:.1f} seconds")
    print(f"  Status:   {'✅ ALL COLLECTIONS VERIFIED' if all_match else '⚠️  SOME MISMATCHES DETECTED'}")
    print()

    for r in results:
        print(f"    {r['collection']:25s} {r['source']:>5d} → {r['migrated']:>5d}  {r['status']}")

    print("\n" + "=" * 60)

    if all_match:
        print("\n✅ Migration complete! Next steps:")
        print("   1. Update backend/.env with the new MONGO_URI and DATABASE_NAME")
        print("   2. Update Render environment variables")
        print("   3. Restart the backend service")
        print("   4. Test login, page editing, and workspace switching")
        print("   5. Keep the old database as backup for at least 7 days")
    else:
        print("\n⚠️  Some collections didn't match. Review the report above.")
        print("   Do NOT switch to the new database until all issues are resolved.")

    # Cleanup
    source_client.close()
    target_client.close()


if __name__ == "__main__":
    asyncio.run(main())
