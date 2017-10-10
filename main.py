#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from sms import Sms


def send_sms(type):
    print '[%s send_sms] 开启定时任务 %s.' % (type, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sms = Sms()
    sms.send_sms()


# 定时执行
def corn_trigger():
    global SCHEDULER
    SCHEDULER.add_job(func=send_sms,
                      args=['cron'], trigger='cron',
                      day='*/1', hour='08', minute='00', second='00', id='corn_job')


SCHEDULER = BlockingScheduler()
if __name__ == '__main__':

    corn_trigger()

    try:
        SCHEDULER.start()
    except (KeyboardInterrupt, SystemExit):
        SCHEDULER.shutdown()
        print 'Started error!'
