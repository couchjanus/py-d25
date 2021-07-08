# Логирование из нескольких модулей

# Здесь мы импортируем logging и модуль snakes. 

import logging
import snakes
 
def main():
    """
    The main entry point of the application
    """
	
    logging.basicConfig(filename="snakes.log", level=logging.INFO)
    logging.info("Program started")
    result = snakes.add(7, 8)
    logging.info("Done!")
 
if __name__ == "__main__":
    main()

# вы получите лог со следующим содержимым:

# INFO:root:Program started
# INFO:root:added 7 and 8 to get 15
# INFO:root:Done!

# Вы не можете однозначно сказать, откуда приходят сообщения.