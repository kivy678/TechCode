# -*- coding:utf-8 -*-

__all__ = [
    'PrintTraceback',
]

################################################################################

import sys
import traceback

################################################################################

def PrintTraceback(exc, out=sys.stderr):
    traceback.print_tb(exc.__traceback__, file=out)
