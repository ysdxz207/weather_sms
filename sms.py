#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from conf import Conf
from weather import Weather
import top.api
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

FORMAT = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
logging.basicConfig(filename='sms.log', level=logging.ERROR, format=FORMAT)


class Sms:
    def __init__(self):
        self.app_key = "23653018"
        self.app_secret = "8ab1387ce04deabf6fb11e049e9c5523"
        self.req = top.setDefaultAppInfo(self.app_key, self.app_secret)
        self.req = top.api.AlibabaAliqinFcSmsNumSendRequest()
        self.req.sms_type = "normal"
        self.req.sms_free_sign_name = "推他新闻"
        self.req.sms_template_code = 'SMS_*****'

    def send_sms(self, mobile, city, weather_str):

        self.req.rec_num = mobile
        self.req.sms_param = "{city:'%s',weather:'%s'}" % (
            city, weather_str)

        try:
            resp = self.req.getResponse()
            if resp['alibaba_aliqin_fc_sms_num_send_response']['result']['success']:
                print '发送成功'
            else:
                err_msg = '发送失败：' + resp['alibaba_aliqin_fc_sms_num_send_response']['result']['msg']
                logging.error(err_msg)
                print err_msg
        except Exception, e:
            err_msg = '发送失败：' + e.submsg
            logging.error(err_msg)
            print err_msg
