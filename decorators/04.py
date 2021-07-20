# Стек декораторов
# мы можем спрятать функцию, которая уже была спрятана. 
# В математике и в программировании это называют композицией функций. 
# Так же как f o g(x) == f(g(x)), 
# если положить в стек @pop на @lock на drop, то получится pop(lock(drop(it))).

def pop(func):

    def inner(*args, **kwargs):
        print("Pop!")
        return func(*args, **kwargs)

    return inner

def lock(func):

    def inner(*args, **kwargs):
        print("Lock!")
        return func(*args, **kwargs)

    return inner

@pop
@lock
def drop(it):
    print("Drop it!")
    return it[:-2]

print(drop("That's the end of that one, isn't it"))

# Pop!
# Lock!
# Drop it
# "That's the end of that one, isn't "

