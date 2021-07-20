# Декораторы для методов класса

def decor(fn):
   def wrapper(self):
       print("Run method: " + str(fn.__name__))
       fn(self)
   return wrapper

# Vector - класс для представления двумерного вектора. 

class Vector():
   def __init__(self, px = 0, py = 0):
       self.px = px
       self.py = py

   # метод normalize() выводит модуль вектора.
   @decor
   def normalize(self):
       print((self.px**2 + self.py**2)**0.5)

vector = Vector(px=10, py=5)
vector.normalize()


# Декоратор на основе классов без переменных

class FunnyDecorator:
    def __init__(self, fn):
        print("Initializing Funny decorator class")
        self.fn = fn
        fn()

    def __call__(self):
        print("Calling Funny decorator call method")
        self.fn()

@FunnyDecorator
def simple_function():
    print("Inside the simple function")

print("Funny Decoration complete!")

simple_function()

# Декоратор на основе классов с переменными

# Декораторы на основе классов ведут себя по-разному в зависимости от того, есть у них переменные или нет.
# когда в декораторе есть переменные, происходит три вещи.
# 1. Переменные декораторов передаются в функцию __init__.
# 2. Функция сама по себе является функцией вызова.
# 3. Функция __сall__ вызывается немедленно и только один раз, примерно так же работает декоратор в функциях

# простой кэширующий декоратор

class SlimCache:
    # This method is called as soon as the decorator is attached to a function.
    def __init__(self, preloads={}):
        """Expects a dictionary of preloaded {input: output} pairs"""
        if preloads is None:
            self.cache = {}
        else:
            self.cache = preloads

    def __call__(self, func):
        # This method is called when a function is passed to the decorator
        def inner(n):
            if n in self.cache:
                return self.cache[n]
            else:
                result = func(n)
                self.cache[n] = result
                return result
        return inner

@SlimCache({1: 1, 2: 1, 4: 3, 8: 21}) # First __init__, then __call__
def fibonacci(n):
    """Returns the nth fibonacci number"""
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# At runtime, the 'inner' function above will actually be called!
# fibonacci(8) never actually gets called, because it's already in the cache!

print(fibonacci(8))

