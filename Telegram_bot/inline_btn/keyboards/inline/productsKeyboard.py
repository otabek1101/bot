from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback

# 1-usul.
categorymenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗Ict Academy Sayitiga o'tish", url="https://ictacademy.uz"),
        ],
        [
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Bot Ajoyib ekan"),
        ],
    ]
)  