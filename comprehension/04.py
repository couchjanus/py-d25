# вы можете добавить один или несколько if условия для фильтрации значений.

# [<expression> for <element> in <iterable> if <condition>]
# Для каждого <element> в <iterable>  если <condition> имеет значение True, 
# добавить <expression> (обычно функция <element> ) в возвращаемом списке.
# Например, это можно использовать для извлечения только четных чисел 
# из последовательности целых чисел:

[x for x in range(10) if x % 2 == 0]
# Out: [0, 2, 4, 6, 8]

# Приведенный выше код эквивалентен:
even_numbers = [] 
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)
# Out: [0, 2, 4, 6, 8]

# Кроме того, усвоение условного списка вида [e for x in y if c], 
# где  e и c являются выражениями в терминах x  
# эквивалентно list(filter(lambda x: c, map(lambda x: e, y)))

# это совершенно отличается от ... if ... else ... условного выражения 
# (иногда известное как трехкомпонентное выражение), 
# которые вы можете использовать для <expression> часть списка понимания. 

[x if x % 2 == 0 else None for x in range(10)]
# Out: [0, None, 2, None, 4, None, 6, None, 8, None]

# Здесь условное выражение - не фильтр, а оператор, 
# определяющий значение, которое будет использоваться для элементов списка:
# <value-if-condition-is-true> if <condition> else <value-if-condition-is-false>

# Это становится более очевидным, если вы объедините его с другими операторами:

[2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]

# Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

# Приведенный выше код эквивалентен:

numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)
print(numbers)

# Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

