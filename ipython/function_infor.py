# -*- coding:utf-8 -*-

from idaapi import *
from idautils import *
from idc import *

from flag import *


def getRef(start_addr):
    for xref in XrefsTo(start_addr, 1):
        if xref.type == 21:
            continue
        else:
            yield xref.frm


def searchName(_name):
    for func in Names():
        if func[1] == _name:
            for addr in getRef(func[0]):
                print(GetDisasm(addr - 4))
                print(GetMnem(addr - 4), GetOpnd(addr - 4, 0), GetOpnd(addr - 4, 1))

searchName("syscall")
