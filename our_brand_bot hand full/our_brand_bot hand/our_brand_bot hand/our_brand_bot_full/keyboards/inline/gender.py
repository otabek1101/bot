from multiprocessing.sharedctypes import Value
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

gender_uz = {
    '🧑🏻‍💼 Erkak':'Erkak',
    '👩🏻‍💼 Ayol':'Ayol'
}

gen_menu_uz = InlineKeyboardMarkup(row_width=2)

for key, value in gender_uz.items():
    gen_menu_uz.insert(InlineKeyboardButton(text=key, callback_data=value))


gender_ru = {
    '🧑🏻‍💼 Мужчина': 'Мужчина',
     '👩🏻‍💼 Женщина': 'Женщина'
}

gen_menu_ru = InlineKeyboardMarkup(row_width=2)

for key, value in gender_ru.items():
    gen_menu_ru.insert(InlineKeyboardButton(text=key, callback_data=value))


gender_us = {
    '🧑🏻‍💼 Male':'Male',
     '👩🏻‍💼 Female':'Female'
}

gen_menu_us = InlineKeyboardMarkup(row_width=2)

for key, value in gender_us.items():
    gen_menu_us.insert(InlineKeyboardButton(text=key, callback_data=value))