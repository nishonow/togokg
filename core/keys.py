from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Main Menu Keyboard
main_menu = InlineKeyboardMarkup()
main_menu.add(
    InlineKeyboardButton("Русский🇷🇺", callback_data='lang_ru'),
    InlineKeyboardButton("Кыргызча🇰🇬", callback_data='lang_kg')
)

to_bot = InlineKeyboardMarkup()
to_bot.add(InlineKeyboardButton(text='Связяться с ботом/Бот менен байлануу', url='https://t.me/ToGoKgz_Bot'))

contact_ru = InlineKeyboardMarkup()
contact_ru.add(InlineKeyboardButton(text="Связаться с оператором", url='https://t.me/Togokg'))

contact_kg = InlineKeyboardMarkup(resize_keyboard=True)
contact_kg.add(InlineKeyboardButton(text="Оператор менен байланышуу", url='https://t.me/Togokg'))

rating_keyboard = InlineKeyboardMarkup()
rating_keyboard.add(
    InlineKeyboardButton("1⭐", callback_data='rating_1'),
    InlineKeyboardButton("2⭐", callback_data='rating_2'),
    InlineKeyboardButton("3⭐", callback_data='rating_3'),
    InlineKeyboardButton("4⭐", callback_data='rating_4'),
    InlineKeyboardButton("5⭐", callback_data='rating_5')
)

rating_keyboard_kg = InlineKeyboardMarkup()
rating_keyboard_kg.add(
    InlineKeyboardButton("1⭐", callback_data='ratingkg_1'),
    InlineKeyboardButton("2⭐", callback_data='ratingkg_2'),
    InlineKeyboardButton("3⭐", callback_data='ratingkg_3'),
    InlineKeyboardButton("4⭐", callback_data='ratingkg_4'),
    InlineKeyboardButton("5⭐", callback_data='ratingkg_5')
)

# RU Menu Keyboard
ru_menu_keyboard = InlineKeyboardMarkup()
ru_menu_keyboard.add(
    InlineKeyboardButton("Не прошла оплата?", callback_data='ru_payment_issue')
).add(
    InlineKeyboardButton("Как арендовать самокат?", callback_data='ru_rent_scooter')
).add(
    InlineKeyboardButton("Как пополнить бонусы?", callback_data='ru_replenish_bonus')
).add(
    InlineKeyboardButton("Какие у нас тарифные планы?", callback_data='ru_tariff_plans')
).add(
    InlineKeyboardButton("За что получили штраф?", callback_data='ru_fine_info')
).add(
    InlineKeyboardButton("Есть проблема с самокатом?", callback_data='ru_scooter_issue')
).add(
    InlineKeyboardButton("Как зарегистрироваться", callback_data='ru_registration')
)

# RU Payment Methods
ru_payment_keyboard = InlineKeyboardMarkup()
ru_payment_keyboard.add(
    InlineKeyboardButton("Банковская карта", callback_data='ru_payment_card')
).add(
    InlineKeyboardButton("MBank", callback_data='ru_payment_mbank')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='ru_payment_odengi')
)

# RU Bonus Replenishment
ru_bonus_replenishment_keyboard = InlineKeyboardMarkup()
ru_bonus_replenishment_keyboard.add(
    InlineKeyboardButton("Банковская карта", callback_data='ru_bonus_card')
).add(
    InlineKeyboardButton("MBank", callback_data='ru_bonus_mbank')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='ru_bonus_odengi')
)

# RU Fine Amount
ru_fine_amount_keyboard = InlineKeyboardMarkup()
ru_fine_amount_keyboard.add(
    InlineKeyboardButton("100", callback_data='ru_fine_100')
).add(
    InlineKeyboardButton("250", callback_data='ru_fine_250')
).add(
    InlineKeyboardButton("300", callback_data='ru_fine_300')
).add(
    InlineKeyboardButton("500", callback_data='ru_fine_500')
)

