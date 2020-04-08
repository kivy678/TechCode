# -*- coding:utf-8 -*-

import os
import time

while True:
    print("subprocess: {0}".format(os.getpid()))
    time.sleep(2)
