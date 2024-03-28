from email import message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
from aiogram import types
from keyboards.inline.link import link_menu
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery
from keyboards.default.update_link import Update_link
from states.update_malumot import Update_insta,Update_tele,Update_you

update_link = ["↪️ Linkni o'zgartirish", "↪️ Изменить ссылку", "↪️ Change Link"]

for i in update_link:
    @dp.message_handler(text= i)
    async def link_tanlash(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            menu = await Update_link(message.from_user.id)
            await message.answer("Qaysi linkni o'zgartirmoqchisiz:", reply_markup=menu)
        
        elif users[11] == 'RUS':
            menu = await Update_link(message.from_user.id)
            await message.answer("Какую ссылку вы хотите изменить:", reply_markup=menu)
        
        elif users[11] == 'ENG':
            menu = await Update_link(message.from_user.id)
            await message.answer("Which link do you want to change:", reply_markup=menu)


update_links_insta = ["Instagram","Инстаграм","Instagram"]

for i in update_links_insta:
    @dp.message_handler(text= i)
    async def link_insta(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            menu = await Update_link(message.from_user.id)
            await message.answer("Instagram link kiriting:")
            await Update_insta.insta.set()
        
        elif users[11] == 'RUS':
            menu = await Update_link(message.from_user.id)
            await message.answer("Введите ссылку на инстаграм:")
            await Update_insta.insta.set()
            
        
        elif users[11] == 'ENG':
            menu = await Update_link(message.from_user.id)
            await message.answer("Enter Instagram link:")
            await Update_insta.insta.set()


@dp.message_handler(state=Update_insta.insta)
async def update_link_insta(message: types.Message, state : FSMContext):            
    insta =message.text
    await db.update_user_insta(insta,message.from_user.id)
    users = await db.select_all_user_one(message.from_user.id)
        
    if users[11] == 'UZB':
        await message.answer("Instagram link o`zgartirildi!")       
        await state.finish()

    elif users[11] == 'RUS':
        await message.answer("Ссылка на инстаграм изменена!")       
        await state.finish()

    elif users[11] == 'ENG':
        await message.answer("Instagram link has been changed!")       
        await state.finish()






update_links_tele = ["Telegram","Телеграмм","Telegram"]

for i in update_links_tele:
    @dp.message_handler(text= i)
    async def link_tele(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            menu = await Update_link(message.from_user.id)
            await message.answer("Telegram link kiriting:")
            await Update_tele.tele.set()
        
        elif users[11] == 'RUS':
            menu = await Update_link(message.from_user.id)
            await message.answer("Введите ссылку на Telegram:")
            await Update_tele.tele.set()
        
        elif users[11] == 'ENG':
            menu = await Update_link(message.from_user.id)
            await message.answer("Enter Telegram link:")
            await Update_tele.tele.set()


@dp.message_handler(state=Update_tele.tele)
async def update_link_tele(message: types.Message, state : FSMContext):            
    tele =message.text
    await db.update_user_tele(tele,message.from_user.id)
    users = await db.select_all_user_one(message.from_user.id)
        
    if users[11] == 'UZB':
        await message.answer("Telegram link o`zgartirildi!")       
        await state.finish()

    elif users[11] == 'RUS':
        await message.answer("Ссылка на Телеграмм изменена!")       
        await state.finish()

    elif users[11] == 'ENG':
        await message.answer("Telegram link has been changed!")       
        await state.finish()







update_links_you = ["YouTube","Ютуб","YouTube"]

for i in update_links_you:
    @dp.message_handler(text= i)
    async def link_you(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            menu = await Update_link(message.from_user.id)
            await message.answer("YouTube link kiriting:")
            await Update_you.you.set()
        
        elif users[11] == 'RUS':
            menu = await Update_link(message.from_user.id)
            await message.answer("Введите ссылку на YouTube:")
            await Update_you.you.set()
        
        elif users[11] == 'ENG':
            menu = await Update_link(message.from_user.id)
            await message.answer("Enter YouTube link:")
            await Update_you.you.set()


@dp.message_handler(state=Update_you.you)
async def update_link_you(message: types.Message, state : FSMContext):            
    you =message.text
    await db.update_user_you(you,message.from_user.id)
    users = await db.select_all_user_one(message.from_user.id)
        
    if users[11] == 'UZB':
        await message.answer("YouTube link o`zgartirildi!")       
        await state.finish()

    elif users[11] == 'RUS':
        await message.answer("Ссылка на YouTube изменена!")       
        await state.finish()

    elif users[11] == 'ENG':
        await message.answer("YouTube link has been changed!")       
        await state.finish()
