import requests
import json

# По умолчанию Requests будет выполнять редиректы для всех HTTP глаголов, кроме HEAD.
# Мы можем использовать свойство history объекта Response, чтобы отслеживать редиректы .

# Список Response.history содержит объекты Response,
# которые были созданы для того, чтобы выполнить запрос.
# Список сортируется от более ранних, до более поздних ответов.

# Например, GitHub перенаправляет все запросы HTTP на HTTPS:
r = requests.get('https://github.com/')
r.url
# 'https://github.com/'
r.status_code
# 200
r.history
# [<Response [301]>]
#
# Если вы используете запросы GET, OPTIONS, POST, PUT, PATCH или DELETE,
# вы можете отключить обработку редиректа с помощью параметра allow_redirects:
#
#
r = requests.get('https://github.com/', allow_redirects=False)
r.status_code
# 301
r.history
# []
#
# Если вы используете HEAD, вы также можете включить редирект:
r = requests.head('https://github.com/', allow_redirects=True)
r.url
# 'https://github.com/'
r.history
# [<Response [301]>]