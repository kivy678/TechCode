# -*- coding:utf-8 -*-

#################################################################
import env

import os
import time

from lockfile import locked

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LOCK_PATH = os.path.join(BASE_DIR, r'locker\lockfile')
PID_PATH = os.path.join(BASE_DIR, r'locker\pid')


@locked(LOCK_PATH, 1)
def main():

    while True:
        print("sleep...")
        time.sleep(5)

    return True


if __name__ == "__main__":
    print(os.getpid())

    with open(PID_PATH, 'w') as fw:
        fw.write(str(os.getpid()))

    main()

    print('Done...')
