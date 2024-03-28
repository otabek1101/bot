from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
                [
                KeyboardButton(text = '🛍Buyurtma berish'),
                ],
                [
                    KeyboardButton(text='🎉Aksiya'),
                    KeyboardButton(text='ℹ️Biz haqimizda')
                ],
                [
                    KeyboardButton(text='📞Biz bilan bog`laning'),
                    KeyboardButton(text='⚙️Sozlamalar '),
                    KeyboardButton(text='🏘Mening manzillarim')

                ],
             ],
    resize_keyboard=True
)