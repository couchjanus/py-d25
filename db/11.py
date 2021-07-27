# Для обновления записи в базе данных используется команда SQL UPDATE.
# Чтобы обновить таблицу task, изменив поле status, можно использовать команду SET
# update task set status = :status where id = :id

# 11.py
import sqlite3
import sys

db_filename = 'todo/todo.db'

id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})
