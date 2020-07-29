# -*- coding:utf-8 -*-

##################################################################################################

from datetime import timedelta
from flask_caching import Cache

from flask import session, escape
from flask_session import Session

##################################################################################################

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

FlaskCache = Cache(config=config)
sess = Session()

##################################################################################################

def setup(app):
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    app.config['SESSION_TYPE'] = "filesystem"
    app.config['SESSION_FILE_THRESHOLD'] = 500

    FlaskCache.init_app(app)
    sess.init_app(app)

##################################################################################################

def getCache(k):
    return FlaskCache.get(k)

def setCache(k, r, timeout=600):
    FlaskCache.set(k, r, timeout=timeout)
    return None

def delCache(k):
    FlaskCache.delete(k)
    return None

##################################################################################################

def getSession(k):
    return session.get(k, False)

def setSession(k, r):
    session[k] = r
    return None

def popSession(k):
    return session.pop(k, None)

def clearSession():
    session.clear()
    return None

def getSession2():
    return session

##################################################################################################
