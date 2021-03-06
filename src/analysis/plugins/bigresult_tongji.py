# -*- coding:utf-8 -*-
"""
"""
__date__ = "29/08/2017"
__author__ = "zhaojm"

import json

from analysis import table_config


def print_big_result(l):
    print '====大结算统计===='
    result = {}
    for item in l:
        # print 'item', item
        scores = item['scores']
        play_mode = item['play_mode']
        cur_round_count = item['cur_round_count']
        if play_mode not in result:
            result[play_mode] = {}
        if cur_round_count not in result[play_mode]:
            result[play_mode][cur_round_count] = {}

        if not scores:
            print 'warn, scores is None'
            continue
        for score in scores:
            if score not in result[play_mode][cur_round_count]:
                result[play_mode][cur_round_count][score] = 0
            result[play_mode][cur_round_count][score] += 1
    print json.dumps(result, sort_keys=True, ensure_ascii=False)

    return result
