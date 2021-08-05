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
        template = env.get_template('base.html')
        return template.render(name='World')
        

if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server, '/', conf)


# В окружении указаны:

# загрузчик FileSystemLoader и путь, в котором следует искать шаблоны
# дополнительные параметры окружения определяют как работать с шаблонами:
# trim_blocks - если установлено в True, удаляет первую пустую строку после блока конструкции (по умолчанию False)
# lstrip_blocks - если установлено в True, пробелы и табы в начале строки удаляются (по умолчанию False)

# Методы Environment
# get_template - это метод, который позволяет загрузить шаблон из загрузчика:

# Если загрузчик существует, этот метод запрашивает шаблон у загрузчика и возвращает Template()
# Если загрузчика нет, отображается исключение TemplateNotFound

# Пример использования программного интерфейса для загрузки шаблона
# Файл html_template с шаблоном HTML:

# <head>
#     <title>{{ title }}</title>
# </head>
# <body>
#     <h1>{{ header_1 }}</h1>
#     {% for link in links %}
#         <li><a href="{{ link[link] }}">{{ link }}</a></li>
#     {% endfor %}
# </body>

