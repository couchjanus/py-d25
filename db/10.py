# Используйте именованные параметры для более сложных запросов с большим количеством параметров или в тех случаях, когда некоторые параметры повторяются в запросе несколько раз. 
# Именованные параметры имеют префикс двоеточия (например, :param_name).

# Позиционные и именованные параметры не нужно заключать в кавычки или экранировать, поскольку они обрабатываются синтаксическим анализатором запросов.
# Параметры запроса могут использоваться с операторами выбора, вставки и обновления. Они могут появляться в любой части запроса.

# 10.py
import sqlite3
import sys

db_filename = 'todo/todo.db'
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """

    cursor.execute(query, {'project_name': project_name})

    for row in cursor.fetchall():
        print(row)
