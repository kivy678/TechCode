# -*- coding:utf-8 -*-

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Target:
    watchDir = os.getcwd()

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir,
                               recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_moved(self, event):
        print(event)

    def on_created(self, event):  # 파일, 디렉터리가 생성되면 실행
        print(event)

    def on_deleted(self, event):  # 파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event):  # 파일, 디렉터리가 수정되면 실행
        print(event)


if __name__ == '__main__':
    t = Target()
    t.run()
