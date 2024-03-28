from aiogram import types
from loader import dp, db
from keyboards.default.balans_btn import Balans_btn

balans = ['💰 Balans', '💰 Баланс', '💰 Balance']

for i in balans:
    
    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        Sum = await db.select_all_user_one(message.from_user.id)

        if Sum[11] == 'UZB':
            text1 = "\nBalans 🤑"
            text1 +=  f'\n💰Sizning hisobingizda: {Sum[12]} so`m mavjud'
            text1 += f'\n\n💵 Umumiy ishlagan pullaringiz: **** so`m'
            text1 += f'\n💸 Yechib oldingiz: **** so`m '
            text1 += f'\n\n💳 Sizning karta raqamingiz: {Sum[10]}'
            text1 += f'\n📞 Paynet uchun tel nomeringiz: {Sum[4]}'
            
            menu = await Balans_btn(message.from_user.id)
            await message.answer(text1, reply_markup=menu)

        elif Sum[11] == "RUS":
            text1 = "\nБаланс 🤑"
            text1 += f'\n💰На вашем счету: {Sum[12]} сумов'
            text1 += f'\n\n💵 Сумма ваших заработанных денег: **** сум'
            text1 += f'\n💸 Вы сняли: **** сум '
            text1 += f'\n\n💳 Номер вашей карты: {Sum[10]}'
            text1 += f'\n📞 Ваш номер телефона для Paynet: {Sum[4]}'

            menu = await Balans_btn(message.from_user.id)
            await message.answer(text1, reply_markup=menu)
        
        elif Sum[11] == "ENG":
            text1 = "\nBalance 🤑"
            text1 += f'\n💰Your account has: {Sum[12]} money'
            text1 += f'\n\n💵 Your total earned money: **** '
            text1 += f'\n💸 You have withdrawn: ****  '
            text1 += f'\n\n💳 Your card number: {Sum[10]}'
            text1 += f'\n📞 Your phone number for Paynet: {Sum[4]}'

            menu = await Balans_btn(message.from_user.id)
            await message.answer(text1, reply_markup=menu)
    
    
#     await message.answer("Balans 🤑")
#     await message.answer("""💰Sizning hisobingizda: **** so'm mavjud

# 💵 Umumiy ishlagan pullaringiz: **** so'm 
# 💸 Yechib oldingiz: **** so'm 

# 💳 Sizning karta raqamingiz: karta raqam
# 📞 Paynet uchun tel nomeringiz: tel nomer""", reply_markup=balns_btn)