# 04.with.except.test.py
# Можно также использовать менеджер контекста, 
# который в любом случае закроет файл:

# with open("my_file", mode) as somefile:
#    do_something(somefile)

# Эта конструкция определяет для открытого файла переменную somefile 
# и выполняет набор инструкций. 
# После их выполнения файл автоматически закрывается. 
# Даже если при выполнении инструкций в блоке with 
# возникнут какие-либо исключения, то файл все равно закрывается.

with open("hello.txt", "w") as somefile:
   somefile.write("hello world")