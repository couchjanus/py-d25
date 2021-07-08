# Логирование из нескольких модулей

import logging
import newSnake
 
def main():
    """
    The main entry point of the application
    """
    
    logger = logging.getLogger("mainApp")
    logger.setLevel(logging.INFO)
    
    # create the logging file handler
    fh = logging.FileHandler("new_snake.log")
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # add handler to logger object
    logger.addHandler(fh)
    
    logger.info("Program started")
    result = newSnake.add(7, 8)
    logger.info("Done!")
 
if __name__ == "__main__":
    main()


# здесь у нас два определенных логгера. 

# 2021-07-08 12:40:30,790 - mainApp - INFO - Program started
# 2021-07-08 12:40:30,790 - mainApp.newSnake.add - INFO - added 7 and 8 to get 15
# 2021-07-08 12:40:30,790 - mainApp - INFO - Done!

# все ссылки на root были удалены. 
# используем объект Formatter, который говорит, что нужно получить время, имя логгера, уровень логирования и сообщение. 
# Все это известно как атрибуты LogRecord. 

