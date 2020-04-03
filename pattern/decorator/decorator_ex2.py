# -*- coding:utf-8 -*-


class WapperClass_EX2:
    def __init__(self, originFunctionCall):
        self.originFunctionCall = originFunctionCall

    def __call__(self, *args, **kwargs):
        print(args)
        self.task("Before")
        self.originFunctionCall(*args, **kwargs)
        self.task("after")

    def task(self, con):
        print(f"{con} call")


@WapperClass_EX2
def ex(*arg, **kwargs):
    print("ex")


if __name__ == '__main__':
    ex('x', 'y', 'z')

    print('main end')
