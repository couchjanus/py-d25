import os, os.path
import cherrypy

from jinja2 import Environment, FileSystemLoader

# GET CURRENT DIRECTORY
ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(ROOT,'global.conf')
conf = os.path.join(ROOT,'config.conf')

class Server(object):
    @cherrypy.expose
    def index(self):
        env = Environment(loader=FileSystemLoader('./templates'))
        template = env.get_template('index.html')
        return template.render(name='World')
        

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server, '/', conf)
