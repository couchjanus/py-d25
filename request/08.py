import json

# Следующий фрагмент кодирует данные , хранящиеся в d в формате JSON
# и сохраняет его в файл
#
filename = "d.json"

d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

#

with open(filename, 'w') as f:
    json.dump(d, f)