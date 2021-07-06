# Yield это ключевое слово, которое используется примерно как return — отличие в том, что функция вернёт генератор.

def createGenerator() :
	mylist = range(3)
	for i in mylist :
		yield i*i

mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
	print(i)

# это удобно, если вы знаете, что функция вернёт большой набор значений, который надо будет прочитать только один раз.

# Чтобы освоить yield, вы должны понимать, что когда вы вызываете функцию, код внутри тела функции не исполняется. Функция только возвращает объект-генератор

# Ваш код будет вызываться каждый раз, когда for обращается к генератору.

# генератором-функцией является та функция, которая содержит в себе инструкцию yield. При вызове метода next объекта этой функции мы получим значение, указанное за yield, и весь контекст, включая значение локальных переменных, будет запомнен в том состоянии, в котором он находятся при выполнении строчки с yield. 

def gener(stop):
	i = 0
	while i < stop:
		yield i
		i += 1

# создав объект
g = gener(7)

# вызвав метод next
next(g)
# получим сначала 0

# После чего параметры функции i = 0 и то, что выполнение функции находится внутри тела цикла, будет запомнено до следующего вызова next. Следующий вызов next, вернет 1.
next(g) # 1

# Так будет происходить, пока условие i < stop выполняется, а именно до тех пор, пока i не достигнет значения 7.
next(g)
next(g)

# StopIteration
# Таким образом, при достижении «конца» итераций, возвращается исключение StopIteration. Выход из генератора можно вызвать явно, написав где-либо в функции инструкцию return, при достижении которой опять же вернется исключение StopIteration.

# То есть объявление типа

def generr(stop):
	i = 0
	while i < stop:
		yield i
		i += 1
	return
# равнозначно предыдущей функции gener.

# Зачем нужны функции, возвращающие генераторы?
# Известно, что объекты типа питоновских списков занимают память пропорционально количеству элементов. Скажем список [0, 1, 2, 3, 4, 5, 6] будет затрачивать память как минимум под шесть целочисленных значений. Если нам нужно будет итерироваться по такому списку, то мы можем явно написать что-то вроде

for i in [0, 1, 2, 3, 4, 5, 6]:
    print(i)

# и получить на стандартный вывод последовательность от 0 до 6.

# Если же нам понадобится итерироваться по списку с гораздо большим количеством целых чисел, скажем, от нуля до нескольких миллиардов с шагом 1, то неужели придется хранить все эти числа в памяти? Это не нужно. Достаточно знать начало, конец и шаг итераций. 

# если мы захотим хранить объект из бесконечного числа субобъектов?

def genera():
	i = 0
	while True:
		yield i
		i += 1

# Вы видите описанный бесконечный цикл. Итерироваться по объекту, возвращенному такой функцией, можно бесконечно. Сам объект будет символом бесконечного множества.
g = genera()

# Использование ключевого слова yield

# в более сложных сценариях необходимо создавать функции, которые возвращают генератор. 
# Ключевое слово yield, в отличие от оператора return, используется для превращения обычной функции Python в генератор. 
# Оно используется в качестве альтернативы одновременному возвращению целого списка.

# посмотрим, что возвращает функция, если не использовать ключевое слово yield:

def cube_numbers(nums):  
    cube_list = []
    for i in nums:
        cube_list.append(i**3)
    return cube_list

cubes = cube_numbers([1, 2, 3, 4, 5])

print(cubes)

# создается функция cube_numbers, которая принимает список чисел, вычисляет их куб и возвращает вызывающему объекту список целиком. При вызове этой функции список кубов возвращается и сохраняется в переменную cubes. 

# Теперь, изменим сценарий, так чтобы он возвращал генератор.

def cube_numbers(nums):  
    for i in nums:
        yield(i**3)

cubes = cube_numbers([1, 2, 3, 4, 5])

print(cubes)

# функция cube_numbers возвращает генератор вместо списка кубов чисел. 
# Создать генератор с помощью ключевого слова yield очень просто. 
# Здесь нам не нужна временная переменная cube_list для хранения куба числа. 
# Кроме того, не используется оператор return, но вместо него используется слово yield для возвращения куба числа внутри цикла.

# Несмотря на то, что был произведён вызов функции cube_numbers, она фактически не выполняется на данный момент времени, и в памяти еще нет элементов.

# Получение значение из генератора:

next(cubes) # функция возвратит "1"

# Теперь, когда снова вызывается next генератора, функция cube_numbers возобновит выполнение с того места, где она ранее остановилась на yield. Функция будет продолжать выполняться до тех пор, пока снова не найдет yield. Следующая функция будет продолжать возвращать значение куба по одному, пока все значения в списке не будут проитерированы.

# Как только все значения будут проитерированы, следующий вызов функции создаст исключение StopIteration. Важно отметить, что генератор кубов не хранит какие-либо элементы в памяти, а значения в кубе вычисляются во время выполнения, возвращаются и забываются. Используется только дополнительная память для хранения данных состояния самого генератора, которая, как правило, гораздо меньше, чем полный список. Это делает генераторы идеально подходящими для ресурсоемких задач.

# Вместо того, чтобы использовать next итератора, можно также использовать цикл for для перебора значений генераторов. При использовании цикла for за кулисами вызывается next итерации, пока не будут возвращены все элементы генератора.

# Но используя ключевое слово yield можно сильно упростить реализацию:

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

for i in fibonacci():
    print(i)
    if i > 100:
        break


# Любая функция в Python, в теле которой встречается ключевое слово yield, называется генераторной функцией — при вызове она возвращает объект-генератор.
# Объект-генератор реализует интерфейс итератора, соответственно с этим объектом можно работать, как с любым другим итерируемым объектом.

fib = fibonacci()
print(next(fib))
# 0
print(next(fib))
# 1

for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break
# 0: 0
# 1: 1
# 2: 1
...

# Рассмотрим работу yield:

def gen_fun():
    print('block 1')
    yield 1
    print('block 2')
    yield 2
    print('end')

for i in gen_fun():
    print(i)

# block 1
# 1
# block 2
# 2
# end


    # при вызове функции gen_fun создается объект-генератор
    # for вызывает iter() с этим объектом и получает итератор этого генератора
    # в цикле вызывает функция next() с этим итератором пока не будет получено исключение StopIteration
    # при каждом вызове next выполнение в функции начинается с того места где было завершено в последний раз и продолжается до следующего yield


# Происходит приблизительно следующее. Генераторная функция разбивается на части:

def gen_fun_1():
    print('block 1')
    return 1


def gen_fun_2():
    print('block 2')
    return 2


def gen_fun_3():
    print('end')


def gen_fun_end():
    raise StopIteration


# Создается стейт-машина в которой при каждом вызове __next__ меняется состояния и в зависимости от него вызывается тот или иной кусок кода. Если в функции, yield в цикле, то соответственно состояние стейт-машины зацикливается пока не будет выполнено условие.

# Свой вариант range:

def cool_range(start, stop, inc):
    x = start
    while x < stop:
        yield x
        x += inc

for n in cool_range(1, 5, 0.5):
    print(n)
# 1
# 1.5
# ...
# 4.5

print(list(cool_range(0, 2, 0.5)))
# [0, 0.5, 1.0, 1.5]