from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buyurtma_btn = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='⬅️Ortga'),
            KeyboardButton(text='📥Savat')
        ],
        [
            KeyboardButton(text='Maksi Boks'),
            KeyboardButton(text='🥪Klab senvich')
        ],
        [
            KeyboardButton(text='🌯Lavash'),
            KeyboardButton(text='🥙Shourma')
        ],
        [
            KeyboardButton(text='🍱Donar blyuda'),
            KeyboardButton(text='🌮Shourma Bagey(xagi)')
        ],
        [
            KeyboardButton(text='🍔Burgeri'),
            KeyboardButton(text='🌭Xot dog')
        ],
        [
            KeyboardButton(text='Sneki'),
            KeyboardButton(text='Garniri')
        ],
        [
            KeyboardButton(text='🥫Sous'),
            KeyboardButton(text='🥤Napitki')
        ],
        [
            KeyboardButton(text='🧁Diserti'),
        ],
    ],
    resize_keyboard=True
)