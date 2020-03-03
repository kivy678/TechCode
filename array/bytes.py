# -*- coding:utf-8 -*-

# 배열 다루기
# 1. 파일을 바이너리로 읽어서 배열로 처리

with open(_path, 'rb') as fr:
    _hex = bytes(fr.read(10)).hex()
    print(_hex)


print('Done...')
