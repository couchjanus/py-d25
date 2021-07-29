# На клиентской стороне работа с сокетами выглядит намного проще.

# Client TCP client.py
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 53000        # Port to listen on (non-privileged ports are > 1023)

# Здесь сокет будет только один и его задача лишь подключиться к заранее известному IP-адресу и порту сервера, сделав вызов connect().

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b'Hello, world')
data = client.recv(1024)
client.close()
print('Received', repr(data))
