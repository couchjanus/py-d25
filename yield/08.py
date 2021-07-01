# профилировщик памяти от PyPi.
# pip install memory-profiler

# Модуль time предоставляет различные функции, связанные со временем. 
# Функция perf_counter() возвращает значение времени (в долях секунды) счетчика производительности. Включает время, прошедшее с времени sleep, и является общесистемным. Контрольная точка возвращаемого значения не определена, поэтому действительна только разница между результатами последовательных вызовов. Между этим мы можем использовать time.sleep() и аналогичные функции.

#: Understand the usage of the perf_counter .
# Python program to show time by perf_counter() 
from time import perf_counter
  
# integer input from user, 2 input in single line
n, m = map(int, input('input 2 integer in single line: ').split()) 

# Start the stopwatch / counter
start = perf_counter() 
  
for i in range(n):
    t = int(input('input n times: ')) # user gave input n times
    if t % m == 0:
        print(t) 

# Stop the stopwatch / counter
stop = perf_counter()
  
print("Elapsed time:", stop, start) 
print("Elapsed time during the whole program in seconds:", stop - start)

# Предположим, нам нужно пройтись по большому списку чисел (например, 100000000) и сохранить квадраты всех чисел, которые нужно хранить отдельно в другом списке.

# Обычный подход

import memory_profiler
import time

def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0: 
            even.append(num*num)

    return even

m1 = memory_profiler.memory_usage()
t1 = time.perf_counter()
cubes = check_even(range(100000000))
t2 = time.perf_counter()
m2 = memory_profiler.memory_usage()
time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")

# После запуска кода выше, мы получим следующее:
# It took 21.876470000000005 Secs and 1929.703125 Mb to execute this method
