from email import message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
from aiogram import types


TIL = {
    'UZB':['🤑 Pul Ishlash','💰 Balans','👤 Shaxsiy Kabinet','📋 Qoidalar',"🧑‍💻 Bog'lanish",'⚙️ Sozlash'],
    'RUS':['🤑 Заработок', '💰 Баланс', '👤 Личный Кабинет', '📋 Правила', '🧑‍💻 Контакты', '⚙️ Настройки'],
    'ENG':['🤑 Earn Money','💰 Balance','👤 Personal Cabinet','📋 Rules',"🧑‍💻 Contact",'⚙️ Settings']
}


    

async def MenuStart(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    menuStart = ReplyKeyboardMarkup(
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
                    KeyboardButton(text=f'{TIL[LAN][4]}'),
                
                ],
                [
                    KeyboardButton(text=f'{TIL[LAN][5]}'),
                
                ],
            ],
            resize_keyboard=True
        )
    
    return menuStart