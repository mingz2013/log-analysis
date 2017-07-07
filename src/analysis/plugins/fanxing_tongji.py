# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import json


def print_fanxing_tongji(l):
    print '====番型统计===='
    result = {}
    for item in l:
        patterns = item['patterns']
        play_mode = item['play_mode']
        if play_mode not in result:
            result[play_mode] = {}
        for pattern in patterns:
            for p in pattern:
                if p not in result[play_mode]:
                    result[play_mode][p] = 0
                result[play_mode][p] += 1
    print json.dumps(result, sort_keys=True, ensure_ascii=False)
    return result
