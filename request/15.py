import requests
import json

# В случае неполадок в сети (например, отказа DNS, отказа соединения и т.д.),
# Requests вызовет исключение ConnectionError.

# Response.raise_for_status() вызовет HTTPError
# если в запросе HTTP возникнет статус код ошибки.

# Если выйдет время запроса, вызывается исключение Timeout.

# Если запрос превышает заданное значение максимального количества редиректов,
# то вызывают исключение TooManyRedirects.

# Все исключения, которые вызывает непосредственно Requests
# унаследованы от requests.exceptions.RequestException.
