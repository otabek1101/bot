from aiogram import types
from loader import dp, db
from keyboards.default.update_shaxsiy_m import Update_shaxs
from states.update_malumot import Update_full_name,Update_age
from aiogram.dispatcher import FSMContext



shaxs = ["👤 Shaxsiy ma'lumotlarni o'zgartirish", "👤 Изменить личные данные", "👤 Change personal data"]

for i in shaxs:
    @dp.message_handler(text = i)
    async def shaxsiy(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            menu = await Update_shaxs(message.from_user.id)
            await message.answer("👤 Shaxsiy ma'lumotlarni o'zgartirish", reply_markup=menu)

        elif users[11] == 'RUS':
            menu = await Update_shaxs(message.from_user.id)
            await message.answer("👤 Изменить личные данные", reply_markup=menu)

        elif users[11] == 'ENG':
            menu = await Update_shaxs(message.from_user.id)
            await message.answer("👤 Change personal data", reply_markup=menu)






full_name = ["👤 Ism familiyangizni o`zgartirish", "👤 Измени имя и фамилию", "👤 Change your first and last name"]

for i in full_name:
    @dp.message_handler(text = i)
    async def update_full_name(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer('👤 To`liq ism familiyangizni kiriting:')
            await Update_full_name.full_name.set()

        elif users[11] == 'RUS':
            await message.answer('👤 Введите свое полное имя:')
            await Update_full_name.full_name.set()

        elif users[11] == 'ENG':
            await message.answer('👤 Enter your full name:')
            await Update_full_name.full_name.set()


@dp.message_handler(state=Update_full_name.full_name)
async def update_full_name(message: types.Message, state : FSMContext):            
    name =message.text
    await db.update_user_full_name(name,message.from_user.id)
    users = await db.select_all_user_one(message.from_user.id)
        
    if users[11] == 'UZB':
        await message.answer("Ism familiya o`zgartirildi!")       
        await state.finish()

    elif users[11] == 'RUS':
        await message.answer("Имя изменено!")       
        await state.finish()

    elif users[11] == 'ENG':
        await message.answer("The name has been changed!")       
        await state.finish()






Age = ['📆 Yoshingizni o`zgartirish', "📆 Измени возраст", '📆 Change your age']

for i in Age:
    @dp.message_handler(text = i)
    async def update_full_age(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer('📆 Yoshingizni kiriting:')
            await Update_age.age.set()

        elif users[11] == 'RUS':
            await message.answer('📆 Введите свой возраст:')
            await Update_age.age.set()

        elif users[11] == 'ENG':
            await message.answer('📆 Enter your age:')
            await Update_age.age.set()


@dp.message_handler(state=Update_age.age)
async def update_age(message: types.Message, state : FSMContext):            
    age =message.text
    await db.update_user_age(age,message.from_user.id)
    users = await db.select_all_user_one(message.from_user.id)
        
    if users[11] == 'UZB':
        await message.answer("Yosh o`zgartirildi!")       
        await state.finish()

    elif users[11] == 'RUS':
        await message.answer("Возраст изменился!")       
        await state.finish()

    elif users[11] == 'ENG':
        await message.answer("The age has been changed!")       
        await state.finish()
