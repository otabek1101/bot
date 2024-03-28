from distutils.cmd import Command
import email
from os import stat
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
# from states.malumot import Malumot_shaxs
from loader import dp
from states.malumot import Malumot_shaxs


@dp.message_handler(Command("rezume"))
async def bot_start(message: types.Message):
    await message.answer("Ism familyangizni to`liq kiriting!")
    await Malumot_shaxs.fish.set()

@dp.message_handler(state=Malumot_shaxs.fish)
async def Fish(message: types.Message, state: FSMContext):
    FISH = message.text
    await state.update_data(
        {'name' :FISH}
    )
    await message.answer("Manzilingizni kiriting!")
    await Malumot_shaxs.adress.set()

@dp.message_handler(state=Malumot_shaxs.adress)
async def Adress(message: types.Message, state: FSMContext):
    ADRESS = message.text
    await state.update_data(
        {'adress' :ADRESS}
    )
    await message.answer(" Telfon raqam kiriting!")
    await Malumot_shaxs.tel.set()

@dp.message_handler(state=Malumot_shaxs.tel)
async def Tel(message: types.Message, state: FSMContext):
    TEL = message.text
    await state.update_data(
        {'tel' :TEL}
    )
    await message.answer(" Rasmingizni kiriting!")
    await Malumot_shaxs.photo.set()

@dp.message_handler(state=Malumot_shaxs.photo, content_types=types.ContentTypes.PHOTO)
async def Photo(message: types.Message, state: FSMContext):
    PHOTO = (message.photo[-1].file_id)
    # print(message.photo[-1].file_id)
    await state.update_data(
        {'photo' :PHOTO}
    )
    await message.answer(" Emailingizni kiriting!")
    await Malumot_shaxs.email.set()

@dp.message_handler(state=Malumot_shaxs.email)
async def Email(message: types.Message, state: FSMContext):
    EMAIL = message.text
    await state.update_data(
        {'email' :EMAIL}
    )
    await message.answer("Kasbingizni kiriting!")
    await Malumot_shaxs.job.set()

@dp.message_handler(state=Malumot_shaxs.job)
async def Job(message: types.Message, state: FSMContext):
    JOB = message.text
    await state.update_data(
        {'job' :JOB}
    )
    await message.answer("Qobliyatingizni kiriting!")
    await Malumot_shaxs.skils.set()

@dp.message_handler(state=Malumot_shaxs.skils)
async def Skils(message: types.Message, state: FSMContext):
    SKILS = message.text
    await state.update_data(
        {'skils' :SKILS}
    )
    
    data = await state.get_data()

    name = data.get('name')
    adress = data.get('adress')
    tell = data.get('tel')
    photo = data.get('photo')
    email = data.get('email')
    job = data.get('job')
    skils = data.get('skils')

    
