from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            host=config.DB_HOST
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    return await connection.fetch(command, *args)
                elif fetchval:
                    return await connection.fetchval(command, *args)
                elif fetchrow:
                    return await connection.fetchrow(command, *args)
                elif execute:
                    return await connection.execute(command, *args)
    async def create_table_users(self):
        command = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            username TEXT,
            rating INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        await self.execute(command, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, name, username):
        command = """
        INSERT INTO users (telegram_id, name, username) 
        VALUES ($1, $2, $3)
        """
        await self.execute(command, telegram_id, name, username, execute=True)

    async def user_exists(self, telegram_id):
        command = """
        SELECT 1 FROM users WHERE telegram_id = $1
        """
        return await self.execute(command, telegram_id, fetchval=True)

    async def count_users(self):
        command = """
        SELECT COUNT(*) FROM users
        """
        return await self.execute(command, fetchval=True)

    async def get_user_ids(self):
        command = """
        SELECT telegram_id FROM users
        """
        records = await self.execute(command, fetch=True)
        return [record['telegram_id'] for record in records]

    async def save_rating(self, telegram_id, rating):
        command = """
        UPDATE users SET rating = $1 WHERE telegram_id = $2
        """
        await self.execute(command, rating, telegram_id, execute=True)

    async def get_rating(self, telegram_id):
        command = """
        SELECT rating FROM users WHERE telegram_id = $1
        """
        return await self.execute(command, telegram_id, fetchval=True)

    async def get_all_ratings(self):
        command = """
        SELECT rating FROM users
        """
        return await self.execute(command, fetch=True)
