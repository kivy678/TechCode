#-*- coding: utf-8 -*-

import os
import paramiko

class SFTP_CONNECT:
    def __init__(self, context):
        self.context = context

        self._user = context.user
        self._passwd = context.passwd
        self._url = context.url
        self._port = context.port
        self._session = None
        self._conn = None

        self.createSession()

    def __del__(self):
        if self._conn:
            self._conn.close()
        if self._session:
            self._session.close()

    def createSession(self):
        try:
            if self._session is None:
                self._session = paramiko.Transport(self._url, self._port)

                return True

        except Exception as e:
            print(e)
            return False

    def connect(self):
        try:
            if self._conn is None:
                self._session.connect(username=self._user, password=self._passwd)
                self._conn = paramiko.SFTPClient.from_transport(self._session)

                print("connect success")
                return True

        except Exception as e:
        	print(e)
        	return False

    def download(self, rname):
        self._conn.chdir('CHW_PATH')
        try:
            if rname in self._conn.listdir():
                print("Download Start...")
                self._conn.get(rname, 'fileName')
                print("Download End...")

                return True

        except Exception as e:
        	print(e)
        	return False

    class Builder:
        def __init__(self):
            self.user = None
            self.passwd = None
            self.url = None
            self.port = None

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
            return SFTP_CONNECT(self)


a = SFTP_CONNECT.Builder()        \
    .setUser('SFTP_USER')         \
    .setPasswd('SFTP_PASSWD')     \
    .setURL('SFTP_URL')			  \
    .setPORT(22)			      \
    .build()
