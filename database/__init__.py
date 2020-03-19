# -*- coding:utf-8 -*-

from database.driver import MySQL, MsSQL, PostgreSQL


class DriverExceptionHander(Exception):
    pass


def createDriver(kwargs):
    try:
        if kwargs == {}:
            raise DriverExceptionHander('Not input Driver information')

        if kwargs.get('port') == 3306:
            return MySQL(kwargs)
        elif kwargs.get('port') == 1433:
            return MsSQL(kwargs)
        elif kwargs.get('port') == 5432:
            return PostgreSQL(kwargs)
        else:
            DriverExceptionHander('Not input Driver information')

    except DriverExceptionHander as e:
        return False
