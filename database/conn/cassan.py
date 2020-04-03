# -*- coding:utf-8 -*-

##########################################################################
from cassandra.cluster import Cluster

from threading import Lock

##########################################################################
from settings import CLUSTER_CONFIG, KEY_SPACENAME

##########################################################################

lock = Lock()
TIME_OUT = 60

class CassandraDataBase():
    def __init__(self):
        self._cluster = Cluster(CLUSTER_CONFIG)

    def connect(self):
        if self._conn is None:
            try:
                lock.acquire()
                self._conn = self._cluster.connect(KEY_SPACENAME)
                lock.release()
            except Exception as e:
                print(e)
                return False

        return True


    def executeQuery_async(self, query, data=None):
        try: 
            rows = self._conn.execute_async(query, data, timeout=TIME_OUT)
            return rows

        except Exception as e:
            print(e)
            return False


    def executeQuery(self, query, data=None):
        try: 
            rows = self._conn.execute(query, data, timeout=TIME_OUT)
            return rows

        except Exception as e:
            print(e)
            return False


    def close(self):
        self._cluster.shutdown()

