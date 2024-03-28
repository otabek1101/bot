from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
mylocation_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
         KeyboardButton(text = '📍Manzil qo`shish',request_location=True)
        ],
        [
         KeyboardButton(text='⬅️Ortga')
        ],
    ],
    resize_keyboard=True
)