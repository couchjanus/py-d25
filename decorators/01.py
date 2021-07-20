# Функции — это объекты первого уровня
# Функцию можно динамически создавать, передавать в функцию и изменять. 

def moo(string):
    lowercase = string.lower()
    return lowercase

moo.yloo = 'You Live Only Once'
print(moo.yloo)

# можно присвоить переменной функцию, так же как обычные значения этой переменной.

foo = moo

print(foo("Hello world")) # hello world

# Функции в роли параметров и возвращаемые значения

# Функцию можно передавать в качестве аргумента другим функциям. 
# Например, есть список целых чисел, на базе него получить другой список, 
# элементами которого будут квадраты первого, 

# исходный список
a = [1, 2, 3, 4, 5]
# функция, возводящая переданное ей число в квадрат
sq = lambda x: x**2
# проверим ее работу
# print(sq(5))
# получаем список квадратов
b = list(map(sq, a))
print(b)

# такую задачу можно решить в одну строчку:
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

lo = lambda x: x.lower()
print(lo("Hello Lambda"))

# Функция как объект
# В Python функция – это специальный объект, который имеет метод __call__(). 

# создадим класс.

class LowerCall():
    def __call__(self, string):
        return string.lower()

# объект такого класса можно вызывать как функцию.

hello = LowerCall()
print(hello("HELLO LOWER CALL"))


# Определение функции внутри другой функции

# функция умножает два числа.

def mul(a):
    def helper(b):
        return a * b
    return helper

# внутри функции mul() создается еще одна функция, которая называется helper(); 
# функция mul() возвращает функцию helper как результат работы.

# Вызывается эта функция так:

mul(4)(2)

# на базе функции mul() можно создавать кастомизированные функции. 
# создадим функцию three_mul, которая умножает на три любое переданное ей число.

three_mul = mul(3)
three_mul(5)

# Внутри функций можно создавать другие функции, вызывать их и возвращать как результат через return.
# На этом построена идея замыкания (closures).

def call_this(f):
    f()
    print("Called it!")

def call_foo(f):
    f('Hell ')

def bar(hell = ""):
    print(hell + "Called bar!")

call_this(bar)
call_foo(bar)

# Определение функции decorator

# def lowercase(func):  
#     def wrapper():
#         f = func()
#         lowercase = f.lower()
#         return lowercase
#     return wrapper

def lowercase(f):  
    def wrapper():
        return f().lower()
    return wrapper

def test_lowercase():  
    return 'HELLO DECORATORS WORLD'

decorate = lowercase(test_lowercase)  
print(decorate())  
