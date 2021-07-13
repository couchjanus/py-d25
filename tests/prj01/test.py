# Вот как будет проходить проверка функции sum() (1,2,3) равна шести:
# assert sum([1, 2, 3]) == 6, "Should be 6"
# Тест не выведет ничего на REPL, так как значения верны. Но если результат sum() неверен, это приведет к ошибке AssertionError и сообщению “Should be 6”.
# assert sum([1, 1, 1]) == 6, "Should be 6"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: Should be 6

# В REPL вы видите AssertionError, потому что результат не соответствует 6. Переместите код в новый файл, названный test_sum.py и выполните снова:

# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     print("Everything passed")

# Вы написали пример теста, утверждение и точку входа.

# $ python test_sum.py
# Everything passed

# sum() принимает любое повторяющееся значение в качестве первого аргумента. Вы проверили список, теперь проверьте так же и tuple. 
# Создайте новый файл test_sum_2.py:

# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     test_sum_tuple()
#     print("Everything passed")

# Когда вы выполняете test_sum_2.py, скрипт выдает ошибку, так как sum() от (1,2,2) не равна 6:

# $ python test_sum_2.py
# Traceback (most recent call last):
#   File "test_sum_2.py", line 9, in <module>
#     test_sum_tuple()
#   File "test_sum_2.py", line 5, in test_sum_tuple
#     assert sum((1, 2, 2)) == 6, "Should be 6"
# AssertionError: Should be 6

# Создайте новую папку проекта и внутри нее еще одну под названием foo. 
# Внутри foo создайте пустой файл с именем __init__.py и файл с именем bar.py:

# prj01/
# │
# └── foo/
#      ├── bar.py
#      └── __init__.py

# В bar.py создайте новую функцию plus()

# def plus(arg):
#     total = 0
#     for val in arg:
#         total += val
#     return total


# Создайте в корне файл test.py, который будет содержать ваш тест:

# prj01/
# │
# ├── foo/
# │     ├── bar.py
# │     └── __init__.py
# |
# └── test.py


from foo.bar import plus

def test_plus():
    assert plus([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_plus()
    print("Everything passed")
