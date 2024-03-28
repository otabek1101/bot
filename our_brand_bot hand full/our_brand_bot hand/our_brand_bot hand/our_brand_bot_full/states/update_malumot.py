from aiogram.dispatcher.filters.state import StatesGroup, State

# Update ful name, age
class Update_malumot(StatesGroup):
    full_name = State()
    age = State()

class Update_tel(StatesGroup):
    tel = State()


class Update_card(StatesGroup):
    card = State()


class Update_insta(StatesGroup):
    insta = State()


class Update_tele(StatesGroup):
    tele = State()


class Update_you(StatesGroup):
    you = State()


class Update_full_name(StatesGroup):
    full_name = State()


class Update_age(StatesGroup):
    age = State()  
