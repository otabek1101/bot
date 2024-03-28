from ast import Break
from aiogram import types
from loader import dp, db
from keyboards.default.hisob_btn import hisob_btn
from keyboards.default.setting_btn import Sett_btn
from keyboards.default.startmenu import MenuStart
from states.update_malumot import Update_tel,Update_card
from aiogram.dispatcher import FSMContext
import re

hisob = ['💳 Hisob raqamni almashtirish', "💳 Изменить номер счета", "💳 Change account number"]

for i in hisob:
    @dp.message_handler(text = i)
    async def cars_change(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            menu = await hisob_btn(message.from_user.id)
            await message.answer("💳 Hisob raqamni almashtirish", reply_markup=menu)

        elif users[11] == 'RUS':
            menu = await hisob_btn(message.from_user.id)
            await message.answer("💳 Изменить номер счета", reply_markup=menu)

        elif users[11] == 'ENG':
            menu = await hisob_btn(message.from_user.id)
            await message.answer("💳 Change account number", reply_markup=menu)

clic = ["💳 Click raqamini o'zgartirish", "💳 Изменить номер клика", "💳 Change Click number"]

for i in clic:
    @dp.message_handler(text = i)
    async def card(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)

        if users[11] == 'UZB':
            await message.answer("💳 Yangi click raqamini kiriting:")
            await Update_card.card.set()

        elif users[11] == 'RUS':
            await message.answer("💳 Введите новый номер клика:")
            await Update_card.card.set()

        elif users[11] == 'ENG':
            await message.answer("💳 Enter the new click number:")
            await Update_card.card.set()



@dp.message_handler(state=Update_card.card)
async def update_card(message: types.Message, state : FSMContext):            
    Card =message.text
    def tekshirish_humo(num):
        humo = re.compile('(^9860[0-9]{12}(?:[0-9]{3})?$)')
        return humo.match(num)

    def tekshirish_uzcard(num):
        uzcard = re.compile('(^8600[0-9]{12}(?:[0-9]{3})?$)')
        return uzcard.match(num)
    def tekshirish_visa(num):
        visa= re.compile('(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)')
        return visa.match(num)
    num = Card

    if tekshirish_humo(num) or tekshirish_uzcard(num) or tekshirish_visa(num):
        await db.update_user_card(Card,message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)
            
        if users[11] == 'UZB':
            await message.answer("💳 Hisob raqam o`zgartirildi!")       
            await state.finish()

        elif users[11] == 'RUS':
            await message.answer("💳 Номер счета изменен!")       
            await state.finish()

        elif users[11] == 'ENG':
            await message.answer("💳 The account number has been changed!")       
            await state.finish()
       
    else:
        users = await db.select_all_user_one(message.from_user.id)
        if users[11] == 'UZB':
            await message.answer("💳 Hisob raqam noto`g`ri kiritilgan qayta urunib ko`ring:")       
            await Update_card.card.set()

        elif users[11] == 'RUS':
            await message.answer("💳 Номер счета введен неправильно, попробуйте еще раз:")       
            await Update_card.card.set()

        elif users[11] == 'ENG':
            await message.answer("💳 Account number entered incorrectly, please try again:")       
            await Update_card.card.set()
        
    

tel = ["📞 Telefon raqamini o'zgartirish",  "📞 Изменить номер телефона", "📞 Change phone number"]

for i in tel:
    @dp.message_handler(text = i)
    async def tell(message: types.Message):
        users = await db.select_all_user_one(message.from_user.id)
        
        if users[11] == 'UZB':
            await message.answer("📞 Yangi telefon nomer kiriting:")
            await Update_tel.tel.set()
            

            
        elif users[11] == 'RUS':
            await message.answer("📞 Введите новый номер телефона:")
            await Update_tel.tel.set()
            
            

        elif users[11] == 'ENG':
            await message.answer("📞 Enter a new phone number:")
            await Update_tel.tel.set()





            
@dp.message_handler(state=Update_tel.tel)
async def update_tell(message: types.Message, state : FSMContext):            
    Tell =message.text

    def tekshirish(num):
        pattern = re.compile('^[\+]?[(]?[9-9]{2}[)]?[-\s\.]?[8-8]{1}[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{5,5}$')
        return pattern.match(num)

    num = Tell

    if tekshirish(num):
        await db.update_user_telling(Tell,message.from_user.id)
        users = await db.select_all_user_one(message.from_user.id)
        if users[11] == 'UZB':
            await message.answer("📞 Telefon nomer o`zgartirildi!")       
            await state.finish()

        elif users[11] == 'RUS':
            await message.answer("📞 Номер телефона изменен!")       
            await state.finish()

        elif users[11] == 'ENG':
            await message.answer("📞 The phone number has been changed!")       
            await state.finish()

    else: 
        users = await db.select_all_user_one(message.from_user.id)
        if users[11] == 'UZB':
            await message.answer("📞 Telefon nomer noto`g`ri kiritilgan qayta urunib ko`ring:")       
            await Update_tel.tel.set()

        elif users[11] == 'RUS':
            await message.answer("📞 Номер телефона введен неверно, попробуйте еще раз:")       
            await Update_tel.tel.set()

        elif users[11] == 'ENG':
            await message.answer("📞 The phone number was entered incorrectly, please try again:")       
            await Update_tel.tel.set() 
        
        
    
        
    



orqa = ['🔙 Ortga','🔙 Назад',"🔙 Go Back"]

for i in orqa:
    @dp.message_handler(text = i)
    async def orqaga(message: types.Message):  
        users = await db.select_all_user_one(message.from_user.id)   
        
        if users[11] == 'UZB':
            menu = await Sett_btn(message.from_user.id)
            await message.answer("Asosiy menyu", reply_markup=menu)

        elif users[11] == "RUS":
            menu = await Sett_btn(message.from_user.id)
            await message.answer("Главное меню", reply_markup=menu)

        elif users[11] == "ENG":
            menu = await Sett_btn(message.from_user.id)
            await message.answer("Main Menu", reply_markup=menu)

main = ["⏪ Asosiy menyu","⏪ Главное меню","⏪ Main Menu"]

for i in main:
    @dp.message_handler(text = i)
    async def asosiy_menu(message: types.Message):  
        users = await db.select_all_user_one(message.from_user.id)   
        
        if users[11] == 'UZB':
            menu = await MenuStart(message.from_user.id)
            await message.answer("Asosiy menyu", reply_markup=menu)

        elif users[11] == "RUS":
            menu = await MenuStart(message.from_user.id)
            await message.answer("Главное меню", reply_markup=menu)

        elif users[11] == "ENG":
            menu = await MenuStart(message.from_user.id)
            await message.answer("Main Menu", reply_markup=menu)