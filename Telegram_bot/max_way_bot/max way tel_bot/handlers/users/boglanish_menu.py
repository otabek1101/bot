from aiogram import types
from keyboards.default.start_btn import start_btn
from loader import dp


@dp.message_handler(text = '📞Biz bilan bog`laning')
async def bot_help(message: types.Message):
    await message.answer('Biz bilan @MaxWaySupport_bot orqali bog`laning yoki\n+998712005400 raqamiga qo`ng`iroq qiling ', reply_markup=start_btn)
