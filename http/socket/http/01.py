import socket
# Hypertext Transfer Protocol (HTTP) - это протокол прикладного уровня, предназначенный для передачи гипертекстовых данных в распределенных информационных системах.
# Когда речь идет о сетевом взаимодействии, протоколы принято условно разделять на уровни. В самом низу находятся протоколы физического уровня, определяющие как данные передаются в физических средах. Протоколы IP и TCP - это протоколы сетевого и транспортного уровня, соответственно. Они определяют более высокоуровневые детали взаимодействия, в частности, IP отвечает за адресацию компьютеров/узлов в сети, а TCP - за надежную передачу данных произвольной длины между узлами. HTTP располагается на самом высоком уровне - прикладном. От нижележащих протоколов HTTP ожидает гарантий надежности доставки данных, а сам концентрируется на определении понятий запросов и ответов (сообщений) и их семантике. Фактически, HTTP является основным протоколом передачи данных в вебе, а сами данные являются гипертекстом, зачастую представленным в формате HTML-страниц.

# Задача HTTP-сервера - принимать входящие HTTP-запросы от клиентов, обрабатывать их и отправлять HTTP-ответы.
# Простейший HTTP-запрос выглядит следующим образом:
#
# GET / HTTP/1.1
# Host: example.com
#
# Сообщение HTTP/1.1 - это обычный текст, который состоит из строк, разделенных символами CRLF, т.е. \r\n. Первая строка запроса называется request line. Она определяет метод method, цель target и версию протокола. Далее идут заголовки запроса. В HTTP/1.1 заголовок Host является обязательным.

# HTTP-ответ:
# HTTP/1.1 200 OK
#
# HTTP-ответы также представлены сообщениями. Первая строка ответа называется status line. Она состоит из версии, трехзначного кода статуса status-code и опционального текста причины.
# Как и в случае с TCP-сервером, для того, чтобы начать обрабатывать HTTP-запросы, сервер должен создать слушающий (listening) сокет. На каждое входящее соединение, сервер должен прочитывать текст HTTP-запроса, вызывать соответствующий обработчик, и, получив от него ответ, отсылать данные клиенту. TCP-соединение может быть как завершено непосредственно после отправки ответа, так и сохранено для повторного использования клиентом.

class NoHandlerError(Exception):
    pass

class Request:
    pass

class Handler:
    def can_handle(self, request):
        return False

    def handle(self, request):
        raise RuntimeError("abstract")

# Реализация полнофункционального HTTP/1.1-сервера требует учета всех требований протокола, определенных группой RFC (RFC7230 "Message Syntax and Routing", RFC7231 "Semantics and Content", RFC7232 "Conditional Requests", RFC7233 "Range Requests", RFC7234 "Caching", RFC7235 "Authentication").
# В качестве основы HTTP-сервера будем использовать следующий класс:

class Server:
    def __init__(self, host='127.0.0.1', port=80):
        self.s = socket.socket()
        server_addr = host, port
        self.s.bind(server_addr)
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    # decorator get
    def get(self, path):
        def decorator(f):
            class DynamicHandler(Handler):
                def can_handle(self, request):
                    return request.method == 'GET' and request.path == path
                def handle(self, request):
                    return f(request)
            self.handlers.append(DynamicHandler())
            return f
        return decorator

    # Обработка запросов происходит синхронно, т.е. возможно обслуживать не более одного клиента в один момент времени.
    # Сервер в бесконечном цикле осуществляет прием входящих соединений, выполняя
    def serve_forever(self):
        self.s.listen()
        while True:
            s2, client_addr = self.s.accept()
            # Каждое соединение s2 является клиентским сокетом.
            # Прием очередного соединения инициирует обработку HTTP-запроса self.handle_client(s2).
            # В случае ошибки на любом из этапов, обработка заканчивается отправкой сообщения об ошибке
            # s2.send(b'HTTP/1.0 500 Internal Server Error\r\n\r\n').
            try:
                self.handle_client(s2)
            except:
                try:
                    s2.send(b'HTTP/1.0 500 Internal Server Error\r\n\r\n')
                except:
                    pass  # the socket has died, do nothing
            finally:
                s2.close()

    def handle_client(self, socket):
        # Обработка заключается в чтении и синтаксическом анализе HTTP-запроса
        # client_handler.parse_request(), непосредственно обработке
        # client_handler.handle_request(request) и отправке ответа
        # client_handler.send_response(response).
        client_handler = ClientHandler(socket, self.handlers)
        request = client_handler.parse_request()
        response = client_handler.handle_request(request)
        client_handler.send_response(response)

# Разбор запроса
class ClientHandler:
    def __init__(self, socket, handlers):
        self.socket = socket
        self.handlers = handlers

    # Разбор запроса состоит из следующих шагов:
    # Читаем первую строку first_line,
    # разбираем ее на метод, цель и версию
    # и сохраняем их в некоторую структуру данных.
    #
    #        first_line = raw_request.pop(0)
    #        # METHOD /path HTTP/version
    #        request.method, request.path, request.http_version = first_line.split()
    #        request.http_version = request.http_version[len('HTTP/'):]

    def parse_request(self):
        raw_request = self.socket.recv(2048).decode().splitlines()
        request = Request()
        first_line = raw_request.pop(0)
        # METHOD /path HTTP/version
        request.method, request.path, request.http_version = first_line.split()
        request.http_version = request.http_version[len('HTTP/'):]

        # Читаем построчно заголовки, сохраняем в request.body.
        request.headers = self.parse_headers(raw_request)
        request.body = '\n'.join(raw_request)

        return request

    def parse_headers(self, raw_request):
        # Разбор заголовков запроса
        headers = dict()
        while True:
            line = raw_request.pop(0)
            if not line:
                # reached the end of headers
                break
            name, colon, value = line.partition(': ')
            headers[name] = value
        return headers

    def handle_request(self, request):
        for handler in self.handlers:
            if handler.can_handle(request):
                return handler.handle(request)
        raise NoHandlerError()

    def send_response(self, response):
        if isinstance(response, str):
            code = 200
            body = response
        else:
            code, body = response
        body = body.encode()

        code_name = {
            200: 'OK',
            201: 'Created',
            404: 'Not Found'
        }[code]

        self.socket.send('HTTP/1.0 {} {}\r\n'.format(code, code_name).encode())
        self.send_header('Server', 'Simple HTTP server 0.1')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body))

        self.finish_headers()
        self.socket.send(body)

    def send_header(self, name, value):
        self.socket.send('{}: {}\r\n'.format(name, value).encode())

    def finish_headers(self):
        self.socket.send(b'\r\n')


server = Server(port=8000)

@server.get('/')
def root(request):
    return '''
        <html>
            <head>
                <title>Hello Python</title>
            </head>
            <body>
                <h1>Hello Python</h1>
            </body>
        </html>'''

server.serve_forever()
