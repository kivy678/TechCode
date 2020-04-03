# -*- coding:utf-8 -*-

from enum import Enum, unique, auto


@unique
class STATUS(Enum):
    enum1 = auto()
    enum2 = auto()
    enum3 = auto()
    enum4 = 'String ENUM1'
    enum5 = 'String ENUM2'
    enum6 = 'String ENUM3'
