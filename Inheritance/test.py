# Указание имени суперкласса
# Если некоторый класс наследует другой суперкласс, то имя суперкласса задается в круглых скобках в заголовке инструкции class.

# Класс A - есть суперклассом для класса B
class A:
    # атрибуты класса A
    pass

# Класс B - есть подклассом класса A
class B(A):
    # атрибуты класса B
    pass

# Наследование атрибутов суперкласса подклассом

# Подкласс наследует атрибуты своих суперклассов.

# Класс A - есть суперклассом для классов B, C
class A:
    # Атрибут класса A: метод AAA()
    def AAA(self):
        print("class A. Method AAA()")

# Класс B - есть подклассом класса A
class B(A):
    # Атрибут класса B: Метод BBB()
    def BBB(self):
        # Из метода BBB() можно доступиться
        # к атрибуту AAA() класса A
        self.AAA() # будет вызвано A.AAA()
        print("class B. Method BBB()")

# Класс C - есть подклассом классов A, B
class C(B):
    # Атрибут класса C: метод CCC()
    def CCC(self):
        # Из метода CCC() можно доступиться
        # к атрибуту AAA() класса A
        # и к атрибуту BBB() класса B.
        self.AAA()
        self.BBB()
        print("class C. Method CCC()")

# Тестирование работы механизма наследования
# 1. Использование экземпляра класса A
objA = A()
objA.AAA() # вызов метода AAA() класса A

# Наследование атрибутов суперкласса экземпляром подкласса
# Экземпляры классов наследуют атрибуты всех доступных классов. Например. Из экземпляра objB можно доступиться к методам (атрибутам) A1(), A2(), A3() класса A.

# Класс A - есть суперклассом для класса B
class A:
    # Атрибуты класса A:
    def A1(self):
        print("A.A1()")

    def A2(self):
        print("A.A2()")

    def A3(self):
        print("A.A3()")

# Класс B - есть подклассом класса A
class B(A):
    # Атрибуты класса B:
    def B1(self):
        print("B.B1()")

# Доступ из экземпляра подкласса B
objB = B()

# Вызов методов суперкласса A
objB.A1()
objB.A2()
objB.A3()


# Обращение к атрибуту суперкласса из экземпляра класса
# Чтобы доступиться к атрибуту суперкласса из экземпляра класса, нужно выполнить обращение вроде
# obj.attribute
# здесь
# obj – имя экземпляра подкласса;
# attribute – имя атрибута суперкласса.
# Такое обращение включает в себя:

# ссылку на экземпляры и классы по инструкции class
# A.attribute
# ссылку на атрибуты аргумента экземпляра self в методах класса.
# self.attribute

# Изменения в подклассе не затрагивают суперкласс. Перегрузка атрибутов
# Если в подклассе вносятся изменения, то эти изменения не затрагивают суперкласс. Это касается также замены имен суперклассов в подклассах, расположенных на более низких уровнях в дереве классов. В этом случае изменяется только унаследованное поведение. Замена атрибутов суперкласса за счет их переопределения в подклассах называется перегрузкой.
 
#В нижеследующем коде демонстрируется замещение имени метода HelloWorld() класса A в подклассе B.

# Класс A есть суперклассом для класса B
class A:
    # Атрибут класса A - метод HelloWorld()
    def HelloWorld(self):
        print("Class A: Hello world!")

# Класс B есть подклассом класса A
class B(A):
    # В классе B есть атрибут с таким же именем
    # как в классе A
    def HelloWorld(self):
        print("Class B: Hello world!")

# Продемонстрироветь замещение имени
# 1. Объявить экземпляр класса B
objB = B()

# 2. Вызвать метод HelloWorld()
objB.HelloWorld() # Class B: Hello world! - метод класса B

# 3. Объявить экземпляр класса A
objA = A()

# 4. Вызвать метод HelloWorld()
objA.HelloWorld() # Class A: Hello world! - метод класса A

# Пример использования наследования. Расширение класса Point к классу ColorPoint
#Условие задачи. Задан класс Point, описывающий точку с координатами x, y на координатной плоскости. Используя механизм наследования нужно расширить возможности класса Point путем добавления нового атрибута цвета. Для этого реализовать подкласс PointColor.

#В классе Point реализовать следующие атрибуты:

