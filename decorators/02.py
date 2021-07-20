# Декорирование функции

# Конструктивно декоратор в Python представляет собой некоторую функцию, аргументом которой является другая функция. Декоратор предназначен для добавления дополнительного функционала к данной функции без изменения содержимого последней.

# 1. Декораторы расположены перед объявлением функций и служат для того, чтобы добавить какой-то функционал не скрывая цель исходной функции.

# 2. Выглядит это примерно так:

# @custom_decorator
# def generic_example_function():
#     # ...
#     pass

# 3. При определении функции декоратора, она должна использоваться как ввод и выводить новую, измененную функцию.

# def custom_decorator(func):
#     # *args, **kwargs allow your decorated function to handle
#     # the inputs it is supposed to without problems

#     def modified_function(*args, **kwargs):
#         # Do some extra stuff
#         # ...
#         return func(*args, **kwargs) 
# # Call the input function as it
# # was originally called and return that

#     return modified_function

def foo(x):
    return x**2
    
def bar(x):
    return x - 2

# Обе функции завершатся ошибкой при вызове со строкой '2'. 
# Мы можем добавить функцию преобразования типа и декорировать этой функцией foo и bar.

# Trespassers will be prosecuted
# trespassers_w
def trespassers_w(f):
    # определяем функцию
    def new_f(x):
        return f(float(x))
    # возвращаем новую функцию
    return new_f

# функция-обёртка trespassers_w требует функцию в качестве аргумента и возвращает новую функцию.

foo_new = trespassers_w(foo)

# trespassers_w возвращает функцию:
print(foo_new)

print(foo_new('2')) # OUT: 4.0

print(trespassers_w(bar)('2')) # OUT: 0

# trespassers_w принимает функцию (A) в качестве аргумента и возвращает новую функцию (B). 
# Новая функция (B) при вызове вызывает функцию (A), но не с аргументом x, 
# а с float(x), и таким образом решает проблему TypeError.

# Синтаксис декоратора:

@trespassers_w
def foom(x):
    return x**2

@trespassers_w
def boom(x):
    return x - 2

print(foom('2'))
print(boom('2'))
