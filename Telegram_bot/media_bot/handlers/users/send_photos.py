from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo_id = "ID"
    photo_url = "https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"
    photo_file = InputFile(path_or_bytesio="photos/1.jpg")
    await message.reply_photo(
        photo_file, caption="Python."
    )
    await message.answer_photo(
        photo_id, caption="Python."
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Python",
    )


@dp.message_handler(Command("kurslar"))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "https://cs10.pikabu.ru/post_img/big/2019/11/12/7/1573558690172919063.jpg"
    photo2 = "https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png"
    photo3 = "https://www.kverner.ru/wp-content/uploads/2018/10/1.jpg"
    photo4 = InputFile(path_or_bytesio="photos/2.jpg")
    video1 = InputFile(path_or_bytesio="photos/11.mp4")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_video(video=video1, caption="Kurslar")
    await message.reply_media_group(media=album)