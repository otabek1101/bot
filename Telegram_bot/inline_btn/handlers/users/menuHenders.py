import logging

from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categorymenu
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"Mahsulot tanlang", reply_markup=categorymenu)