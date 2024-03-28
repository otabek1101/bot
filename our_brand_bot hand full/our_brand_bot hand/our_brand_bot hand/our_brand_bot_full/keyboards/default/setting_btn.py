from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
TIL = {
    'UZB':["🇺🇿 Tilni tanlash", '💳 Hisob raqamni almashtirish', "👤 Shaxsiy ma'lumotlarni o'zgartirish","↪️ Linkni o'zgartirish", "⏪ Asosiy menyu"],
    'RUS':["🇷🇺 Выбор языка", "💳 Изменить номер счета", "👤 Изменить личные данные","↪️ Изменить ссылку", "⏪ Главное меню"],
    'ENG':["🇺🇸 Language selection", "💳 Change account number", "👤 Change personal data", "↪️ Change Link", "⏪ Main Menu"]
}

async def Sett_btn(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    sett_btn = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=f'{TIL[LAN][0]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][1]}'),
                KeyboardButton(text=f'{TIL[LAN][2]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][3]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][4]}'),
            
            ],
        
        ],
        resize_keyboard=True
    )
    return sett_btn