# -*- coding:utf-8 -*-

import os
import shutil
import requests

from urllib.parse import urljoin

REQUEST_TIMEOUT = 30
REQUEST_RECV_CHUNK_SIZE = 4096


class WEB_CONNECT:
    def __init__(self, context):
        self.context = context

        self._user 		= context.user
        self._passwd 	= context.passwd
        self._url 		= context.url
        self._port 		= context.port
        self._session 	= None

        self.createSession()

    def createSession(self):
        if self._session is None:
            self._session = requests.Session()

        self._session.auth = (self._user, self._passwd)

        return True

    def connect(self):
        try:
            with self._session.get(self._url, timeout=REQUEST_TIMEOUT) as res:
                if res.status_code == 200:
                    print("connect success")

                    return True
                else:
                    return False

        except Exception as e:
            return False

    def download(self, name):
        FILE_DOWNLOAD = urljoin(self._url, name)
        FULL_SAVE_PATH = os.path.join('SAVE_PATH', name)

        try:
            with self._session.get(FILE_DOWNLOAD,
            			    timeout=REQUEST_TIMEOUT,
                                    stream=True,
                                    verify=False) as res:
                if res.status_code == 200:
                    with open(FULL_SAVE_PATH, 'wb') as fw:
                        shutil.copyfileobj(res.raw, fw)
                    print("Download Done...")
                else:
                    return False

        except Exception as e:
            return False

    class Builder:
        def __init__(self):
            self.user 	= None
            self.passwd = None
            self.url 	= None
            self.port 	= None

        def __getattr__(self, key):
            try:
                return self.__dict__[key]
            except KeyError as e:
                return None

        def setUser(self, user):
            self.user = user
            return self

        def setPasswd(self, passwd):
            self.passwd = passwd
            return self

        def setURL(self, url):
            self.url = url
            return self

        def setPORT(self, port):
            self.port = port
            return self

        def build(self):
            return WEB_CONNECT(self)


a = WEB_CONNECT.Builder()        \
    .setUser('WEB_USER')           \
    .setPasswd('WEB_PASSWD')       \
    .setURL('WEB_URL')			 \
    .build()

a.connect()
a.download('fileName')
