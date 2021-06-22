# rename.test.py
import os

# Для переименования вызывается функция rename(source, target),
# первый параметр которой - путь к исходному файлу, а второй - новое имя файла.
# В качестве путей могут использоваться как абсолютные, так и относительные.
# Например, пусть в папке C://SomeDir/ располагается файл somefile.txt.
# Переименуем его в файл "hello.txt":

# Метод rename () принимает два аргумента: текущее имя файла и новое имя файла.
# os.rename(current_file_name, new_file_name)

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# Метод удаления ()
# Вы можете использовать метод remove () для удаления файлов, указав в качестве аргумента имя удаляемого файла.
# os.remove(file_name)

# Delete file test2.txt
os.remove("text2.txt")
