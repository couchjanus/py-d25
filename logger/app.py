# log_with_config.py
import logging
import logging.config
import newSnake
 
def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    dictLogConfig = {
        "version":1,
        "handlers":{
            "fileHandler":{
                "class":"logging.FileHandler",
                "formatter":"myFormatter",
                "filename":"config2.log"
            }
        },
        "loggers":{
            "exampleApp":{
                "handlers":["fileHandler"],
                "level":"INFO",
            }
        },
        "formatters":{
            "myFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }
    
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("mainApp")
    logger.info("Program started")
    result = newSnake.add(7, 8)
    logger.info("Done!")
 
if __name__ == "__main__":
    main()
