# Как решался вопрос контроля типов в Python без использования аннотаций. 
# Один из возможных вариантов решения данной задачи – это использование комментариев, составленных определенным образом.
name = "John" # type: str
# Мы создали переменную с именем name и предполагаем, что ее тип – str. 
# Естественно, для самого интерпретатора Python это не имеет значения.
name = "John" # type: str
print(name)
name = 10
print(name)
# И это будет корректно с точки зрения Python. 

# Аннотации для переменных пишут через двоеточие после идентификатора. 
# После этого может идти инициализация значения. Например,
price: int = 5
title: str

# Можно использовать один из трех способов создания аннотированных переменных.
var = value # type: annotation
var: annotation; var = value
var: annotation = value
