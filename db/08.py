# Метод fetchmany возвращает список строк данных.

# cursor.fetchmany([size=cursor.arraysize])

# С помощью параметра size можно указывать, какое количество строк возвращается. По умолчанию параметр size равен значению cursor.arraysize:

# print(cursor.arraysize)

# Значение, передаваемое в fetchmany() - это максимальное количество возвращаемых элементов. Если доступно меньше элементов, возвращаемая последовательность будет меньше максимального значения.
# 08.py
import sqlite3

db_filename = 'todo/todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    
    print(cursor.arraysize)

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pycat' order by deadline
    """)

    print('\nNext 5 tasks:')
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))
