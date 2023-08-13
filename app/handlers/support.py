from aiogram import types

from ..loader import dp


@dp.message_handler(text=["💡 Поддержка"])
async def call_support(message: types.Message):
    """
    Функция высылает ответ за команду и предлагает перейти в другой бот -
    сервиса для продвижения каналов.
    :return:
    """
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="💡 Поддержка",
                                          url="https://t.me/smoservice_bot"))
    await message.answer(text=f"Всегда рады Вам помочь! Заходите: ",
                         reply_markup=markup)
