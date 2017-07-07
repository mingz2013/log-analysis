# -*- coding:utf-8 -*-
'''
Created on 01/07/2017

@author: zhaojm
'''
import json
import time


def print_shijian_tongji(l):
    print '====时间统计===='
    result = {}
    for item in l:
        time_now = item['time_now']
        play_mode = item['play_mode']
        if play_mode not in result:
            result[play_mode] = {}

        t = time.strptime(time_now, '%Y-%m-%d %H:%M:%S.%f')
        h = t.tm_hour
        if t.tm_hour not in result[play_mode]:
            result[play_mode][h] = 0
        result[play_mode][h] += 1
    print json.dumps(result, sort_keys=True, ensure_ascii=False)

    return result
