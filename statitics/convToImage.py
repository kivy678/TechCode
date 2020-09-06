# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np
import struct

from io import StringIO

value = StringIO()


PATH = r'C:\tmp\test.bin'
WPATH = r'C:\tmp\out.png'

with open(PATH, 'rb') as fr:
    while True:
        content = fr.read(1)

        if not content:
            break

        value.write(format(struct.unpack('<B', content)[0], 'b'))


sq = np.sqrt(len(value.getvalue()))
v = int(np.ceil(sq))
print(v)


cmap = {'0': (255,255,255),'1': (0,0,0)}

data = [cmap[letter] for letter in value.getvalue()]
img = Image.new('RGB', (v, v), "white")
img.putdata(data)
img.save(WPATH, 'PNG')

value.close()
