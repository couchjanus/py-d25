# A basic web application
# The following example demonstrates the most basic application 
# you could write with CherryPy. 
# It starts a server and hosts an application that will be served 
# at request reaching http://127.0.0.1:8080/

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())

# Store this code snippet into a file named 01/aev.py and execute it as follows:
# $ python srv.py

# This will display something along the following:
# python 01/srv.py 

# [31/Jul/2021:21:06:56] ENGINE Listening for SIGTERM.
# [31/Jul/2021:21:06:56] ENGINE Listening for SIGHUP.
# [31/Jul/2021:21:06:56] ENGINE Listening for SIGUSR1.
# Первые три строки указывают, что сервер будет обрабатывать сигнал. 

# [31/Jul/2021:21:06:56] ENGINE Bus STARTING
# Строка сообщает текущее состояние сервера, поскольку в этот момент он находится в стадии ЗАПУСКА. 

# CherryPy Checker:
# The Application mounted at '' has an empty config.
# уведомление, что для приложения не задана конкретная конфигурация. 
# По умолчанию CherryPy имеет функцию, которая проверяет правильность синтаксиса настроек, которые вы можете предоставить для настройки приложения. Если ничего не указано, в журналах отображается предупреждающее сообщение. Этот журнал безвреден и не помешает работе CherryPy.

# Затем сервер запускает несколько внутренних утилит. 
# [31/Jul/2021:21:06:56] ENGINE Started monitor thread 'Autoreloader'.
# [31/Jul/2021:21:06:56] ENGINE Serving on http://127.0.0.1:8080
# сервер указывает, что теперь он готов принимать входящие сообщения, поскольку он прослушивает адрес 127.0.0.1:8080 - на этом этапе ваше приложение готово к использованию.
# [31/Jul/2021:21:06:56] ENGINE Bus STARTED
