from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
import cgi

PORT = 8000


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def server_close(self):
        self.socket.close()

    def do_GET(self):
        if self.path == "/":
            self.path = "/form.html"

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        if self.path == "/send":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })

            res = form["your_name"].value

            print("Your name is: %s" % res)
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b"Thanks %s !" % res.encode('utf-8'))
            return


try:
    httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
    print('Started httpserver on port ', PORT)
    httpd.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    httpd.server_close()

# Run it by typing: python httpd07.py

# Then open your web browser on this URL: http://127.0.0.1:8000