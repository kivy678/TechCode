# -*- coding:utf-8 -*-

class GET_SET:
    def __init__(self):
        self._val = None


    def __getattr__(self, key):
        try:
            return self.__dict__[key]
        except KeyError as e:
            return None


    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, _val):
        self._val = _val


if __name__ == '__main__':
    gs = GET_SET()
    gs.val = 10
    print(gs.val)
