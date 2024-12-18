from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from keys import (
    ru_menu_keyboard,
    ru_payment_keyboard,
    ru_bonus_replenishment_keyboard,
    ru_fine_amount_keyboard,
    ru_scooter_problems_keyboard,
    ru_registration_keyboard,
    contact_ru
)

CHANNEL_ID = -1002276623671

@dp.callback_query_handler(text='1')
async def ru_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Отлично! Чем мы можем вам помочь?", reply_markup=ru_menu_keyboard)

@dp.callback_query_handler(text='1.1')
async def ru_payment(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Выберите ваш способ оплаты", reply_markup=ru_payment_keyboard)

@dp.callback_query_handler(text='1.2')
async def ru_payment_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 11  # Replace with the actual message ID for the video in your channel
    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption="Чтобы арендовать самокат, пожалуйста, повторите действия как на видео.\n\n"
                "Если вам всё ещё нужна помощь нажмите на /start"
    )

@dp.callback_query_handler(text='1.3')
async def ru_bonus(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Выберите ваш способ пополнения бонусов", reply_markup=ru_bonus_replenishment_keyboard)

@dp.callback_query_handler(text='1.4')
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

@dp.callback_query_handler(text='1.5')
async def ru_fines(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Пожалуйста, укажите сумму вашего штрафа", reply_markup=ru_fine_amount_keyboard)

@dp.callback_query_handler(text='1.6')
async def ru_scooter_issues(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Пожалуйста, опишите проблему. Самокат...", reply_markup=ru_scooter_problems_keyboard)

@dp.callback_query_handler(text='1.7')
async def ru_registration(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Вы регистрируетесь...", reply_markup=ru_registration_keyboard)

@dp.callback_query_handler(text='1.1.1')
async def ru_payment_card_status(call: CallbackQuery):
    vidid = 7  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Уважаемый клиент, статус вашей оплаты ещё не подтверждён. "
    msg +="Пожалуйста повторите действия как показано на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"
    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.1.2')
async def ru_payment_mbank_status(call: CallbackQuery):
    vidid = 7  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg = "Уважаемый клиент, статус вашей оплаты ещё не подтверждён. "
    msg +="Пожалуйста повторите действия как показано на видео. Если запросить статус не удалось, "
    msg +="то пожалуйста обратитесь к вашему банку.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.1.3')
async def ru_payment_odin_status(call: CallbackQuery):
    vidid = 7  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Уважаемый клиент, статус вашей оплаты ещё не подтверждён. "
    msg +="Пожалуйста повторите действия как показано на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.3.1')
async def ru_bonus_card(call: CallbackQuery):
    vidid = 6  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Чтобы пополнить бонусы через банковскую карту, пожалуйста, повторите действия как на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.3.2')
async def ru_bonus_mbank(call: CallbackQuery):
    vidid = 6  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Чтобы пополнить бонусы через MBank, пожалуйста, повторите действия как на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.3.3')
async def ru_bonus_odengi(call: CallbackQuery):
    vidid = 10  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Чтобы пополнить бонусы через O!Деньги, пожалуйста, повторите действия как на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.5.1')
async def ru_fine_100(call: CallbackQuery):
    await call.message.edit_text(
        "Уважаемый клиент, вы получили штраф за парковку в труднодоступном месте.\n\n"
        "Если вам всё ещё нужна помощь нажмите на /start"
    )

@dp.callback_query_handler(text='1.5.2')
async def ru_fine_250(call: CallbackQuery):
    await call.message.edit_text(
        "Уважаемый клиент, вы получили штраф за поездку вдвоём на одном самокате.\n\n"
        "Если вам всё ещё нужна помощь нажмите на /start"
    )

@dp.callback_query_handler(text='1.5.3')
async def ru_fine_300(call: CallbackQuery):
    await call.message.edit_text(
        "Уважаемый клиент, вы получили штраф за поездку втроём на одном самокате.\n\n"
        "Если вам всё ещё нужна помощь нажмите на /start"
    )

@dp.callback_query_handler(text='1.5.4')
async def ru_fine_500(call: CallbackQuery):
    await call.message.edit_text(
        "Уважаемый клиент, вы получили штраф за выезд в красную зону.\n\n"
        "Если вам всё ещё нужна помощь нажмите на /start"
    )

@dp.callback_query_handler(text='1.6.1')
async def ru_issue_not_on(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Не включился' нашему оператору одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.6.2')
async def ru_issue_not_driving(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Скорость' нашему оператору одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.6.3')
async def ru_issue_slow_speed(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Скорость' нашему оператору одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.6.4')
async def ru_issue_broken(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер самоката и опишите поломку одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.6.5')
async def ru_issue_off(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер вашего аккаунта, самоката и слово 'Выключился' нашему оператору одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.6.6')
async def ru_issue_error(call: CallbackQuery):
    await call.message.edit_text(
        "Пожалуйста напишите номер вашего аккаунта, самоката и ошибку на дисплее нашему оператору одним сообщением. "
        "Первый освободившийся оператор свяжется с вами! 🥰\n\n",
        reply_markup=contact_ru
    )

@dp.callback_query_handler(text='1.7.1')
async def ru_registration_phone(call: CallbackQuery):
    vidid = 9  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Уважаемый клиент, чтобы зарегистрироваться по номеру телефона, пожалуйста, повторите действия как на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='1.7.2')
async def ru_registration_telegram(call: CallbackQuery):
    vidid = 8  # Replace with actual message_id
    await call.message.edit_reply_markup()
    msg ="Уважаемый клиент, чтобы зарегистрироваться через телеграм, пожалуйста, повторите действия как на видео.\n\n"
    msg +="Если вам всё ещё нужна помощь нажмите на /start"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )
