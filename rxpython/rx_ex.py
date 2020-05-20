# -*- coding:utf-8 -*-

##########################################################################################

import rx
from rx import operators as ops
from rx.subject import Subject

##########################################################################################


class startWork(Subject):
    def on_next(self, num):
        print(num)

    def on_completed(self):
        print('on_completed')

    def on_error(self, error):
        print('on_error')


def buffer_count():
    return rx.pipe(
        ops.flat_map(range(10)),
        ops.filter(lambda x: x >= 5),
        ops.buffer_with_count(4)
    )


def classficationStart():
    rx.from_iterable(range(2)).pipe(
        buffer_count()
    ).subscribe(startWork())

if __name__ ==  '__main__':
    classficationStart()
