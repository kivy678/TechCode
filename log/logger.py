# -*- coding:utf-8 -*-

__all__ = [
    'getLogger',
    'getFileLogger',
    'getLoggerFileNo',
    'attachLoggerObject',
]

################################################################################

import logging
import logging.handlers

from modules.constraint import *

################################################################################

LOGGER_FORMAT_STRING = '%(asctime)-15s|%(levelname)s|%(filename)s|%(lineno)d|%(module)s|%(funcName)s|%(message)s'
LOGFMT = logging.Formatter(LOGGER_FORMAT_STRING)

LOG_MAXBYTES = 32 * 1024 * 1024
LOG_BACKUPS = 3

################################################################################


def getLogger():
    logger = logging.getLogger(LOGGER_IDENT)
    logger.setLevel(logging.INFO)

    return logger


def getFileLogger(path, logger=None, stream: bool = False):
    if not logger:
        logger = getLogger()

    def handlerExistCheck(_logger, _cls):
        if _cls in map(lambda x: x.__class__, _logger.handlers):
            return True
        return False

    if handlerExistCheck(logger, logging.handlers.RotatingFileHandler) is False:
        handler = logging.handlers.RotatingFileHandler(path)
        handler.setFormatter(LOGFMT)
        logger.addHandler(handler)

    if stream is True and handlerExistCheck(logger, logging.StreamHandler) is False:
        handler = logging.StreamHandler()
        handler.setFormatter(LOGFMT)
        logger.addHandler(handler)

    return logger


def getLoggerFileNo(logger):
    return list(filter(lambda x: not (x is None),
                       map(lambda x: x.stream.fileno(),
                           filter(lambda x: hasattr(x, 'stream') and hasattr(x.stream, 'fileno'),
                                  logger.handlers))))


def attachLoggerObject(obj, logger):

    for handle in LOGGER_ATTACH_METHODS:
        if hasattr(obj, handle) is False and hasattr(logger, handle) is True:
            setattr(obj, handle, getattr(logger, handle))
