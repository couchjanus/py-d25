# Модуль http.server определяет классы для реализации HTTP-серверов (веб-серверов).
# Модуль http.server не рекомендуется для использования в продакшне, так как он выполняет только базовые проверки безопасности.
# Класс http.server.HTTPServer, является подклассом socketserver.TCPServer(). Он создает и прослушивает HTTP-сокет, отправляя запросы обработчику.
# Чтобы создать веб-сервер в Python, нужно импортировать два модуля: http.server и socketserver:

import http.server
import socketserver

PORT = 8000

# Экземпляр TCPServer описывает сервер, который использует протокол TCP для отправки и получения сообщений (http - это протокол прикладного уровня поверх TCP).
# Чтобы создать экземпляр TCP-сервера, нам нужны две вещи:
# TCP-адрес (IP-адрес и номер порта)
# обработчик
#
# socketserver.TCPServer (("", PORT), обработчик)
# TCP-адрес передается в виде кортежа (IP-адрес, номер порта)
# Передача пустой строки в качестве IP-адреса означает, что сервер будет прослушивать любой сетевой интерфейс (все доступные IP-адреса).
# Если PORT хранит значение 8000, сервер будет слушать входящие запросы на этот порт.

Handler = http.server.SimpleHTTPRequestHandler

# Веб-сервер - это процесс, который прослушивает входящие запросы на определенный TCP-адрес. TCP-адрес идентифицируется по IP-адресу и номеру порта.
#
# Код для создания и запуска сервера выглядит так:

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    # serve_forever - это метод в экземпляре TCPServer, который запускает сервер, слушает и отвечает на входящие запросы.
    #
    # with socketserver.TCPServer(("", PORT), Handler) as httpd:
    #    print("serving at port", PORT)
    #    httpd.serve_forever()
    #
    # # Run it by typing: python httpd01.py
    # # Then open your web browser on this URL: http://127.0.0.1:8000
    # Поскольку веб-сервер прослушивает любой интерфейс, он также прослушивает интерфейс обратной связи.

    httpd.serve_forever()

# Run it by typing: python httpd/01.py
# Then open your web browser on this URL: http://127.0.0.1:8000