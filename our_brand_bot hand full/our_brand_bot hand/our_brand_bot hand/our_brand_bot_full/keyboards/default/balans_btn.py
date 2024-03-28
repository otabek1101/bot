from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


TIL = {
    'UZB':["📤 Pulni yechib olish","⏪ Asosiy menyu"],
    'RUS':['📤 Снять деньги',"⏪ Главное меню"],
    'ENG':["📤 Withdraw money","⏪ Main Menu"]
}

async def Balans_btn(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    balns_btn = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=f'{TIL[LAN][0]}'),
            
            ],
            
            [
                KeyboardButton(text=f'{TIL[LAN][1]}'),
            
            ],
        
        ],
        resize_keyboard=True
    )
    return balns_btn