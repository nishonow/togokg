from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
import asyncio
from config import ADMINS
from db import user_exists, add_user, count_users, get_all_user_ids
from loader import dp, bot

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='Пользователи'))
menu.add(KeyboardButton(text='Отправить сообщение'))

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Нет", callback_data='no')]
    ]
)

@dp.message_handler(user_id=ADMINS, text='/admin')
async def welcome_admin(message: Message):
    await message.answer("Добро пожаловать, администратор, что вы хотите?", reply_markup=menu)


@dp.message_handler(user_id=ADMINS, text='Пользователи')
async def get_users_count(message: types.Message):
    total_users = count_users()

    await message.answer(f"У нас {total_users} пользователей.")

@dp.message_handler(user_id=ADMINS, text="Отправить сообщение")
async def msg_all(message: types.Message, state: FSMContext):
    await message.answer("Отправьте мне сообщение и я разошлю его всем нашим пользователям.\n\nЧто бы отменить нажмите «Нет»", reply_markup=cancel)
    await state.set_state('msg_all')

@dp.callback_query_handler(text='no', state='msg_all')
async def no_msg_all(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Отправка сообщения отменено.")
    await state.finish()

@dp.message_handler(state='msg_all', content_types='any')
async def msg_to_all(message: types.Message, state: FSMContext):
    total_users_id = get_all_user_ids()
    msg_id = message.message_id
    from_chat = message.from_user.id
    success = 0
    error = 0
    for idx, id in enumerate(total_users_id):
        try:
            await bot.copy_message(id, from_chat, msg_id)
            success += 1
            
            if idx % 30 == 0:
                await asyncio.sleep(1)

        except:
            error += 1
    await message.answer(f"Ваше сообщение отправлено всем пользователям.\nОтправлено: {success}\nНе отправлено: {error}")
    await state.finish()
