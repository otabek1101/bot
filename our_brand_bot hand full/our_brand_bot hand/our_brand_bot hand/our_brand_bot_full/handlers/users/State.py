
from ast import Add
from tkinter.tix import INTEGER

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery

import requests
from states.malumot import Malumot_shaxs
from loader import dp,bot,db
from keyboards.inline.til import til_menu , key
from keyboards.inline.link import link_menu
from keyboards.inline.gender import gen_menu_uz,gen_menu_ru,gen_menu_us
from keyboards.default.contact import tell_btn
from keyboards.default.startmenu import MenuStart
import asyncpg
import re


from data.config import ADMINS





@dp.message_handler(Command('start'), state=None)
async def til_tanlash(message: types.Message):

   
   
    users = await db.select_all_users()
    A = 0
    for i in users:
        if i[1] == message.from_user.id:
            A+=1
            break
    if A == 1:
        menu = await MenuStart(message.from_user.id)
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu)
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!")
        await message.answer('🇺🇿 🇷🇺 🇺🇸 Tilni tanlang: ', reply_markup=til_menu)

        await Malumot_shaxs.til.set()



@dp.callback_query_handler(state=Malumot_shaxs.til)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    global Til
    Til = call.data
    
    await state.update_data(
        {'tillar':Til}
    )
        
    if Til == 'UZB':
        await call.message.delete()
        await call.answer(cache_time=60)
        await call.message.answer('Instagram linkingizni kiriting: ')
        await Malumot_shaxs.link_ins.set()
    elif Til == "RUS":
        await call.message.delete()
        await call.answer(cache_time=60)
        await call.message.answer('Введите ссылку на ваш инстаграм: ')
        await Malumot_shaxs.link_ins.set()
    elif Til == "ENG":
        await call.message.delete()
        await call.answer(cache_time=60)
        await call.message.answer('Enter your Instagram link: ')
        await Malumot_shaxs.link_ins.set()



@dp.message_handler(state=Malumot_shaxs.link_ins)
async def link(message: types.Message,state: FSMContext):

    if Til == 'UZB':
        # link_ins = message.text
        URL = f"https://www.instagram.com/message.text"
        request = requests.get(URL)
        print(request.status_code)
        if request.status_code == 200:
            link_ins = message.text
            await state.update_data(
            {'link_ins':link_ins}
            )
        else:
            await message.answer('Kiritilgan link noto`g`ri iltimos tekshirib qayta urunib ko`ring:') 
            await Malumot_shaxs.link_ins.set()
    elif Til == "RUS":
        URL = f"https://www.instagram.com/message.text"
        request = requests.get(URL)
        print(request.status_code)
        if request.status_code == 200:
            link_ins = message.text
            await state.update_data(
            {'link_ins':link_ins}
            )
        else:
            await message.answer('Введенная ссылка неверна, проверьте и повторите попытку:') 
            await Malumot_shaxs.link_ins.set()
    elif Til == "ENG":
        URL = f"https://www.instagram.com/message.text"
        request = requests.get(URL)
        print(request.status_code)
        if request.status_code == 200:
            link_ins = message.text
            await state.update_data(
            {'link_ins':link_ins}
            )
        else:
            await message.answer('The entered link is incorrect, please check and try again:') 
            await Malumot_shaxs.link_ins.set()

    if Til == 'UZB':
        await message.answer('Telegram linkingizni kiritng: ')
        await Malumot_shaxs.link_tg.set()
    elif Til == "RUS":
        await message.answer('Введите ссылку на ваш Telegram: ')
        await Malumot_shaxs.link_tg.set()
    elif Til == "ENG":
        await message.answer('Enter your Telegram link: ')
        await Malumot_shaxs.link_tg.set()



@dp.message_handler(state=Malumot_shaxs.link_tg)
async def link(message: types.Message,state: FSMContext):
    link_tg = message.text


    await state.update_data(
        {'link_tg':link_tg}
    )

    if Til == 'UZB':
        await message.answer('YouTube linkingizni kiritng: ')
        await Malumot_shaxs.link_you.set()
    elif Til == "RUS":
        await message.answer('Введите ссылку на YouTube: ')
        await Malumot_shaxs.link_you.set()
    elif Til == "ENG":
        await message.answer('Enter your YouTube link: ')
        await Malumot_shaxs.link_you.set()




@dp.message_handler(state=Malumot_shaxs.link_you)
async def link(message: types.Message,state: FSMContext):
    link_you = message.text


    await state.update_data(
        {'link_you':link_you}
    )

    if Til == 'UZB':
        await message.answer('👤 To`liq ism familiyangizni kiriting:')
        await Malumot_shaxs.full_name.set()
    elif Til == "RUS":
        await message.answer('👤 Введите свое полное имя:')
        await Malumot_shaxs.full_name.set()
    elif Til == "ENG":
        await message.answer('👤 Enter your full name:')
        await Malumot_shaxs.full_name.set()


@dp.message_handler(state=Malumot_shaxs.full_name)
async def name(message: types.Message,state: FSMContext):
    Name = message.text

    await state.update_data(
        {'name':Name}
    )

    if Til == 'UZB':
        menu = await tell_btn(Til)
        await message.answer('📞 Telefon raqamingizni kiriting:', reply_markup=menu)
        await Malumot_shaxs.tel.set()
    elif Til == "RUS":
        menu = await tell_btn(Til)
        await message.answer('📞 Введите свой номер телефона:', reply_markup=menu)
        await Malumot_shaxs.tel.set()
    elif Til == "ENG":
        menu = await tell_btn(Til)
        await message.answer('📞 Enter your phone number:', reply_markup=menu)
        await Malumot_shaxs.tel.set()


