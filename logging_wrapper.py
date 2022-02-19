import logging

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

WRITE = "w"
APPEND = "a"

DEFAULT_FORMAT = (
    "[%(asctime)s] [%(levelname)8s] : %(message)s (%(name)s:%(funcName)s:%(lineno)s)"
)
DEFAULT_FILENAME = "info.log"


def init_logger(
    logger_name, filepath=DEFAULT_FILENAME, level=DEBUG, format=DEFAULT_FORMAT
):

    # create a logger instance
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # create file and console handlers
    file_handler = logging.FileHandler(filepath)
    console_handler = logging.StreamHandler()

    # set logging level
    file_handler.setLevel(level)
    console_handler.setLevel(level)

    # set formaters
    formater = logging.Formatter(
        format,
        datefmt="%d-%b-%y %H:%M:%S",
    )

    # add formaters to handlers
    file_handler.setFormatter(formater)
    console_handler.setFormatter(formater)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # return the logger
    return logger
