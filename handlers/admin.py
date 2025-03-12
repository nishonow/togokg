from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
import asyncio
from config import ADMINS
from core.db import get_user_ids, count_users, count_users_last_24h, get_all_ratings, get_users_with_ratings
from loader import dp, bot
from datetime import datetime
import pytz

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='👥 Пользователи'))
menu.add(KeyboardButton(text='📢 Отправить сообщение'))
menu.add(KeyboardButton(text='⭐ Посмотреть оценку'))

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="❌ Отмена", callback_data='no')]
    ]
)

ratings_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👀 Показать оценки", callback_data="see_ratings:0")]
    ]
)

confirm_broadcast = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Да", callback_data="confirm_broadcast"),
         InlineKeyboardButton(text="❌ Нет", callback_data="cancel_broadcast")]
    ]
)

USERS_PER_PAGE = 20

@dp.message_handler(user_id=ADMINS, text='/admin')
async def welcome_admin(message: Message):
    await message.answer("👋 Привет, администратор! Чем могу помочь?", reply_markup=menu)

@dp.message_handler(user_id=ADMINS, text='⭐ Посмотреть оценку')
async def show_ratings(message: types.Message):
    all_ratings = await get_all_ratings()
    average = sum(all_ratings) / len(all_ratings) if all_ratings else 0
    formatted_average = f"{average:.2f}"
    await message.answer(f"📊 Средняя оценка: {formatted_average} ⭐\n"
                         f"📈 Всего оценок: {len(all_ratings)}",
                         reply_markup=ratings_button)

@dp.callback_query_handler(lambda c: c.data.startswith("see_ratings"))
async def handle_see_ratings(callback: CallbackQuery):
    page = int(callback.data.split(":")[1])
    users_with_ratings = await get_users_with_ratings()
    if not users_with_ratings:
        await callback.message.edit_text("😕 Нет пользователей с оценками.")
        return

    total_users = len(users_with_ratings)
    total_pages = (total_users + USERS_PER_PAGE - 1) // USERS_PER_PAGE
    start_idx = page * USERS_PER_PAGE
    end_idx = min(start_idx + USERS_PER_PAGE, total_users)
    paginated_users = users_with_ratings[start_idx:end_idx]

    response = f"👥 Пользователи с оценками (Страница {page + 1}/{total_pages}):\n\n"
    for telegram_id, name, rating in paginated_users:
        user_link = f"tg://user?id={telegram_id}"
        response += f"[{name}]({user_link}) - {rating} ⭐\n"

    nav_buttons = [
        InlineKeyboardButton(text="⬅️ Назад", callback_data=f"see_ratings:{page - 1}") if page > 0 else None,
        InlineKeyboardButton(text="➡️ Вперед", callback_data=f"see_ratings:{page + 1}") if page < total_pages - 1 else None
    ]
    nav_buttons = [btn for btn in nav_buttons if btn]
    back_button = [InlineKeyboardButton(text="🔙 Вернуться", callback_data="back_to_ratings")]

    pagination_keyboard = InlineKeyboardMarkup(inline_keyboard=[nav_buttons, back_button])
    await callback.message.edit_text(response, reply_markup=pagination_keyboard, parse_mode="Markdown",
                                     disable_web_page_preview=True)

@dp.callback_query_handler(text="back_to_ratings")
async def handle_back_to_ratings(callback: CallbackQuery):
    all_ratings = await get_all_ratings()
    average = sum(all_ratings) / len(all_ratings) if all_ratings else 0
    formatted_average = f"{average:.2f}"
    await callback.message.edit_text(f"📊 Средняя оценка: {formatted_average} ⭐\n"
                                     f"📈 Всего оценок: {len(all_ratings)}",
                                     reply_markup=ratings_button)

@dp.message_handler(user_id=ADMINS, text='👥 Пользователи')
async def get_users_count(message: types.Message):
    total_users = await count_users()
    last_24h_users = await count_users_last_24h()
    timestamp = datetime.now(pytz.timezone('Asia/Bishkek')).strftime('%H:%M:%S %d.%m.%Y')
    await message.answer(f"📊 Статистика пользователей:\n"
                         f"👥 Всего: {total_users}\n"
                         f"🆕 Новых за 24 часа: {last_24h_users}\n"
                         f"⏰ Обновлено: {timestamp}",)


@dp.message_handler(user_id=ADMINS, text="📢 Отправить сообщение")
async def msg_all(message: types.Message, state: FSMContext):
    message_send = await message.answer(
        "✍️ Введите сообщение для рассылки всем пользователям.\n\nНажмите «❌ Отмена», чтобы отменить.",
        reply_markup=cancel)
    await state.set_state('msg_all')
    await state.update_data(prompt_msg_id=message_send.message_id)

@dp.callback_query_handler(text='no', state='msg_all')
async def no_msg_all(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("🚫 Рассылка отменена.")
    await state.finish()

@dp.message_handler(state='msg_all', content_types=types.ContentTypes.ANY)
async def msg_to_all(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    prompt_msg_id = state_data['prompt_msg_id']
    await bot.edit_message_reply_markup(chat_id=message.from_user.id, message_id=prompt_msg_id, reply_markup=None)
    await state.update_data(msg_id=message.message_id, from_chat=message.chat.id)

    await bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )
    await message.answer("👀 Это предварительный просмотр.\nОтправить всем пользователям?", reply_markup=confirm_broadcast)

@dp.callback_query_handler(text="confirm_broadcast", state='msg_all')
async def confirm_broadcast_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    data = await state.get_data()
    msg_id = data['msg_id']
    from_chat = data['from_chat']

    total_users_id = await get_user_ids()
    total = len(total_users_id)
    success = 0
    error = 0

    progress_msg = await callback.message.answer(f"📤 Отправка сообщения...\n📊 Прогресс: 0/{total}")
    await state.finish()
    for i, user_id in enumerate(total_users_id, 1):
        try:
            await bot.copy_message(chat_id=user_id, from_chat_id=from_chat, message_id=msg_id)
            success += 1
        except Exception:
            error += 1

        if i % 10 == 0 or i == total:
            await bot.edit_message_text(
                f"📤 Отправка сообщения...\n📊 Прогресс: {success + error}/{total}",
                chat_id=callback.message.chat.id,
                message_id=progress_msg.message_id
            )
        await asyncio.sleep(0.04)

    await callback.message.answer(
        f"✅ Рассылка завершена!\n\n📬 Отправлено: {success}\n❌ Не отправлено: {error}")

@dp.callback_query_handler(text="cancel_broadcast", state='msg_all')
async def cancel_broadcast_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer("🚫 Рассылка отменена.")
    await state.finish()