# 06.py
# С помощью запроса SQL SELECT можно выполнять выборку данных из таблицы.
# С помощью данного SQL SELECT запроса выбираются все значения из таблицы task, поле project  которых строго равно 'pycat'.
# select id, priority, details, status, deadline from task
#    where project = 'pycat'
import sqlite3

db_filename = 'todo/todo.db'

# Чтобы извлечь значения из таблицы, создайте курсор на основе соединения с базой данных. Курсор создает согласованное представление данных и является основным средством взаимодействия с системой транзакций баз данных.

# with sqlite3.connect(db_filename) as conn:
#    cursor = conn.cursor()
# Метод execute() выполняет SQL-запросы. Метод cursor.execute принимает запрос SQL в качестве параметра и возвращает resultSet - строки базы данных.

# cursor.execute("""
#    select id, priority, details, status, deadline from task  where project = 'pycat'
#    """)

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priority, details, status, deadline from task
    where project = 'pycat'
    """)

    # Запросы это двухэтапный процесс. Сначала выполняется запрос с помощью метода курсора execute() для отбора данных. Затем используется fetchall(), чтобы получить результаты. Метод fetchall() получает все записи.
    # Технически, это последовательность кортежей. Каждый из внутренних кортежей представляет строку в таблице.

    #    for row in cursor.fetchall():
    #        task_id, priority, details, status, deadline = row
    #        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
    #            task_id, priority, details, status, deadline))

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
            task_id, priority, details, status, deadline))
