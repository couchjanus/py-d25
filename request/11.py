import requests
import json

# послать form-encoded данные таким же образом, как это делается в HTML форме.
# Для этого просто передайте соответствующий словарь в аргументе data.
# Ваш словарь данных в таком случае будет автоматически закодирован как HTML форма,
# когда будет сделан запрос:
payload = {'key1': 'value1', 'key2': 'value2'}
res = requests.post("https://httpbin.org/post", data=payload)
print(res.text)
# {
#   ...
#   "form": {
#     "key2": "value2",
#     "key1": "value1"
#   },
#   ...
# }
#

# Аргумент data также может иметь несколько значений для каждого ключа.
# Это можно сделать, указав data в формате tuple,
# либо в виде словаря со списками в качестве значений.
# Особенно полезно, когда форма имеет несколько элементов,
# которые используют один и тот же ключ:
#
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
# {
#   ...
#   "form": {
#     "key1": [
#       "value1",
#       "value2"
#     ]
#   },
#   ...
# }
r1.text == r2.text # True