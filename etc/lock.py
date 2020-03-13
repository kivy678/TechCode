# -*- coding:utf-8 -*-

#################################################################
import os
import time

from lockfile import locked


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LOCK_PATH = os.path.join(BASE_DIR, 'lockfile')


########################### LOCK 다루기 ###########################

@locked(LOCK_PATH, 1)
def main():
    while True:
        print("sleep...")

        time.sleep(10)

    return True


#################################################################


if __name__ == "__main__":
    main()					# "lockfile.lock" 파일이 생성되면서 중복 실행이 불가능

    print('Done...')
