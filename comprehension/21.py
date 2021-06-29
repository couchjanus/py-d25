# Лямбда-функции часто используются с функциями высшего порядка zip(), map(), filter(), reduce(), которые принимают одну или несколько функций в качестве аргументов или возвращают одну или несколько функций.
# Функция zip позволяет пройтись одновременно по нескольким итерируемым объектам:

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']

for i, j in zip(a, b):
   print(i, j)

# Выражение zip(a, b) создает объект-итератор, из которого на каждом шаге цикла извлекается кортеж, состоящий из двух элементов. Первый берется из списка a, второй - из b.
# 10 a
# 20 b
# 30 c
# 40 d
for i in zip(a, b):
   print(i, type(i))
# (10, 'a') <class 'tuple'>
# (20, 'b') <class 'tuple'>

# В списке b на один элемент больше. Функция zip возвращает итератор, который останавливается, когда исчерпывается самая короткая последовательность.  Если требуется учесть все значения из самой длинной, то следует использовать функцию zip_longest из модуля itertools:
import itertools

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
c = [1.1, 1.2]
for i in itertools.zip_longest(a,b,c):
   print(i)
# (40, 'd', None)

# Если элемента не хватает, то по-умолчанию подставляется объект None. Можно указать свой вариант заполнения:
for i in itertools.zip_longest(a,b,c, fillvalue=0):
   print(i)

# (10, 'a', 1.1)
# (20, 'b', 1.2)
# (30, 'c', 0)
# (40, 'd', 0)
# (0, 'e', 0)

# Если требуется получить не итератор, возвращаемый zip(), а список из элементов, то к объекту zip применима функция list, которая преобразует итератор в список:
a = [10, 20, 30, 40]
c = [1.1, 1.2, 1.3, 1.4]
ac = zip(a, c)
print(type(ac))
# <class 'zip'>
ac = list(ac)
print(type(ac)) # <class 'list'>
print(ac) # [(10, 1.1), (20, 1.2), (30, 1.3), (40, 1.4)]

# Функцию zip применяют для выполнения совместных или одновременных действий над элементами разных списков.
values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]

for i, j in zip(values, coefficient):
   print(i*j)
# 4.0200000000000005
# 6.5
# 5.98
a = []
b = []

for i, j in zip(range(10,20), range(1,10)):
   a.append(i)
   b.append(j)

print(a) # [10, 11, 12, 13, 14, 15, 16, 17, 18]
print(b) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Конвертирование 2-х списков в словарь

column_names = ['id', 'color', 'style']
column_values = [1, 'red', 'bold']

# name_to_value_dict = {'id': 1, 'color': 'red', 'style': 'bold'}


# Конвертирование 2-х списков в словарь с помощью цикла
name_value_tuples = zip(column_names, column_values)
name_to_value_dict = {}
for key, value in name_value_tuples:
   if key in name_to_value_dict:
       pass # Insert logic for handling duplicate keys
   else:
       name_to_value_dict[key] = value

print(name_to_value_dict)

# Конвертирование 2-х списков в словарь  с помощью генераторов словарей:

name_to_value_dict = {key:value for key, value in zip(column_names, column_values)}
print(name_to_value_dict)

# словарь можно создать и без генератора — dict(zip(list1, list2)).
name_to_value_dict = dict(zip(column_names, column_values))
print(name_to_value_dict)

