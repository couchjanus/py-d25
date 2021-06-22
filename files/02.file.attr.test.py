# 02.file.attr.test.py

# При открытии файла создается файловый объект, 
# из которого можно получить следующую информацию о файле:

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

# Name of the file:  foo.txt
# Closed or not :  False
# Opening mode :  wb

# file.fileno ()
# Возвращает целочисленный файловый дескриптор, 
# который используется базовой реализацией для запроса операций ввода-вывода из операционной системы.
print ("целочисленный файловый дескриптор : ", fo.fileno())

# file.isatty ()
# Возвращает True, если файл подключен к tty (-подобному) устройству, иначе False.

if fo.isatty():
	print ("файл подключен к tty-подобному устройству")
else:
	print ("файл не подключен к tty-подобному устройству")

fo.close()