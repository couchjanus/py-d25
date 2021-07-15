# Проверка типов
# Python - язык с неявной динамической типизацией, 
# т.е. точный тип передаваемых аргументов не известен, 
# могут возникнуть проблемы при передаче не ожидаемых значений.

# Ошибка при попытке сложить Point и int
# if __name__ == "__main__":

#     p1 = Point(0, 5)
#     p2 = Point(-5, 10)

#     print(p1 + 2)  # Ошибка: AttributeError: 'int' object has no attribute 'x'
# перед действием рекомендуется проверить, экземпляром какого класса 
# является переданный объект. 
# Выполнить такую проверку можно используя функции type() 
# или isinstance(obj, class).

# Изменение действия в зависимости от типа переданного параметра
class Point:
    """point on the plane."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Вернуть строку в виде 'Точка 2D (x, y)'."""
        return "Точка 2D ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Создать новый объект как сумму координат self и other."""

        if isinstance(other, self.__class__):
            # Точка с точкой
            # Возвращаем новый объект!
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            # Точка и число
            # Добавим к обеим координатам self число other и вернем результат
            # Возвращаем старый, измененный, объект!
            self.x += other
            self.y += other
            return self
        else:
            # В противном случае возбуждаем исключение
            raise TypeError("Не могу добавить {1} к {0}".
                            format(self.__class__, type(other)))

if __name__ == "__main__":

    p1 = Point(0, 5)
    p2 = Point(-5, 10)

    print(p1 + 2)    # (2, 7)
    print(p1 + 5.0)  # (7.0, 12.0)
    # TypeError: Не могу добавить <class 'str'> к <class '__main__.Point'>
    print(p1 + "я строка")
