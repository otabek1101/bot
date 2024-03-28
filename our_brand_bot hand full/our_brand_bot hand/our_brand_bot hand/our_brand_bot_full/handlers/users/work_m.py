from aiogram import types
from loader import dp, db
from keyboards.default.work_money import Work_btn
from keyboards.default.startmenu import MenuStart

ish = ['🤑 Pul Ishlash','🤑 Заработок','🤑 Earn Money']
    



for i in ish:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        work_btn = await Work_btn(message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
             await message.answer("Pul ishlash 🤑", reply_markup=work_btn)

        elif users[11] == "RUS":
            await message.answer("Заработок 🤑", reply_markup=work_btn)

        elif users[11] == "ENG":
            await message.answer("Earn Money 🤑", reply_markup=work_btn)

# orqa = ['🔙 Ortga','🔙 Назад',"🔙 Go Back"]

# for i in orqa:
#     @dp.message_handler(text = i)
#     async def bot_help(message: types.Message):  
#         users = await db.select_all_user_one(message.from_user.id)   
        
#         if users[11] == 'UZB':
#             menu = await MenuStart(message.from_user.id)
#             await message.answer("Asosiy menyu", reply_markup=menu)

#         elif users[11] == "RUS":
#             menu = await MenuStart(message.from_user.id)
#             await message.answer("Главное меню", reply_markup=menu)

#         elif users[11] == "ENG":
#             menu = await MenuStart(message.from_user.id)
#             await message.answer("Main Menu", reply_markup=menu)

dust = ["👥 Do'stalrni taklif qilish","👥 Пригласить друзей","👥 Invite friends"]

for i in dust:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)   
        
        if users[11] == 'UZB':
        
            await message.answer("""📎 Ushbu referal linkini do'stlaringizga yuboring 👉\nhttps://t.me/paynetbot?refllink216294947\n
        🤖 Botdan ro'yxatdan o'tgan har bir do'stingiz uchun sizga: 250 so'm to'lanadi\n

        💸 Pullaringizni paynet orqali telefon raqamingizga yoki kartangizga yechib olishingiz mumkin""")

        elif users[11] == "RUS":
            await message.answer("""RUS 📎 Ushbu referal linkini do'stlaringizga yuboring 👉\nhttps://t.me/paynetbot?refllink216294947\n
        🤖 Botdan ro'yxatdan o'tgan har bir do'stingiz uchun sizga: 250 so'm to'lanadi\n

        💸 Pullaringizni paynet orqali telefon raqamingizga yoki kartangizga yechib olishingiz mumkin""")

        elif users[11] == "ENG":
            await message.answer("""ENG 📎 Ushbu referal linkini do'stlaringizga yuboring 👉\nhttps://t.me/paynetbot?refllink216294947\n
        🤖 Botdan ro'yxatdan o'tgan har bir do'stingiz uchun sizga: 250 so'm to'lanadi\n

        💸 Pullaringizni paynet orqali telefon raqamingizga yoki kartangizga yechib olishingiz mumkin""")
       


vz = ["📲 Vazifa bajarish",'📲 Выполнить задание','📲 Complete a task']

for i in vz:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)   
        
        if users[11] == 'UZB':
            await message.answer("📲 Internetda vazifa bajarib pul ishlash")

        elif users[11] == "RUS":
            await message.answer("📲 Зарабатывай, выполняя задания в интернете")

        elif users[11] == "ENG":
             await message.answer("📲 Make money doing tasks on the Internet")
