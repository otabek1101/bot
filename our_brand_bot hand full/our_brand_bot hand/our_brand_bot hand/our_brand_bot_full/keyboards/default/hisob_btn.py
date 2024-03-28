from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


TIL = {
    'UZB':["💳 Click raqamini o'zgartirish","📞 Telefon raqamini o'zgartirish","⏪ Asosiy menyu",'🔙 Ortga'],
    'RUS':["💳 Изменить номер клика", "📞 Изменить номер телефона","⏪ Главное меню",'🔙 Назад'],
    'ENG':["💳 Change Click number","📞 Change phone number","⏪ Main Menu",'🔙 Go Back']
}

async def hisob_btn(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    Hisob_btn = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=f'{TIL[LAN][0]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][1]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][2]}'),
                KeyboardButton(text=f'{TIL[LAN][3]}'),
            ],
        
        ],
        resize_keyboard=True
    )
    return Hisob_btn