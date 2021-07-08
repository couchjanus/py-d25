# Для того, чтобы указать, что переменная содержит список можно использовать тип list в качестве аннотации. Однако если хочется конкретизировать, какие элементы содержит список, он такая аннотация уже не подойдёт. Мы указываем тип элементов списка в квадратных скобках.
titles: List[str] = ["hello", "world"]
titles.append(100500)  # Argument 1 to "append" of "list" has incompatible type "int"; expected "str"
titles = ["hello", 1]  # List item 1 has incompatible type "int"; expected "str"
items: List = ["hello", 1]
# Предполагается, что список содержит неопределенное количество однотипных элементов. Но при этом нет ограничений на аннотацию элемента: можно использовать Any, Optional, List и другие. Если тип элемента не указан, предполагается, что это Any.


# Кортежи в отличие от списков часто используются для разнотипных элементов. Синтаксис похож с одним отличием: в квадратных скобках указывается тип каждого элемента кортежа по отдельности.
# Если же планируется использовать кортеж аналогично списку: хранить неизвестное количество однотипных элементов, можно воспользоваться многоточием (...).
# Аннотация Tuple без указания типов элементов работает аналогично Tuple[Any, ...]
price_container: Tuple[int] = (1,)
price_container = ("hello")  # Incompatible types in assignment (expression has type "str", variable has type "Tuple[int]")
price_container = (1, 2)  # Incompatible types in assignment (expression has type "Tuple[int, int]", variable has type "Tuple[int]")

price_with_title: Tuple[int, str] = (1, "hello")

prices: Tuple[int, ...] = (1, 2)
prices = (1, )
prices = (1, "str")  # Incompatible types in assignment (expression has type "Tuple[int, str]", variable has type "Tuple[int, ...]")

something: Tuple = (1, 2, "hello")

# Для словарей используется typing.Dict. Отдельно аннотируется тип ключа и тип значений:
book_authors: Dict[str, str] = {"Fahrenheit 451": "Bradbury"}
book_authors["1984"] = 0  # Incompatible types in assignment (expression has type "int", target has type "str")
book_authors[1984] = "Orwell"  # Invalid index type "int" for "Dict[str, str]"; expected type "str"
# Аналогично используются typing.DefaultDict и typing.OrderedDict
# Для указания типа результата функции можно использовать любую аннотацию. Но есть несколько особенных случаев.

# Если функция ничего не возвращает (например, как print), её результат всегда равен None. Для аннотации так же используем None.
# Корректными вариантами завершения такой функции будут: явный возврат None, возврат без указания значения и завершение без вызова return.
def nothing(a: int) -> None:
    if a == 1:
        return
    elif a == 2:
        return None
    elif a == 3:
        return ""  # No return value expected
    else:
        pass

# Если же функция никогда не возвращает управление (например, как sys.exit), следует использовать аннотацию NoReturn:
    def forever() -> NoReturn:
        while True:
            pass
# Если это генераторная функция, то есть её тело содержит оператор yield, для возвращаемого можно воспользоватьтся аннотацией Iterable[T], либо Generator[YT, ST, RT]:
def generate_two() -> Iterable[int]:
    yield 1
    yield "2"  # Incompatible types in "yield" (actual type "str", expected type "int")

# Иногда анализатор статический анализатор не может корректно определить тип переменной, в этом случае можно использовать функцию cast. Её единственная задача — показать анализатору, что выражение имеет определённый тип. Например:

from typing import List, cast

def find_first_str(a: List[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    return cast(str, a[index])


