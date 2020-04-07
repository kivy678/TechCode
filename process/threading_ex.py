# -*- coding:utf-8 -*-

import os
import time

from threading import Thread

############################### 함수를 이용한 예제 ###############################
def bot1(val):
    print(f"bot function: {val}")
    time.sleep(1)

    return str(f"rtn = {val}")

############################### 클래스를 이용한 예제 ###############################
class bot2(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        self.val = val

    def run(self):
        print(f"bot class: {self.val}")
        time.sleep(1)

        return str(f"rtn = {self.val}")


if __name__ =='__main__':
    START = 10
    th1 = Thread(target=bot1, args=(START,))
    th1.start()
    th1.join()

    th2 = bot2(START)
    th2.start()
    th2.join()

    print("Main done...")
