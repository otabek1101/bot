from aiogram import types
from loader import dp, db
from keyboards.default.clik_pay import Clic_btn
from keyboards.default.balans_btn import Balans_btn

pul = ["📤 Pulni yechib olish", '📤 Снять деньги', "📤 Withdraw money"]

for i in pul:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            clic = await Clic_btn(message.from_user.id)
            await message.answer("👇 To'lov turini tanlang", reply_markup=clic)

        elif users[11] == 'RUS':
            clic = await Clic_btn(message.from_user.id)
            await message.answer("👇 Выберите тип оплаты", reply_markup=clic)

        elif users[11] == 'ENG':
            clic = await Clic_btn(message.from_user.id)
            await message.answer("👇 Select payment type", reply_markup=clic)

clic = ["💳 Click", '💳 Клик', "💳 Click"]

for i in clic:

    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer(f"""Click raqamingiz: {users[10]}

    Agar boshqa kartaga pul yechmoqchi bo'lsangiz /sozlash bo'limidan karta raqamini o'zgartiring""")

        elif users[11] == 'RUS':
            await message.answer(f"""Ваш номер клика: {users[10]}

     Если вы хотите вывести деньги на другую карту, измените номер карты в разделе /settings""")

        elif users[11] == 'ENG':
            await message.answer(f"""Your click number:{users[10]}

     If you want to withdraw money to another card, change the card number from the /settings section""")
        
pay = ["🟢 Paynet", "🟢 Пайнет", "🟢 Paynet"]

for i in pay: 

    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer(f"""Paynet uchun tel nomeringiz: {users[4]}

    Agar boshqa nomerga pul yechmoqchi bo'lsangiz /sozlash bo'limidan nomerni o'zgartiring""")

        elif users[11] == 'RUS':
            await message.answer(f"""Ваш номер телефона для Paynet: {users[4]}

     Если вы хотите вывести деньги на другой номер, измените номер в разделе /settings""")

        elif users[11] == 'ENG':
            await message.answer(f"""Your phone number for Paynet: {users[4]}

     If you want to withdraw money to another number, change the number from the /settings section""")



orqa = ['⏮ Ortga','⏮ Назад',"⏮ Go Back"]

for i in orqa:
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):  
        users = await db.select_all_user_one(message.from_user.id)   
        
        if users[11] == 'UZB':
            menu = await Balans_btn(message.from_user.id)
            await message.answer("Asosiy menyu", reply_markup=menu)

        elif users[11] == "RUS":
            menu = await Balans_btn(message.from_user.id)
            await message.answer("Главное меню", reply_markup=menu)

        elif users[11] == "ENG":
            menu = await Balans_btn(message.from_user.id)
            await message.answer("Main Menu", reply_markup=menu)
