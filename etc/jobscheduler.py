# -*- coding:utf-8 -*-

##########################################################################
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

##########################################################################

##########################################################################

class JobScheduler:
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()

    def addJob(self, f, d=None, h=None, m=None, s=None, job_id=None, arg=None):
        self.sched.add_job(f, 'cron', day=d, hour=h, minute=m, second=s, day_of_week='mon-fri', id=job_id, args=arg)

    def removeJob(self, job_id):
        self.sched.remove_job(job_id)

    def addCallback(self, f):
        self.sched.add_listener(f, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    def __del__(self):
        if self.sched:
            self.sched.shutdown()
