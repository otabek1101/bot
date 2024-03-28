from cgitb import text
import imp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buyurtma_btn import buyurtma_btn
from keyboards.default.start_btn import start_btn

from loader import dp, bot


@dp.message_handler(text= '🛍Buyurtma berish')
async def bot_buyurtma_menu(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo='https://avatars.mds.yandex.net/get-altay/5479189/2a0000017e213677b7decc38f5a2c64be8d3/XXL', caption='Buyurtma qiling', reply_markup=buyurtma_btn)

@dp.message_handler(text= '⬅️Ortga')
async def bot_ortga(message: types.Message):
    await message.answer('Asosiy menyu' ,reply_markup=start_btn)