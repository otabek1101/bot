from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


TIL = {
    'UZB':["💳 Click","🟢 Paynet","⏪ Asosiy menyu",'⏮ Ortga'],
    'RUS':['💳 Клик',"🟢 Пайнет","⏪ Главное меню",'⏮ Назад'],
    'ENG':["💳 Click","🟢 Paynet","⏪ Main Menu",'⏮ Go Back']
}

async def Clic_btn(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    clik_btn = ReplyKeyboardMarkup(
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
    return clik_btn