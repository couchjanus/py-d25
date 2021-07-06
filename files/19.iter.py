# 19.iter.py
import os,hashlib

# Основное назначение итератора – это упрощение навигации по элементам объекта, который, как правило, представляет собой некоторую коллекцию (список, словарь и т.п.). Итератор представляет собой объект перечислитель, который для данного объекта выдает следующий элемент, либо бросает исключение, если элементов больше нет.
# Основное место использования итераторов – это цикл for. Если вы перебираете элементы в некотором списке или символы в строке с помощью цикла for, то это означает, что при каждой итерации цикла происходит обращение к итератору, содержащемуся в строке/списке, с требованием выдать следующий элемент, если элементов в объекте больше нет, то итератор генерирует исключение, обрабатываемое в рамках цикла for незаметно для пользователя.
# Для того, чтобы получить объект итератор необходимо использовать функцию iter(), а для  извлечения следующего элемента из итератора – функцию next().

# Оператор lambda это анонимная, или несвязанная функция, при этом довольно ограниченная.
# Python разрешает создание анонимных функций (например, функции, которые не связаны с именем) во время выполнения, используя конструкцию “lambda”. 
# Определение lambda функции не включает оператор “return” - эта конструкция всегда содержит выражении, результат которого возвращается. Обычно определение lambda функция используется везде, где ожидается функция и нет надобности присваивать значение переменной.

# lambda: f.read(2048)

# Поскольку мы можем отслеживать файлы, размер которых превышает объем доступной памяти, нам нужно разбить их на куски, чтобы система не остановилась. 

# for chunk in iter(lambda: f.read(2048), ""):

# Функция iter() позволяет многократно выполнять задачу, пока не будут выполнены определенные критерии. В качестве параметра используем lambda для считывания 2048 байт за раз и остановимся, как только файл достигнет своего конца, вернув "". (Причина считывания 2048 байт состоит в том, что MD5 использует размер блока 128. Используя кратное число, мы можем не только быстрее прочитать файл, но и помочь быстрее вычислить хэш.)

# Функция encode() возвращает кодированную версию строки. Кодировкой по умолчанию является текущая кодировка строки. 

# str.encode(encoding = 'UTF-8',errors = 'strict')

# encoding –  кодирование, которое будет использоваться. Стандартные кодировки.
# errors –  можно задавать установки других схем обработки ошибок. Значение по умолчанию для ошибок strict означает, что ошибки кодирования принимают UnicodeError. Другие возможные значения ignore, replace, xmlcharrefreplace, backslashreplace и любое другое имя, зарегистрированное через codecs.register_error().
# Возвращаемое значение - декодированная строка.

# Передать зашифрованную последовательность байтов можно с помощью метода update(). В этом случае объект присоединяется к предыдущему значению:

# hash.update(chunk.encode('utf-8'))

# Получить зашифрованную последовательность байтов и строку позволяют два метода — digest() и hexdigest():

# md5 = hash.hexdigest()
# print(file,md5)


def walk(dir):
   for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
        hash = hashlib.md5()
        with open(os.path.join(dir,file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8'))
        md5 = hash.hexdigest()
        print(file,md5)
walk(os.getcwd())