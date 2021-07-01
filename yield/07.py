# Модуль itertools содержит специальные функции для работы с итерируемыми объектами. Желаете продублировать генератор? Соединить два генератора последовательно? Сгруппировать значения вложенных списков в одну строчку? Применить map или zip без создания ещё одного списка?
import itertools
# Просто добавьте import itertools.

# Давайте посмотрим на возможные порядки финиширования на скачках (4 лошади):

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
# <itertools.permutations object at 0xb754f1dc>
print(list(itertools.permutations(horses)))

# Как использовать объекты с бесконечной генерацией чисел?
# Функция islice принимает как минимум объект-генератор и значение, до которого нужно итерироваться. Возвращает конечный итератор.

from itertools import islice
def gener():
    i = 0
    while True:
        yield i
        i += 1

for i in islice(gener(), 5):
    print(i),

# 0 1 2 3 4
