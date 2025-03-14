import asyncio
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from core.db import save_rating, get_all_ratings
from loader import dp, bot
from core.keys import (
    kg_menu_keyboard,
    kg_payment_methods_keyboard,
    kg_bonus_replenishment_keyboard,
    kg_fine_amount_keyboard,
    kg_scooter_problems_keyboard,
    kg_registration_keyboard,
    contact_kg, rating_keyboard_kg
)

CHANNEL_ID = -1002276623671
RENT_SCOOTER_ID = 11
KG_PAYMENT_CARD = 7
KG_PAYMENT_MBANK = 7
KG_PAYMENT_ODENGI = 7
KG_BONUS_CARD = 6
KG_BONUS_ODENGI = 10
KG_REGISTRATION_PHONE = 9
KG_REGISTRATION_TELEGRAM = 8

# RATING HANDLERS ===========================================================

@dp.callback_query_handler(lambda c: c.data.startswith('ratingkg_'))
async def save_user_rating_kg(call: CallbackQuery):
    rating = int(call.data.split('_')[1])
    await save_rating(call.from_user.id, rating)
    await call.message.edit_reply_markup()
    await call.message.answer("Баалаганыңыз үчүн рахмат!")


async def send_ask_kg(chat_id):
    await asyncio.sleep(60)  # Wait for 1 minute

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Ооба", callback_data="video_solved_yes_kg"),
        InlineKeyboardButton(text="Жок", callback_data="video_solved_no_kg")
    )

    await bot.send_message(chat_id, "Бул видео көйгөйүңүздү чечүүгө жардам бердиби?", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ["video_solved_yes_kg", "video_solved_no_kg"])
async def handle_video_response_kg(call: CallbackQuery):
    if call.data == "video_solved_yes_kg":
        await call.message.edit_reply_markup()
        await call.message.answer("Биздин боттун жардамына баа бериңиз🫶", reply_markup=rating_keyboard_kg)
    elif call.data == "video_solved_no_kg":
        await call.message.edit_reply_markup()
        await call.message.answer("Кошумча жардам алуу үчүн администраторубузга кайрылыңыз.", reply_markup=contact_kg)

# MENU HANDLERS ==============================================================
@dp.callback_query_handler(text='lang_kg')
async def kg_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Сизге кандай жардам бере алабыз?", reply_markup=kg_menu_keyboard)

# PAYMENT HANDLERS ===========================================================
@dp.callback_query_handler(text='kg_payment_issue')
async def kg_payment(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Төлөм ыкмасын тандаңыз", reply_markup=kg_payment_methods_keyboard)

@dp.callback_query_handler(text='kg_payment_card')
async def kg_payment_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Урматтуу каардар, төлөмүңүздүн абалы дагы эле тастыктала элек. Видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_PAYMENT_CARD, caption=msg)
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_payment_mbank')
async def kg_payment_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Урматтуу каардар, төлөмүңүздүн абалы дагы эле тастыктала элек. Видеодогудай кадамдарды кайталаңыз. Эгер абалды сурап билүү мүмкүн болбосо, банкыңызга кайрылыңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_PAYMENT_MBANK, caption=msg)
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_payment_odengi')
async def kg_payment_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Урматтуу каардар, төлөмүңүздүн абалы дагы эле тастыктала элек. Видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_PAYMENT_ODENGI, caption=msg)
    await send_ask_kg(call.message.chat.id)

