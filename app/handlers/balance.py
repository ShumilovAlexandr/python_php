# import datetime
# import hashlib
# import json
# import os
#
# import requests
#
# from aiogram import types
# from sqlalchemy import (select,
#                         insert,
#                         update,
#                         desc)
# from dotenv import load_dotenv
# from urllib.parse import urlencode
# from aiogram.dispatcher import FSMContext
# from datetime import timedelta
#
# from ..main import (dp,
#                     bot)
# from ..databases.tables import (balance,
#                                 tempsess)
# from ..databases.db import session
# from ..smoservice import SMO_URL
# from ..utils.state import SumFSM
#
# load_dotenv()
#
#
# async def check_balance(user_id):
#     """Получаем с SMOService баланс пользователя."""
#     # TODO возможно, вот эту эпопею надо получать с БД. Но как данные о
#     #  балансе попадают в БД?
#     param = {
#         "user_id": user_id,
#         "api_key": os.getenv("API_KEY_SMOSERVICE"),
#         "action": "balance"
#     }
#     response = requests.post(SMO_URL, param)
#     result = json.loads(response.text)
#
#     return result["data"]["balance"]
#
#
# @dp.message_handler(commands=['balance'])
# async def show_balance(message: types.Message):
#     """
#     Функция выводит баланс пользователя и предлагает пополнить текущий баланс.
#     :return:
#     """
#     # Получаем сумму из API smooservice и пересохраняем данные в БД.
#     # TODO 2 вот про это я имел ввиду в примечании выше. Может, именно тут
#     #  надо получать данные из БД.
#     result = await check_balance(os.getenv("USER_ID"))
#     save_balance_in_db = (update(balance).
#                           where(balance.row_id == message.from_user.id).
#                           values(balance.sum == result))
#     session.add(save_balance_in_db)
#     session.commit()
#
#     # Делаем запись в таблицу, чтобы сохранить историю запроса пользователем
#     # информации о балансе.
#     request_date = datetime.\
#         datetime.\
#         now().time().\
#         replace(second=0, microsecond=0)
#     data = {
#         "chat_id": message.chat.id,
#         "o_tipe": "balance",
#         "time": request_date
#     }
#     save_data = insert(tempsess).values(data)
#     session.add(save_data)
#     session.commit()
#
#     # Сформировывает инлайн кнопку на ссылку для пополнение баланса
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(types.InlineKeyboardButton(text="Пополнить баланс",
#                                           callback_data="balance"))
#     await message.answer(text=f"Ваш баланс равен {result} руб.",
#                          reply_markup=markup)
#
#
# async def generate_link(summa, chat_id):
#     """Создание ссылки на оплату."""
#     secrets = os.getenv("ROSKASSA_SECRETKEY")
#     data = {
#         "shop_id": os.getenv("ROSKASSA_PUBLICKEY"),
#         "amount": summa,
#         "currency": "RUB",
#         "order_id": chat_id
#     }
#     sorted_data = dict(sorted(data.items()))
#     encoded_data = urlencode(sorted_data)
#     sign = hashlib.md5((encoded_data + secrets).encode()).hexdigest()
#     return sign
#
#
# @dp.callback_query_handler(lambda c: c.data == "balance")
# async def top_up_balance(callback: types.CallbackQuery, state: FSMContext):
#     """
#     Обрабатываем нажатие пользователем кнопки Пополнить баланс. В данном
#     случае, здесь ожидается введение пользователем суммы.
#     """
#     await callback.message.answer("Вы можете пополнить баланс, указав сумму "
#                                   "пополнения в рублях: ")
#     await state.set_state(SumFSM.summa)
#
#
# @dp.message_handler(state=SumFSM.summa)
# async def perfom_balance_oper(message: types.Message, state: FSMContext):
#     """
#     Тут уже происходит непосредственно обработка введенной суммы и
#     формирование ссылки на пополнение баланса.
#     """
#     # Проверяем, если ли в БД на очереди операции на пополнение
#     # баланса
#     operation_balance = select(tempsess).\
#         where(tempsess.chat_id == message.chat.id).\
#         where(tempsess.o_tipe == 'balance').\
#         order_by(desc(tempsess.rowid)).\
#         limit(1)
#     result_balance = session.execute(operation_balance)
#     # Если же в БД также нет на очереди операций на пополнение баланса.
#     if result_balance is None:
#         # Шлем в чат соответствующее сообщение
#         await message.answer(text="Произошла ошибка. Начните пополнение "
#                                   "баланса заново.")
#     # Если же записи на пополнение баланса есть (не позже чем 10-ти
#     # минутные)
#     else:
#         pay_link = await generate_link(message.text, message.chat.id)
#         markup = types.InlineKeyboardMarkup(row_width=1)
#         markup.add(types.InlineKeyboardButton(text=f"Пополнить на "
#                                                    f"{message.text} "
#                                                    f"руб.", url=pay_link))
#         await state.finish()
#         await message.answer("Перейдите по ссылке для пополнения",
#                              reply_markup=markup)
#
