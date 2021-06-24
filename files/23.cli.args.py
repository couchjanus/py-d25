# 22.shelve.monit.py
import sys

# print(sys.argv)
# print(sys.argv[1:])

# argv = sys.argv
# print(len(argv))
# arg = argv.pop()
# print(arg)
# print(len(argv))

if len (sys.argv) > 0:
    print ("Привет, {}!".format (sys.argv[0]))

for param in sys.argv:
    print(param)

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
        print ("Привет, {}!".format (param_value) )
    else:
        print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
        sys.exit (1)
