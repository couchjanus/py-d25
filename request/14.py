import requests
import json

# Вы можете сделать так, чтобы Requests прекратил ожидание ответа
# после определенного количества секунд с помощью параметра timeout.
# Почти весь код должен использовать этот параметр в запросах.
# Несоблюдение этого требования может привести к зависанию вашей программы:
requests.get('https://github.com/', timeout=0.001)
# Traceback (most recent call last):
#   File "", line 1, in
# requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)

# Timeout это не ограничение по времени полной загрузки ответа.
# Исключение возникает, если сервер не дал ответ за timeout секунд
# (точнее, если ни одного байта не было получено от основного сокета за timeout секунд).