#координаты точки;
# метод иницализации, который получает 2 параметра — координаты точки x, y;
# метод вычисления расстояния от точки до начала координат;
# метод getPoint(), который возвращает точку в виде списка.
# В подклассе PointColor реализовать следующие атрибуты:

# цвет точки color;
# метод начальной инициализации, который получает 3 параметра: координаты точки и цвет;
# метод доступа к цвету color с именем getColor().
# Решение. Текст программы, решающий задачу, следующий.

import math

# Класс, описывающий точку на координатной плоскости
class Point:
    # Метод начальной инициализации данных класса
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод вычисления расстояния от точки до начала координат
    def length(self):
        # теорема Пифагора
        len = math.sqrt(self.x*self.x+self.y*self.y)
        return len

    # Метод, возвращающий координаты точки в виде списка
    def getPoint(self):
        return [self.x, self.y]

# Класс, расширяющий класс Point
class PointColor(Point):
    # Метод начальной инициализации
    def __init__(self, x, y, color):
        # доступ к x, y суперкласса Point
        self.x = x
        self.y = y

        # ввести новую переменную color
        self.color = color

    # Вернуть цвет
    def getColor(self):
        return self.color;

# Использование класса Point
point1 = Point(3, 4)
print("point1.length = ", point1.length()) # length = 5.0
print("point11 = ", point1.getPoint())

# Использование класса PointColor
point2 = PointColor(5, 6, "Red")
print("point2.x = ", point2.getPoint()[0])
print("point2.y = ", point2.getPoint()[1])
print("point2.color = ", point2.getColor())

# Результат выполнения программы

# point1.length = 5.0
# point11 = [3, 4]
# point2.x = 5
# point2.y = 6
# point2.color = Red


# Чтобы классы реализовывали заданный набор методов в статически типизированных языках, таких как Java, используются интерфейсы и абстрактные классы.
# Абстрактные базовые классы существуют для наследования, но никогда сами не используются для создания объектов. Python предоставляет модуль abc для определения абстрактных базовых классов.

# Этот модуль определяет мета-класс и набор декораторов. Для определения абстрактного базового класса мы устанавливаем ABC как мета-класс абстрактного класса и помечаем декораторами @abstractmethod и @abstractproperty методы и свойства которые должны быть реализованы в неабстрактных потомках.

# Если потомки не реализуют абстрактные методы и свойства то не смогут создавать объекты:

from abc import ABC, abstractmethod
 
class Vehicle(object):
 
    __meta-class__ = ABCMeta
 
    @abstractmethod
 
    def change_gear(self):
        pass
 
    @abstractmethod
    def start_engine(self):
        pass
 
class Car(Vehicle):
 
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

# abstract methods not implemented
car = Car("Toyota", "Avensis", "silver")
 
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class Car with abstract methods change_gear, start_engine

# Как только класс реализовал все абстрактные методы появляется возможность создавать объекты:


# from abc import ABCMeta, abstractmethod
 
# class Vehicle(object):
 
#     __meta-class__ = ABCMeta
 
#     @abstractmethod
#     def change_gear(self):
#         pass
 
#     @abstractmethod
#     def start_engine(self):
#         pass
 
# class Car(Vehicle):
 
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
 
#     def change_gear(self):
#         print("Changing gear")
 
#     def start_engine(self):
#         print("Changing engine")

# car = Car("Toyota", "Avensis", "silver")
# print(isinstance(car, Vehicle)) # True


# Сделаем реализацию класса Rectangle с использованием свойств:
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError
    def area(self):
        return self.__width * self.__height

# Теперь работать с width и height можно так, как будто они являются атрибутами:

rect = Rectangle(10, 20)
rect.width

rect.height

# Можно не только читать, но и задавать новые значения свойствам:

rect.width = 50
rect.width

rect.height = 70
rect.height

# в setter’ах этих свойств осуществляется проверка входных значений, если значение меньше нуля, то будет выброшено исключение ValueError:

# rect.width = -10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "test.py", line 28, in width
#     raise ValueError
# ValueError

from dataclasses import dataclass


# Обычный класс
class Number:
    def __init__(self, val):
        self.val = val
 
one = Number(1)
one.val

# Инициализация dataclass

@dataclass
class Number:
  val:int 
 
one = Number(1)
one.val

# Нет необходимости определять __init__ и затем присваивать значения self
# Мы определили атрибуты-члены класса что гораздо более читабельно, наряду с определением типов (type hinting). Теперь мы сразу видим, что val имеет тип int.

