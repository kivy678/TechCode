# -*- coding:utf-8 -*-

#################################################################
import os
import array as ar
import numpy as np

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BIN_PATH = os.path.join(BASE_DIR, 'example.bin')
READ_SIZE = 10

########################### 배열다루기 ###########################

# 1. array
byteArray = ar.array('B')
byteArray.frombytes(b'abcdefg')
print(byteArray)
# >>> array('B', [97, 98, 99, 100, 101, 102, 103])

print(byteArray.tobytes())
# >>> b'abcdefg'

byteArray.insert(0, 128)
byteArray.pop()

print(byteArray.tobytes())
# >>> b'\x80abcdef'

with open(BIN_PATH, 'rb') as fr:
    byteArray = ar.array('B')
    byteArray.fromfile(fr, READ_SIZE)
    print(byteArray.tobytes())
# >>> b'\x01\x02\x03\x04\x05\x06\x07\x08\t\xaa'


# 2. numpy
arr1 = np.array([1, 2, 3, 4, 5])


#################################################################


print('Done...')