@dp.message_handler(state=Malumot_shaxs.tel, content_types=types.ContentType.CONTACT)
async def Tel(message: types.Message,state: FSMContext):
    tel = message.contact.phone_number
    # print(message)


    await state.update_data(
        {'tell':tel}
    )

    if Til == 'UZB':
        await message.answer('📆 Yoshingizni kiriting:',reply_markup=ReplyKeyboardRemove())
        await Malumot_shaxs.age.set()
    elif Til == "RUS":
        await message.answer('📆 Введите свой возраст:',reply_markup=ReplyKeyboardRemove())
        await Malumot_shaxs.age.set()
    elif Til == "ENG":
        await message.answer('📆 Enter your age:',reply_markup=ReplyKeyboardRemove())
        await Malumot_shaxs.age.set()       



@dp.message_handler(state=Malumot_shaxs.age    )
async def age(message: types.Message,state: FSMContext):
    Age = message.text


    await state.update_data(
        {'yosh':Age}
    )
    
    if Til == 'UZB':
        await message.answer('🙎🏻‍♂️🙍🏻‍♀️ Jinsingizni tanlang:',reply_markup=gen_menu_uz)
        await Malumot_shaxs.gender.set()
    elif Til == "RUS":
        await message.answer('🙎🏻‍♂️🙍🏻‍♀️ Выберите свой пол:',reply_markup=gen_menu_ru)
        await Malumot_shaxs.gender.set()
    elif Til == "ENG":
        await message.answer('🙎🏻‍♂️🙍🏻‍♀️ Choose your gender:',reply_markup=gen_menu_us)
        await Malumot_shaxs.gender.set()


@dp.callback_query_handler(state=Malumot_shaxs.gender)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    Gen = call.data
    await state.update_data(
        {'jins':Gen}
    )
    await call.message.delete()
    await call.answer(cache_time=60)


    if Til == 'UZB':
        await call.message.answer('💳 Hisob raqamingizni kiriting: ')
        await Malumot_shaxs.card.set()
    elif Til == "RUS":
        await call.message.answer('💳 Введите номер вашего счета: ')
        await Malumot_shaxs.card.set()
    elif Til == "ENG":
        await call.message.answer('💳 Enter your account number: ')
        await Malumot_shaxs.card.set()


@dp.message_handler(state=Malumot_shaxs.card)
async def update_card(message: types.Message, state : FSMContext):            
    Card =message.text
    def tekshirish_humo(num):
        humo = re.compile('(^9860[0-9]{12}(?:[0-9]{3})?$)')
        return humo.match(num)

    def tekshirish_uzcard(num):
        uzcard = re.compile('(^8600[0-9]{12}(?:[0-9]{3})?$)')
        return uzcard.match(num)
    def tekshirish_visa(num):
        visa= re.compile('(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)')
        return visa.match(num)
    num = Card

    if tekshirish_humo(num) or tekshirish_uzcard(num) or tekshirish_visa(num):
        await db.update_user_card(Card,message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)
            
        if Til == 'UZB':
            await message.answer("💳 Hisob raqam qabul qilindi")       
            await state.update_data(
        {'karta':Card}
    )


        elif Til ==  'RUS':
            await message.answer("💳 Номер счета принят")       
            await state.update_data(
        {'karta':Card}
    )


        elif Til ==  'ENG':
            await message.answer("💳 Account number accepted")       
            await state.update_data(
        {'karta':Card}
    )

       
    else:
        
        if  Til == 'UZB':
            await message.answer("💳 Hisob raqam noto`g`ri kiritilgan qayta urunib ko`ring:")       
            await Malumot_shaxs.card.set()

        elif Til ==  'RUS':
            await message.answer("💳 Номер счета введен неправильно, попробуйте еще раз:")       
            await Malumot_shaxs.card.set()

        elif Til ==  'ENG':
            await message.answer("💳 Account number entered incorrectly, please try again:")       
            await Malumot_shaxs.card.set()


    
    data = await state.get_data()

    til = data.get('tillar')
    link_ins = data.get('link_ins')
    link_tg = data.get('link_tg')
    link_you = data.get('link_you')
    name = data.get('name')
    tel = data.get('tell')
    jins = data.get('jins')
    age = data.get('yosh')
    card = data.get('karta')

    # # global text
    # # text = f'Tanlangan til: {til}'
    # # text += f'\nLink Instagram: {link_ins}'
    # # text += f'\nLink Telegram: {link_tg}'
    # # text += f'\nLink YouTube: {link_you}'
    # # text += f'\nIsm familiya: {name}'
    # # text += f'\nTelefon raqam: {tell}'
    # # text += f'\nJins: {jins}'
    # # text += f'\nYosh: {age}'
    # # text += f'\nHisob raqam: {card}'

    
    # # await message.answer(text)

    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=name,
            username=message.from_user.username,
            telling=tel,
            gen=jins,
            Age=age,
            Link_ins=link_ins,
            Link_tg=link_tg,
            Link_you=link_you,
            Cards=card,
            Til=til

            

        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    menu = await MenuStart(message.from_user.id)
    if Til == 'UZB':
        await message.answer('🤖 Botga xush kelibsiz', reply_markup=menu)
        await state.finish()
    elif Til == "RUS":
        await message.answer('🤖 Добро пожаловать в бота', reply_markup=menu)
        await state.finish()
    elif Til == "ENG":
        await message.answer('🤖 Welcome to the bot', reply_markup=menu)
        await state.finish()
 
    
    # await message.answer("Sizning malumotlariz qabul qilindi")

    # ADMINGA xabar beramiz
    menu = await MenuStart(message.from_user.id)
    count = await db.count_users()
    msg = f"{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)



