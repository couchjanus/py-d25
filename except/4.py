# Вам нужно перебрать > 20 номеров, 
# но список составлен из пользовательского ввода 
# и может не содержать 20 номеров. 
# вы хотите, чтобы остальные числа интерпретировались как 0:

def do_stuff_with_number(n):
   print(n)

def catch_this():
   the_list = (1, 2, 3, 4, 5)
   for i in range(20):
       try:
           do_stuff_with_number(the_list[i])
       except IndexError: # Raised when accessing a non-existing index of a list
           do_stuff_with_number(0)
           print('Raised when accessing a non-existing index of a list')

catch_this()
