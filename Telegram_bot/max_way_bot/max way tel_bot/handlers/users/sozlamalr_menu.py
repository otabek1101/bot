from aiogram import types

from loader import dp, bot
from keyboards.default.sozlamalar_btn import sozlamalar_btn
from keyboards.default.til_btn import lan_btn

@dp.message_handler(text = '⚙️Sozlamalar')
async def bot_help(message: types.Message):
    
    await message.answer('Sozlamalar bolimi', reply_markup=sozlamalar_btn)
  

@dp.message_handler(text = 'Tilni ozgartirish')
async def bot_help(message: types.Message):
    
    await message.answer('Til tanlang', reply_markup=lan_btn)
  