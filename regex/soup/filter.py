import requests
from bs4 import BeautifulSoup
import re

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

url = "https://en.wikipedia.org/wiki/Python_(programming_language)/"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

# Beautiful Soup будет фильтровать дерево, сопоставляя все теги с заданным регулярным выражением, если передать объект регулярного выражения методу find_all().

# Код будет искать все теги заголовка в документе.
print('Все теги заголовка в документе:')
for heading in soup.find_all(re.compile("^h[1-6]")):
    print(heading.name + ' ' + heading.text.strip())

# Вместо использования регулярного выражения можно добиться того же результата, передав список всех тегов.
print('Все теги заголовка в документе без  регулярного выражения:')
for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    print(heading.name + ' ' + heading.text.strip())

# Можно передать True в качестве параметра методу find_all(). 
# Код вернет все теги в документе. 
print('Все теги в документе: ', len(soup.find_all(True)))

# Можно определить свою собственную функцию, которая принимает элемент в качестве единственного аргумента. 
# Функция должна вернуть True, если есть совпадение, а False - в противном случае. 

def big_lists(tag):
    return len(tag.contents) > 2 and tag.name == 'ul'
     
print('Собственная функция: ', len(soup.find_all(big_lists)))
