# !/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser
import codecs


cf = ConfigParser.ConfigParser()
with codecs.open('conf.ini', encoding="utf-8-sig" ) as f:
  cf.readfp(f)

secs = cf.sections()


class Conf:

    def __init__(self):
        pass

    def get_confs(self):
        confs = []
        for section in secs:
            config = {}
            config['weather_type'] = section
            config['mobile'] = cf.get(section, 'mobile')
            config['city'] = cf.get(section, 'city')
            config['hour'] = cf.get(section, 'hour')
            config['minute'] = cf.get(section, 'minute')
            config['second'] = cf.get(section, 'second')
            confs.append(config)
        return confs
