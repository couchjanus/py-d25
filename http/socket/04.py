# Сервер TCP srv.py
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
   # Если данных приходится ждать слишком долго,
   # можно перед использованием функции recv задать (однократно) таймаут
   # с помощью функции settimeout.

    conn.settimeout(60) # установка таймаута
    with conn:
        print('Connected by: ', addr)
        print('IP-адрес: ', addr[0])
        print('TCP порт: ', addr[1])

        while True:
            # если другая сторона сторона закрывает сокет, recv вернёт пустой объект bytes.
            data = conn.recv(1024)
            # если за 60 секунд не придут данные, функция recv вернёт пустой объект bytes, как и при закрытом соединении.
            if not data:
                print("No data")
                # клиенту, и серверу необходимо закрыть сокет с помощью функции close.
                conn.close()  # Теперь этот сокет использовать нельзя.
            conn.send(b"Your data: " + data)

# telnet 127.0.0.1 65432
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# hello
# Your data: hello
# Connection closed by foreign host.
