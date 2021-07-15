# Создание и использование класса

# Создание класса начинается с ключевого слова class и указания имени класса. 

# Простой пример класса

class Point:
    """Point on the plane."""
    pass


if __name__ == "__main__":

    # Создание объекта (экземпляра класса)
    p = Point()

    print(p)        # <__main__.Point object at 0x0000000001E43898>
    print(type(p))  # <class '__main__.Point'>

