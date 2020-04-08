# -*- coding:utf-8 -*-

from idaapi import *
from idautils import *
from idc import *

from flag import *

def getString():
    for i in Strings():
        if i.strtype == UFT_16:
            yield '{0:x};UTF-16;{1};{2}'.format(i.ea, i.length,  str(i))    # startaddress;type;stringsize;string
        else:
            yield '{0:x};ASCII;{1};{2}'.format(i.ea, i.length,  str(i))

