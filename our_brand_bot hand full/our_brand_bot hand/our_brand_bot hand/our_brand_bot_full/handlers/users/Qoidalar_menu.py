from aiogram import types
from loader import dp, db
from keyboards.default.startmenu import MenuStart


rul = ['📋 Qoidalar', '📋 Правила', '📋 Rules']
    


for i in rul:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            await message.answer("👮‍♂ Qoidalar")
        elif users[11] == 'RUS':
             await message.answer("👮‍♂ Правила")
        elif users[11] == 'ENG':
            await message.answer("👮‍♂ Rules")
