from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Main Menu Keyboard
main_menu = InlineKeyboardMarkup()
main_menu.add(
    InlineKeyboardButton("Русский🇷🇺", callback_data='1'),
    InlineKeyboardButton("Кыргызча🇰🇬", callback_data='2')
)

to_bot = InlineKeyboardMarkup()
to_bot.add(InlineKeyboardButton(text='Связяться с ботом/Бот менен байлануу', url='https://t.me/ToGoKgz_Bot'))

contact_ru = InlineKeyboardMarkup()
contact_ru.add(InlineKeyboardButton(text="Связаться с оператором", url='https://t.me/Togokg'))

contact_kg = InlineKeyboardMarkup(resize_keyboard=True)
contact_kg.add(InlineKeyboardButton(text="Оператор менен байланышуу", url='https://t.me/Togokg'))

# RU Menu Keyboard
ru_menu_keyboard = InlineKeyboardMarkup()
ru_menu_keyboard.add(
    InlineKeyboardButton("Не прошла оплата?", callback_data='1.1')
).add(
    InlineKeyboardButton("Как арендовать самокат?", callback_data='1.2')
).add(
    InlineKeyboardButton("Как пополнить бонусы?", callback_data='1.3')
).add(
    InlineKeyboardButton("Какие у нас тарифные планы?", callback_data='1.4')
).add(
    InlineKeyboardButton("За что получили штраф?", callback_data='1.5')
).add(
    InlineKeyboardButton("Есть проблема с самокатом?", callback_data='1.6')
).add(
    InlineKeyboardButton("Как зарегистрироваться", callback_data='1.7')
)

# RU Payment Methods
ru_payment_keyboard = InlineKeyboardMarkup()
ru_payment_keyboard.add(
    InlineKeyboardButton("Банковская карта", callback_data='1.1.1')
).add(
    InlineKeyboardButton("MBank", callback_data='1.1.2')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='1.1.3')
)

# RU Bonus Replenishment
ru_bonus_replenishment_keyboard = InlineKeyboardMarkup()
ru_bonus_replenishment_keyboard.add(
    InlineKeyboardButton("Банковская карта", callback_data='1.3.1')
).add(
    InlineKeyboardButton("MBank", callback_data='1.3.2')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='1.3.3')
)

# RU Fine Amount
ru_fine_amount_keyboard = InlineKeyboardMarkup()
ru_fine_amount_keyboard.add(
    InlineKeyboardButton("100", callback_data='1.5.1')
).add(
    InlineKeyboardButton("250", callback_data='1.5.2')
).add(
    InlineKeyboardButton("300", callback_data='1.5.3')
).add(
    InlineKeyboardButton("500", callback_data='1.5.4')
)

# RU Scooter Problems
ru_scooter_problems_keyboard = InlineKeyboardMarkup()
ru_scooter_problems_keyboard.add(
    InlineKeyboardButton("...не включился", callback_data='1.6.1')
).add(
    InlineKeyboardButton("...не едет", callback_data='1.6.2')
).add(
    InlineKeyboardButton("...не разгоняется до 25 км/ч", callback_data='1.6.3')
).add(
    InlineKeyboardButton("... сломан", callback_data='1.6.4')
).add(
    InlineKeyboardButton("...выключился", callback_data='1.6.5')
).add(
    InlineKeyboardButton("...показывает ошибку на дисплее", callback_data='1.6.6')
)

# RU Registration Options
ru_registration_keyboard = InlineKeyboardMarkup()
ru_registration_keyboard.add(
    InlineKeyboardButton("...по номеру телефона", callback_data='1.7.1')
).add(
    InlineKeyboardButton("...через телеграм", callback_data='1.7.2')
)

# KG Menu Keyboard
kg_menu_keyboard = InlineKeyboardMarkup()
kg_menu_keyboard.add(
    InlineKeyboardButton("Төлөм ишке ашпай калдыбы?", callback_data='2.1')
).add(
    InlineKeyboardButton("Скутерди кантип ижарага алса болот?", callback_data='2.2')
).add(
    InlineKeyboardButton("Кантип бонустарды толтуруу керек?", callback_data='2.3')
).add(
    InlineKeyboardButton("Биздин тарифтик пландарыбыз кандай?", callback_data='2.4')
).add(
    InlineKeyboardButton("Эмне үчүн айып акча алдыңыз?", callback_data='2.5')
).add(
    InlineKeyboardButton("Скутериңизде көйгөй барбы?", callback_data='2.6')
).add(
    InlineKeyboardButton("Кантип катталса болот?", callback_data='2.7')
)

# KG Payment Methods
kg_payment_methods_keyboard = InlineKeyboardMarkup()
kg_payment_methods_keyboard.add(
    InlineKeyboardButton("Банк картасы", callback_data='2.1.1')
).add(
    InlineKeyboardButton("MBank", callback_data='2.1.2')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='2.1.3')
)

# KG Bonus Replenishment
kg_bonus_replenishment_keyboard = InlineKeyboardMarkup()
kg_bonus_replenishment_keyboard.add(
    InlineKeyboardButton("Банк картасы", callback_data='2.3.1')
).add(
    InlineKeyboardButton("MBank", callback_data='2.3.2')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='2.3.3')
)

# KG Fine Amount
kg_fine_amount_keyboard = InlineKeyboardMarkup()
kg_fine_amount_keyboard.add(
    InlineKeyboardButton("100", callback_data='2.5.1')
).add(
    InlineKeyboardButton("250", callback_data='2.5.2')
).add(
    InlineKeyboardButton("300", callback_data='2.5.3')
).add(
    InlineKeyboardButton("500", callback_data='2.5.4')
)

# KG Scooter Problems
kg_scooter_problems_keyboard = InlineKeyboardMarkup()
kg_scooter_problems_keyboard.add(
    InlineKeyboardButton("...күйгүзүлгөн", callback_data='2.6.1')
).add(
    InlineKeyboardButton("...журбайт", callback_data='2.6.2')
).add(
    InlineKeyboardButton("...25 км/саатка чейин ылдамдабайт", callback_data='2.6.3')
).add(
    InlineKeyboardButton("...сынган", callback_data='2.6.4')
).add(
    InlineKeyboardButton("... өчүп калды", callback_data='2.6.5')
).add(
    InlineKeyboardButton("...дисплейде катаны көрсөтөт", callback_data='2.6.6')
)

# KG Registration Options
kg_registration_keyboard = InlineKeyboardMarkup()
kg_registration_keyboard.add(
    InlineKeyboardButton("...телефон номер...", callback_data='2.7.1')
).add(
    InlineKeyboardButton("...телеграм...", callback_data='2.7.2')
)
