# 15.listdir.test.py
# Вывести список файлов и подкаталогов для данного каталога: os.listdir(path)
# Следующий пример рекурсивно выводит список всех файлов и подкаталогов 
# для данного каталога:
import os

def walk(dir):
 for name in os.listdir(dir):
   path = os.path.join(dir, name)
   if os.path.isfile(path):
       print(path)
   else:
       walk(path)

path = os.getcwd()
walk(path)

# os.scandir() was introduced in Python 3.5 and is documented in PEP 471. os.scandir() returns an iterator as opposed to a list when called:

with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)

# Another way to get a directory listing is to use the pathlib module:

from pathlib import Path

entries = Path(path)
for entry in entries.iterdir():
    print(entry.name)

# List all files in a directory using scandir()

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# List all files in directory using pathlib
basepath = Path(path)
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)

# List all subdirectories using os.listdir

for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)

# List all subdirectories using scandir()

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
