# -*- coding:utf-8 -*-

import tempfile
import time

# windows
# %appData%\Local\Temp\랜덤명으로 생성
# 파일이나 폴더가 close되면 삭제가 된다.
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)


print('done...')
