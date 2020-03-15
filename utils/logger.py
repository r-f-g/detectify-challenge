import logging
from datetime import datetime

MESSAGE_FORMAT = "%(asctime)s.%(msecs)03d: %(levelname)-6s@%(name)-15s[%(lineno)d]: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def set_up_logger(log_file: str, debug: bool = False):
    # set up global logger
    logger = logging.getLogger("")
    logger.setLevel(logging.INFO if not debug else logging.DEBUG)
    logger.handlers = []  # remove default handlers

    # set up log file
    file_handler = logging.FileHandler(f"{log_file}__{datetime.now():%Y%m%d-%H%M}.log", mode="w")
    file_handler.setFormatter(logging.Formatter(MESSAGE_FORMAT, datefmt=DATE_FORMAT))
    logger.addHandler(file_handler)
