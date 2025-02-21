from aiogram import executor
from loader import dp, db
import core
import handlers
import logging

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)

async def on_startup(dp):
    await db.create()
    await db.create_table_users()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)