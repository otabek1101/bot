from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startmenu import menuStart
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    users = await db.select_all_users()
    A = 0
    for i in users:
        if i[3] == message.from_user.id:
            A+=1
            break
    if A == 1:
        await message.answer(f"Salom, {message.from_user.full_name}!")
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup = menuStart)
