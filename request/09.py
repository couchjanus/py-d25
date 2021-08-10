import json

# Следующий фрагмент открывает JSON закодированный файл
filename = 'd.json'
# и возвращает объект, который хранится в файле.
#
with open(filename, 'r') as f:
    print(json.load(f))
# `load` vs` load`, `dump` vs` dumps`

# json модуль содержит функции для чтения и записи
# из Юникода строк, и чтения и записи в файлах.
# Они различаются по замыкающей s в имени функции.

# используем строковые функции:
#
data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data)
# u'{"foo": "bar", "baz": []}'

json.loads(json_string)
# {u"foo": u"bar", u"baz": []}
#
# используем файловые функции:
#
from io import StringIO
#
json_file = StringIO()
data = {u"foo": u"bar", u"baz": []}
json.dump(data, json_file)
json_file.seek(0)  # Seek back to the start of the file before reading
json_file_content = json_file.read()
# u'{"foo": "bar", "baz": []}'

json_file.seek(0)  # Seek back to the start of the file before reading
json.load(json_file)
# {u"foo": u"bar", u"baz": []}
#
# основное отличие состоит в том, что при выгрузке данных JSON
# вы должны передать дескриптор файла в функцию,
# а не захватывать возвращаемое значение.
# Также вы должны искать начало файла перед чтением или записью,
# чтобы избежать повреждения данных.

# При открытии файла курсор находится в положении 0 , поэтому также будет работать:
#
json_file_path = './data.json'
data = {u"foo": u"bar", u"baz": []}

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)

with open(json_file_path) as json_file:
    json_file_content = json_file.read()
    print(json_file_content)
    # u'{"foo": "bar", "baz": []}'

with open(json_file_path) as json_file:
    print(json.load(json_file))
    # {u"foo": u"bar", u"baz": []}
