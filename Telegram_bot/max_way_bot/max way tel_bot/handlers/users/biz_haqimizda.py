from aiogram import types
from keyboards.default.start_btn import start_btn
from loader import dp


@dp.message_handler(text = 'ℹ️Biz haqimizda')
async def bot_help(message: types.Message):
    await message.answer('🍟 Max Way☎️\nAloqa markazi: +998712005400', reply_markup=start_btn)
