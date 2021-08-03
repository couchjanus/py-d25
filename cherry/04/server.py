import os
import cherrypy
import string
import random

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(HTTP_ROOT,'global.conf')

# Submit this form

class Server(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="16" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def gen(self):
        return ''.join(random.sample(string.hexdigits, 8))

    # указывать длину строки динамически
    @cherrypy.expose
    def generate(self, length=16):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server)

# форма использует метод GET
# когда вы нажали кнопку Give it now!, форма отправляется на URL-адрес /generate. 
# HTML-формы также поддерживают метод POST, в этом случае строка запроса не добавляется к URL-адресу, а отправляется как тело клиентского запроса на сервер. 
# CherryPy обрабатывает и GET, и POST одинаково, используя параметры обработчика для работы с парами запроса (ключ, значение).