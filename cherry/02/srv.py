import cherrypy

class Server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

if __name__ == '__main__':
    server = Server()
    conf = {
        'server.socket_port': 8000,
        'engine.autoreload.on': True,
        'log.screen': True,
        'checker.on': True,
        'restart_enable': True,
    }
    config = {
        'global': conf
    }
    cherrypy.config.update(config)
    cherrypy.tree.mount(server, '/', config=config)
    cherrypy.quickstart(server)
