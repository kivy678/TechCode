# -*- coding:utf-8 -*-


class BaseClass(object):
    def __init__(self):
        self.action()

    def action(self):
        pass


class ActionClass(BaseClass):
    def action(self):
        print('action class call')


class EventRequest:
    def __init__(self, RequestAction):
        self.RequestAction = RequestAction

    def start(self):
        self.RequestAction()


if __name__ == "__main__":
    ev = EventRequest(ActionClass)
    ev.start()

    print('main end')
