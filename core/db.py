import aiosqlite
import datetime

DB_PATH = "../bot.db"

# Initialize database
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            name TEXT NOT NULL,
            username TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL
        )
        """)

        await db.commit()

# Check if a user exists by Telegram ID
async def user_exists(telegram_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,)) as cursor:
            exists = await cursor.fetchone() is not None
    return exists

# Add a user (only if new)
async def add_user(telegram_id, name, username):
    if not await user_exists(telegram_id):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
            INSERT INTO users (telegram_id, name, username) 
            VALUES (?, ?, ?)
            """, (telegram_id, name, username))
            await db.commit()

# Count total users
async def count_users():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            total_users = (await cursor.fetchone())[0]
    return total_users

async def get_user_ids():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT telegram_id FROM users") as cursor:
            telegram_ids = [row[0] for row in await cursor.fetchall()]
    return telegram_ids



async def on_startup():
    await init_db()