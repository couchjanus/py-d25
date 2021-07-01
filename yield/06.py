# метод send.

# у объекта генератора появилось еще несколько методов: .close(), .throw() и .send(). И это привело, можно сказать, к революции в области Data Flow Programming. С помощью .close() теперь можно извне заставить генератор остановиться на следующем обращении к нему, а с помощью .throw() — заставить его бросить исключение:

import itertools

def my_generator3():
  # Бесконечный счетчик
  counter = itertools.count()
  while True:
    yield next(counter)

myiterator = my_generator3()
myiterator2 = my_generator3()

for item in myiterator:
  print(item, end=" ")
  if item == 3:
    # Корректно завершаем генератор
    myiterator.close()

for item in myiterator2:
  print(item, end=" ")
  if item == 2:
    # Все плохо
    myiterator2.throw(Exception("Everything is bad"))

## 0 1 2 3

## 0 1 2 Traceback (most recent call last):
## File "test.py", line 28, in &lt;module&gt;
## myiterator2.throw(Exception("Everything is bad"))
## File "test.py", line 12, in my_generator3
## yield next(counter)
## Exception: Everything is bad

# метод .send() позволяет отправить данные в генератор перед вызовом следующего блока кода!

def my_coroutine():
  # Бесконечный счетчик
  counter = itertools.count()
  while True:
    y = (yield next(counter))
    if y:
      # Меняем начало отсчета
      counter = itertools.count(y)

myiterator = my_coroutine()

for item in myiterator:
  print(item, end=" ")
  if item == 1:
    # Отправляем число в генератор
    myiterator.send(4)
  elif item == 6:
    myiterator.close()
## 0 1 5 6

# по вызову yield (как, в общем случае, и return) происходит передача управления. Сопрограмма сама решает, когда перенаправить flow в другое место (например, в другую сопрограмму). И это позволяет строить красивые разветвленные деревья обработки потоков данных. 
