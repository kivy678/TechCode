# -*- coding:utf-8 -*-

from idaapi import *
from idautils import *
from idc import *

def get_imports():
    for i in range(get_import_module_qty()):
        dllname = get_import_module_name(i)
        if not dllname:
            continue

        entries = []
        def cb(ea, name, ordinal):
            entries.append((ea, name, ordinal))
            return True  # continue enumeration

        enum_import_names(i, cb)
        for ea, name, ordinal in entries:
            yield '{0:x};{1};{2}'.format(ea, dllname, name) 
