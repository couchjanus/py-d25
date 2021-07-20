class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity
apple_order = Order('apple', 1, 10)

print(dir(apple_order))
# print(apple_order.total.__str__)
# print(apple_order.total())

# Если этот код начать использовать, мы столкнемся с проблемой. 
# Наши данные ни как не проверяются. 
# цена (price) и количество (quantity) может принимать любое значение:

apple_order.quantity = -10
print(apple_order.quantity.__gt__(0))
# print(apple_order.total)

# нам нужно создать класс NonNegative 
# и реализовать протокол дескрипторов:

# class NonNegative:
#     def __init__(self, name):
#         self.name = name  # 
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]  #
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Cannot be negative.')
#         instance.__dict__[self.name] = value  

# Таким образом, мы явно передаем имя атрибута price 
# что бы использовать его как ключ при доступе к экземпляру __dict__.

# При использовании дескрипторов наше новое определение класса станет таким:

# class Order:
#     price = NonNegative('price')  # 
#     quantity = NonNegative('quantity')
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self.price = price
#         self.quantity = quantity
#     def total(self):
#         return self.price * self.quantity
# apple_order = Order('apple', 1, 10)
# apple_order.total() # 10
# apple_order.price = -10 # ValueError: Cannot be negative
# apple_order.quantity = -10 # ValueError: Cannot be negative

# протокол дескрипторов появившийся в Python 3.6:
# object.__set_name__(self, owner, name)
# Вызывается во время создания класса. 
# В этом случае дескриптор назначается на имя атрибута.
# С этим протоколом, мы можем привязать имя атрибута к дескриптору:

# class NonNegative:
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Cannot be negative.')
#         instance.__dict__[self.name] = value
#     def __set_name__(self, owner, name):
#         self.name = name

# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self.price = price
#         self.quantity = quantity
#     def total(self):
#         return self.price * self.quantity
# apple_order = Order('apple', 1, 10)
# apple_order.total() # 10
# apple_order.price = -10 # ValueError: Cannot be negative
# apple_order.quantity = -10 # ValueError: Cannot be negative