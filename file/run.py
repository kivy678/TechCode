# -*- coding:utf-8 -*-

from file_observer2 import Target

class CreateObserverDir(Target):
    def __init__(self, watchDir):
        super().__init__(watchDir)

    def on_created(self, event):
        print('event...')

t = CreateObserverDir(r'C:\test\tmp')
t.run()

print('done')
