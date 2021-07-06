import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})

url = "https://en.wikipedia.org/wiki/Python_(programming_language)/"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

print(soup.title)
 
print(soup.title.name)
 
print(soup.title.string)

print(soup.h1)
 
print(soup.h1.string)
 
print(soup.h1['class'])
 
print(soup.h1['id'])
 
print(soup.h1.attrs)

# Beautiful Soup будет искать в документе тег, который точно соответствует строке.

for heading in soup.find_all('h3'):
    print(heading.text)

for sub_heading in soup.find_all('h2'):
    print(sub_heading.text)
     
print(soup.p.contents)
 
print(soup.p.contents[0])
 
for child in soup.p.children:
    print(child.name)

print(soup.p.parent.name)
 
for parent in soup.p.parents:
    print(parent.name)
 
print(soup.p.b.previous_sibling)
