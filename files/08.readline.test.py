# readline.test.py

# Поскольку строки разделяются символом перевода строки "\n", 
# то чтобы исключить излишнего переноса на другую строку 
# в функцию print передается значение end="".

# вызовем метод readline() для чтения отдельных строк:
with open("hello.txt", "r") as file:
   str1 = file.readline()
   print(str1, end="")
   str2 = file.readline()
   print(str2)

# Итерация по файлу является базовой операцией и имеет множество вариантов. 
# Использование функции read() для байтового чтения:
filename = "hello.txt"
f = open(filename)
while True:
 char = f.read(1)
 if not char: break
 print(char)
f.close()

# Построчное чтение текстовых файлов и функция readline():
f = open(filename)
while True:
 line = f.readline()
 if not line: break
 print(line)
f.close()

# Файл сам может выступать в роли итератора:

# for line in open(filename):
#    readline(line)

with open("hello.txt", "r") as file:
   for line in file:
       print(line)

# Несмотря на то, что мы явно не применяем метод readline() для чтения 
# каждой строки, при переборе файла этот метод автоматически вызывается 
# для получения каждой новой строки. 
# Поэтому в цикле вручную нет смысла вызывать метод readline. 

# Метод readline можно использовать для построчного считывания файла 
# в цикле while:
with open("hello.txt", "r") as file:
   line = file.readline()
   while line:
       print(line, end="")
       line = file.readline()

# file.readlines ([sizehint])
# Читает до EOF, используя readline () и возвращает список, 
# содержащий строки. 
# Если присутствует необязательный аргумент sizehint, 
# вместо чтения до EOF читаются целые строки, 
# составляющие приблизительно байты sizehint 
# (возможно, после округления до внутреннего размера буфера).

# метод readlines() для считывания всего файла в список строк:
with open("hello.txt", "r") as file:
   contents = file.readlines()
   str1 = contents[0]
   str2 = contents[1]
   print(str1, end="")
   print(str2)
