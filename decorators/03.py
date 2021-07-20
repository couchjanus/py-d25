# Logging before and after a function be executed
def logger(func):
    def wrapper(): # Function called by the decorator
        print('Start')
        func() # External function
        print('End')
    return wrapper

@logger # Decorator
def my_function(): # External function
    print('...Executing function...')

my_function()

# Аргументы декоратора

# Если функция требует наличие аргумента, то его можно передать через декоратор.

def print_them_args(fn):

    def the_name_of_this_one_doesnt_matter(*args):
        # внутренняя функция перехватит значения аргументов в виде *args, **kwargs. 

        print("{} called with {}".format(fn.__name__, [*args]))

        return fn(*args)
    return the_name_of_this_one_doesnt_matter

@print_them_args
def add(a, b):
    return a + b

add(5, 8)

# Передача аргументов в функцию через декоратор

from time import sleep

def delay(seconds): 
    """The outermost function handles the decorator's arguments"""

    def decorator(fn): 
        """It defines a decorator function, like we are used to"""

        def inner(*args, **kwargs): 
            """ The decorator function defines the modified function
            Because we do things this way, the inner function
            gets access to the arguments supplied to the decorator initially"""
            print("{} called with {} and {}".format(fn.__name__, [*args], {**kwargs}))
            sleep(seconds)
            return fn(*args, **kwargs)

        return inner  
    # Decorator function returns the modified function
    return decorator 

# Finally, the outer function returns the custom decorator

@delay(5)
def it_may_be(times, name = ''):
    return name + " said: It is nearly Luncheon Time! " * times

print(it_may_be(3, name = 'Winnie-the-Pooh'))


# Возврат результата работы функции через декоратор

# Довольно часто, создаваемые функции возвращают какое-либо значение. Для того, чтобы его можно было возвращать через декоратор необходимо соответствующим образом построить внутреннюю функцию.

def decor_with_return(fn):
   def wrapper(*args, **kwargs):
       print("Run method: " + str(fn.__name__))
       return fn(*args, **kwargs)
   return wrapper

# Этот декоратор можно использовать для оборачивания функций, которые принимают различные аргументы и возвращают значение.

@decor_with_return
def calc_sqrt(val):
   return val**0.5

tmp = calc_sqrt(16)
print(tmp)
