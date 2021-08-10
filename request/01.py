# Создание GET и POST запроса
import requests

# Получить веб-страницу с помощью get-запроса.
# общий тайм-лайн GitHub:
res = requests.get('https://api.github.com/events')
# Мы получили объект Response с именем res.
print(res)
# С помощью этого объекта можно получить всю необходимую информацию.

# Простой API Requests - все типы HTTP запросов очевидны.
# POST запрос:
res = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(res)
# Другие типы HTTP запросов: PUT, DELETE, HEAD и OPTIONS:
res = requests.put('https://httpbin.org/put', data = {'key':'value'})
print(res)
res = requests.delete('https://httpbin.org/delete')
print(res)
res = requests.head('https://httpbin.org/get')
print(res)
res = requests.options('https://httpbin.org/get')
print(res)

# Передача параметров в URL
# отправить какие-то данные в строке запроса URL.
# Если вы настраиваете URL вручную, эти данные будут представлены в нем
# в виде пар ключ/значение после знака вопроса. Например, httpbin.org/get?key=val.
# Requests позволяет передать эти аргументы в качестве словаря, используя аргумент params.
# Если вы хотите передать key1=value1 и key2=value2 ресурсу httpbin.org/get,
# вы должны использовать следующий код:

payload = {'key1': 'value1', 'key2': 'value2'}
res = requests.get('https://httpbin.org/get', params=payload)
print(res.url)

# URL был сформирован правильно:
# https://httpbin.org/get?key2=value2&key1=value1

# Ключ словаря, значение которого None, не будет добавлен в строке запроса URL.
# Вы можете передать список параметров в качестве значения:


payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
res = requests.get('https://httpbin.org/get', params=payload)
print(res.url)
# https://httpbin.org/get?key1=value1&key2=value2&key2=value3


# Содержимое ответа (response)

res = requests.get('https://api.github.com/events')
print(res.text)
# '[{"repository":{"open_issues":0,"url":"https://github.com/...

# Requests будет автоматически декодировать содержимое ответа сервера.
# Большинство кодировок unicode декодируются без проблем.
# Когда вы делаете запрос, Requests делает предположение о кодировке, основанное на заголовках HTTP.
# Эта же кодировка текста, используется при обращение к res.text.
# Можно узнать, какую кодировку использует Requests, и изменить её с помощью res.encoding:

print(res.encoding)
# 'utf-8'
# res.encoding = 'ISO-8859-1'

# Если вы измените кодировку, Requests будет использовать новое значение res.encoding всякий раз,
# когда вы будете использовать res.text.
# Вы можете сделать это в любой ситуации, где нужна более специализированная логика работы с кодировкой содержимого ответа.

# Например, в HTML и XML есть возможность задавать кодировку прямо в теле документа.
# В подобных ситуациях вы должны использовать res.content, чтобы найти кодировку,
# а затем установить res.encoding.
# Это позволит вам использовать res.text с правильной кодировкой.

# Requests может также использовать пользовательские кодировки в случае, если в них есть потребность.
# Если вы создали свою собственную кодировку и зарегистрировали ее в модуле codecs,
# используйте имя кодека в качестве значения res.encoding.


# Бинарное содержимое ответа
# Вы можете также получить доступ к телу ответа в виде байтов для не текстовых ответов:

print(res.content)
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...

# Передача со сжатием gzip и deflate автоматически декодируются.
# Например, чтобы создать изображение на основе бинарных данных,
# возвращаемых при ответе на запрос, используйте следующий код:

# from PIL import Image
# from io import BytesIO
#
# i = Image.open(BytesIO(r.content))
