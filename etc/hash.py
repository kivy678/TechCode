# -*- coding:utf-8 -*-

import hashlib
import base64

PATH = r'C:\tmp\test'

def getMD5(path):
    with open(path, 'rb') as fr:
        md5 = hashlib.md5()
        md5.update(fr.read())
        print(md5.hexdigest())

        return md5.hexdigest()


encoded = base64.b64encode(getMD5(PATH).encode())
print(encoded)

data = base64.b64decode(encoded)
print(data)
