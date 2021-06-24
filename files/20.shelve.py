# 20.shelve.py
import os,hashlib
import shelve

# Хранение хэшей
# Для работы с бинарными файлами в Python может применяться модуль shelve. Он сохраняет объекты в файл с определенным ключом. Затем по этому ключу может извлечь ранее сохраненный объект из файла. Процесс работы с данными через shelve напоминает работу со словарями, которые также используют ключи для сохранения и извлечения объектов. Для открытия файла модуль shelve использует функцию open():
# shelve.open(путь_к_файлу[, flag="c"[, protocol=None[, writeback=False]]])
# Где параметр flag может принимать значения:
# c: файл открывается для чтения и записи (значение по умолчанию). Если файл не существует, то он создается.
# r: файл открывается только для чтения.
# w: файл открывается для записи.
# n: файл открывается для записи Если файл не существует, то он создается. Если он существует, то он перезаписывается
# shelve.open(FILENAME)

# Для закрытия подключения к файлу вызывается метод close():
# import shelve
# d = shelve.open(filename)
# d.close()
# Либо можно открывать файл с помощью оператора with. Сохраним и считаем в файл несколько объектов:

# for k, v in files.items():
#     with shelve.open(FILENAME) as repo:
#         repo[k] = v

def walk(dir):
    files={}
    for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
        hash = hashlib.md5()
        with open(os.path.join(dir,file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8'))
        md5 = hash.hexdigest()
        files[file]=md5
    return files

files = walk(os.getcwd())

print(files)

FILENAME = "repohash"

for k, v in files.items():
    print(k,v)

for k, v in files.items():
    with shelve.open(FILENAME) as repo:
        repo[k] = v

with shelve.open(FILENAME) as repo:
    for f in repo.keys():
        print(f)       
    print()
    for h in repo.values():
        print(h) 
