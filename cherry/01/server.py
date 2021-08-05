import os, os.path
import cherrypy

from jinja2 import Environment, BaseLoader
from jinja2 import Template

import string
import random

# GET CURRENT DIRECTORY
ROOT = os.path.abspath(os.path.dirname(__file__))
glob = os.path.join(ROOT,'global.conf')
conf = os.path.join(ROOT,'config.conf')

# OUR CONTROLLER
class Server(object):
    @cherrypy.expose
    def index(self):
        template = Template("Hello {{name}}!")
        return template.render(name='Jinja')

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        # Пример цикла for, который проходит по списку словарей и заполняет поля таблицы:
        users = [
            {
            'id': 1,
            'name':'Anton', 
            'status': 1
            },
            {
            'id': 2,
            'name':'Mary', 
            'status': 1
            },
            {
            'id': 3,
            'name':'Ann', 
            'status': 0
            }, 
            {
            'id': 4,
            'name':'John', 
            'status': 0
            }
        ]

        myStr = """
            <html>
            <head><title>{{ title }}</title></head>
            <body>
            <h1>{{ title }}</h1>
            <table class="table table-hover">
                <tr>
                    <th>#</th>
                    <th>User</th>
                    <th>Status</th>
                </tr>
                {% for user in users %}
                <tr>
                    <td>{{user['id']}}</td>
                    <td>{{user['name']}}</td>
                    <td>
                    {% if user['status'] == 1 %}
                        Activated
                    {% else %}
                        Not Activated
                    {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </table>
            </body>
            </html>"""
        template = Environment(loader=BaseLoader()).from_string(myStr)
        return template.render(users = users, title="Users")

    @cherrypy.expose
    def set(self):
        cookie = cherrypy.response.cookie
        cookie['cookieName'] = 'cookieValue'
        cookie['cookieName']['path'] = '/'
        cookie['cookieName']['max-age'] = 3600
        cookie['cookieName']['version'] = 1
        myCook = """
            <html>
            <head><title>{{ title }}</title></head>
            <body>Hello, I just sent you a cookie: {{ variable }}
            {# Комментарии #}
            {# Это кусок кода, который стал временно не нужен, но удалять жалко
                {% for user in users %}
                    ...
                {% endfor %}
            #}
            </body>
            </html>"""
        template = Environment(loader=BaseLoader()).from_string(myCook)
        return template.render(variable=cookie['cookieName']['max-age'], title="My Cookies")
    
    @cherrypy.expose
    def read(self):
        # Цикл for
        # Цикл for проходит по каждому элементу последовательности.
        # Пример цикла for в шаблоне, который генерирует список users:
        users = ['Anton', 'Mary', 'Ann', 'John']
        myCook = """
            <html>
            <head><title>{{ title }}</title></head>
            <body>
            <h2>We have {{ len }} users.</h2>
            <p>Here is a list of users name:</p>
            <ul>
                {% for name in users %}
                  <li>{{ name }}: </li>
                {% endfor %}
            </ul>
            </body>
            </html>"""
        template = Environment(loader=BaseLoader()).from_string(myCook)
        return template.render(users = users, len = len(users), title="All Users")


if __name__ == '__main__':
    server = Server()
    cherrypy.config.update(glob)
    cherrypy.tree.mount(server, '/', config=glob)
    cherrypy.quickstart(server, '/', conf)
