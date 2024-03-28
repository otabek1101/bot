from aiogram import types
from loader import dp, db
from keyboards.default.balans_btn import Balans_btn

kon = ["🧑‍💻 Bog'lanish", '🧑‍💻 Контакты', "🧑‍💻 Contact"]
 
for i in kon:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer("📞 Kontakt")

        elif users[11] == 'RUS':
            await message.answer("📞 Контакт")

        elif users[11] == 'ENG':
            await message.answer("📞 Contact")
