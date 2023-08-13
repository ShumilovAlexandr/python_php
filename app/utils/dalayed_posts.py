# import datetime
#
# from sqlalchemy import (select,
#                         update)
# from aiogram import types
# from datetime import timedelta
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
#
# from ..databases.tables import delayed_posts
# from ..databases.db import session
# from ..main import (dp,
#                     bot)
#
# scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
#
#
# @dp.message_handler()
# async def send_message(message: types.Message):
#     # Получаем текущее время, для проведения выборки из таблицы
#     cur_time = datetime. \
#         datetime. \
#         now(). \
#         replace(second=0,
#                 microsecond=0)
#     # Выполняем выборку.
#     stmt = select(delayed_posts).\
#         where(delayed_posts.send_date_time <= cur_time)
#     result = session.execute(stmt)
#
#     while result.stop == 1:
#         # Обновляем данные в базе данных, заложив в
#         # delayed_posts.send_date_time время отправки
#         # такого сообщения в будущем.
#         save_time_to_db = cur_time + timedelta(hours=336)
#         save_delayed_post = (update(delayed_posts).
#                              where(delayed_posts.rowid == result.row_id).
#                              values(delayed_posts.
#                                     send_date_time == save_time_to_db))
#         session.add(save_delayed_post)
#         session.commit()
#         await message.answer(text="<b>Не дай боту заскучать</b>! "
#                                   "Верный спутник SMM-продвижения по "
#                                   "прежнему здесь. "
#                                   "Без обеда и выходных, он принимает заказы. "
#                                   "Подписчики, Лайки и просмотры! "
#                                   "1. Напишите команду /start; "
#                                   "2. Выберите услугу; "
#                                   "3. Укажите параметры. "
#                                   "<b>Раз, два, три - и ваш заказ на получение"
#                                   " лайков, просмотров и подписчиков "
#                                   "запущен</b>", parse_mode="Markdown")
#
#
# scheduler.add_job(await send_message, trigger="interval", hours=336)
