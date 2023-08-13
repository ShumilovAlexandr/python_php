# import datetime
# import json
# import os
# import requests
#
# from aiogram import types
# from sqlalchemy import (select,
#                         update,
#                         delete)
# from dotenv import load_dotenv
# from datetime import timedelta
#
# from ..main import (dp,
#                     bot)
# from ..databases.db import session
# from ..databases.tables import (smoservices,
#                                 orders,
#                                 tempsess)
# from ..smoservice import SMO_URL
#
#
# load_dotenv()
#
#
# @dp.message_handler(commands=['my_orders'])
# async def make_order(message: types.Message):
#     """
#     В данной функции выводим список активных заказов пользователя.
#     Также, дополнительно, пользователь может сделать новый заказ.
#
#     :param message:
#     :return:
#     """
#     orders_list = select(orders).\
#         where(orders.chat_id == message.chat.id).\
#         order_by(orders.row_id)
#     result = session.execute(orders_list).fetchall()
#
#     answer = "Ваши заказы: "
#
#     for res in result:
#         if res[6] == 1:
#             answer += f"с id {res[7]} в количестве {res[3]} единиц на сумму " \
#                       f"{res[4]} RUB ЗАВЕРШЕН."
#         else:
#             params = {
#                 "user_id": os.getenv("USER_ID"),
#                 "api_key": os.getenv("API_KEY_SMOSERVICE"),
#                 "action": "check_order",
#                 "order_id": res[7]
#             }
#             # Отправляю запрос на API smooservice
#             response = requests.post(SMO_URL, params)
#             smo_data = json.loads(response.text)
#
#             order_status = "Завершен" if smo_data["data"]["status"] == \
#                            "completed" else smo_data["data"]["status"]
#             answer += f"{res[7]} в количестве {res[3]} единиц на сумму " \
#                       f"{res[4]} RUB {order_status}"
#
#             if smo_data["data"]["status"] == "completed":
#                 # Если у заказа статус Completed, обновляем информацию в БД
#                 update_query = (update(orders.status).
#                                 where(orders.row_id == res[0]).
#                                 values(orders.status == 1))
#                 session.add(update_query)
#                 session.commit()
#
#             elif smo_data["data"]["status"] == "Отменен":
#                 update_data = (update(balace.sum).
#                                where(balance.userid == res[1]).
#                                values(balance.rowid ==
#                                       balance.sum + res["4"]))
#                 session.add(update_data)
#                 session.commit()
#
#                 # Соответственно, если заказ Отменен, удаляем его из таблицы БД
#                 order_delete_query = delete(orders).where(
#                     orders.smo_order_id == res[7])
#                 session.execute(order_delete_query)
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton(text="Создать новый заказ",
#                                           callback_data="order"))
#     await message.answer(answer, reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "order")
# async def show_the_nomenclature(call: types.CallbackQuery):
#     # Создаем кнопки.
#     instagram = types.InlineKeyboardButton(text="Инстаграмм",
#                                            callback_data="1")
#     vkontakte = types.InlineKeyboardButton(text="ВКонтакте",
#                                            callback_data="2")
#     youtube = types.InlineKeyboardButton(text="Ютуб", callback_data="3")
#     telegram = types.InlineKeyboardButton(text="Телеграм",
#                                           callback_data="4")
#     odnoklas = types.InlineKeyboardButton(text="Одноклассники",
#                                           callback_data="5")
#     facebook = types.InlineKeyboardButton(text="Фейсбук", callback_data="6")
#     twitter = types.InlineKeyboardButton(text="Твиттер", callback_data="7")
#     world = types.InlineKeyboardButton(text="Мой мир", callback_data="8")
#     aksfm = types.InlineKeyboardButton(text="АКСфм", callback_data="9")
#     twich = types.InlineKeyboardButton(text="Твич", callback_data="10")
#     music = types.InlineKeyboardButton(text="Музыка",
#                                        callback_data="11")
#     application = types.InlineKeyboardButton(text="Приложения",
#                                              callback_data="12")
#     tiktok = types.InlineKeyboardButton(text="ТикТок", callback_data="13")
#
#     # Здесь мы кнопки передаем для вывода на экран в боте
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(instagram, vkontakte, youtube, telegram, odnoklas, facebook,
#                twitter, world, aksfm, twich, music, application, tiktok)
#     await bot.send_message(call.message.chat.id,
#                            "Выберите категорию, в которой Вы бы хотели "
#                            "заказать услугу:", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda m: m.data <= '13')
# async def show_menu(call: types.CallbackQuery):
#     match call.message.text:
#         case "1":
#             prefix = "inst-"
#         case "2":
#             prefix = "vk-"
#         case "3":
#             prefix = "yt-"
#         case "4":
#             prefix = "tg-"
#         case "5":
#             prefix = "ok-"
#         case "6":
#             prefix = "fb-"
#         case "7":
#             prefix = "tw-"
#         case "8":
#             prefix = "mm-"
#         case "9":
#             prefix = "dasoasd-"
#         case "10":
#             prefix = "twh-"
#         case "11":
#             prefix = "spotify-"
#         case "12":
#             prefix = "app-"
#         case "13":
#             prefix = "tt-"
#
#     markup = types.InlineKeyboardMarkup(row_width=1)
#
#     category_select = select(smoservices.name).\
#         where(smoservices.code.like(f"%btn_{prefix}%"))
#     result = session.execute(category_select).fetchall()
#
#     buttons = [types.InlineKeyboardButton(text="Назад",
#                                           callback_data="btn_14")]
#     for res in result:
#         buttons.append(types.InlineKeyboardButton(text=res,
#                                                   callback_data=f"{res}"))
#     markup.add(buttons)
#     await bot.send_message(call.message.chat.id,
#                            "Выбери сервис",
#                            reply_markup=markup)
#
#
# # TODO Доделать. Лучше все перекроить, ориентир - БОТ
# @dp.callback_query_handler(lambda c: c.data.startswith("btn_"))
# async def process_order(call: types.CallbackQuery):
#     await bot.send_message(call.message.chat.id, )
#
#
#
#
#
#
#
#     # TODO все что ниже в другом хендлере, который будет обрабатывать
#     #  введеное пользователем число
#     # temptime = (datetime.
#     #             datetime.
#     #             now() - timedelta(minutes=10)).time()
#     # row = select(tempsess).\
#     #     where(tempsess.chat_id == call.message.chat.id).\
#     #     where(tempsess.o_tipe == "order" and tempsess.time > temptime).\
#     #     order_by(desc(tempsess.rowid)).limit(1)
#     # stmt = session.execute(row).fetchall()
#     # if stmt.time < temptime:
#     #     await bot.send_message(call.message.chat.id, "У Вас нет активной "
#     #                                                  "услуги или время "
#     #                                                  "оформления заказа "
#     #                                                  "истекло. Создайте "
#     #                                                  "задачу заново")
#     #     return
#     # else:
#     #     service_price = select(smoservices).\
#     #         where(smoservices.id == row.serviceid)
#     #     result_service = session.execute(service_price).fetchall()
#
#
# # TODO не забыть обработать кнопку назад
