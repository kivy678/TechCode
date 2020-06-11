# -*- coding:utf-8 -*-

##########################################################################################
from abc import *

import pymysql
import pymssql
import psycopg2

##########################################################################################

__all__ = ['MySQL', 'MsSQL', "PostgreSQL",]


class DriverExceptionHander(Exception): pass

class DriverManager(object):
    __metaclass__       = ABCMeta

    def __init__(self, config=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._config    = config
        self._conn      = None


    def __del__(self):
        if self._conn:
            self._conn.close()  

        del self._conn 


    @abstractmethod
    def connect(self):
        pass


    @abstractmethod
    def query(self, q, p=None):
        pass


    @abstractmethod
    def call(self, q, p=None):
        pass


    def close(self):
        if self._conn:
            self._conn.close()


##########################################################################################
class MySQL(DriverManager):
    def __init__(self, config):
        super().__init__(config)
        self.connect()


    def connect(self):
        try:
            if self._conn is None:
                self._conn = pymysql.connect(**self._config)

        except Exception as e:
            raise DriverExceptionHander('Can`t connect MySQL')


    def query(self, q, p=None):
        try:
            with self._conn.cursor() as cur:
                cur.execute(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            #print(e)
            self._conn.rollback()
            return False


    def call(self, q, p=None):
        try:
            with self._conn.cursor() as cur:
                cur.callproc(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            #print(e)
            self._conn.rollback()
            return False



##########################################################################################
class MsSQL(DriverManager):
    def __init__(self, config):
        super().__init__(config)
        self.connect()


    def connect(self):
        try:
            if self._conn is None:
                self._conn = pymssql.connect(**self._config)

        except Exception as e:
            raise DriverExceptionHander('Can`t connect MsSQL')


    def query(self, q, p=None):
        try:
            with self._conn.cursor() as cur:
                cur.execute(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            #print(e)
            self._conn.rollback()
            return False


    def call(self):
        try:
            with self._conn.cursor() as cur:
                cur.callproc(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            #print(e)
            self._conn.rollback()
            return False


##########################################################################################
class PostgreSQL(DriverManager):
    def __init__(self, config):
        super(PostgreSQL, self).__init__(config)
        self.connect()

    def connect(self):
        try:
            if self._conn is None:
                self._conn = psycopg2.connect(**self._config)

        except Exception as e:
            raise DriverExceptionHander('Can`t connect PostgreSQL')

    def query(self, q, p=None):
        try:
            with self._conn.cursor() as cur:
                cur.execute(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            LOG.info(e)
            self._conn.rollback()
            return False

    def call(self):
        try:
            with self._conn.cursor() as cur:
                cur.callproc(q, p)
                rows = cur.fetchall()
                self._conn.commit()

                return rows

        except Exception as e:
            # LOG.info(e)
            self._conn.rollback()
            return False


##########################################################################################