# Также возможно определить значения по умолчанию:

@dataclass
class Number:
    val:int = 0


# Представление объекта — это значимое строковое представление объекта, которое очень полезно при отладке.
# Представление объектов Python по умолчанию не особо понятно и читабельно, обычно это что типа такого object at 0x7ff395b2ccc0:

class Number:
    def __init__(self, val = 0):
        self.val = val
 
a = Number(1)
a # <__main__.Number object at 0x7ff395b2ccc0>
# Это не дает нам понимание о полезности объекта и приводит к сложности при отладки.

# Значимое представление может быть реализовано путем определения метода __repr__ в определении класса.

def __repr__(self):
    return self.val
# Теперь мы получаем читаемое представление объекта:

# dataclass автоматически добавляет функцию __repr__, поэтому нам не нужно ее реализовывать вручную.

@dataclass
class Number:
    val: int = 0
a = Number(1)
Number(val = 1)

# Сравнение между двумя объектами a иb обычно состоит из следующих операций:
# a < b
# a > b
# a == b
# a >= b
# a <= b
# В python можно определить методы в классах, которые могут выполнять вышеуказанные операции. Для простоты, я продемонстрирую лишь реализацию == и <.

# Обычный класс

class Number:
    def __init__( self, val = 0):
       self.val = val
 
    def __eq__(self, other):
        return self.val == other.val
 
    def __lt__(self, other):
        return self.val < other.val

# dataclass

@dataclass(order = True)
class Number:
    val: int = 0

# Нам не нужно определять методы __eq__ и __lt__, потому что декоратор dataclass автоматически добавляет их в определение класса при вызове с order = True

# Когда вы используете dataclass, он добавляет функции __eq__ и __lt__ в определение класса. Мы уже знаем это. Как эти функции знают, что нужно проверить равенство или сделать сравнение?

# Сгенерированная функцией __eq__ будет сравнивать кортеж своих атрибутов с кортежем атрибутов другого экземпляра того же класса. В нашем случае вот что эквивалентно автоматически сгенерированной функции __eq__:

def __eq__(self, other):
    return (self.val,) == (other.val,)


# Мы напишем класс данных Person, которое будет содержать имя (name) и возраст (age).

@dataclass(order = True)
class Person:
    name: str
    age:int = 0
# Автоматически сгенерированный метод __eq__ будет эквивалентен:

def __eq__(self, other):
    return (self.name, self.age) == ( other.name, other.age)
# Обратите внимание на порядок атрибутов. Они всегда будут генерироваться в порядке, который вы определили в определении класса данных.

# Аналогично, эквивалентная функция __le__ будет похожа на:

def __le__(self, other):
    return (self.name, self.age) <= (other.name, other.age)
# Необходимость определения функции, подобной __le__, обычно возникает, когда вам нужно отсортировать список ваших объектов данных. Встроенная функция сортировки Python основана на сравнении двух объектов.

import random
a = [Number(random.randint(1,10)) for _ in range(10)] #generate list of random numbers
a
# [Number(val=2), Number(val=7), Number(val=6), Number(val=5), Number(val=10), Number(val=9), Number(val=1), Number(val=10), Number(val=1), Number(val=7)]
sorted_a = sorted(a) #Sort Numbers in ascending order
# [Number(val=1), Number(val=1), Number(val=2), Number(val=5), Number(val=6), Number(val=7), Number(val=7), Number(val=9), Number(val=10), Number(val=10)]
reverse_sorted_a = sorted(a, reverse = True) #Sort Numbers in descending order 
reverse_sorted_a
# [Number(val=10), Number(val=10), Number(val=9), Number(val=7), Number(val=7), Number(val=6), Number(val=5), Number(val=2), Number(val=1), Number(val=1)]

# dataclass как вызываемый декоратор
# Не всегда желательно, что бы были определены все методы. Возможно вам понадобится только хранение значений и проверка равенства. Таким образом, вам нужны только определенные методы __init__ и __eq__. Если бы мы могли сказать декоратору не генерировать другие методы, это уменьшило бы некоторые накладные расходы, и у нас были бы только нужные операции над объектом данных. К счастью, этого можно достичь, используя декоратор класса данных в качестве вызываемого объекта.