# RU Scooter Problems
ru_scooter_problems_keyboard = InlineKeyboardMarkup()
ru_scooter_problems_keyboard.add(
    InlineKeyboardButton("...не включился", callback_data='ru_issue_not_on')
).add(
    InlineKeyboardButton("...не едет", callback_data='ru_issue_not_driving')
).add(
    InlineKeyboardButton("...не разгоняется до 25 км/ч", callback_data='ru_issue_slow_speed')
).add(
    InlineKeyboardButton("... сломан", callback_data='ru_issue_broken')
).add(
    InlineKeyboardButton("...выключился", callback_data='ru_issue_off')
).add(
    InlineKeyboardButton("...показывает ошибку на дисплее", callback_data='ru_issue_error')
)

# RU Registration Options
ru_registration_keyboard = InlineKeyboardMarkup()
ru_registration_keyboard.add(
    InlineKeyboardButton("...по номеру телефона", callback_data='ru_registration_phone')
).add(
    InlineKeyboardButton("...через телеграм", callback_data='ru_registration_telegram')
)

# KG Menu Keyboard
kg_menu_keyboard = InlineKeyboardMarkup()
kg_menu_keyboard.add(
    InlineKeyboardButton("Төлөм ишке ашпай калдыбы?", callback_data='kg_payment_issue')
).add(
    InlineKeyboardButton("Скутерди кантип ижарага алса болот?", callback_data='kg_rent_scooter')
).add(
    InlineKeyboardButton("Кантип бонустарды толтуруу керек?", callback_data='kg_replenish_bonus')
).add(
    InlineKeyboardButton("Биздин тарифтик пландарыбыз кандай?", callback_data='kg_tariff_plans')
).add(
    InlineKeyboardButton("Эмне үчүн айып акча алдыңыз?", callback_data='kg_fine_info')
).add(
    InlineKeyboardButton("Скутериңизде көйгөй барбы?", callback_data='kg_scooter_issue')
).add(
    InlineKeyboardButton("Кантип катталса болот?", callback_data='kg_registration')
)

# KG Payment Methods
kg_payment_methods_keyboard = InlineKeyboardMarkup()
kg_payment_methods_keyboard.add(
    InlineKeyboardButton("Банк картасы", callback_data='kg_payment_card')
).add(
    InlineKeyboardButton("MBank", callback_data='kg_payment_mbank')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='kg_payment_odengi')
)

# KG Bonus Replenishment
kg_bonus_replenishment_keyboard = InlineKeyboardMarkup()
kg_bonus_replenishment_keyboard.add(
    InlineKeyboardButton("Банк картасы", callback_data='kg_bonus_card')
).add(
    InlineKeyboardButton("MBank", callback_data='kg_bonus_mbank')
).add(
    InlineKeyboardButton("О!Деньги", callback_data='kg_bonus_odengi')
)

# KG Fine Amount
kg_fine_amount_keyboard = InlineKeyboardMarkup()
kg_fine_amount_keyboard.add(
    InlineKeyboardButton("100", callback_data='kg_fine_100')
).add(
    InlineKeyboardButton("250", callback_data='kg_fine_250')
).add(
    InlineKeyboardButton("300", callback_data='kg_fine_300')
).add(
    InlineKeyboardButton("500", callback_data='kg_fine_500')
)

# KG Scooter Problems
kg_scooter_problems_keyboard = InlineKeyboardMarkup()
kg_scooter_problems_keyboard.add(
    InlineKeyboardButton("...күйгүзүлгөн", callback_data='kg_issue_not_on')
).add(
    InlineKeyboardButton("...журбайт", callback_data='kg_issue_not_driving')
).add(
    InlineKeyboardButton("...25 км/саатка чейин ылдамдабайт", callback_data='kg_issue_slow_speed')
).add(
    InlineKeyboardButton("... сынган", callback_data='kg_issue_broken')
).add(
    InlineKeyboardButton("... өчүп калды", callback_data='kg_issue_off')
).add(
    InlineKeyboardButton("...дисплейде катаны көрсөтөт", callback_data='kg_issue_error')
)

# KG Registration Options
kg_registration_keyboard = InlineKeyboardMarkup()
kg_registration_keyboard.add(
    InlineKeyboardButton("...телефон номер...", callback_data='kg_registration_phone')
).add(
    InlineKeyboardButton("...телеграм...", callback_data='kg_registration_telegram')
)