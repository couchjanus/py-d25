# 02.py
import socket # Для работы с сокетами нужно импортировать модуль socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# Чтение данных
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by: ', addr)
        print('IP-адрес: ', addr[0])
        print('TCP порт: ', addr[1])

        while True:
        # Для чтения данных используется функция recv,
        # первым параметром которой нужно передать количество полученных байт данных.
        # Если столько байт, сколько указано, не пришло, а какие-то данные уже появились,
        # функция всё равно возвращает всё, что имеется, поэтому надо контролировать размер полученных данных.

            data = conn.recv(1024)

            # Тип возвращаемых данных - bytes. У этого типа есть почти все методы, что и у строк
            if not data:
                break
            else:
                # Для того, чтобы извлечь текстовые данные со строками, нужно декодировать данные и использовать уже полученную строку.
                print("Data: " + data.decode("utf-8"))
                # Если вы попытаетесь использовать байты вместо строк, вы получите ошибку:
                # print("Data: "+data)

# telnet 127.0.0.1 65432
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# hello
# hello world
# quit
# ^]
# telnet> quit
# Connection closed.
