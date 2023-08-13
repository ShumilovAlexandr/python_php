import datetime

from aiogram import (executor,
                     types)
from dotenv import load_dotenv
from sqlalchemy import (insert,
                        select)

from app.databases.db import session
from app.databases.tables import Users
from app.loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """
    Стартовая страница бота.

    Тут в базу данных записываются данные о новом пользователе, если он
    ранее не обращался в бот.
    """
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(input_field_placeholder="Выбери в "
                                                                 "меню ниже экрана "
                                                                 "интересующий Вас раздел",
                                         one_time_keyboard=False)
    # Кнопки создаются отдельно, чтобы добавлять их в вывод построчно
    new = types.KeyboardButton(text="🔥 Создать новый заказ", callback_data="new")
    my_orders = types.KeyboardButton(text="💹 Мои заказы", callback_data="my_orders")
    my_balance = types.KeyboardButton(text="💼 Мой баланс", callback_data="my_balance")
    make_money= types.KeyboardButton(text="💰 Заработать", callback_data="make_money")
    support = types.KeyboardButton(text="💡 Поддержка", callback_data="support")
    faq = types.KeyboardButton(text="📢 FAQ", callback_data="faq")

    # Добавляю кнопки в вывод
    keyboard.add(new)
    keyboard.add(my_orders, my_balance)
    keyboard.add(make_money, support, faq)

    # Проверяем наличие данного пользователя в БД
    request_users = select(Users).where(Users.chat_id == chat_id)
    row = session.execute(request_users).fetchone()
    # и если пользователя такого нет, то заносим его в БД
    if not row:
        data = {
            "chat_id": chat_id,
            "first_name": first_name,
            "last_name": last_name,
            "username": message.from_user.username,
            "registration_date": datetime.datetime.now().date()
        }
        stmt = insert(Users).values(data)
        session.execute(stmt)
        session.commit()

    await message.answer(text="Выбери в меню ниже экрана интересующий "
                              "Вас раздел: ", reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
