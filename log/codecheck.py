# -*- coding:utf-8 -*-

##########################################################################
import timeit

from logger import getFileLogger, getLoggerFileNo

LOG = getFileLogger('report.log')


class CODE_SPEED:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = timeit.default_timer()
        LOG.info('***** START DOWNLOAD Time: ' + str(start_time) + ' *****')
        result = self.func(*args, **kwargs)
        LOG.info('***** WORKING END Time: ' +
                 str(timeit.default_timer() - start_time) + ' *****')

        return True
