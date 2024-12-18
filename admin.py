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

@dp.message_handler(state='msg_all', content_types=types.ContentTypes.ANY)
async def msg_to_all(message: types.Message, state: FSMContext):
    total_users_id = get_all_user_ids()  # Function to fetch all user IDs
    msg_id = message.message_id
    from_chat = message.chat.id  # The ID of the chat where the message originated
    success = 0
    error = 0

    for idx, user_id in enumerate(total_users_id):
        try:
            await bot.copy_message(chat_id=user_id, from_chat_id=from_chat, message_id=msg_id)
            success += 1

            await asyncio.sleep(0.05)  # ~50ms delay


            if (idx + 1) % 30 == 0:
                await asyncio.sleep(1)  # 1 second delay after 30 messages

        except Exception as e:
            error += 1

    # Inform the admin about the results
    await message.answer(f"✅ Ваше сообщение отправлено всем пользователям.\n\n"
                         f"Отправлено: {success}\nНе отправлено: {error}")
    await state.finish()