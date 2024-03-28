from aiogram import types
from loader import dp, db
from keyboards.default.balans_btn import Balans_btn

kab = ['👤 Shaxsiy Kabinet', '👤 Личный Кабинет', '👤 Personal Cabinet']

for i in kab:

    @dp.message_handler(text = i)
    async def bot_help(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
        
            await message.answer(f'Assalomu aleykum {message.from_user.full_name}!')

            
            text = f'✅ Tanlangan til: {users[11]}'
            text += f'\n✅ Link Instagram: {users[7]}'
            text += f'\n✅ Link Telegram: {users[8]}'
            text += f'\n✅ Link YouTube: {users[9]}'
            text += f'\n✅ Ism familiya: {users[2]}'
            text += f'\n✅ Telefon raqam: {users[4]}'
            text += f'\n✅ Jinsi: {users[5]}'
            text += f'\n✅ Yoshi: {users[6]}'
            text += f'\n✅ Hisob raqam: {users[10]}'

            
            await message.answer(text)
            
        elif users[11] == "RUS":
            await message.answer(f'Здравствуйте {message.from_user.full_name}!')

            
            text = f'✅ Выбранный язык: {users[11]}'
            text += f'\n✅ Ссылка на инстаграм: {users[7]}'
            text += f'\n✅ Ссылка на телеграмму: {users[8]}'
            text += f'\n✅ Ссылка на YouTube: {users[9]}'
            text += f'\n✅ Имя и фамилия: {users[2]}'
            text += f'\n✅ Номер телефона: {users[4]}'
            text += f'\n✅ Пол: {users[5]}'
            text += f'\n✅ Возраст: {users[6]}'
            text += f'\n✅ Номер счета: {users[10]}'

            
            await message.answer(text)
        
        elif users[11] == "ENG":
            await message.answer(f'Hello {message.from_user.full_name}!')


            text = f'✅ Selected language: {users[11]}'
            text += f'\n✅ Link Instagram: {users[7]}'
            text += f'\n✅ Link Telegram: {users[8]}'
            text += f'\n✅ Link YouTube: {users[9]}'
            text += f'\n✅ Name is surname: {users[2]}'
            text += f'\n✅ Phone number: {users[4]}'
            text += f'\n✅ Gender: {users[5]}'
            text += f'\n✅ Age: {users[6]}'
            text += f'\n✅ Account number: {users[10]}'

            
            await message.answer(text)
    
#     await message.answer("""👤 Shaxsiy Kabinetzz

# Assalomu alaykum (Foydalanuvchi niki) 

# ✅ Ismingiz: Ism 
# ✅ Jinsingiz: Jins
# ✅ Yoshingiz: Yosh 
# ✅ Manzil: Manzil
# ✅ Tel nomeringiz: nomer

# 👥 Do'stlaringiz: **** ta
# 📎 Shaxsiy referal linkingiz: https://t.me/paynetbot?reflink216274368""")