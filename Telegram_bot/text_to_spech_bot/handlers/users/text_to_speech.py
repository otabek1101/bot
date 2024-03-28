from aiogram import types

from loader import dp, bot


from gtts import gTTS


@dp.message_handler(state = None)
async def text_to_S(message: types.Message):
    mytext = message.text

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save(f"audio/{message.from_user.id}.mp3")

    await bot.send_audio(message.from_user.id, open(f"audio/{message.from_user.id}.mp3", "rb" ))