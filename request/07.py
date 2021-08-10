import json

# Создание JSON из Python dict
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}
print(json.dumps(d))

# Вернет следующее:
# {"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}

# Создание Python dict из JSON
s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
print(json.loads(s))

# Вернет следующее:
# {u'alice': 1, u'foo': u'bar', u'wonderland': [1, 2, 3]}