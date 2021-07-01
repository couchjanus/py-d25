# Функция iter возвращает объект итератора.
# iter(obj[, sentinel])
# -> iterator

# obj : Объект коллекции, поддерживающей итерирование (реализует __iter__()), либо объект, поддерживающий протокол последовательности (реализует __getitem__(), где аргумент целое, начиная с нуля). Если передан другой объект, возбуждается TypeError
# sentinel : Если этот аргумент предоставлен, то ожидается, что obj содержит объект, поддерживающий вызов. В этом случае, созданный итератор будет вызывать указанный объект (без аргументов) с каждым обращением к своему __next__() и проверять полученное значение на равенство с sentinel. Если полученное значение равно sentinel, возбуждается StopIteration
# , иначе возвращается полученное значение.
# Функция возвращает итератор по объекту, поддерживающему итерирование по его элементам.

# working of iter() 
# initializing list  
lis1 = [1, 2, 3, 4, 5, 6] 

# printing type  
print ("The list is of type : " + str(type(lis1))) 

# converting list using iter() 
lis1 = iter(lis1) 

# printing type  
print ("The iterator is of type : " + str(type(lis1))) 
  
# using next() to print iterator values 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 
print (next(lis1)) 
# Output:
# The list is of type : 
# The iterator is of type : 
# 1
# 2
# 3
# 4
# 5

# property of iter() 
# converting list using iter() 
lis1 = [1, 2, 3, 4, 5, 6] 
lis1 = iter(lis1) 

# prints this  
print ("Values at 1st iteration : ") 
for i in range(5): 
    print (next(lis1)) 
  
# doesn't print this 
# print ("Values at 2nd iteration : ") 
# for i in range(5): 
#     print (next(lis1)) 

# Output:

# Values at 1st iteration : 
# 1
# 2
# 3
# 4
# 5
# Values at 2nd iteration : 
# Exception :

# Traceback (most recent call last):
#   File "/home/0d0e86c6115170d7cd9083bcef1f22ef.py", line 18, in 
#     print (next(lis1))
# StopIteration

# Функция next() вызывает метод __next__. Ей можно передать второй аргумент который она будет возвращать по окончанию итерации вместо ошибки StopIteration.

# itr = iter(aggregate)

# while True:
#     item = next(itr, None)
#     if item is None:
#         break
#     print(item)

# iter() можно вызывать с двумя аргументами, что позволит создать из вызываемого объекта(функция или класс с реализованным методом __call__) итератор. Первый аргумент должен быть вызываемым объектом, а второй — неким ограничителем. Вызываемый объект вызывается на каждой итерации и итерирование завершается, когда возбуждается исключение StopIteration или возвращается значения ограничителя.

# Например, из функции которая произвольно возвращает 11-77, можно сделать итератор, который будет возвращать значения пока не «выпадет» 66:

from random import randint

def d6():
    return randint(11, 77)

for roll in iter(d6, 66):
    print(roll)

# В зависимости от наличия sentinel, в obj ожидаются различные типы объектов.

# Одно из применений sentinel — чтение строк, пока не будет достигнута нужная. Следующий пример считывает файл, пока метод readline() не вернёт пустую строку:

# with open('mydata.txt') as fp:
#     for line in iter(fp.readline, ''):
#         # Делаем что-либо с line.
#         pass
