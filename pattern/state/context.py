# -*- coding:utf-8 -*-

##########################################################################
from abc import *

##########################################################################


class CONTEXT(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(CONTEXT).__init__()

    @abstractmethod
    def printf(self):
        pass
