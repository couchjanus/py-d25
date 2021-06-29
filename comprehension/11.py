# Словарное включение
# Одно из применений генераторов заключается в создании словаря, 
# Это так распространенно, что для этого теперь есть новый синтаксис генератора словарей. 
# Оба этих примера меняют ключи и значения словаря.

teachers = {
    'Andy': 'English',
    'Joan': 'Maths',
    'Alice': 'Computer Science',
}
# используем  списковое включение
subjects = dict((subject, teacher) for teacher, subject in teachers.items())
print(subjects)
# используем словарное включение 
subjects = {subject: teacher for teacher, subject in teachers.items()}
print(subjects)

# Словарь включений аналогичен списковым включениям, 
# за исключением того, что он создаёт объект словаря вместо списка.

{x: x * x for x in (1, 2, 3, 4)}
# Out: {1: 1, 2: 4, 3: 9, 4: 16}

# это просто еще один способ написания:

dict((x, x * x) for x in (1, 2, 3, 4))
# Out: {1: 1, 2: 4, 3: 9, 4: 16} 

# Как и в случае со списком, мы можем использовать условный оператор 
# внутри словаря включения, чтобы получить только элементы словаря, 
# удовлетворяющие заданному критерию.

{name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6}  
# Out: {'Exchange': 8, 'Overflow': 8} 
# Или переписать с помощью генераторного выражения.

dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6)
# Out: {'Exchange': 8, 'Overflow': 8} 

# Начиная со словаря и используя словарь в качестве фильтра пары ключ-значение
initial_dict = {'x': 1, 'y': 2}
{key: value for key, value in initial_dict.items() if key == 'x'}
# Out: {'x': 1}
