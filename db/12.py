# Команда DELETE удаляет строки из таблицы или представления таблицы базы данных.
# DELETE FROM table WHERE id = 2;
# Параметры команды DELETE
# table — имя таблицы, из которой удаляются строки; если определяется представление, сервер удаляет строки из основной таблицы представления
# WHERE — удаляет только строки, которые удовлетворяют условию; условие может ссылаться на таблицу и содержать подзапрос.

# 12.py
import sqlite3
import sys

db_filename = 'todo/todo.db'

id = int(sys.argv[1])

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "DELETE FROM task WHERE id = :id"
    cursor.execute(query, {'id': id})
