# -*- coding:utf-8 -*-

##########################################################################
import redis

##########################################################################

class RedisQueue():
    def connect(self, config):
        if self._conn is None:
            try:
                _conn_pool = redis.ConnectionPool(**config)
                self._conn = redis.StrictRedis(connection_pool=_conn_pool)
                self._conn.ping()

                return self._conn

            except Exception as e:
                print(e)
                return False

        return True


    def close(self):
        self._conn.connection_pool.disconnect()