# BONUS HANDLERS =============================================================
@dp.callback_query_handler(text='kg_replenish_bonus')
async def kg_bonuses(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Бонустарды толтуруу ыкмасын тандаңыз", reply_markup=kg_bonus_replenishment_keyboard)

@dp.callback_query_handler(text='kg_bonus_card')
async def kg_bonus_card(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Бонустарды банк картасы аркылуу толтуруу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_BONUS_CARD, caption=msg)
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_bonus_mbank')
async def kg_bonus_mbank(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Бонустарды MBank аркылуу толтуруу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_BONUS_CARD, caption=msg)
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_bonus_odengi')
async def kg_bonus_odengi(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Бонустарды O!Деньги аркылуу толтуруу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_BONUS_ODENGI, caption=msg)
    await send_ask_kg(call.message.chat.id)

# SCOOTER HANDLERS ===========================================================
@dp.callback_query_handler(text='kg_rent_scooter')
async def kg_rent_scooter(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=RENT_SCOOTER_ID, caption="Скутерди ижарага алуу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз")
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_scooter_issue')
async def kg_scooter_issues(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Сураныч, көйгөйдү сүрөттөп бериңиз. Скутер...", reply_markup=kg_scooter_problems_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('kg_issue_'))
async def kg_issue_handler(call: CallbackQuery):
    issue_messages = {
        'kg_issue_not_on': "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутердин номерин жана 'Не включился' деген сөздү жазыңыз. ",
        'kg_issue_not_driving': "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутер номериңизди жана 'Скорость' деген сөздү жазыңыз. ",
        'kg_issue_slow_speed': "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутер номериңизди жана 'Скорость' деген сөздү жазыңыз. ",
        'kg_issue_broken': "Сураныч, скутердин номерин жазып, бир билдирүүдө бузулууну сүрөттөп бериңиз. ",
        'kg_issue_off': "Сураныч, бир билдирүүдө биздин операторго эсеп номериңизди, скутердин номериңизди жана 'Выключился' деген сөздү жазыңыз. ",
        'kg_issue_error': "Сураныч, аккаунтуңуздун номерин, скутердин номерин жана дисплейдеги катаны биздин операторго бир билдирүү менен жазыңыз. "
    }
    message = issue_messages.get(call.data, "Ката кетти. Сураныч, кайра аракет кылыңыз.")
    message += "Биринчи жеткиликтүү оператор сиз менен байланышат! 🥰\n\n"
    await call.message.edit_text(message, reply_markup=contact_kg)

# FINE HANDLERS ==============================================================
@dp.callback_query_handler(text='kg_fine_info')
async def kg_fines(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Сураныч, айып акчанын суммасын көрсөтүңүз", reply_markup=kg_fine_amount_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('kg_fine_'))
async def kg_fine_handler(call: CallbackQuery):
    fine_messages = {
        'kg_fine_100': "Урматтуу каардар, сиз жетүүгө кыйын болгон жерде токтогонуңуз үчүн айып акча алдыңыз.\n\n",
        'kg_fine_250': "Урматтуу каардар, сиз бир скутерде эки адам чогуу жүргөнүңүз үчүн айып акча алдыңыз.\n\n",
        'kg_fine_300': "Урматтуу каардар, сиз бир скутерде үч адам чогуу жүргөнүңүз үчүн айып акча алдыңыз.\n\n",
        'kg_fine_500': "Урматтуу каардар, сиз кызыл зонага айдаганыңыз үчүн айып акча алдыңыз.\n\n"
    }
    message = fine_messages.get(call.data, "Урматтуу каардар, ката кетти.\n\n")
    message += "Эгер дагы эле жардам керек болсо /start басыныз"
    await call.message.edit_text(message)

# REGISTRATION HANDLERS ======================================================
@dp.callback_query_handler(text='kg_registration')
async def kg_registration(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Сиз катталуудасыз...", reply_markup=kg_registration_keyboard)

@dp.callback_query_handler(text='kg_registration_phone')
async def kg_registration_phone(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Урматтуу каардар, телефон номери аркылуу катталуу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_REGISTRATION_PHONE, caption=msg)
    await send_ask_kg(call.message.chat.id)

@dp.callback_query_handler(text='kg_registration_telegram')
async def kg_registration_telegram(call: CallbackQuery):
    await call.message.edit_reply_markup()
    msg = "Урматтуу каардар, телеграм аркылуу катталуу үчүн видеодогудай кадамдарды кайталаңыз.\n\nЭгер дагы эле жардам керек болсо /start басыныз"
    await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=CHANNEL_ID, message_id=KG_REGISTRATION_TELEGRAM, caption=msg)
    await send_ask_kg(call.message.chat.id)

# TARIFF HANDLERS ============================================================
@dp.callback_query_handler(text='kg_tariff_plans')
async def kg_tariffs(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(
        "Мүнөттүк тариф:\n"
        "07:00 – 12:00 → 3.4 бонус/мүн\n"
        "12:00 – 17:00 → 5.5 бонус/мүн\n"
        "17:00 – 07:00 → 6.5 бонус/мүн\n\n"
        "Тарифтик пакеттер:\n"
        "10 мүн → 55 + 50 бонус\n"
        "15 мүн → 75 + 50 бонус\n"
        "25 мүн → 115 + 50 бонус\n"
        "40 мүн → 169 + 50 бонус\n"
        "1 саат → 240 + 50 бонус\n\n"
        "🔹 Мүнөттүк тариф үчүн кеминде 100 бонус талап кылынат (90 — депозит, 10 — баштоо). "
        "Эгер баланс 90 бонустун астына түшсө, депозит кайрадан кармалат.\n\n"
        "Каражат жетишсиз болгон учурда:\n"
        "▪️ Биринчи карыз → ылдамдык 5 км/с чейин төмөндөйт, бүтүрүү жашыл аймакта гана мүмкүн\n"
        "▪️ Экинчи карыз → самокат автоматтык түрдө бүтөт, карыз аккаунтта сакталат.\n\n"
        "🔹 Пакеттик тарифтер үчүн 50 бонус депозит талап кылынат. "
        "Каражат жетишсиз болгон учурда карыз пайда болот, бүтүрүү жашыл аймакта гана мүмкүн.\n\n"
        "❗ Самокат автоматтык түрдө бүтпөйт, төмөнкү учурлардан тышкары:\n"
        "▪️ Мүнөттүк тариф → карыз 180 бонуска жеткенде\n"
        "▪️ Пакеттик тариф → карыз 100 бонуска жеткенде\n\n"
        "Улантуу үчүн эсебиңизди толуктаңыз жана карызыңызды жабыңыз.\n\n"
        "Эгер жардам керек болсо, /start баскычын басыңыз."
    )
