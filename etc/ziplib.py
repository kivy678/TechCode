# -*- coding:utf-8 -*-

import os
from uuid import uuid4

import subprocess as sp

from settings import TEMP_DIR, RAR_PATH, ZIP_PATH

class UTIL:

    @staticmethod
    def decompressRAR(_path):
        dst = os.path.join(TEMP_DIR, uuid4().hex)
        DST = dst + "\\"

        try:
            res = sp.call([
                RAR_PATH,
                "x",
                "-IBCK",
                "-INUL",
                "-o+",
                "-p-",
                _path,
                DST
            ])

            if res == 0:
                return dst
        except Exception as e:
            pass

        return None

    @staticmethod
    def decompress7z(_path):
        dst = os.path.join(TEMP_DIR, uuid4().hex)
        DST = dst + "\\"

        try:
            res = sp.call([
                ZIP_PATH,
                'x',
                '-o'+ DST,
                '-aoa',
                '-scs'+'UTF-8',
                '-p'+'ignore',
                _path
            ])

            if res == 0:
                return dst
        except Exception as e:
            pass

        return None

