import timeit

# Списки могут использовать вложенный for . 
# Вы можете закодировать любое количество вложенных циклов для внутри списка понимания, 
# и каждый for цикла может иметь дополнительный связанный, if тест. 
# При этом порядок следования for построений такой же порядок, 
# как при написании серии вложенных for заявлений. 
# Общая структура списочных представлений выглядит следующим образом:

# [ expression for target1 in iterable1 [if condition1]
#              for target2 in iterable2 [if condition2]...
#              for targetN in iterableN [if conditionN] ]

 
# Например, следующий код уплощение списка списков с использованием нескольких for операторов:

data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)

# Out: [1, 2, 3, 4, 5, 6]
# Можно эквивалентно записать в виде списка с кратной for конструкцией:

data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)
# Out: [1, 2, 3, 4, 5, 6]

 
# Как в расширенной форме, так и в понимании списка, 
# внешний цикл (первый для оператора) идет первым.
# В дополнение к более компактному вложенному пониманию также значительно быстрее.

data = [[1,2],[3,4],[5,6]]
def f():
     output=[]
     for each_list in data:
         for element in each_list:
             output.append(element)
     return output
print(timeit.timeit("f()", globals=globals()))
# Out: 529 ns ± 4.75 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

print(timeit.timeit("[inner for outer in data for inner in outer]", globals=globals()))
# Out:360 ns ± 14.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
 # Накладные расходы на вызов функции выше примерно 170ns.

# Встроенный, if ы вложены подобным образом , 
# и может происходить в любом положении после первого for :

data = [[1], [2, 3], [4, 5]]
output = [element for each_list in data
                if len(each_list) == 2
                for element in each_list
                if element != 5]
print(output)

# Out: [2, 3, 4] 
