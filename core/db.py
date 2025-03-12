import aiosqlite
from datetime import datetime, timedelta

DB_PATH = "bot.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            name TEXT NOT NULL,
            username TEXT,
            rating INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()

async def user_exists(telegram_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,)) as cursor:
            return await cursor.fetchone() is not None

async def add_user(telegram_id: int, name: str, username: str | None):
    if not await user_exists(telegram_id):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO users (telegram_id, name, username) VALUES (?, ?, ?)",
                (telegram_id, name, username)
            )
            await db.commit()

async def count_users() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            return (await cursor.fetchone())[0]

async def count_users_last_24h() -> int:
    # Calculate the timestamp for 24 hours ago
    last_24h = datetime.now() - timedelta(hours=24)
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT COUNT(*) FROM users WHERE created_at >= ?",
            (last_24h,)
        ) as cursor:
            result = await cursor.fetchone()
            return result[0]

async def get_user_ids() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT telegram_id FROM users") as cursor:
            return [row[0] for row in await cursor.fetchall()]

async def save_rating(telegram_id: int, rating: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET rating = ? WHERE telegram_id = ?", (rating, telegram_id))
        await db.commit()

async def get_rating(telegram_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT rating FROM users WHERE telegram_id = ?", (telegram_id,)) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def get_all_ratings() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT rating FROM users WHERE rating != 0") as cursor:
            return [row[0] for row in await cursor.fetchall()]

async def get_users_with_ratings() -> list[tuple[int, str, int]]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT telegram_id, name, rating FROM users WHERE rating != 0") as cursor:
            return await cursor.fetchall()

async def on_startup():
    await init_db()