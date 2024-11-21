from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from keys import kg_menu_keyboard, contact_kg, kg_payment_methods_keyboard, kg_bonus_replenishment_keyboard, kg_fine_amount_keyboard, kg_scooter_problems_keyboard, kg_registration_keyboard

CHANNEL_ID = -1002276623671


@dp.callback_query_handler(text='2')
async def ru_meu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Абдан жакшы! Биз сизге кантип жардам бере алабыз?", reply_markup=kg_menu_keyboard)

@dp.callback_query_handler(text='2.1')
async def kg_payment_methods_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Төлөм ыкмаңызды тандаңыз", reply_markup=kg_payment_methods_keyboard)

@dp.callback_query_handler(text='2.2')
async def kg_scooter_rental_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 11  # Replace with actual message_id

    msg ="Скутерди ижарага алуу үчүн, видеодогудай кадамдарды кайталаңыз.\n\n"
    msg +="Эгер дагы эле жардам керек болсо /start басыныз"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid
    )

@dp.callback_query_handler(text='2.3')
async def kg_bonus_replenishment_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Төлөм ыкмаңызды тандаңыз", reply_markup=kg_bonus_replenishment_keyboard)

@dp.callback_query_handler(text='2.4')
async def kg_tariffs_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(
        "Мүнөттүк тарифтер:\n"
        "07:00дөн 12:00гө чейин - 3,4 бонустар\n"
        "12:00дөн 17:00гө чейин - 5,5 бонустар\n"
        "17:00дөн 07:00гө чейин - 6,5 бонус \n\n"
        "Тарифтик пакеттер:\n"
        "10 мүнөт - 55 бонус\n"
        "15 мүнөт - 75 бонус\n"
        "25 мүнөт - 115 бонус\n"
        "40 мүнөт - 169 бонус\n"
        "1 саат - 240 бонус\n\n"
        "Мүнөт тарифин колдонуудан мурун, сиздин эсебиңизде 90дон ашык бонус бар экенин текшериңиз. "
        "Скутерди мүнөттүк ылдамдыкта ижарага алууда депозит катары 90 бонус алынат же 10 бонус куйгузулат.\n\n"
        "Эгер дагы эле жардам керек болсо /start басыныз"
    )

@dp.callback_query_handler(text='2.5')
async def kg_fine_amount_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Айып акчаныздын суммасын көрсөтүңүз", reply_markup=kg_fine_amount_keyboard)

@dp.callback_query_handler(text='2.6')
async def kg_scooter_problems_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Көйгөйдү сүрөттөп бериңиз. Скутер...", reply_markup=kg_scooter_problems_keyboard)

@dp.callback_query_handler(text='2.7')
async def kg_registration_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Сиз ... аркылуу катталасыз.", reply_markup=kg_registration_keyboard)

@dp.callback_query_handler(text='2.1.1')
async def kg_payment_card_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 7  # Replace with actual message_id

    msg = "Урматтуу каардар, төлөмүңүздүн абалы азырынча тастыктала элек. "
    msg += "Сураныч, видеодо көрсөтүлгөндөй кадамдарды кайталаңыз.\n\n"
    msg += "Эгер дагы эле жардам керек болсо /start басыныз"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='2.3.1')
async def kg_bonus_card_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 6  # Replace with actual message_id

    msg= "Банк картасы аркылуу бонустарды толуктоо үчүн видеодогудай кадамдарды кайталаңыз.\n\n"
    msg +="Эгер дагы эле жардам керек болсо /start басыныз"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='2.3.2')
async def kg_bonus_mbank_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 6  # Replace with actual message_id

    msg ="MBank аркылуу бонустарды толуктоо үчүн видеодогудай кадамдарды кайталаңыз.\n\n"
    msg +="Эгер дагы эле жардам керек болсо /start басыныз"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='2.3.3')
async def kg_bonus_odengi_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 10  # Replace with actual message_id

    msg = "O!Деньги аркылуу бонустарды толуктоо үчүн видеодогудай кадамдарды кайталаңыз.\n\n"
    msg += "Эгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='2.5.1')
async def kg_fine_100_handler(call: types.CallbackQuery):

    await call.message.edit_text(
        "Урматтуу каардар, сиз жетүүгө кыйын жерге токтотконуз үчүн айып акча алдыңыз.\n\n"
        "Эгер дагы эле жардам керек болсо /start басыныз"
    )

@dp.callback_query_handler(text='2.5.2')
async def kg_fine_250_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Урматтуу каардар, сиз бир скутерде 2 адам чогуу жүргөнүз үчүн айып акча алдыңыз.\n\n"
        "Эгер дагы эле жардам керек болсо /start басыныз"
    )

@dp.callback_query_handler(text='2.5.3')
async def kg_fine_300_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Урматтуу каардар, сиз бир скутерде 3 адам чогуу жүргөнүз үчүн айып акча алдыңыз.\n\n"
        "Эгер дагы эле жардам керек болсо /start басыныз"
    )

@dp.callback_query_handler(text='2.5.4')
async def kg_fine_500_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Урматтуу каардар, сиз кызыл зонага айдаганыңыз үчүн айып акча алдыңыз.\n\n"
        "Эгер дагы эле жардам керек болсо /start басыныз"
    )

@dp.callback_query_handler(text='2.6.1')
async def kg_issue_not_on_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутердин номерин жана 'Не включился' деген сөздү жазыңыз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.6.2')
async def kg_issue_not_driving_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутер номериңизди жана 'Скорость' деген сөздү жазыңыз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.6.3')
async def kg_issue_slow_speed_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутер номериңизди жана 'Скорость' деген сөздү жазыңыз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.6.4')
async def kg_issue_broken_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, скутердин номерин жазып, бир билдирүүдө бузулууну сүрөттөп бериңиз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.6.5')
async def kg_issue_off_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутердин номериңизди жана 'Выключился' деген сөздү жазыңыз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.6.6')
async def kg_issue_error_handler(call: types.CallbackQuery):
    await call.message.edit_text(
        "Сураныч, аккаунтуңуздун номерин, скутердин номерин жана дисплейдеги катаны биздин операторго бир билдирүү менен жазыңыз. "
        "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n",
        reply_markup=contact_kg
    )

@dp.callback_query_handler(text='2.7.1')
async def kg_registration_phone_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 9  # Replace with actual message_id
    msg = "Урматтуу каардар, телефон номери аркылуу катталуу үчүн видеодогудай кадамдарды кайталаңыз.\n\n"
    msg += "Эгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

@dp.callback_query_handler(text='2.7.2')
async def kg_registration_telegram_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    vidid = 8 # Replace with actual message_id
    msg = "Урматтуу каардар, телеграм аркылуу катталуу үчүн видеодогудай кадамдарды кайталаңыз.\n\n"
    msg += "Эгер дагы эле жардам керек болсо /start басыныз"

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=CHANNEL_ID,
        message_id=vidid,
        caption=msg
    )

