# 24.cli.monit.py
import sys
import os, hashlib
import time

files={}

monitor=[]

d = {}

if len (sys.argv) == 1:
    print ("Привет, {}!".format (sys.argv[0]))
else:
    if len (sys.argv) < 3:
        print ("Ошибка. Слишком мало параметров.")
        sys.exit (1)

    if len (sys.argv) > 3:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    param_name = sys.argv[1]
    param_value = sys.argv[2]

    if (param_name == "--name" or param_name == "-n"):
        print ("Просматриваем каталог, {}!".format (param_value) )
    else:
        print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
        sys.exit (1)

for dirname, dirnames, filenames in os.walk(os.getcwd() + '/' + param_value):
    for subdirname in dirnames:
        d = {
        'path': os.path.join(dirname, subdirname),
        'recursive':True
        }
        monitor.append(d)

print(monitor)
