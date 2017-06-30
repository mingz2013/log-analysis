# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import json


def print_fanxing_tongji(l):
    print '====番型统计===='
    play_mode_result = {}

    for item in l:
        patterns = item['patterns']
        play_mode = item['play_mode:']
        if play_mode not in play_mode_result:
            play_mode_result[play_mode] = []
        play_mode_result[play_mode].append(patterns)

    k_v_result = {}
    for (play_mode, patterns_list) in play_mode_result.items():
        k_v_result[play_mode] = {}
        for patterns in patterns_list:
            for pattern in patterns:
                for p in pattern:
                    if p not in k_v_result[play_mode]:
                        k_v_result[play_mode][p] = 0
                    k_v_result[play_mode][p] += 1

    print json.dumps(k_v_result, ensure_ascii=False)

    return k_v_result
