# При описании предметной области классы могут образовывать иерархию, в корне которой стоит базовый класс, а нижележащие классы (подклассы) наследуют свои атрибуты и методы, уточняя и расширяя поведение вышележащего класса (надкласса). 
# Если один класс наследует (расширяет) другой класс, то этот класс называется подкласс. А класс, который наследуется, называется суперкласс.

# Если некоторый класс наследует другой суперкласс, то имя суперкласса задается в круглых скобках в заголовке инструкции class.

# Класс A - суперкласс для класса B
# class A:
    # атрибуты класса A

# Класс B - подкласс класса A
# class B(A):
    # атрибуты класса B

# Подкласс наследует атрибуты своих суперклассов.

# Класс A - суперкласс для классов B, C
class A:
    # Атрибут класса A: метод super_m()
    def super_m(self):
        print("class A. Method super_m()")

# Класс B - подкласс класса A
class B(A):
    # Атрибут класса B: Метод foo_m()
    def foo_m(self):
        # Из метода foo_m() можно доступиться
        # к атрибуту super_m() класса A
        self.super_m() # будет вызвано A.super_m()
        print("class B. Method foo_m()")

# Класс C - подкласс классов A, B
class C(B):
    # Атрибут класса C: метод bar_m()
    def bar_m(self):
        # Из метода bar_m() можно доступиться
        # к атрибуту super_m() класса A
        # и к атрибуту foo_m() класса B.
        self.super_m()
        self.foo_m()
        print("class C. Method bar_m()")

# Тестирование работы механизма наследования

objA = A()
objA.super_m() # вызов метода super_m() класса A