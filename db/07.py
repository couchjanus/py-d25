# Для получения первого результата можно использовать функцию fetchone(). 
# Извлекаем только одну запись, вызываем метод fetchone().

#    data = cursor.fetchone()

# Метод fetchone() возвращает следующую строку из таблицы. 
# После обработки всех строк метод начинает возвращать None.
# За счет этого метод можно использовать в цикле

import sqlite3

db_filename = 'todo/todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select name, description, deadline from project
    where name = 'pycat'
    """)
    name, description, deadline = cursor.fetchone()

    print('Project details for {} ({})\n  due {}'.format(
        description, name, deadline))
