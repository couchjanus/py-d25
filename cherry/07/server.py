import os, os.path
import cherrypy
import string
import random

HTTP_ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(HTTP_ROOT,'global.conf')
conf = os.path.join(HTTP_ROOT,'config.conf')

# What about my javascripts, CSS and images?
# Web application are usually also made of static content such as javascript, CSS files or images. CherryPy provides support to serve static content to end-users.

# Let’s assume, you want to associate a stylesheet with your application to display a blue background color (why not?).

# First, save the following stylesheet into a file named style.css and stored into a local directory public/css.

#    body {
#      background-color: blue;
#    }
# Now let’s update the HTML code so that we link to the stylesheet using the http://localhost:8080/static/css/style.css URL.

class Server(object):
    @cherrypy.expose
    def index(self):
        if 'count' not in cherrypy.session:
            cherrypy.session['count'] = 0
            cherrypy.session['count'] += 1

        return """<html>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
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

    @cherrypy.expose
    def set(self):
        cookie = cherrypy.response.cookie
        cookie['cookieName'] = 'cookieValue'
        cookie['cookieName']['path'] = '/'
        cookie['cookieName']['max-age'] = 3600
        cookie['cookieName']['version'] = 1
        return "<html><body>Hello, I just sent you a cookie</body></html>"
    
    @cherrypy.expose
    def read(self):
        cookie = cherrypy.request.cookie
        res = """<html><body>Hi, you sent me %s cookies.<br />
                Here is a list of cookie names/values:<br />""" % len(cookie)
        for name in cookie.keys():
            res += "name: %s, value: %s<br>" % (name, cookie[name].value)
        return res + "</body></html>"

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)

    cherrypy.tree.mount(server, '/', config=glob)
    config = {
        '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
    }

    cherrypy.quickstart(server, '/', config)
