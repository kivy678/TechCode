# -*- coding:utf-8 -*-

##########################################################################

import traceback

##########################################################################
def PrintTraceBack(exc):
    print('Exception trigger')
    print()
    traceback.print_tb(exc.__traceback__)
    print()
    print()

try:
    raise Exception
except Exception as e:
    PrintTraceBack(e)
