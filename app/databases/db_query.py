from .db import get_connection


def clear_records(table):
    """
    Функция очищает данные из таблицы smoservices.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"TRUNCATE TABLE '{table}'")
    cur.close()
    return available_time

