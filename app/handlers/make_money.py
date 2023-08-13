# import os
#
# from dotenv import load_dotenv
# from aiogram import types
# from sqlalchemy import (select,
#                         func)
#
# from ..main import (dp,
#                     bot)
# from ..databases.db import session
# from ..databases.tables import users
#
# load_dotenv()
#
#
# @dp.message_handler(commands=['make_money'])
# async def make_money(message: types.Message):
#     """
#     В данной функции можно просмотреть, сколько активных рефералов пригласил
#     пользователь на данный момент, а также здесь сформирована ссылка для
#     отправки пригласительной другим пользователям в данный бот.
#
#     :param message: сообщение, направленное пользователем боту.
#     :return:
#     """
#     # Ссылка для приглашения.
#     invite_link = f"https://t.me/{os.getenv('BOT_USERNAME')}?start=" \
#                   f"{message.chat.id}"
#
#     # Количество приглашенных пользователей конкретным пользователем.
#     # Сначала получаем id всех пользователей, потом проводим их подсчет.
#     referal_users = select(users.row_id).where(users.ref_user_id ==
#                                                message.from_user.id)
#     count_referal = select(func.count()).select_from(referal_users)
#     result = session.execute(count_referal)
#
#     # Выводим клавиатуру и шлём ответ в чат.
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(types.InlineKeyboardButton(text="Копировать ссылку на бот",
#                                           url=invite_link,
#                                           callback_data="alert"))
#     await message.answer(f"Приглашайте активных пользователей в бот и "
#                          f"получайте <b>{os.getenv('REF_PERCENT')}%</b> от "
#                          f"суммы пополнения рефералов!"
#                          f"Вы уже пригласили {result} пользователей.",
#                          reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "alert")
# async def show_notification(call: types.CallbackQuery):
#     """
#     Вызывает всплывающее уведомление после нажатия на кнопку пользователем.
#     :param call: информация о callback запросе, направленная пользователем.
#     :return:
#     """
#     await bot.answer_callback_query(call.id,
#                                     text='Ссылка скопирована',
#                                     show_alert=True)
#
# # TODO тут лучше пересмотреть на счет приглашения (там как то по другому
# #  вроде должно быть). Да и вообще, посмотри внимательно о том,
# #  как реализован данный функционал в гите по ссылке.
