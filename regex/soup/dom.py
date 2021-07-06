import requests
from bs4 import BeautifulSoup
import re

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

url = "https://en.wikipedia.org/wiki/Python_(programming_language)/"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

# Поиск дерева DOM с использованием встроенных функций

# Метод поиска find_all() вернет список всех потомков, соответствующих критериям поиска:

find_all(name, attrs, recursive, string, limit, **kwargs)

# Аргумент name - это имя тега. Можно пердавать строку, список, регулярное выражение, функцию или значение True в качестве имени.
# Можно фильтровать элементы в дереве DOM на основе разных атрибутов, таких как id, href и т.д. 
# Получить все элементы с определенным атрибутом независимо от его значения, используя attribute=True. 

print('Получить все элементы с определенным атрибутом: ', len(soup.find_all(id=True)))

# Поиск элементов с определенным классом отличается от поиска обычных атрибутов. Поскольку class является зарезервированным ключевым словом в Python, придется использовать аргумент class_ при поиске элементов с определенным классом.
 
print('Поиск элементов с определенным классом: ', len(soup.find_all(class_=True)))
# print('Поиск элементов с определенным классом: ', soup.find_all(class_=True)) 

print('Поиск элементов с классом body: ', len(soup.find_all(class_="body")))
 
print('Поиск элементов с атрибутом href: ', len(soup.find_all(href=True)))

# Если нужны только первые 2 значения, можно передать методу в качестве значения limit=2. 

print(soup.find_all(class_="body", limit=2))

# Искать элемент только в прямых дочерних элементах путем передачи recursive=False методу find_all().

print(len(soup.html.find_all("meta")))
 
print(len(soup.html.find_all("meta", recursive=False)))
 
# Найти ровно один результат для определенного поискового запроса с помощью метод find(), а не передавать limit=1 в find_all(). 
# Единственная разница между результатами, возвращаемыми этими двумя методами, заключается в том, что find_all() возвращает список только с одним элементом, а find() возвращает ровно один результат.

print(soup.find_all("h2", limit=1))
 
print(soup.find("h2"))

# Можно искать элементы с помощью селекторов CSS с помощью метода select():

print(len(soup.select(".body a")))
 
print(len(soup.select("li > a")))
 
print(soup.select("li:nth-of-type(1)"))
 
print(len(soup.select("li > a:nth-of-type(2)")))
 
print(len(soup.select("li > a:nth-of-type(3)")))
 
print(len(soup.select("[class*=mw]")))
 
print(len(soup.select("[class$=body]")))
