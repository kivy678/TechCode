# -*- coding:utf-8 -*-

#################################################################
import os
#import shlex

import subprocess

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TIME_PATH = os.path.join(BASE_DIR, 'timer.py')

PID_PATH = os.path.join(BASE_DIR, 'pid')


###################### Popen ###############################
def subCall1():
    proc = subprocess.Popen(["python", TIME_PATH],
                            creationflags=subprocess.CREATE_NEW_CONSOLE)


def subCall2():
    proc = subprocess.Popen(["python", TIME_PATH])
    print(str(proc.pid))

    try:
        if proc.poll() is not None:
            print("Create Failed")
        else:
            proc.kill()
            print('Sub END....')

    except Exception as e:
        print(e)

def subCall3():
    proc = subprocess.call(["python", TIME_PATH])
    print(str(proc.pid))


if __name__ == "__main__":
    subCall1()
    #subCall2()
    #subCall3()

    print('Done...')
