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

with open(BIN_PATH, 'rb') as fr:
    byteArray = ar.array('B')
    byteArray.fromfile(fr, READ_SIZE)
    print(byteArray.tolist())
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 170]


#################################################################
"""
bytes는 불변의 자료형
"""

bytes(5)
#>>> b'\x00\x00\x00\x00\x00'
bytes([i for i in range(20)])
#>>> b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13'
bytes(b'Hello World')
#>>> b'Hello World'


#################################################################
"""
bytearray 요소를 변경할 수 있는 시퀀스 자료형
"""
x = bytearray(b'Hello World')
x[0] = ord('T')
#>>> b'Tello World'

x.decode('utf-8')
#>>> Tello Word

#################################################################

# 2. numpy
arr1 = np.array([1, 2, 3, 4, 5])


#################################################################


print('Done...')
