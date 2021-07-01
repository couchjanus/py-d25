# С использованием генераторов
# сравним обычный подход с подходом, в котором используются генераторы, в вопросах памяти и времени, которые тратятся на выполнение кода.

import memory_profiler
import time

def check_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num 


m1 = memory_profiler.memory_usage()
t1 = time.perf_counter()
cubes = check_even(range(100000000))
t2 = time.perf_counter()
m2 = memory_profiler.memory_usage()
time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")

# После запуска кода выше, мы получим следующее:
# It took 2.9999999995311555e-05 Secs and 0.02656277 Mb to execute this method

# время выполнения и затраченная память значительно сократились. Генераторы работают по принципу, известному как ленивые вычисления. Это значит, что они могут экономить ресурсы процессора, памяти и других вычислительных ресурсов.
