import requests

# Если в запросе есть cookies, вы сможете быстро получить к ним доступ:
# url = 'https://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']
# 'example_cookie_value'

# Чтобы отправить собственные cookies на сервер, используйте параметр cookies:
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
res = requests.get(url, cookies=cookies)

print(res.text)
# '{"cookies": {"cookies_are": "working"}}'

# Cookies возвращаются в RequestsCookieJar, который работает как dict,
# но также предлагает более полный интерфейс,
# подходящий для использования в нескольких доменах или путях.

# Словарь с cookie может также передаваться в запросы:

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'https://httpbin.org/cookies'
res = requests.get(url, cookies=jar)
print(res.text)
# '{"cookies": {"tasty_cookie": "yum"}}'
