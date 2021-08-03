import os
import cherrypy
import string
import random

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(HTTP_ROOT,'global.conf')

# Different URLs lead to different functions

class Server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    # Очевидно, что ваши приложения будут обрабатывать более одного URL. 
    # Приложение, которое генерирует случайную строку при каждом вызове:

    @cherrypy.expose
    def gen(self):
        return ''.join(random.sample(string.hexdigits, 8))

    # указывать длину строки динамически
    @cherrypy.expose
    def generate(self, length=16):
        return ''.join(random.sample(string.hexdigits, int(length)))

    # перейдите по адресу http://localhost:8000/generate?Length=16, и ваш браузер отобразит сгенерированную строку длиной 16. 

    # раздел после ? называется строкой запроса. Традиционно строка запроса используется для контекстуализации URL-адреса путем передачи набора пар (ключ, значение). Формат этих пар - ключ=значение. Каждая пара разделяется символом &.

    # мы должны преобразовать заданное значение длины в целое число. Действительно, значения отправляются от клиента на наш сервер в виде строк.

    # ключи строки запроса сопоставляются с параметрами функции.

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server)


# Go now to http://localhost:8080/gen and your browser will display a random string.

# URL-адрес, который вы ввели в браузер: 
# http://localhost:8080/gen
# содержит различные части:

# http:// указывает на то, что это URL-адрес, использующий протокол HTTP (RFC 2616).
# localhost:8080 - это адрес сервера. Он состоит из имени хоста и порта.
# /gen, является сегментом URL-адреса. 
# Это то, что CherryPy использует для поиска функции или метода ответа.
# CherryPy использует метод index() для обработки / и метод gen() для обработки /генерации


