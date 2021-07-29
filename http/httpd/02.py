# Example with SSL support
# http.server.BaseHTTPRequestHandler() - класс используется для обработки HTTP-запросов, поступающих на сервер;
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="key.pem",
                               certfile='cert.pem', server_side=True)

httpd.serve_forever()
# Для создания файлов ключей и сертификатов с помощью OpenSSL используйте следующую команду
#
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365


# To generate key and cert files with OpenSSL use following command

# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

# import http.server
# import socketserver
# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

