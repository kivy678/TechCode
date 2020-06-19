# -*- coding:utf-8 -*-

from functools import singledispatch

@singledispatch
def func(val, val2):
    print("Defualt: ", val, val2)


@func.register
def _(val: int, val2: str):
    print('Int String')


@func.register
def _(val: str, val2: str):
    print('String String')


func('a', 'b')
func(1, 'c')
