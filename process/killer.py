# -*- coding:utf-8 -*-

#################################################################
import os
import shlex
import subprocess

import signal

#################################################################
cmd = '''tasklist /FI "PID eq 18736" /NH /FO "CSV"'''


def isRunning():
    s = shlex.split(cmd)
    proc = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True)

    rep = proc.stdout.read().decode().strip()
    print(int(rep.split('","')[1]))


if __name__ == "__main__":
    isRunning()
    # os.kill(36920, signal.SIGTERM)
    print('Done...')
