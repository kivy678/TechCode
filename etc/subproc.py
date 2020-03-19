# -*- coding:utf-8 -*-

#################################################################
import os
import shlex

import subprocess

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TIME_PATH = os.path.join(BASE_DIR, 'timer.py')


def main():
    proc = subprocess.Popen(["python", TIME_PATH],creationflags=subprocess.CREATE_NEW_CONSOLE)
    print(proc.pid)

    try:
        if proc.poll() is not None:
            print("Create Failed")
        else:
            proc.kill()
            print('Sub END....')
            
    except Exception as e:
        print(e)


#################################################################


if __name__ == "__main__":
    main()					# "lockfile.lock" 파일이 생성되면서 중복 실행이 불가능

    print('Done...')
