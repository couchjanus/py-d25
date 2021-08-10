import json
import requests

res = requests.get('https://api.github.com/events')

# Если вы работаете с данными в формате JSON, воспользуйтесь встроенным JSON декодером:
print(res.json())
# [{'repository': {'open_issues': 0, 'url': 'https://github.com/...

# Если декодирование в JSON не удалось, res.json() вернет исключение.
# Например, если ответ с кодом 204 (No Content),
# или на случай если ответ содержит не валидный JSON,
# попытка обращения к res.json() будет возвращать ValueError: No JSON object could be decoded.

# успешный вызов res.json() не указывает на успешный ответ сервера.
# Некоторые серверы могут возвращать объект JSON при неудачном ответе
# (например, сведения об ошибке HTTP 500).

# Для того, чтобы проверить успешен ли запрос, используйте res.raise_for_status()
# или проверьте какой res.status_code.

# Если ответ имеет тип контента application/json,
# библиотека Requests может конвертировать его в словарь и список,

