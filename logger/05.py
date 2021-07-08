# Логирование из нескольких модулей

import logging
import logging.config
import newSnake
 
def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("mainApp")
    
    logger.info("Main Program started")
    result = newSnake.add(7, 8)
    logger.info("Main App Done!")
 
if __name__ == "__main__":
    main()
