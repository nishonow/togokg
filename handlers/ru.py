import asyncio

from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from core.db import save_rating, get_all_ratings
from loader import dp, bot
from core.keys import (
    ru_menu_keyboard,
    ru_payment_keyboard,
    ru_bonus_replenishment_keyboard,
    ru_fine_amount_keyboard,
    ru_scooter_problems_keyboard,
    ru_registration_keyboard,
    contact_ru, rating_keyboard
)

CHANNEL_ID = -1002276623671
RENT_SCOOTER_ID = 18
RU_PAYMENT_CARD = 22 # need to edit this to not send video
RU_PAYMENT_MBANK = 21
RU_PAYMENT_ODENGI = 7
RU_BONUS_CARD = 22
RU_BONUS_MBANK = 23
RU_BONUS_ODENGI = 10
RU_REGISTRATION_PHONE = 19
RU_REGISTRATION_TELEGRAM = 20

# RATING HANDLERS ===========================================================
# @dp.message_handler(text='/rating')
# async def rating(message: Message):
#     user_rating = await db.get_rating(message.from_user.id)
#     if user_rating != 0:
#         await message.answer(f"Вы уже оценили нашего бота на {user_rating} ⭐\n\nВы можете изменить свой оценкa", reply_markup=rating_keyboard)
#     else:
#         await message.answer("Пожалуйста, оцените нашего бота", reply_markup=rating_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('rating_'))
async def save_user_rating(call: CallbackQuery):
    rating = int(call.data.split('_')[1])
    await save_rating(call.from_user.id, rating)
    await call.message.edit_reply_markup()
    await call.message.answer("Спасибо за вашу оценку!")


async def send_ask(chat_id):
    await asyncio.sleep(60)  # Wait for 1 minute
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Да", callback_data="video_solved_yes"),
        InlineKeyboardButton(text="Нет", callback_data="video_solved_no")
    )
    await bot.send_message(chat_id, "Помогло ли это видео решить вашу проблему?", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ["video_solved_yes", "video_solved_no"])
async def handle_video_response(call: CallbackQuery):
    if call.data == "video_solved_yes":
        await call.message.edit_reply_markup()
        await call.message.answer("Пожалуйста оцените помощь нашего бота🫶", reply_markup=rating_keyboard)
    elif call.data == "video_solved_no":
        await call.message.edit_reply_markup()
        await call.message.answer("Пожалуйста, свяжитесь с нашим администратором для получения дальнейшей помощи.", reply_markup=contact_ru)

# MENU HANDLERS ==============================================================
@dp.callback_query_handler(text='lang_ru')
async def ru_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Отлично! Чем мы можем вам помочь?", reply_markup=ru_menu_keyboard)

# PAYMENT HANDLERS ===========================================================
@dp.callback_query_handler(text='ru_payment_issue')
async def ru_payment(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Выберите ваш способ оплаты", reply_markup=ru_payment_keyboard)

@dp.callback_query_handler(text='ru_payment_card')
async def ru_payment_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_CARD, caption=msg)
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_payment_mbank')
async def ru_payment_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео. Если запросить статус не удалось, то пожалуйста обратитесь к вашему банку.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_MBANK, caption=msg)
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_payment_odengi')
async def ru_payment_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_ODENGI, caption=msg)
    await send_ask(call.message.chat.id)

# BONUS HANDLERS =============================================================
@dp.callback_query_handler(text='ru_replenish_bonus')
async def ru_bonuses(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Выберите ваш способ пополнения бонусов", reply_markup=ru_bonus_replenishment_keyboard)

@dp.callback_query_handler(text='ru_bonus_card')
async def ru_bonus_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Чтобы пополнить бонусы через банковскую карту, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_BONUS_CARD, caption=msg)
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_bonus_mbank')
async def ru_bonus_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Чтобы пополнить бонусы через MBank, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_BONUS_MBANK, caption=msg)
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_bonus_odengi')
async def ru_bonus_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Чтобы пополнить бонусы через O!Деньги, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_BONUS_ODENGI, caption=msg)
    await send_ask(call.message.chat.id)

