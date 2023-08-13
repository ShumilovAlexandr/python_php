# import json
# import os
# import aiohttp
# import asyncio
#
# from dotenv import load_dotenv
# from sqlalchemy import insert
#
# from databases.tables import smoservices
# from databases.db_query import clear_records
#
#
# load_dotenv()
#
# # Словарь для отправки запроса для получения списка услуг
# params = {
#     "user_id": os.getenv("USER_ID"),
#     "api_key": os.getenv("API_KEY_SMOSERVICE"),
#     "action": "services"
# }
#
# # URL для отправки запроса
# SMO_URL = "https://smoservice.media/api/"
#
#
# # Отправляем запрос на получение данных с сервиса раскрутки
# async def get_services():
#     async with aiohttp.ClientSession() as session:
#         response = await session.post(SMO_URL,
#                                       data=params)
#         return await response.json()
#
#
# # Тут проводится запись данных в таблицу БД,
# # предварительно очистив ее
# async def save_data_smoservice():
#     data_info = await get_services()
#     if data_info is not None:
#         clear_records(smoservices)
#         for data in data_info["data"]:
#             stmt = insert(smoservices)\
#                 .values(data)
#             session.execute(stmt)
#             session.commit()
# asyncio.run(save_data_smoservice())
