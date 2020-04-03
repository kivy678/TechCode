# -*- coding:utf-8 -*-


##########################################################################
from state1 import TEST1
from state2 import TEST2

##########################################################################


class TEST_EXAM:
    def __init__(self):
        self._context = TEST1()

    def switch(self, state):
        self._context = state

    def printf(self):
        self._context.printf()


a = TEST_EXAM()
a.printf()

a.switch(TEST2())
a.printf()
