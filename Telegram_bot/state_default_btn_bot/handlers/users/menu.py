from cgitb import text
from operator import imod
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="Python")
async def show_menu(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menuPython)

@dp.message_handler(text = "#00 Kirish")
async def show_menu(message: Message):
    await message.answer("https://www.ictacademy.uz", reply_markup=ReplyKeyboardRemove())