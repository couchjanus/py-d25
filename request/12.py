import requests
import json

# Бывают случаи, когда нужно отправить данные не закодированные методом form-encoded.
# Если вы передадите в запрос строку вместо словаря,
# эти данные отправятся в не измененном виде.
#
# пример, GitHub API v3 принимает закодированные JSON POST/PATCH данные:
#
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

# Вместо того, чтобы кодировать dict, вы можете передать его напрямую,
# используя параметр json, и он будет автоматически закодирован:

#
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

# параметр json игнорируется, если передаются data или files.
# Использование параметра json в запросе изменит заголовок Content-Type на application/json.

# POST отправка Multipart-Encoded файла
# Запросы упрощают загрузку файлов с многостраничным кодированием (Multipart-Encoded) :

url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }

# Вы можете установить имя файла, content_type и заголовки в явном виде:
#
url = 'https://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }
#
# Можете отправить строки, которые будут приняты в виде файлов:
#
url = 'https://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
r.text
# {
#   ...
#   "files": {
#     "file": "some,data,to,send\\nanother,row,to,send\\n"
#   },
#   ...
# }
#
# В случае, если вы отправляете очень большой файл как запрос multipart/form-data,
# возможно понадобиться отправить запрос потоком.
# По умолчанию, requests не поддерживает этого, но есть отдельный пакет,
# который это делает — requests-toolbelt.
# Настоятельно рекомендуется открывать файлы в бинарном режиме.
# Это связано с тем, что запросы могут пытаться предоставить для вас заголовок Content-Length,
# и если это значение будет установлено на количество байтов в файле будут возникать ошибки,
# при открытии файла в текстовом режиме.
