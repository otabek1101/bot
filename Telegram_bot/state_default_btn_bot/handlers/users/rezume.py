from email import message
from email.headerregistry import Address
from tkinter.messagebox import Message
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
import data
from states.malumot import Malumot_shaxs
from keyboards.default.tell import tellButton
from loader import dp,bot 


@dp.message_handler(text='Rezume', state=None)
async def rezume_start(message: types.Message):
    await message.answer('Ism familyangizni to`liq kiriting', reply_markup=ReplyKeyboardRemove())
    await Malumot_shaxs.fish.set()

@dp.message_handler(state=Malumot_shaxs.fish)
async def Fish(message: types.Message,state: FSMContext):
    Fish = message.text


    await state.update_data(
        {'name':Fish}
    )
    await message.answer('Manzilingizni kiriting')
    await Malumot_shaxs.address.set()

@dp.message_handler(state=Malumot_shaxs.address)
async def address(message: types.Message,state: FSMContext):
    Address = message.text


    await state.update_data(
        {'add':Address}
    )
    await message.answer('Telefon raqamingizni kiriting', reply_markup=tellButton)
    await Malumot_shaxs.tel.set()

@dp.message_handler(state=Malumot_shaxs.tel, content_types=types.ContentType.CONTACT)
async def Tel(message: types.Message,state: FSMContext):
    tel = message.contact.phone_number
    # print(message)


    await state.update_data(
        {'tell':tel}
    )
    await message.answer('Rasmingizni kiriting', reply_markup=ReplyKeyboardRemove())
    await Malumot_shaxs.photo.set()

@dp.message_handler(state=Malumot_shaxs.photo, content_types='photo')
async def Photo(message: types.Message,state: FSMContext):
    photo = message.photo[-1].file_id
    #  print(message)


    await state.update_data(
        {'Photo':photo}
    )
    await message.answer('Emaillingizni kiriting')
    await Malumot_shaxs.email.set()

@dp.message_handler(state=Malumot_shaxs.email)
async def Email(message: types.Message,state: FSMContext):
    email = message.text


    await state.update_data(
        {'Email':email}
    )
    await message.answer('Kasbingizni kiriting')
    await Malumot_shaxs.job .set()


@dp.message_handler(state=Malumot_shaxs.job)
async def Job(message: types.Message,state: FSMContext):
    job = message.text


    await state.update_data(
        {'Job':job}
    )
    await message.answer('Qobiliyatlaringizni kiriting')
    await Malumot_shaxs.skills.set()


@dp.message_handler(state=Malumot_shaxs.skills)
async def Skills(message: types.Message,state: FSMContext):
    skills = message.text


    await state.update_data(
        {'Skills':skills}
    )

    data = await state.get_data()

    name = data.get('name')
    add = data.get('add')
    tell = data.get('tell')
    rasm = data.get('Photo')
    email = data.get('Email')
    kasb = data.get('Job')
    Qobiliyat = data.get('Skills')

    text = f'Foydalanuvchi ismi: {name}'
    text += f'\nManzili: {add}'
    text += f'\nTelefon raqami: {tell}'
    text += f'\nEmail manzili: {email}'
    text += f'\nKasbi: {kasb}'
    text += f'\nQobiliyatlari: {Qobiliyat}'

    await bot.send_photo(chat_id=message.from_user.id, photo=rasm, caption=text)

    await state.finish()
