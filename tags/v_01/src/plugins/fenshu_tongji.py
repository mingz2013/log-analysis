# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''
import json


def print_fenshu_tongji(l):
    print '====分数统计===='
    result = {}
    for item in l:
        scores = item['scores']
        play_mode = item['play_mode:']
        if play_mode not in result:
            result[play_mode] = {}
        for score in scores:
            if score not in result[play_mode]:
                result[play_mode][score] = 0
            result[play_mode][score] += 1
    print json.dumps(result, ensure_ascii=False)

    return result
