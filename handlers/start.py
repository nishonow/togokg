from aiogram.types import Message
from core.db import user_exists, add_user
from core.keys import main_menu, to_bot
from loader import dp

@dp.message_handler(text='/start')
async def new_user(message: Message):
    telegram_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username

    if not await user_exists(telegram_id):
        await add_user(telegram_id, name, username)

    await message.answer("Здравствуйте! Вас приветствует служба поддержки ToGo.Kgz. Пожалуйста выберите язык обслуживания😇\n\n"
                         "Саламатсызбы! ToGo.Kgz колдоо тобуна кош келиңиз. Кызмат тилин тандаңыз😇",
                         reply_markup=main_menu)

@dp.message_handler(text='/start@ToGoKgz_Bot')
async def new_group(message: Message):

    await message.answer("Здравствуйте! Что бы мы могли вам помочь пожалуйста перейдите к нашему боту\n\n"
                         "Саламатсызбы! Биз сизге жардам беришибиз үчүн, биздин ботко кириңиз",
                         reply_markup=to_bot)
