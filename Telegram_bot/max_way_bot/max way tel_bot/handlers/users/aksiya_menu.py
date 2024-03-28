from aiogram import types
from keyboards.default.start_btn import start_btn

from loader import dp


@dp.message_handler(text = '🎉Aksiya')
async def bot_aksiya(message: types.Message):
    await message.answer('Ayni paytda aksiya yo`q', reply_markup=start_btn)
