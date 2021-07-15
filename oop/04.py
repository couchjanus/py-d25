# Переопределение операций для класса Point 
# сложения/разности двух объектов
# инверсии их координат 
# равенства/неравенства.

class Point:
    """point on the plane."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Вернуть строку в виде 'Точка 2D (x, y)'."""
        return "Точка 2D ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Создать новый объект как сумму координат 'self' и 'other'."""

        
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Создать новый объект как разность координат 'self' и 'other'."""
        
        # Вместо Point можно использовать self.__class__,
        # что позволит не привязываться к имени класса и быть
        # валидным для потомков
        return self.__class__(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """Вернуть новый объект, инвертировав координаты."""
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        """Вернуть ответ, являются ли точки одинаковыми."""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Вернуть ответ, являются ли точки разными.

        Используем реализованную операцию ==."""
        return not (self == other)

    def distance(self):
        """Вернуть расстояние до центра координат."""
        return (self.x**2 + self.y**2)**0.5

if __name__ == "__main__":

    p1 = Point(0, 5)
    p2 = Point(-5, 10)

    # Если Python не найдет в определении класса метода '__add__()',
    # строка ниже сгенерирует исключение:
    # 'TypeError: unsupported operand type(s) for +: 'Point' and 'Point''
    print(p1 + p2)             # Точка 2D (-5, 15)
    print(p1 - p2)             # Точка 2D (5, -5)
    print(-p2)                 # Точка 2D (5, -10)
    print(p1 == p2, p1 != p2)  # False True
    print("Расстояние до центра координат (p1): {:.2f}".format(p1.distance()))  # 5.00
    print("Расстояние до центра координат (p2): {:.2f}".format(p2.distance()))  # 11.18