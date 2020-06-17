# -*- coding:utf-8 -*-

##########################################################################
import threading
from functools import wraps

##########################################################################

lock = threading.Lock()

def synchronized(lock, True):
    def wrapper(f):
        @wraps(f)
        def inner_wrapper(*args, **kwargs):
            if True:
                with lock:
                    return f(*args, **kwargs)
            else:
                return f(*args, **kwargs)

        return inner_wrapper
    return wrapper



class Singleton:
    _instance = None
    
    @classmethod
    def _getInstance(cls):
        return cls._instance


    @classmethod
    @synchronized(lock, True)    
    def instance(cls, *args, **kargs):

        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance
