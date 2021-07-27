# В некоторых случаях в SQL-зanpoc необходимо подставлять данные, полученные от пользователя. Если данные не обработать и подставить в SQL зanpoc, то пользователь получает возможность видоизменить запрос и, например, зайти в закрытый раздел без ввода пароля. Чтобы значения были правильно подставлены, нужно их передавать в ви­де кортежа или словаря во втором параметре метода execute. В этом случае в SQL­ запросе указываются следующие специальные заполнители:
# ? - при указании значения в виде кортежа;
# <key> - при указании значения в виде словаря.
# Когда мы используем параметризованные запросы, мы используем местозаполнители вместо прямого написания значений в SQL запросе. Запросы с указанием параметров отдельно увеличивают безопасность и производительность.
# 09.py
import sqlite3
import sys

db_filename = 'todo/todo.db'
# print(sys.argv)
# python 09.py pycat

print(len(sys.argv))

project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = ?
    """

    cursor.execute(query, (project_name,))

    for row in cursor.fetchall():
        print(row)
