import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from datetime import datetime

# Load the .env file from the current directory
load_dotenv()

async def seed_user():
    url = os.getenv('MONGO_URI')
    db_name = os.getenv('DATABASE_NAME')
    
    if not url:
        print("❌ Error: MONGO_URI not found in .env")
        return

    print(f"Connecting to: {url.split('@')[-1]}...") # Don't print password
    client = AsyncIOMotorClient(url)
    db = client[db_name]
    
    user_email = 'dinksiraelisa@gmail.com'
    user_password = '12345678'
    
    user_data = {
        'name': 'Dinksira Elisa',
        'email': user_email,
        'passwordHash': user_password, # System uses plain text
        'role': 'super_admin',         # Give full permissions
        'status': 'approved',          # Allow login immediately
        'createdAt': datetime.utcnow(),
        'method': 'google'             # Mark as google-capable
    }
    
    print(f"Upserting user {user_email} into database {db_name}...")
    
    result = await db.users.update_one(
        {'email': user_email},
        {'$set': user_data},
        upsert=True
    )
    
    if result.upserted_id:
        print(f"✅ Success: New user created with ID {result.upserted_id}")
    else:
        print(f"✅ Success: Existing user updated")
        
    client.close()

if __name__ == '__main__':
    asyncio.run(seed_user())
