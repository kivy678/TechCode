# -*- coding:utf-8 -*-

##########################################################################
from joblib import Memory

from settings import CACHE_DIR

##########################################################################

MEM = Memory(CACHE_DIR, verbose=0)
