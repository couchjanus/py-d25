from typing import Optional

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

# Иногда вы не хотите ограничивать возможные типы переменной. Например, если это действительно не важно, или если вы планируете сделать обработку разных типов самостоятельно. В этом случае, можно использовать аннотацию Any. На следующий код mypy не будет ругаться:
Any = {}
unknown_item: Any = 1
print(unknown_item)
print(unknown_item.startswith("hello"))
print(unknown_item // 0)

# В этом случае предполагается, что хоть передан может быть любой объект, обращаться с ним можно только как с экземпляром object.

unknown_object: object
print(unknown_object)
print(unknown_object.startswith("hello"))  # error: "object" has no attribute "startswith"
print(unknown_object // 0)  # error: Unsupported operand types for // ("object" and "int")

# Для случаев, когда необходимо допустить использование не любых типов, а только некоторых, можно использовать аннотацию typing.Union с указанием списка типов в квадратных скобках.
def hundreds(x: Union[int, float]) -> int:
    return (int(x) // 100) % 10

hundreds(100.0)
hundreds(100)
hundreds("100")  # Argument 1 to "hundreds" has incompatible type "str"; expected "Union[int, float]"
