# -*- coding:utf-8 -*-

from idaapi import *
from idautils import *
from idc import *

from flag import *

def getRef(start_addr):
    for xref in XrefsTo(start_addr, 1):
        if xref.type == Ordinary_Flow:#or xref.iscode == 0: ida function -> XrefTypeName(xref.type)
            continue
        else:
            #Log.info('{0};{1:x};{2:x};{3}'.format(XrefTypeName(xref.type), xref.to, xref.frm, xref.iscode))
            #yield '{0:x};{1:x}'.format(xref.to, xref.frm)
            yield '{0:x}'.format(xref.frm)
