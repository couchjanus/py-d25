# 01.py

# Способы формирования списков
# В языке Python имеется 3 способа создавать (генерировать) списки:
# при помощи циклов;
# при помощи функции map();
# при помощи list comprehension.

# Использование цикла For. Последовательность действий такова:
# Создаем пустой список.
# Обходим список, в котором требуется произвести ряд преобразований, или осуществляем требуемое количество итераций цикла при помощи функции range().
# Добавляем в пустой список новые значения / элементы с помощью метода append().

# Генерация списка кубов для чисел от 0 до 9 с использованием функции range()
s = []  # Создаем пустой список
for i in range(10):  # Осуществляем 10 итераций - от 0 до 9
    s.append(i ** 3)  # Добавляем к списку куб каждого числа
print(s)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Списковое включение создает новый list, применяя выражение к каждому элементу итерируемого. 
# Наиболее простой формой является:
# [ <expression> for <element> in <iterable> ]
# Также есть необязательное условие if:
# [ <expression> for <element> in <iterable> if <condition> ]

# Каждый <element> в <iterable> подключается к <expression> 
# если (необязательно) <условие> имеет значение true . 
# Все результаты сразу возвращаются в новый список. 
# Генератор включений вычисляет медленно, 
# а списковые включения оценивают весь итератор — занимая память, пропорционально длине итератора.

# Вместо того, чтобы создавать пустой список и добавлять каждый элемент в конец, 
# мы просто определяем список и его содержимое одновременно, следуя этому формату:
# new_list = [expression for member in iterable]

[x + 1 for x in (1, 2, 3)] # Результат:  [2, 3, 4]

# списковые включения примерно эквивалентны следующему циклу for:
squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x) # Out:[1, 4, 9, 16]
print(squares)

# List comprehensions — это способ составления списков. 
# мы можем переписать цикл for из первого примера всего в одну строку кода:

squares = [i * i for i in range(10)]
print(squares) 
# Результат: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Выражение for  устанавливает i для каждого значения по очереди из (1, 2, 3, 4). 
# Результат выражения i * i добавляется во внутренний список. 
# Внутренний список присваивается переменным квадратам после завершения.