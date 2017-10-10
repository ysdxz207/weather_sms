#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

class Weather:

    def __init__(self, city):
        self.weather_notice_index = [0, 2, 4]
        self.city = city
        self.url = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak=4cc4c12708a0da07124b9bfab7c53591&location=' + city

    def get_weather_str(self, weather_type):
        r = requests.get(self.url)

        if weather_type == 'children':
            self.weather_notice_index = [0, 2, 3, 4]
        if weather_type == 'parents':
            self.weather_notice_index = [0, 2, 3]

        index = r.json()['results'][0]['index']

        notice = ''

        for i in self.weather_notice_index:
            notice += index[i]['des']

        # city = "城市：" + r.json()['results'][0]['currentCity']

        weather_info = '今天'
        size = 2
        for i in range(0, size):
            weather_info += r.json()['results'][0]['weather_data'][i]['date']
            weather_info += "："+r.json()['results'][0]['weather_data'][i]['weather']
            weather_info += "\n风力："+r.json()['results'][0]['weather_data'][i]['wind']
            weather_info += "\n温度："+r.json()['results'][0]['weather_data'][i]['temperature']
            weather_info += '\n\n' if (i+1) != size else ''

        weather_info += '\n\n今天出门建议：' + notice
        return weather_info
