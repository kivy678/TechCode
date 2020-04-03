from __future__ import annotations
from abc import *



class State(object):
    #__metaclass__ = ABCMeta


    def Idle(self):
        print('parent idle')


    def Attack(self):
        pass


    def damge(self):
        print('parent damge')


    def process(self):
        self.Idle()
        self.Attack()
        self.damge()



class context(State):
    def Attack(self):
        print('attack')



class context2(State):
    def Idle(self):
        print('idle')
        print('idle')


    def Attack(self):
        print('attack')
        print('attack')


    def damge(self):
        print('damge')
        print('damge')



a = context()
a.process()
print('')
ab = context2()
ab.process()


