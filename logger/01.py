# Создание простого логгера;

import logging

# Простейший способ создания лога – это использовать функцию basicConfig модуля logging и передать ей несколько ключевых аргументов. 
# Функция принимает: filename, filemode, format, datefmt, level и stream. 
logging.basicConfig(filename="sample.log", level=logging.INFO)

# Существует пять уровней логирования (в порядке возрастания): DEBUG, INFO, WARNING, ERROR и CRITICAL.  

# Если вы хотите, чтобы ваш логгер перезаписывал лог, передайте filemode=”w”
# add filemode="w" to overwrite

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
