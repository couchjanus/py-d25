# Test Runner Unittest

# Unittest содержит как структуру тестирования Python, так и test runners. У него есть несколько требований:

#     Нужно помещать свои тесты в классы как методы.
#     Нужно использовать ряд специальных методов утверждения в unittest − TestCase вместо assert.

# Для преобразования в unittest:
#     Импортируйте его из стандартной библиотеки.
#     Создайте класс TestPlus, который наследуется от класса TestCase.
#     Преобразуйте тестовые функции в методы путем добавления self в качестве первого аргумента.
#     Изменить утверждение на использование метода self.assertEqual() в классе TestCase.
#     Изменить точку входа в командной строке для вызова unittest.main().
#     Создайте test_plus_unittest.py:

import unittest
from foo.bar import plus

class TestSum(unittest.TestCase):

    def test_plus_list(self):
        self.assertEqual(plus([1, 2, 3]), 6, "Should be 6")

    def test_plus_tuple(self):
        self.assertEqual(plus((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

#  python test_plus_unittest.py 
# .F
# ======================================================================
# FAIL: test_plus_tuple (__main__.TestSum)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/janus/work/py-g25/tests/prj02/test_plus_unittest.py", line 26, in test_plus_tuple
#     self.assertEqual(plus((1, 2, 2)), 6, "Should be 6")
# AssertionError: 5 != 6 : Should be 6

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# FAILED (failures=1)


# Test Runner Nose

# Совместим с любыми тестами, написанными с использованием unittest. 
# Чтобы начать тестирование Python-кода, установите его из PyPl и выполните в командной строке. 
# Он попытается обнаружить все скрипты с именем test*.py, наследующие от unittest.

# pip install nose2
# python -m nose2

# .F
# ======================================================================
# FAIL: test_plus_tuple (test_plus_unittest.TestSum)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/janus/work/py-g25/tests/prj02/test_plus_unittest.py", line 26, in test_plus_tuple
#     self.assertEqual(plus((1, 2, 2)), 6, "Should be 6")
# AssertionError: 5 != 6 : Should be 6

# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# FAILED (failures=1)
