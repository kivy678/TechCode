# -*- coding:utf-8 -*-

from functools import wraps

def WapperFunction_EX1(*args, **kwargs):
    def wrapper(f):
        @wraps(f)
        def inner_wrapper(*in_args, **in_kwargs):
            print(args, kwargs)
            print(in_args, in_kwargs)
            return f(*args, **kwargs)
        return inner_wrapper
    return wrapper


@WapperFunction_EX1(hello="WORLD")
def ex(*arg, **kwargs):
    print("ex")


if __name__ == '__main__':
    ex('a', 'b', 'c')

    print('main end')
