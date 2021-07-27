# 05.py
# Команда INSERT осуществляет вставку в таблицу новой строки. В простейшем случае она имеет следующий вид:

# INSERT INTO <имя таблицы> VALUES(<значение>, <значение>, … );

# При такой записи указанные в скобках после ключевого слова VALUES значения вводятся в поля таблицы в том порядке, в котором соответствующие столбцы указаны при создании таблицы, то есть в операторе CREATE TABLE.

import os
import sqlite3

db_filename = 'todo/todo.db'
schema_filename = 'todo/todo_schema.sql'

# Выполняем поиск файла базы данных перед его открытием с помощью connect()
db_is_new = not os.path.exists(db_filename)

# Скрипт создает пустой файл, если файл не существует.
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Schema Created Successfully')
        
    else:
        print('Database exists, assume schema does, too.')
        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pycat', 'Python Cat of the Week',
                '2021-07-27');

        insert into task (details, status, deadline, project)
        values ('write about select cat', 'done', '2021-07-28',
                'pycat');

        insert into task (details, status, deadline, project)
        values ('write about random cat', 'waiting', '2021-07-29',
                'pycat');

        insert into task (details, status, deadline, project)
        values ('write about black cat', 'active', '2021-07-30',
                'pycat');
        """)
