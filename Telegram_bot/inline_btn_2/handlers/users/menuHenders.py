import logging

from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categorymenu, course_menu
from loader import dp

@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulot tanlang", reply_markup=categorymenu)

@dp.callback_query_handler(text="courses")
async def by_courses(call: CallbackQuery):

    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=course_menu)
    await call.answer(cache_time=60)