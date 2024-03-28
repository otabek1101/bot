from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
TIL = {
    'UZB':["👤 Ism familiyangizni o`zgartirish",'📆 Yoshingizni o`zgartirish',"⏪ Asosiy menyu", "🔙 Ortga"],
    'RUS':["👤 Измени имя и фамилию", "📆 Измени возраст","⏪ Главное меню","🔙 Назад"],
    'ENG':["👤 Change your first and last name",'📆 Change your age',"⏪ Main Menu","🔙 Go Back"]
}

async def Update_shaxs(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    update_shaxs = ReplyKeyboardMarkup(
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
    return update_shaxs