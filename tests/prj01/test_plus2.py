from foo.bar import plus

def test_plus_seq():
    assert plus(1, 2, 3) == 6, "Should be 6"

def test_plus():
    assert plus([1, 2, 3]) == 6, "Should be 6"

# plus() принимает любое повторяющееся значение в качестве первого аргумента. 
# проверили list, теперь проверим tuple. 

def test_plus_tuple():
    assert plus((1, 2, 3)) == 6, "Should be 6"

if __name__ == "__main__":
    test_plus()
    print("Everything passed for list")
    test_plus_seq()
    print("Everything passed for seq")
    test_plus_tuple()
    print("Everything passed")

# Когда вы выполняете test_plus2.py, скрипт выдает ошибку, так как plus((1,2,2)) не равна 6:
# Traceback (most recent call last):
#   File "/home/janus/work/py-g25/tests/prj01/test_plus2.py", line 14, in <module>
#     test_plus_tuple()
#   File "/home/janus/work/py-g25/tests/prj01/test_plus2.py", line 10, in test_plus_tuple
#     assert plus((1, 2, 2)) == 6, "Should be 6"
# AssertionError: Should be 6
