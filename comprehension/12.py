# Использование Set и Dictionary Comprehensions
# Хотя list comprehension в Python является распространенным инструментом, 
# вы также можете создавать множественные и словарные представления 
# (set and dictionary comprehensions). 
# set comprehension почти точно такое же, как представление списка. 
# Разница лишь в том, что заданные значения обеспечивают, 
# чтобы выходные данные не содержали дубликатов. 
# Вы можете создать set comprehension, используя фигурные скобки вместо скобок:

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
# {'a', 'e', 'u', 'i'}
# В примере set comprehension выводит все уникальные гласные, 
# которые он нашел в quote. 
# В отличие от списков, наборы не гарантируют, что элементы будут сохранены 
# в определенном порядке. Вот почему первым членом набора является a, 
# хотя первый гласный в quote — i.

# Dictionary comprehensions аналогично, с дополнительным требованием определения ключа:

squares = {i: i * i for i in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# Чтобы создать словарь квадратов, воспользуемся фигурными скобками ({}), 
# а также парой ключ-значение (i: i * i) в своем выражении.