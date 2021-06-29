# Генерация списка заглавных букв из «comprehension»
# Так как строка является итерируемым объектом, то по ней можно пройтись в цикле.
word = 'comprehension'  # Начальное слово
s = []  # Создаем пустой список
for i in word.upper():  # Проходимся по каждой букве в слове
    s.append(i)  # Приводим все буквы к верхнему регистру
print(s)  

# Получить список заглавных символов из строки
[s.upper() for s in "Hello World"] # Out:['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Убрать все запятые с конца строки в списке
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']] # Out:['these', 'words', 'mostly', 'have,commas']

# Организовать буквы в словах в алфавитном порядке
sentence = "Beautiful is better than ugly"
["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()] # Out:['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy'] 

