import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

async def verify():
    url = os.getenv('MONGO_URI')
    db_name = os.getenv('DATABASE_NAME')
    client = AsyncIOMotorClient(url)
    db = client[db_name]
    
    user = await db.users.find_one({'email': 'dinksiraelisa@gmail.com'})
    if user:
        print(f"SUCCESS: User found!")
        print(f"Email: {user.get('email')}")
        print(f"Role: {user.get('role')}")
        print(f"Status: {user.get('status')}")
    else:
        print("FAILURE: User not found.")
    
    client.close()

if __name__ == '__main__':
    asyncio.run(verify())
