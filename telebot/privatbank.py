import re
import requests
import json

# Python-скрипт, который будет реализовывать логику конкретных запросов курсов валют.
# Использовать будем PrivatBank API.
# URL: https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5.

# Пример ответа:
# [{"ccy":"USD","base_ccy":"UAH","buy":"26.70000","sale":"27.10000"},{"ccy":"EUR","base_ccy":"UAH","buy":"31.35000","sale":"31.95000"},{"ccy":"RUR","base_ccy":"UAH","buy":"0.35500","sale":"0.38500"},{"ccy":"BTC","base_ccy":"USD","buy":"42414.6003","sale":"46879.2951"}]

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(ccy_key):
    for exc in load_exchange():
        if ccy_key == exc['ccy']:
            return exc
    return False


def get_exchanges(ccy_pattern):
    result = []
    ccy_pattern = re.escape(ccy_pattern) + '.*'

    for exc in load_exchange():
        if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
    return result

# Загружаем текущий курс валюты

# exchange_now = get_exchange("USD")

# print(exchange_now) # {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '26.70000', 'sale': '27.10000'}
