# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import json


def print_tongji(l):
    print '====解散统计===='
    result = {}

    result['total'] = len(l)

    play_mode_result = {}
    for item in l:
        play_mode = item['play_mode']
        if play_mode not in play_mode_result:
            play_mode_result[play_mode] = 0
        play_mode_result[play_mode] += 1

    result['play_mode'] = play_mode_result

    print json.dumps(result, sort_keys=True, ensure_ascii=False)
    return result
