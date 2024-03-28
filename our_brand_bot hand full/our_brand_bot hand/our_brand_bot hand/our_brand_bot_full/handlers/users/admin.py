from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from loader import dp, db
from keyboards.default.admin import AdminStart


@dp.message_handler(text = '/admin', user_id = ADMINS)
async def bot_help(message: types.Message):
    admin = await db.select_all_user_one(message.from_user.id)

    if admin[11] == 'UZB':
        menu = await AdminStart(message.from_user.id)
        await message.answer('Hush kelibsiz admin', reply_markup=menu)
    elif admin[11] == 'RUS':
        menu = await AdminStart(message.from_user.id)
        await message.answer('Добро пожаловать, админ', reply_markup=menu)
    elif admin[11] == 'ENG':
        menu = await AdminStart(message.from_user.id)
        await message.answer('Welcome admin', reply_markup=menu)
