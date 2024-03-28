from multiprocessing.sharedctypes import Value
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LINK = {
    'Instagram':'link:insta',
    'TikTok':'link:tik',
    'YouTube':'link:tube'
}

link_menu = InlineKeyboardMarkup(row_width=3)

for key, value in LINK.items():
    link_menu.insert(InlineKeyboardButton(text=key, callback_data=value))