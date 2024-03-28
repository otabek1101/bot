from email import message
from re import M
from aiogram import types

from loader import dp, db
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.setting_btn import Sett_btn
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery

from keyboards.inline.til import til_menu


soz =['Sozlash','Настройки','Settings']
    

for i in soz:
    @dp.message_handler(Command(i))
    async def bot_help(message: types.Message):
        set_btn = await Sett_btn(message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer("⚙️ Sozlash", reply_markup=set_btn)

        elif users[11] == "RUS":
             await message.answer('⚙️ Настройки', reply_markup=set_btn)

        elif users[11] == "ENG":
            await message.answer('⚙️ Settings', reply_markup=set_btn)

sz =['⚙️ Sozlash','⚙️ Настройки','⚙️ Settings']

for i in sz:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        set_btn = await Sett_btn(message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer("⚙️ Sozlash", reply_markup=set_btn)

        elif users[11] == "RUS":
             await message.answer('⚙️ Настройки', reply_markup=set_btn)

        elif users[11] == "ENG":
            await message.answer('⚙️ Settings', reply_markup=set_btn)

til =['🇺🇿 Tilni tanlash','🇷🇺 Выбор языка','🇺🇸 Language selection']


for i in til:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer("🇺🇿 Til tanlang", reply_markup=til_menu)

        elif users[11] == "RUS":
            await message.answer("🇷🇺 Выберите язык", reply_markup=til_menu)

        elif users[11] == "ENG":
            await message.answer("🇺🇸 Choose a language", reply_markup=til_menu)


@dp.callback_query_handler(text = 'UZB')
async def buy_courses(call: CallbackQuery):
    TIL = await db.update_user_til('UZB', call.from_user.id)
    await call.answer('Til o`zgardi')
    menu = await Sett_btn(call.from_user.id)
    await call.message.answer('Til o`zgardi',reply_markup=menu)
    await call.message.delete()
    await call.answer(cache_time=60)



@dp.callback_query_handler(text = 'RUS')
async def buy_courses(call: CallbackQuery):
    TIL = await db.update_user_til('RUS', call.from_user.id)
    await call.answer('Язык изменился')
    menu = await Sett_btn(call.from_user.id)
    await call.message.answer('Язык изменился',reply_markup=menu)
    await call.message.delete()
    await call.answer(cache_time=60)



@dp.callback_query_handler(text = 'ENG')
async def buy_courses(call: CallbackQuery):
    TIL = await db.update_user_til('ENG', call.from_user.id)
    await call.answer('The language changed')
    menu = await Sett_btn(call.from_user.id)
    await call.message.answer('The language changed',reply_markup=menu)
    await call.message.delete()
    await call.answer(cache_time=60)
