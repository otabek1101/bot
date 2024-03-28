from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


Mobile_prog = Product(
    title="Mobil dasturlash",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Mobil Programming",
            amount=100000000, #1mln
        ),
        LabeledPrice(
            label="Chegirma",
            amount=10000000, #-100ming
        ),
    ],
    start_parameter="create_invoise_mobilprog_course",
    photo_url="https://iiht-kharghar.com/wp-content/uploads/android-app.jpg",
    photo_width=1280,
    photo_height=564,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)
Web_prog = Product(
    title="Web dasturlash",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Web Programming",
            amount=100000000, #1mln
        ),
        LabeledPrice(
            label="Chegirma",
            amount=10000000, #-100ming
        ),
    ],
    start_parameter="create_invoise_webprog_course",
    photo_url="https://iiht-kharghar.com/wp-content/uploads/android-app.jpg",
    photo_width=1280,
    photo_height=564,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)
Phone = Product(
    title="Iphone 13",
    description="Holati yangi",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Iphone 13",
            amount=1100000000, #11mln
        ),
        LabeledPrice(
            label="Yetkazib berish (5 kun)",
            amount=1000000, #10ming
        ),
    ],
    start_parameter="create_invoise_phone_phone",
    photo_url="https://bizoon.uz/wp-content/uploads/2021/11/iphone-13-starlight-select-2021.png",
    photo_width=1280,
    photo_height=564,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, #foydalanuvchi manzilini Kiritish shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 1000000,
        ),
        LabeledPrice(
            "3 ish kunida yetkazish", 1000000
        ),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fat',
    title="Express pochta (1 kun)",
    prices=[
        LabeledPrice(
            "1 ish kunida yetkazish", 3000000
        ),
    ]
)
PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title="Do`kondan olib ketish",
    prices=[
        LabeledPrice(
            "Yetkazib berishsiz", -1000000
        ),
    ]
)