# SCOOTER HANDLERS ===========================================================
@dp.callback_query_handler(text='ru_rent_scooter')
async def ru_rent_scooter(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RENT_SCOOTER_ID, caption="Чтобы арендовать самокат, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start")
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_scooter_issue')
async def ru_scooter_issues(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Пожалуйста, опишите проблему. Самокат...", reply_markup=ru_scooter_problems_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('ru_issue_'))
async def ru_issue_handler(call: CallbackQuery):
    issue_messages = {
        'ru_issue_not_on': "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Не включился' нашему оператору одним сообщением. ",
        'ru_issue_not_driving': "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Скорость' нашему оператору одним сообщением. ",
        'ru_issue_slow_speed': "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Скорость' нашему оператору одним сообщением. ",
        'ru_issue_broken': "Пожалуйста напишите номер самоката и опишите поломку одним сообщением. ",
        'ru_issue_off': "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Выключился' нашему оператору одним сообщением. ",
        'ru_issue_error': "Пожалуйста напишите номер вашего аккаунта, самоката и ошибку на дисплее нашему оператору одним сообщением. "
    }
    message = issue_messages.get(call.data, "Произошла ошибка. Пожалуйста, попробуйте снова.")
    message += "Первый освободившийся оператор свяжется с вами! 🥰\n\n"
    await call.message.edit_text(message, reply_markup=contact_ru)

# FINE HANDLERS ==============================================================
@dp.callback_query_handler(text='ru_fine_info')
async def ru_fines(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Пожалуйста, укажите сумму вашего штрафа", reply_markup=ru_fine_amount_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('ru_fine_'))
async def ru_fine_handler(call: CallbackQuery):
    fine_messages = {
        'ru_fine_100': "Уважаемый клиент, вы получили штраф за парковку в труднодоступном месте.\n\n",
        'ru_fine_250': "Уважаемый клиент, вы получили штраф за поездку вдвоём на одном самокате.\n\n",
        'ru_fine_300': "Уважаемый клиент, вы получили штраф за поездку втроём на одном самокате.\n\n",
        'ru_fine_500': "Уважаемый клиент, вы получили штраф за выезд в красную зону.\n\n"
    }
    message = fine_messages.get(call.data, "Уважаемый клиент, произошла ошибка.\n\n")
    message += "Если вам всё ещё нужна помощь нажмите на /start"
    await call.message.edit_text(message)

# REGISTRATION HANDLERS ======================================================
@dp.callback_query_handler(text='ru_registration')
async def ru_registration(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Вы регистрируетесь...", reply_markup=ru_registration_keyboard)

@dp.callback_query_handler(text='ru_registration_phone')
async def ru_registration_phone(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, чтобы зарегистрироваться по номеру телефона, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_REGISTRATION_PHONE, caption=msg)
    await send_ask(call.message.chat.id)

@dp.callback_query_handler(text='ru_registration_telegram')
async def ru_registration_telegram(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, чтобы зарегистрироваться через телеграм, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_REGISTRATION_TELEGRAM, caption=msg)
    await send_ask(call.message.chat.id)

# TARIFF HANDLERS ============================================================
@dp.callback_query_handler(text='ru_tariff_plans')
async def ru_tariffs(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(
        "Минутный тариф:\n"
        "07:00 – 12:00 → 3.4 бонуса/мин\n"
        "12:00 – 17:00 → 5.5 бонуса/мин\n"
        "17:00 – 07:00 → 6.5 бонуса/мин\n\n"
        "Пакеты тарифов:\n"
        "10 мин → 55 + 50 бонусов\n"
        "15 мин → 75 + 50 бонусов\n"
        "25 мин → 115 + 50 бонусов\n"
        "40 мин → 169 + 50 бонусов\n"
        "1 час → 240 + 50 бонусов\n\n"
        "🔹 Минутный тариф требует минимум 100 бонусов (90 — депозит, 10 — запуск). "
        "Если баланс падает ниже 90 бонусов, депозит списывается заново.\n\n"
        "При нехватке средств:\n"
        "▪️ Первый долг → скорость снижена до 5 км/ч, завершение только в зелёной зоне\n"
        "▪️ Второй долг → самокат завершится автоматически, долг на аккаунте.\n\n"
        "🔹 Пакетные тарифы требуют 50 бонусов депозита. "
        "При нехватке средств образуется долг, завершение только в зелёной зоне.\n\n"
        "❗ Самокат не завершится автоматически, кроме случаев:\n"
        "▪️ Минутный тариф → долг достигнет 180 бонусов\n"
        "▪️ Пакетный тариф → долг достигнет 100 бонусов\n\n"
        "Для продолжения аренды пополните счёт и оплатите долг.\n\n"
        "Если нужна помощь, нажмите /start."
    )