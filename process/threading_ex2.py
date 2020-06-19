# -*- coding:utf-8 -*-

import os
import time

from concurrent.futures import ThreadPoolExecutor
from functools import wraps

def worker(src, drc):
    print(f'bot: {src} {drc}')

def wrapper(f):
    def inner_wrapper(*in_args: iter, **in_kwargs):
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(worker, *in_args)
        return f()
    return inner_wrapper

@wrapper
def ex(*arg, **kwargs):
    print("ex")

if __name__ =='__main__':
    ex( (i for i in range(10)), (i for i in range(10)) )

    print("Main done...")
