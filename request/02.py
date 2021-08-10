# Создание GET и POST запроса
import requests

# Коды HTTP находятся в диапазоне от 1XX до 5XX.
# 1XX -  информация
# 2XX - успешно
# 3XX - перенаправление
# 4XX - ошибка клиента (ошибка на вашей стороне)
# 5XX - ошибка сервера (ошибка на их стороне)
# При выполнении запросов мы хотим получить коды состояния в диапазоне 200.
# Requests понимает, что коды состояния 4XX и 5XX сигнализируют об ошибках,
# и поэтому при возврате этих кодов состояния объекту ответа на запрос присваивается значение False.
# Проверив истинность ответа, вы можете убедиться, что запрос успешно обработан:
res = requests.get('https://api.github.com/events')
if res:
    print('Response OK')
else:
    print('Response Failed')
#
# Сообщение Response Failed появится только при возврате кода состояния 400 или 500.
# Попробуйте заменить URL на несуществующий, чтобы увидеть ошибку ответа 404.
#
# Чтобы посмотреть код состояния, добавьте следующую строку:
#
print(res.status_code)
#
# Так вы увидите код состояния и сможете сами его проверить.
#
# Ошибка результата с кодом 404
#
# У requests есть встроенный объект вывода кодов состояния:
#
print(res.status_code == requests.codes.ok)
# True
#
# Если мы сделали неудачный запрос (ошибка 4XX или 5XX),
# то можем вызвать исключение с помощью res.raise_for_status():
#
bad_r = requests.get('https://httpbin.org/status/404')
bad_r.status_code
# 404
bad_r.raise_for_status()
# Traceback (most recent call last):
#   File "requests/models.py", line 832, in raise_for_status
#     raise http_error
# requests.exceptions.HTTPError: 404 Client Error
#
# Но если status_code для res оказался 200, то когда мы вызываем raise_for_status() мы получаем:
#
res.raise_for_status()
# None