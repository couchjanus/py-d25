# Сервер TCP srv.py
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
            data = conn.recv(1024)
            if not data:
                # Клиент отключился
                break
            # Для отправки данных в сокет используется функция send.
            conn.send(b"Your data: " + data)

# telnet 127.0.0.1 65432
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# hello
# Your data: hello
# hello server
# Your data: hello server
# ^]
# telnet> quit
# Connection closed.

