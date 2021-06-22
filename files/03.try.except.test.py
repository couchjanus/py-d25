# 03.try.except.test.py
# При открытии файла или в процессе работы с ним 
# мы можем столкнуться с различными исключениями, 
# например, к нему нет доступа и т.д. 
# В этом случае программа выбрасывает исключение, 
# а ее выполнение не дойдет до вызова метода close, 
# и соответственно файл не будет закрыт.

# В этом случае мы можем обрабатывать исключения:
# try:

# except Exception as ex:

try:
   somefile = open("hello.txt", "w")
   try:
       somefile.write("hello world")
   except Exception as e:
       print(e)
   finally:
       somefile.close()
except Exception as ex:
   print(ex)
