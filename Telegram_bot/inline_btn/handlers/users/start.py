from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenuKeys import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!, do'konga hush kelibsiz!", reply_markup=menuStart)

