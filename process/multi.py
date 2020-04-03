# -*- coding:utf-8 -*-

import time
from concurrent.futures import ProcessPoolExecutor, TimeoutError

############################### map을 이용한 분배 ###############################
def bot(val):
    print(f"bot: {val}")
    time.sleep(5)

    return str(f"rtn = {val}")

def callback(fn):
    print(f"Call Back Fuction Me....{fn.result()}")


def map_exam():
    with ProcessPoolExecutor(max_workers=4) as executor:
        for code in executor.map(bot, [i for i in range(10)]):
            print(f"[*]: {code}")

def submit_exam():
    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(bot, 1)
        future.add_done_callback(callback)
        try:
            print("Call Bot... wait result")
            print(f"[*]: {future.result(timeout=10)}")

        except TimeoutError as e:
            print("Time out")


if __name__ == '__main__':
    #map_exam()
    submit_exam()

