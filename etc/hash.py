# -*- coding:utf-8 -*-

import hashlib
import base64

PATH = r'C:\tmp\test'

def getMD5(path):
    with open(path, 'rb') as fr:
        m = hashlib.md5()
        for chunk in iter(lambda: fr.read(m.block_size * 128), b''):
        	m.update(chunk)
        	
        print(m.hexdigest())

        return m.hexdigest()


encoded = base64.b64encode(getMD5(PATH).encode())
print(encoded)

data = base64.b64decode(encoded)
print(data)
