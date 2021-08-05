import os
import sqlite3

db_filename = 'product.db'
schema_filename = 'schema.sql'

db_is_new = not os.path.exists(db_filename)

# Скрипт создает пустой файл, если файл не существует.
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Schema Created Successfully')
        print('Inserting initial data')
        
    else:
        print('Database exists, assume schema does, too.')
       