# Из официальных документов декоратор может использоваться как вызываемый со следующими аргументами:
# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
# class C:
#  …
# init : По умолчанию будет создан метод __init__. Если ему передано значение False, у класса не будет метода __init__.
# repr : Метод __repr__ генерируется по умолчанию. Если ему передано значение False, у класса не будет метода __repr__.
# eq: По умолчанию будет создан метод __eq__. Если ему передано значение False, метод __eq__ не будет добавлен классом данных, но по умолчанию все равное будет object.__eq__.
# order : По умолчанию генерируются методы __gt__, __ge__, __lt__, __le__. Если будет False, они не будут заданы.
# Аргумент frozen мы обсудим чуть позже. Аргумент unsafe_hash заслуживает отдельного поста из-за его сложных вариантов использования.

# нам нужно:
# 1. __init__
# 2. __eq__

# Эти функции генерируются по умолчанию, поэтому нам не нужно генерировать другие функции. Как нам это сделать? Просто передайте соответствующим аргументам значение False.

@dataclass(repr = False) # order, unsafe_hash and frozen are False
class Number:
    val: int = 0
a = Number(1)
a
# <__main__.Number object at 0x7ff395afe898>
b = Number(2)
c = Number(1)
a == b # False
a < b 
# Traceback (most recent call last):
# File “<stdin>”, line 1, in <module>
# TypeError: ‘<’ not supported between instances of ‘Number’ and ‘Number’

# Frozen экземпляры
# Frozen (Замороженные) экземпляры — это объекты, атрибуты которых нельзя изменить после инициализации объекта.

# В Python невозможно создать действительно неизменяемые объекты. Всегда можно найти способ изменить объект.

# Создать неизменяемые атрибуты в объекте в Python — трудная задача, и я не буду подробно останавливаться на этом.

# Вот что мы ожидаем от неизменного объекта:

a = Number(10) # Предполагая, что числовой класс является неизменным
a.val = 10 # Тут должна появится Error
# С помощью классов данных можно определить замороженный объект, используя декоратор dataclass как вызываемый объект с аргументом frozen = True.

# Когда создается экземпляр замороженного объекта класса данных, любая попытка изменить атрибуты объекта вызывает FrozenInstanceError.

@dataclass(frozen = True)
class Number:
    val: int = 0

a = Number(1)
a.val

a.val = 2
# Traceback (most recent call last):
# File “<stdin>”, line 1, in <module>
# File “<string>”, line 3, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field ‘val’
# Таким образом, замороженный экземпляр — отличный способ для хранения…

# С помощью Dataclasses мы может отказаться от использования метода __init__ для присваивания переменных self. Но теперь мы теряем гибкость выполнения вызовов функций, которые могут потребоваться сразу после назначения переменных.

# Давайте обсудим пример, в котором мы определяем класс Float для хранения чисел с плавающей точкой, и сразу вычисляем целую и десятичную части, после инициализации.

# Обычный класс

import math
class Float:
    def __init__(self, val = 0):
        self.val = val
        self.process()
 
    def process(self):
        self.decimal, self.integer = math.modf(self.val)
 
a = Float( 2.2)
a.decimal

a.integer

# в классах данных обработка после инициализации выполняется с помощью метода __post_init__.

# Сгенерированный метод __init__ вызывает метод __post_init__. 
# Таким образом, любая обработка может быть выполнена в этом методе.

import math
@dataclass
class FloatNumber:
    val: float = 0.0
 
    def __post_init__(self):
        self.decimal, self.integer = math.modf(self.val)
 
a = Number(2.2)
a.val
a.integer
a.decimal


# Dataclasses поддерживают наследование так же как обычные классы Python.

# Таким образом, атрибуты, определенные в родительском классе, будут доступны и в дочернем классе.

@dataclass
class Person:
    age: int = 0
    name: str
@dataclass
class Student(Person):
    grade: int

s = Student(20, "John Doe", 12)
s.age
s.name
s.grade

# аргументы для Student находятся в порядке полей, определенных в определении класса.

# __post_init__ — это просто еще одна функция, ее вызов не меняется:
# вызывается только метод __post_init__ класса B. 
@dataclass
class A:
    a: int
    
    def __post_init__(self):
        print("A")
@dataclass
class B(A):
    b: int
    
    def __post_init__(self):
        print("B")
a = B(1,2)

# Поскольку метод __post_init__ класса A - это функция родительского класса, 
# его можно вызвать с помощью super.

@dataclass
class B(A):
    b: int
    
    def __post_init__(self):
        super().__post_init__() #Call post init of A
        print("B")
a = B(1,2)
