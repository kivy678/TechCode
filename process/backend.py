# -*- coding:utf-8 -*-

##########################################################################
import os, sys
import signal
import time

##########################################################################
from daemon import DaemonContext
from daemon.pidfile import PIDLockFile

from logger import LOG, getLoggerFileNo

##########################################################################

class BACKEND_DAEMON(object):
    def __init__(self, name):                
        self.PID_PATH = os.path.join('PID_DIR', '{}.pid'.format(name))
        #self.LOG_PATH = os.path.join(LOG_DIR, '{}.log'.format(name))

        self.pidfile = PIDLockFile(self.PID_PATH)
        self.logger = LOG

    def start(self, *args, **kwds):
        with DaemonContext(pidfile=self.pidfile,
                           working_directory='WORK_DIR',
                           initgroups=False,
                           files_preserve=getLoggerFileNo(self.logger)):
            try:
                self.run(*args, **kwds)
            except Exception as e:
                self.logger.error(e)

    def run(self, *args, **kwds):
        pass

    def stop(self):
        if self.pidfile.is_locked():
            os.kill(self.pidfile.read_pid(), signal.SIGTERM)
        time.sleep(1)
