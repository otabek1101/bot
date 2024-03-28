from multiprocessing.sharedctypes import Value
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Tillar = {
    '🇺🇿 UZ':'UZB',
    '🇷🇺 RU':'RUS',
    '🇺🇸 EN':'ENG'
}

til_menu = InlineKeyboardMarkup(row_width=3)

for key, value in Tillar.items():
    til_menu.insert(InlineKeyboardButton(text=key, callback_data=value))