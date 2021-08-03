import os
import cherrypy
import string
import random

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(HTTP_ROOT,'global.conf')
conf = os.path.join(HTTP_ROOT,'config.conf')

# Track my end-user’s activity

class Server(object):
    @cherrypy.expose
    def index(self):
        if 'count' not in cherrypy.session:
            cherrypy.session['count'] = 0
            cherrypy.session['count'] += 1

        return """<html>
          <head></head>
          <body>""" + str(cherrypy.session['count']) +"""<form method="get" action="generate">
              <input type="text" value="16" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server, '/', config=conf)

# генерируем строку и сохраняем ее в текущем сеансе.
# Если перейти на http://localhostt:8080/, сгенерировать случайную строку, 
# а затем перейти на http://localhostt:8080/display, 
# вы увидите только что сгенерированную строку.

