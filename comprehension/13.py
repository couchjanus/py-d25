# Переключение ключа и значения словаря (инвертировать словарь)

my_dict = {1: 'a', 2: 'b', 3: 'c'}
# если вы хотели поменять местами ключи и значения, 
# вы можете использовать несколько подходов в зависимости от вашего стиля кодирования:

swapped = {v: k for k, v in my_dict.items()}
swapped = dict((v, k) for k, v in my_dict.items())
swapped = dict(zip(my_dict.values(), my_dict))
swapped = dict(zip(my_dict.values(), my_dict.keys()))
swapped = dict(map(reversed, my_dict.items()))

print(swapped)

# Out: {a: 1, b: 2, c: 3}


