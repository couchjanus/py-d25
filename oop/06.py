# В ряде языков, например, С++, существует четкое разделение членов класса на закрытые, защищенные и публичные. 

# В Python все члены класса являются общедоступными, хотя существует возможность эмуляции закрытых. 

# Концепция отсутствия закрытых атрибутов в Python описывается фразой одного из разработчиков языка: «Мы все взрослые люди. Если программист хочет выстрелить себе в ногу - нужно предоставить ему возможность это сделать».

# В Python регулирование открытости и закрытости атрибутов определяется конвенцией.
# Атрибут, который должен быть не общедоступным (Non-Public) обозначается при помощи ведущего подчеркивания _: 

# _spam для поля 
# или 
# _get_count() для метода. 

# Данный синтаксис указывает на то, что атрибут используется для внутренней реализации класса и не предназначен для использования извне и должен быть использован/изменен только если разработчик-пользователь класса абсолютно уверен в этом. 

# При этом атрибут с _ доступен извне, как и обычный public-атрибут класса.

# Атрибут, который должен быть закрытым (Private), обозначается при помощи ведущего двойного подчеркивания __: 

# __private для поля 
# или 
# __get_count() для метода. 

# Данный синтаксис указывает на то, что атрибут используется для внутренней реализации класса и не предназначен для использования извне и не должен быть использован/изменен разработчиком-пользователем класса. 
# При этом атрибут с __ оказывается недоступным извне, используя технику сокрытия имен (Name Mangling). Несмотря на это, в отличие от ряда языков (например, Java) такие закрытые члены класса также можно изменять, но более сложным способом - их можно увидеть, используя функцию dir().
# Организация доступа к членам класса в Python построена на принципе универсального доступа, гласящем, что «все услуги, предлагаемые модулем должны быть доступны через единую нотацию, которая не раскрывает, реализованы ли они посредством хранения либо вычисления».
# В частности, это предполагает:
# предоставлять доступ к переменным напрямую, например, foo.x = 0, а не foo.set_x(0);
# в случае необходимости проверки устанавливаемого значения использовать свойства, которые сохраняют единый синтаксис доступа, установка значения foo.x = 0 приводит к вызову foo.set_x(0).

# Преимуществом данного подхода является возможность использование синтаксиса foo.x += 1, хотя на самом деле внутри происходит вызов foo.set_x(foo.get_x() + 1).

# Простая реализация класса окружности
import math

class Circle:
    """Окружность."""

    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r

    def length(self):
        """Вернуть длину окружности."""
        return 2 * math.pi * self.r

    def square(self):
        """Вернуть площадь окружности."""
        return math.pi * self.r**2

    def __str__(self):
        return "Окружность ({0.x}; {0.y}) радиус={0.r}".format(self)


if __name__ == "__main__":

    c = Circle(3, 4, 1)
    print(c)  # Окружность (3; 4) радиус=1
    print(c.length(), c.square())  # 6.283185307179586 3.141592653589793

# В приведенной реализации все атрибуты общедоступны 
# и имеется проблема возможности указания напрямую отрицательного радиуса. 
# Один из вариантов - добавить сеттеры и геттеры для радиуса, 
# а сам радиус обозначить как не общедоступный атрибут.