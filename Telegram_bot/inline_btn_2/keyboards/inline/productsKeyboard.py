from multiprocessing.sharedctypes import Value
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

# 3-usul
course = {
    'Python':'courses:python',
    'C++':'courses;Cpp',
    'Java':'courses:java',
    'C#':'courses:C#',
    'Js':'courses:js'
}

course_menu = InlineKeyboardMarkup(row_width=2)

for key, value in course.items():
    course_menu.insert(InlineKeyboardButton(text=key, callback_data=value))