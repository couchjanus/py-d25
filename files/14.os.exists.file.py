# 14.os.exists.file.py
# Модуль os.path
# os.path является вложенным модулем в модуль os, 
# и реализует некоторые полезные функции для работы с путями.
import os

# Каждая программа имеет текущий каталог. 
# Функция os.getcwd возвращает текущий каталог:

cwd = os.getcwd()

print(cwd)

# os.path.exists(path) - возвращает True, 
# если path указывает на существующий путь 
# или дескриптор открытого файла.

# Если мы попытаемся открыть файл, который не существует, 
# то Python выбросит исключение FileNotFoundError. 
# Для отлова исключения мы можем использовать конструкцию try...except. 
# Однако можно уже до открытия файла проверить, 
# существует ли он или нет с помощью метода os.path.exists(path). 

# Проверить наличие файла в текущем каталоге:
# os.path.exists('my_file')

# В метод os.path.exists(path) передается путь, который необходимо проверить

filename = input("Введите путь к файлу: ")

if os.path.exists(filename):
   print("Указанный файл существует")
   print('Current working directory : ', os.getcwd())
   print('Current file name : ', __file__)
else:
   print("Файл не существует")
   print('Current working directory : ', os.getcwd())

# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
# os.path.dirname(path) - возвращает имя директории пути path.

print('File name :    ', os.path.basename(__file__))
print('Directory Name:     ', os.path.dirname(__file__))
print('Abspath :    ', os.path.abspath(__file__))

# os.path.getatime(path) - время последнего доступа к файлу, в секундах.
print('время последнего доступа к файлу : ', os.path.getatime(__file__))
# os.path.getmtime(path) - время последнего изменения файла, в секундах.
print('время последнего изменения файла : ', os.path.getmtime(__file__))
# os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
print('время последнего изменения файла : ', os.path.getctime(__file__))
# os.path.getsize(path) - размер файла в байтах.
print('размер файла в байтах : ', os.path.getsize(__file__))
# os.path.isabs(path) - является ли путь абсолютным.
print('является ли путь абсолютным : ', os.path.isabs(__file__))
# os.path.isfile(path) - является ли путь файлом.
print('является ли путь файлом : ', os.path.isfile(__file__))
# os.path.isdir(path) - является ли путь директорией.
print('является ли путь директорией : ', os.path.isdir(__file__))
# os.path.islink(path) - является ли путь символической ссылкой.

# os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
print('канонический путь : ', os.path.realpath(__file__))
print('Absolute path of file:     ', 
      os.path.abspath(__file__))
print('Absolute directoryname: ', 
      os.path.dirname(os.path.abspath(__file__)))
# os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
print('путь относительно директории start : ', os.path.relpath(__file__, start='/../..'))

# os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
print('кортеж (голова, хвост) : ', os.path.split(os.path.realpath(__file__)))
# os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).
# os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.

# os.path.ismount(path) - является ли путь точкой монтирования.
# os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
# os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).
# os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.

# os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.
# os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
# os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.
# os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
# os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
# os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.
