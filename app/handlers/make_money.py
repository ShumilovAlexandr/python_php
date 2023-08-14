import os

from dotenv import load_dotenv
from aiogram import types
from sqlalchemy import (select,
                        func,
                        update)

from ..loader import (dp,
                      bot)
from ..databases.db import session
from ..databases.tables import Users

load_dotenv()


@dp.message_handler(text=["💰 Заработать"])
async def make_money(message: types.Message):
    """
    В данной функции можно просмотреть, сколько активных рефералов пригласил
    пользователь на данный момент, а также здесь сформирована ссылка для
    отправки пригласительной другим пользователям в данный бот.

    :param message: сообщение, направленное пользователем боту.
    :return:
    """
    # Ссылка для приглашения.
    invite_link = f"https://t.me/smoapp_bot?start=" \
                  f"{message.chat.id}"

    # Количество приглашенных пользователей конкретным пользователем.
    referal_users = select(Users.id).where(Users.ref_user_id ==
                                               message.from_user.id)
    count_referal = select(func.count()).select_from(referal_users)
    result = session.scalar(count_referal)

    await message.answer(f"Приглашайте активных пользователей в бот и "
                         f"получайте {os.getenv('REF_PERCENT')}% от "
                         f"суммы пополнения рефералов.\n" \
                         f"\n"\
                         f"Вы пригласили: {result} человек\n" \
                         f"\n"\
                         "Ваш заработок: {income} ₽.\n" \
                         f"\n"\
                         f"Используйте эту ссылку для приглашения "
                         f"пользователей: {invite_link}")


# @dp.message_handler(lambda msg: message.text.startswith("/start"))
# async def start_with_referal(message: types.Message):
#     ref = message.text[7:].strip()
#     if ref != message.chat.id:
#         request_ref = select(Users.ref_user_id).\
#             where(Users.chat_id == message.chat.id)
#         ref_result = session.execute(request_ref).fetchall()
#         if not ref_result:
#             ref_upd = (update(Users).
#                        where(Users.chat_id == message.chat.id).
#                        values(ref_user_id = ref))
#             session.add(ref_upd)
#             session.commit()
#     await message.answer(f"{message.from_user.first_name} "
#                          f"{message.from_user.last_name} зарегистрировался "
#                          f"по вашей партнерской ссылке." )

