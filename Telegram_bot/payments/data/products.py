from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


A_I = Product(
    title="Sun'iy intellekt",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='AI',
            amount=100000000, #1mln
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-10000000, #-100 ming
        ),
    ],
    start_parameter="create_invoice_ai_course",
    photo_url='https://logos-world.net/wp-content/uploads/2021/10/Python-Logo-700x394.png',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title="Pythonda Darslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=5000000,#50ming
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=1000000,#10 ming
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://m.media-amazon.com/images/I/418ow0JdGSL.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 1000000),
        LabeledPrice(
            '3 ish kunida yetkazish', 1000000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 2000000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -1000000)
                                       ])