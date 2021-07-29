from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

PORT = 8000


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def server_close(self):
        self.socket.close()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        self.wfile.write(b'''
        	<form action="http://127.0.0.1:8000" method="POST">
        	   	<input type="submit" value="Post This" name=value>
        	</form>
        	''')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


try:
    # Create a web server and define the handler to manage the
    # incoming request

    httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)

    print('Started httpserver on port ', PORT)
    # Wait forever for incoming htto requests
    httpd.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    httpd.server_close()

# Run it by typing: python httpd06.py

# Then open your web browser on this URL: http://127.0.0.1:8000