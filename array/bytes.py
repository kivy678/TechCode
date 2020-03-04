# -*- coding:utf-8 -*-

# 배열 다루기
# required python 3.5 이상
# 1. 파일을 바이너리로 읽어서 배열로 처리

PATH = r''
READ_SIZE = 10

with open(PATH, 'rb') as fr:
    hex_values = bytes(fr.read(READ_SIZE)).hex()
    print(hex_values)



print('Done...')
