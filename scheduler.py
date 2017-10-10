#!/usr/bin/python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler

from conf import Conf
from sms import Sms
from weather import Weather
from datetime import datetime


class Scheduler:
    def __init__(self):
        self.SCHEDULER = BlockingScheduler()
        conf = Conf()
        confs = conf.get_confs()

        for conf in confs:
            self.add_corn_trigger(conf)

    def add_corn_trigger(self, conf):
        mobile = conf['mobile'].encode("ascii")
        hour = conf['hour'].encode("ascii")
        minute = conf['minute'].encode("ascii")
        second = conf['second'].encode("ascii")

        self.SCHEDULER.add_job(func=self.get_weather_and_send_sms,
                          args=[conf], trigger='cron',
                          day='*/1', hour=hour, minute=minute, second=second, id=('corn_job' + mobile))

    def get_weather_and_send_sms(self, conf):
        print '开启定时任务 %s.' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        mobile = conf['mobile']
        weather_type = conf['weather_type']
        city = conf['city']

        weather = Weather(city)
        weather_str = weather.get_weather_str(weather_type)
        sms = Sms()
        sms.send_sms(mobile, city, weather_str)

    def start(self):
        try:
            self.SCHEDULER.start()
        except (KeyboardInterrupt, SystemExit):
            self.SCHEDULER.shutdown()
            print 'Started error!'
