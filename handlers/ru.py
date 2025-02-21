from aiogram.types import CallbackQuery, Message
from loader import dp, bot, db
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
RENT_SCOOTER_ID = 11
RU_PAYMENT_CARD = 7
RU_PAYMENT_MBANK = 7
RU_PAYMENT_ODENGI = 7
RU_BONUS_CARD = 6
RU_BONUS_ODENGI = 10
RU_REGISTRATION_PHONE = 9
RU_REGISTRATION_TELEGRAM = 8

# RATING HANDLERS ===========================================================
@dp.message_handler(text='/rating')
async def rating(message: Message):
    user_rating = await db.get_rating(message.from_user.id)
    if user_rating != 0:
        await message.answer(f"Вы уже оценили нашего бота на {user_rating} ⭐\n\nВы можете изменить свой оценкa", reply_markup=rating_keyboard)
    else:
        await message.answer("Пожалуйста, оцените нашего бота", reply_markup=rating_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('r_'))
async def save_user_rating(call: CallbackQuery):
    rating = int(call.data.split('_')[1])
    await db.save_rating(call.from_user.id, rating)
    await call.message.edit_reply_markup()
    await call.message.answer("Спасибо за вашу оценку!")

@dp.message_handler(text='/see_rating')
async def see_rating(message: Message):
    ratings = await db.get_all_ratings()
    ratings = [rating[0] for rating in ratings]
    average_rating = sum(ratings) / len(ratings)
    await message.answer(f"Все оценки {len(ratings)}\n\nСредний рейтинг нашего бота: {average_rating} ⭐")

# MENU HANDLERS ==============================================================
@dp.callback_query_handler(text='lang_ru')
async def ru_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Отлично! Чем мы можем вам помочь?", reply_markup=ru_menu_keyboard)

# PAYMENT HANDLERS ===========================================================
@dp.callback_query_handler(text='ru_payment_issue')
async def ru_payment(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Выберите ��аш способ оплаты", reply_markup=ru_payment_keyboard)

@dp.callback_query_handler(text='ru_payment_card')
async def ru_payment_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_CARD, caption=msg)

@dp.callback_query_handler(text='ru_payment_mbank')
async def ru_payment_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео. Если запросить статус не удалось, то пожалуйста обратитесь к вашему банку.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_MBANK, caption=msg)

@dp.callback_query_handler(text='ru_payment_odengi')
async def ru_payment_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. Пожалуйста повторите действия как показано на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_PAYMENT_ODENGI, caption=msg)

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

@dp.callback_query_handler(text='ru_bonus_mbank')
async def ru_bonus_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Чтобы пополнить бонусы через MBank, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_BONUS_CARD, caption=msg)

@dp.callback_query_handler(text='ru_bonus_odengi')
async def ru_bonus_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Чтобы пополнить бонусы че��ез O!Деньги, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_BONUS_ODENGI, caption=msg)

# SCOOTER HANDLERS ===========================================================
@dp.callback_query_handler(text='ru_rent_scooter')
async def ru_rent_scooter(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RENT_SCOOTER_ID, caption="Чтобы арендовать самокат, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start")

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

@dp.callback_query_handler(text='ru_registration_telegram')
async def ru_registration_telegram(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, чтобы зарегистрироваться через телеграм, пожалуйста, повторите действия как на видео.\n\nЕсли вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RU_REGISTRATION_TELEGRAM, caption=msg)

# TARIFF HANDLERS ============================================================
@dp.callback_query_handler(text='ru_tariff_plans')
async def ru_tariffs(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(
        "Тарифы минутный:\n"
        "С 07:00 до 12:00 - 3.4 бонусов\n"
        "С 12:00 до 17:00 - 5.5 бонусов\n"
        "С 17:00 до 07:00 - 6.5 бонусов\n\n"
        "Пакеты тарифов:\n"
        "10 Минут - 55 бонусов\n"
        "15 Минут - 75 бонусов\n"
        "25 Минут - 115 бонусов\n"
        "40 Минут - 169 бонусов\n"
        "1 час - 240 бонусов\n\n"
        "Перед использованием минутного тарифа убедитесь, что на вашем аккаунте имеется больше 100 бонусов. "
        "90 бонусов взимается как депозит, а 10 бонусов для запуска самоката.\n\n"
        "Если вам всё ещё нужна помощь нажмите на /start"
    )