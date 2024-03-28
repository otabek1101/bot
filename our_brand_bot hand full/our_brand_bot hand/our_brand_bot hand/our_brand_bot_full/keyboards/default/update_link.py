
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
TIL = {
    'UZB':["Instagram", "Telegram", "YouTube","⏪ Asosiy menyu", "🔙 Ortga"],
    'RUS':["Инстаграм", "Телеграмм", "Ютуб","⏪ Главное меню","🔙 Назад"],
    'ENG':["Instagram", "Telegram", "YouTube","⏪ Main Menu","🔙 Go Back"]
}

async def Update_link(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    update_link = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=f'{TIL[LAN][0]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][1]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][2]}'),
            
            ],
            [
                KeyboardButton(text=f'{TIL[LAN][3]}'),
                KeyboardButton(text=f'{TIL[LAN][4]}'),
            
            ],
        ],
        resize_keyboard=True
    )
    return update_link