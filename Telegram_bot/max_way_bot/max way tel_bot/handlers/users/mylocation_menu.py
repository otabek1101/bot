from aiogram import types

from loader import dp, bot
from keyboards.default.home_btn import home_btn
from keyboards.default.mylocation_btn import mylocation_btn

@dp.message_handler(text = '🏘Mening manzillarim')
async def bot_help(message: types.Message):
    
    await message.answer('Mening manzillarim bo`limi', reply_markup=home_btn)

@dp.message_handler(text = '📍Manzil qo`shish')
async def bot_help(message: types.Message):
    
    await message.answer('📍 Manzilingizni ko`rsating', reply_markup=mylocation_btn)