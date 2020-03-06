# -*- coding:utf-8 -*-

#################################################################
import os
import struct

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BIN_PATH = os.path.join(BASE_DIR, 'example.bin')
READ_SIZE = 10

################## 바이너리 데이터 배열로 처리하기 ##################

# 1. bytes 메소드 사용 (python 3.5 이상)
with open(BIN_PATH, 'rb') as fr:
    result = bytes(fr.read(READ_SIZE)).hex()
    print(result)
# >>> 010203040506070809aa


# 2. unpack 메소드 사용
with open(BIN_PATH, 'rb') as fr:
    result = ''.join(map(lambda x: "{:02x}".format(
        x), struct.unpack("<10B", fr.read(READ_SIZE))))

    print(result)
# >>> 010203040506070809aa

#################################################################

print('Done...')
