from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from states.rek_state import Rek_state

from loader import dp, bot

@dp.message_handler(Command="reklam")
async def get_file_id_p(message: types.Message):
    await message.reply("Post uchun rasm taylang")
    await Rek_state.photo.set()

@dp.message_handler(state=Rek_state.photo, content_types='photo')
async def Photo(message: types.Message,state: FSMContext):
    photo = message.photo[-1].file_id

    await state.update_data(
        {'Photo': photo}
    )
    await message.answer('Ma`lumot kiriting')
    await Rek_state.captions.set()

@dp.message_handler(state=Rek_state.captions)
async def Captions(message: types.Message,state: FSMContext):
    captions = message.text

    await state.update_data(
        {'Captions': captions}
    )

    data = await state.get_data()

    photo = data.get('Photo')
    captions = data.get('Captions')

    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=captions)

    await state.finish()