from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp, db


TIL = {
    'UZB':['Telefon raqam'],
    'RUS':['Контакт'],
    'ENG':['Contact']
}

async def tell_btn(LAN):
    
    Tel_button = ReplyKeyboardMarkup(
        keyboard= [
            [
                KeyboardButton(text=f'{TIL[LAN][0]}',request_contact=True),
            ],
        ],
        resize_keyboard=True
    )
    return Tel_button