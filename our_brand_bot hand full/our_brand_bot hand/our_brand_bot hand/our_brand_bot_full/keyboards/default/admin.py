from email import message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
from aiogram import types


TIL = {
    'UZB':["🔁 Kanallarni o'zgartirish", "📈 Statistika sozlamalari", "⚙️ Qoidalarni sozlash", "⚙️ Kontaktlarni sozlash", "⏪ Asosiy menyu" ],
    'RUS':["🔁 Изменить каналы", "📈 Настройки статистики", "⚙️ Настройки правил", "⚙️ Настройки контактов","⏪ Главное меню"],
    'ENG':["🔁 Change Channels", "📈 Statistics Settings", "⚙️ Rules Settings", "⚙️ Contacts Settings","⏪ Main Menu"]
}


    

async def AdminStart(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    adminStart = ReplyKeyboardMarkup(
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
                
                ],
                [
                    KeyboardButton(text=f'{TIL[LAN][4]}'),
            
                ],
        
            ],
            resize_keyboard=True
        )
    
    return adminStart