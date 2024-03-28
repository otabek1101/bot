from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db
TIL = {
    'UZB':["👥 Do'stalrni taklif qilish", '📲 Vazifa bajarish', "⏪ Asosiy menyu"],
    'RUS':['👥 Пригласить друзей', '📲 Выполнить задание', "⏪ Главное меню"],
    'ENG':["👥 Invite friends", '📲 Complete a task', "⏪ Main Menu"]
}

async def Work_btn(id):
    LAN1 = await db.select_all_user_one(id)
    global LAN
    LAN = LAN1[11]
    work_btn = ReplyKeyboardMarkup(
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
        
        ],
        resize_keyboard=True
    )
    return work_btn