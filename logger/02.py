# Модуль logging также может учитывать некоторые исключения в файле, или там, где вы указали.

import logging
 
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")
 
try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")

# Здесь мы использовали метод getLogger модуля logging, чтобы вернуть объект логгера под названием ex. 

# Это удобно, если у вас есть несколько логгеров в одном приложении, так как это позволяет вам узнать, какие сообщения приходят с каждого логгера. 

# Этот пример провоцирует возникновение ошибки RuntimeError, 
# затем это регистрируется в файле

