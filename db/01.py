# База данных SQLite хранится в виде одного файла в файловой системе. Библиотека sqlite3 управляет доступом к файлу, включая его блокировку, чтобы предотвратить повреждение, когда его используют несколько авторов. База данных создается при первом обращении к файлу. Приложение отвечает за управление определениями таблиц или схем в базе данных. Сначала нам нужно импортировать модуль sqlite3 и создать связь с базой 
import sqlite3 as lite # Подключаем модуль sqlite3
# Получить номер версии используемого модуля sqlite можно с помощью атрибутов sqlite_version и sqlite_version_info. 
print(lite.version) # '2.6.0' - это версия pysqlite

# Атрибут sqlite_version возвращает номер версии в виде строки
print(lite.sqlite_version)

#  Атрибут sqlite_version_info возвращает номер версии в виде кортежа из 3 или 4 чисел.
print(lite.sqlite_version_info)


# Открываем базу данных
con = lite.connect("test.db")
# Работаем с базой данных
# Закрьmаем базу данных
con.close()
# Во избежание проблем с базой данных рекомендуется всегда закрывать объект соединения после завершения работы.

# Режим доступа rwc (чтение и запись - если база данных не существует, она будет создана) 
# Доступ к базе, хранящейся: в файле c:\book\testdb.db
# con = sqlite3.connect(r"file:///c:/book/testdb.db", uri = True)
con = lite.connect(r"file:////home/janus/work/py-g25/db/storages/testdb.db?mode=rwc", uri = True)

# Доступ только для чтения
# con = sqlite3.connect(r"file:///c:/book/testdb.db?mode = ro", uri =True)
# mоdе = ro - задает режим доступа к базе только чтение. 
con = lite.connect(r"file:////home/janus/work/py-g25/db/storages/testdb.db?mode=ro", uri = True)

# immutable = 1 - указывает, что база полностью недоступна для записи (например, запи­сана на компакт-диске, не поддерживающем запись). В результате отключается меха­низм транзакций и блокировок SQLite, что позволяет несколько повысить производи­тельность.
# Доступ к неизменяемой базе данных
con = lite.connect(r"file:////home/janus/work/py-g25/db/storages/testdb.db?immutable=1", uri = True)
