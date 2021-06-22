# 07.read.from.file.py

# Метод read () читает строку из открытого файла. 
# Важно отметить, что строки Python могут иметь двоичные данные. 

# Синтаксис
# fileObject.read([count])
# Здесь переданный параметр - это количество байтов, 
# которые нужно прочитать из открытого файла. 
# Этот метод начинает чтение с начала файла и, если счетчик отсутствует, 
# он пытается прочитать как можно больше, возможно, до конца файла.

# Для чтения файл открывается с режимом r (Read), 
# и затем мы можем считать его содержимое различными методами:

# readline(): считывает одну строку из файла
# read(): считывает все содержимое файла в одну строку
# readlines(): считывает все строки файла в список

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("Read String is : ", str)
# Close opend file
fo.close()

# Если файл небольшой, то его можно разом считать с помощью метода read():

with open("hello.txt", "r") as file:
   content = file.read()
   print(content)

# При чтении файла мы можем столкнуться с тем, 
# что его кодировка не совпадает с ASCII. 
# В этом случае мы явным образом можем указать кодировку с помощью параметра encoding:

filename = "hello.txt"
with open(filename, encoding="utf8") as file:
   text = file.read()

# file.next ()
# Возвращает следующую строку из файла каждый раз, когда он вызывается.

# Open a file
fo = open("hello.txt", "r")
print ("Name of the file: ", fo.name)

for index in range(2):
   line = next(fo)
   print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()
