# -*- coding:utf-8 -*-

from flask.ext.cache import Cache

FlaskCache = Cache(config = { 'CACHE_TYPE': 'simple' })

def setup(app):
    FlaskCache.init_app(app)

def getCache(k, f, timeout=600, *args, **kwargs):
    r = FlaskCache.get(k)

    if not r is None:
        return r

    try:
        r = f(*args, **kwargs)

        if not r is None:
            FlaskCache.set(k, r, timeout=timeout)
            return r
    except:
        return None

def queryCache(k, f, timeout=600):
    r = FlaskCache.get(k)

    if not r is None:
        return r

    try:
        r = f()
    except:
        r = None

    if not r is None:
        FlaskCache.set(k, r, timeout=timeout)

    return r
