import os, os.path
import cherrypy

from jinja2 import Environment, FileSystemLoader

from product import Product

# GET CURRENT DIRECTORY
ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(ROOT,'global.conf')
conf = os.path.join(ROOT,'config.conf')

class Server(object):
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('./templates'))
        self.product = Product()

    @cherrypy.expose
    def index(self):
        products = self.product.all()
        # return str(products)
        
        template = self.env.get_template('index.html')
        return template.render(products = products, title='Happy Shoping')
    @cherrypy.expose
    def about(self):
        template = self.env.get_template('about.html')
        return template.render(name='World')
    @cherrypy.expose
    def product(self):
        template = self.env.get_template('product.html')
        return template.render(name='World')

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server, '/', conf)
