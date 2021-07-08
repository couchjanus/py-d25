# newSnake.py
import logging
 
module_logger = logging.getLogger("mainApp.newSnake")
 
def add(x, y):
    """"""
    logger = logging.getLogger("mainApp.newSnake.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
