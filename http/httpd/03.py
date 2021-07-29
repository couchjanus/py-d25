from http.server import HTTPServer, BaseHTTPRequestHandler


# Пример HTTP web-сервера, обрабатывающего запросы GET.
# Это очень простой пример HTTP-сервера, который отвечает Hello, world! на запросы.
# Обратите внимание, что self.send_response(200) и self.end_headers() являются обязательными,
# в противном случае ответ не будет считаться действительным.
# Проверить работу сервера можно при помощи утилиты терминала curl.

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

# Run it by typing: python httpd03.py
# Then open your web browser on this URL: http://127.0.0.1:8000

# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
# PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser
# class myHandler(BaseHTTPRequestHandler):
#     # Handler for the GET requests
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         # Send the html message
#         self.wfile.write("Hello World !")
#         return

# try:
# 	#Create a web server and define the handler to manage the
# 	#incoming request
# 	server = HTTPServer(('', PORT_NUMBER), myHandler)
# 	print('Started httpserver on port ' , PORT_NUMBER)

# 	#Wait forever for incoming htto requests
# 	server.serve_forever()

# except KeyboardInterrupt:
# 	print('^C received, shutting down the web server')
# 	server.socket.close()

# Run it by typing:
# Then open your web browser on this URL: http://ip_address:8080.
