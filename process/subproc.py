# -*- coding:utf-8 -*-

#################################################################
import os
import shlex

import subprocess

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TIME_PATH = os.path.join(BASE_DIR, 'timer.py')

PID_PATH = os.path.join(BASE_DIR, 'pid')


###################### Popen ###############################

COMMAND = ["python", TIME_PATH]

def subCall1():
    proc = subprocess.Popen(COMMAND,
                            creationflags=subprocess.CREATE_NEW_CONSOLE)


def subCall2():
    proc = subprocess.Popen(COMMAND)
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
    proc = subprocess.call(COMMAND)
    print(str(proc.pid))


def subCall4():
    with subprocess.call(COMMAND, stdout=subprocess.PIPE) as proc:
        try:
            return proc.communicate(timeout=5)[0].decode('utf-8').strip()
        except subprocess.TimeoutExpired:
            proc.kill()
            return proc.communicate()[0].decode('utf-8').strip()


def parseString(cmd):
    s = shlex.shlex(cmd)
    s.whitespace_split = True

    return s


if __name__ == "__main__":
    subCall1()
    #subCall2()
    #subCall3()

    print('Done...')
